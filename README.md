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
client = Tremendous("[SANDBOX_ACCESS_TOKEN]", "https://testflight.tremendous.com/api/v2")

```

Campaigns are created within the dashboard by team admins.
They define the catalog and presentation of your reward.
API requests can always override these settings
within the specific reward object by specifying the catalog, message, etc.

```python
campaigns = client.campaigns.list()
campaign_id = campaigns[0]["id"]
```

The funding source you select is how you are charged for the order.

```python
funding_sources = client.funding_sources.list()
funding_source_id = funding_sources[0]["id"]
```

Optionally pass a unique external_id for each order create call
to guarantee that your order is idempotent and not executed multiple times.

```python
external_id = "[ID FROM YOUR SYSTEM]"
```

An array data representing the rewards you'd like to send.

```python
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
```

Submit the order.
```
client.orders.create(order_data)
```

[1]: https://www.tremendous.com/docs
[2]: https://testflight.tremendous.com/login
