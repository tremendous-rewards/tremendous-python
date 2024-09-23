import json
import os

import pytest
from tremendous import Configuration, ApiClient, TremendousApi, CreateOrderRequest, SingleRewardOrder
from tremendous.exceptions import BadRequestException

CAMPAIGN_ID = os.environ["TEST_CAMPAIGN_ID"]
RECIPIENT_EMAIL = os.environ["TEST_RECIPIENT_EMAIL"]

class TestOrders:
  configuration = Configuration(
     server_index=Configuration.Environment["testflight"],
      access_token = os.environ["SANDBOX_API_TOKEN"]
  )

  api = ApiClient(configuration)
  client = TremendousApi(api)

  def test_list_orders(self):
    orders = self.client.list_orders().orders

    assert len(orders) > 0

    for order in orders[:10]:
        assert hasattr(order, "id")
        assert hasattr(order, "created_at")
        assert hasattr(order, "payment")

  def test_submit_order(self):
    request = CreateOrderRequest(
      SingleRewardOrder(
        payment = {
          "funding_source_id": "balance"
        },
        reward = {
          "campaign_id": CAMPAIGN_ID,
          "delivery": {
              "method": "EMAIL"
          },
          "recipient": {
              "name": "Recipient Name",
              "email": RECIPIENT_EMAIL
          },
          "value": {
              "denomination": 5.0,
              "currency_code": "USD"
          }
        })
      )

    data = self.client.create_order(request)

    assert data.order.id != None
    assert data.order.campaign_id == CAMPAIGN_ID
    assert data.order.status == "EXECUTED"

  def test_raise_validation_errors(self):
    with pytest.raises(BadRequestException) as e_info:
      request = CreateOrderRequest(
        SingleRewardOrder(
          payment = {
            "funding_source_id": "NOT A VALID FUNDING SOURCE ID"
          },
          reward = {
            "campaign_id": CAMPAIGN_ID,
            "delivery": {
                "method": "EMAIL"
            },
            "recipient": {
                "name": "Recipient Name",
                "email": RECIPIENT_EMAIL
            },
            "value": {
                "denomination": 5.0,
                "currency_code": "USD"
            }
          })
        )

      self.client.create_order(request)

    response = json.loads(e_info.value.body)
    assert "message" in response["errors"]
    assert "payload" in response["errors"]
