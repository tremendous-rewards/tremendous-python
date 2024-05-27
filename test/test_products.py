import os
from tremendous import Configuration, ApiClient, TremendousApi

PRODUCT_ID = os.environ["TEST_PRODUCT_ID"]

class TestProducts:
  configuration = Configuration(
     server_index=Configuration.Environment["testflight"],
      access_token = os.environ["SANDBOX_API_TOKEN"]
  )

  api = ApiClient(configuration)
  client = TremendousApi(api)

  def test_list_products(self):
    products = self.client.list_products().products

    assert len(products) > 0

    for product in products[:10]:
        assert hasattr(product, "id")
        assert hasattr(product, "name")
        assert hasattr(product, "currency_codes")

  def test_get_product(self):
    product = self.client.get_product(PRODUCT_ID).product

    assert product.id == PRODUCT_ID
    assert hasattr(product, "name")
    assert hasattr(product, "currency_codes")
