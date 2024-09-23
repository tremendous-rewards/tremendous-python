# Upgrading from v2

The `3.x.x` and `4.x.x` releases are a full rewrite based on our [API schema][ref] docs

Here we have "before and after" of how a few API calls looked like with our v2 version, and how they
can be written using the new library.

[ref]: https://developers.tremendous.com/reference

## Configuring the client

### `v2`

```py
from tremendous import Tremendous

client = Tremendous("[SANDBOX_ACCESS_TOKEN]", "https://testflight.tremendous.com/api/v2")
```

### `v4`

```py
from tremendous import Configuration, ApiClient, TremendousApi

configuration = Configuration(server_index=Configuration.Environment["testflight"], access_token="[SANDBOX_ACCESS_TOKEN]")

api = ApiClient(configuration)
client = TremendousApi(api)
```

## Creating an `Order`

### `v2`

```py
order_data = {
  "external_id": external_id,
  "payment": {
    "funding_source_id": funding_source_id,
  },
  "reward": {
    "value": {
      "denomination": 20,
      "currency_code": "USD"
    },
    "campaign_id": campaign_id,
    "delivery": {
      "method": "EMAIL",
    },
    "recipient": {
      "email": "sam@yourdomain.com",
      "name": "Sam Stevens"
    }
  }
}

order = client.orders.create(order_data)
```

### `v4`

```py
from tremendous import CreateOrderRequest, SingleRewardOrder

request = CreateOrderRequest(
  SingleRewardOrder(
    payment = {
      "funding_source_id": "balance"
    },
    reward = {
      "value": {
        "denomination": 20,
        "currency_code": "USD"
      },
      "campaign_id": campaign_id,
      "delivery": {
        "method": "EMAIL",
      },
      "recipient": {
        "email": "sam@yourdomain.com",
        "name": "Sam Stevens"
      }
    }
  )
)

response = client.create_order(request)
response.order.id # => "the order id"
```

## Retrieving an `Order`

### `v2`

```py
order = client.orders.show("[ORDER_ID]")

print("Order was created at %s" % order.created_at)
```

### `v3`

```py
order = client.get_order("[ORDER_ID]").order

print("Order was created at %s" % order.created_at)
```

## Listing `Funding Source`s

### `v2`

```py
funding_sources = client.funding_sources.list


for funding_source in funding_sources:
  print("* %s => %s" % (funding_source.method, funding_source.id))
```

### `v3`

```py
funding_sources = client.list_funding_sources().funding_sources

for funding_source in funding_sources:
  print("* %s => %s" % (funding_source.method, funding_source.id))
```

## Handling errors

## `v2`

On `v2`, failed requests would always raise `ValueError` with the response body

```py
from tremendous import Tremendous

client = Tremendous("INVALID_TOKEN", "https://testflight.tremendous.com/api/v2")

try:
  client.products.list()
except ValueError as error:
  print("API request failed! %s" % error)
```

## `v3`

On `v2`, all errors raised by the lib are subclasses of `Tremendous.ApiException`

```py
from tremendous import Configuration, ApiClient, TremendousApi, ApiException

configuration = Configuration(access_token="INVALID_TOKEN")

api = ApiClient(configuration)
client = TremendousApi(api)

try:
  client.list_orders()
except ApiException as error:
  print("API request failed! Status: %s, Reason: %s" % (error.status, error.reason))
```
