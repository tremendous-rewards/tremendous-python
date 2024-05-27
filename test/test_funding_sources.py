import os
from tremendous import Configuration, ApiClient, TremendousApi

class TestFundingSources:
  configuration = Configuration(
     server_index=Configuration.Environment["testflight"],
      access_token = os.environ["SANDBOX_API_TOKEN"]
  )

  api = ApiClient(configuration)
  client = TremendousApi(api)

  def test_list_funding_sources(self):
    funding_sources = self.client.list_funding_sources().funding_sources

    assert len(funding_sources) > 0

    for funding_source in funding_sources:
        assert hasattr(funding_source, "id")
        assert hasattr(funding_source, "method")
        assert hasattr(funding_source, "meta")
