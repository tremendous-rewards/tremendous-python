# Tremendous

A Python client library for the [Tremendous API][docs].

> [!NOTE]
> This branch includes the v4 version of the Tremendous Python client, a new version based
> on our [API schema][ref] docs. If you are using the v2 versions, please check our
> [`UPGRADING`](UPGRADING.md) guide

## Installation

```sh
$ pip install tremendous-python
```

## Getting started

All API requests require an access token.  A sandbox access token is assigned upon signup through the [Tremendous Sandbox Environment][docs]. Once you are ready to move to production, you will be assigned a production access token.

### Authentication


```py
from tremendous import Configuration, ApiClient, TremendousApi

# you can use `Configuration.Environment["production"]` when ready to use our production environment.
configuration = Configuration(server_index=Configuration.Environment["testflight"], access_token="[SANDBOX_ACCESS_TOKEN]")

api = ApiClient(configuration)
client = TremendousApi(api)
```

### Examples

Submitting an order:

```py
from tremendous import CreateOrderRequest, SingleRewardOrder

request = CreateOrderRequest(
  SingleRewardOrder(
    payment = {
      "funding_source_id": "balance"
    },
    reward = {
      "campaign_id": "CAMPAIGN_ID",
      "delivery": {
          "method": "EMAIL"
      },
      "recipient": {
        "email": "sarah@tremendous.com",
        "name": "Sarah Smith"
      },
      "value": {
          "denomination": 20,
          "currency_code": "USD"
      }
    }
  )
)

response = client.create_order(request)
print("Order created! ID: %s" % response.order.id)
```

Retrieving an Order and a Reward

```py
order = client.get_order("[ORDER_ID]").order
reward = client.get_reward("[REWARD_ID]").reward

print("The order status is %s" % order.status)
print("The reward was delivered to %s" % reward.recipient.email)
```

Listing products:

```py
products = api_client.list_products().products

for product in products:
  print(product.name)
```

Listing funding sources:

```py
funding_sources = client.funding_sources().funding_sources

for funding_source in funding_sources:
  print("* %s => %s" % (funding_source.method, funding_source.id))
```

[ref]: https://developers.tremendous.com/reference
[docs]: https://tremendous.com/docs
