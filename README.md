tremendous-python
==============

A python client library for the [Tremendous API][1].

## Installation

```console
$ pip install tremendous-python
```

## Getting started

All API requests require an access token.  A sandbox access token is assigned upon signup through the [Tremendous Dashboard][2]. Once you are ready to move to production, you will be assigned a production access token.

### Authentication

```python
from tremendous import Tremendous

# Sandbox environment
client = Tremendous("[SANDBOX_ACCESS_TOKEN]", "https://testflight.tremendous.com")

# Production environment
client = Tremendous("[PRODUCTION_ACCESS_TOKEN]", "https://www.tremendous.com")
```

### Orders

See [API documentation][3] for all Order options.  Use the FoundingSources resource to look up a valid method for your payment (i.e. credit card, ACH, etc).

```python
# Create a new order, specifying your gift options
# as an array of objects.
response = client.create_order({
  "funding_source_id": "[FUNDING_SOURCE_ID]",
  "gifts": [
    {
      "amount": 40,
      "message": "Such a great way to show appreciation to others!",
      "recipient": {
        "deliver_method": "EMAIL",
        "email": "person@yourteam.com",
        "name": "Person Example"
      }
    }
  ]
})

if response.ok:
    order = response.to_json()["order"]


# Return historical orders, optionally passing a starting offset for results.
response = client.get_orders({offset: 10})

# Return a order by order_id
response = client.get_order("[ORDER_ID]")
```

### Funding Sources
Production funding sources must be added through the web dashboard. A sandbox funding source is provided during development.

```python
# Retrieve a list of your funding sources (credit card, ach, etc).
response = client.get_funding_sources()
```

### Gifts
Retrieve a single or many historical gifts sent by your account.

```python
response = client.get_gifts({offset: 10})

response = client.get_gift("[GIFT_ID]")
```

[1]: https://tremendous.com/docs
[2]: https://tremendous.com/rewards
[3]: https://tremendous.com/docs
