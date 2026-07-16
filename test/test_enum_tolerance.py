import pytest
from pydantic import ValidationError

from tremendous import ListProductsResponseProductsInner


# Responses with enum values unknown to this SDK version must not fail parsing.
# The API adds enum values (product categories, fraud reasons, statuses) in
# most releases, and previously released versions of the SDK must keep working
# when they encounter them.
class TestEnumTolerance:
  def product_attributes(self, **overrides):
    attributes = {
      "id": "ABCD1234",
      "name": "Test Product",
      "description": "A test product",
      "category": "merchant_card",
      "disclosure": "",
      "currency_codes": ["USD"],
      "countries": [{"abbr": "US"}],
      "images": [],
    }
    attributes.update(overrides)
    return attributes

  def test_parses_known_enum_values(self):
    product = ListProductsResponseProductsInner.from_dict(self.product_attributes())

    assert product.category == "merchant_card"

  def test_parses_unknown_enum_values_preserving_the_raw_value(self):
    product = ListProductsResponseProductsInner.from_dict(
      self.product_attributes(category="a_category_added_in_the_future")
    )

    assert product.category == "a_category_added_in_the_future"

  def test_still_rejects_a_missing_required_enum_value(self):
    with pytest.raises(ValidationError, match="category"):
      ListProductsResponseProductsInner.from_dict(self.product_attributes(category=None))
