import json
import warnings

import pytest

from tremendous.models.list_products_response import ListProductsResponse


def build_product(**overrides):
  product = {
    "id": "ABCD1234",
    "name": "Test Product",
    "description": "A test product",
    "category": "merchant_card",
    "disclosure": "",
    "currency_codes": ["USD"],
    "countries": [{"abbr": "US"}],
    "images": [],
  }
  product.update(overrides)
  return product


class TestEnumTolerance:
  """Responses with enum values unknown to this SDK version must not fail parsing.

  See https://github.com/tremendous-rewards/tremendous-python/issues/129
  """

  def test_known_category_parses_without_warning(self):
    body = json.dumps({"products": [build_product()]})

    with warnings.catch_warnings():
      warnings.simplefilter("error")
      response = ListProductsResponse.from_json(body)

    assert response.products[0].category == "merchant_card"

  def test_unknown_category_parses_with_warning(self):
    body = json.dumps({"products": [build_product(category="a_category_added_in_the_future")]})

    with pytest.warns(UserWarning, match="Unrecognized value 'a_category_added_in_the_future'"):
      response = ListProductsResponse.from_json(body)

    assert response.products[0].category == "a_category_added_in_the_future"

  def test_unknown_list_item_parses_with_warning(self):
    body = json.dumps({"products": [build_product(currency_codes=["USD", "XYZ"])]})

    with pytest.warns(UserWarning, match="Unrecognized value 'XYZ'"):
      response = ListProductsResponse.from_json(body)

    assert response.products[0].currency_codes == ["USD", "XYZ"]
