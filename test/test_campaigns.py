import os
from tremendous import Configuration, ApiClient, TremendousApi

CAMPAIGN_ID = os.environ["TEST_CAMPAIGN_ID"]

class TestCampaigns:
  configuration = Configuration(
     server_index=Configuration.Environment["testflight"],
      access_token = os.environ["SANDBOX_API_TOKEN"]
  )

  api = ApiClient(configuration)
  client = TremendousApi(api)

  def test_list_campaigns(self):
    campaigns = self.client.list_campaigns().campaigns

    assert len(campaigns) > 0

    for campaign in campaigns[:10]:
        assert hasattr(campaign, "id")
        assert hasattr(campaign, "name")
        assert hasattr(campaign, "description")
        assert hasattr(campaign, "products")

  def test_get_campaign(self):
    campaign = self.client.get_campaign(CAMPAIGN_ID).campaign

    assert campaign.id == CAMPAIGN_ID
    assert len(campaign.products) == 3
    assert campaign.name == "Default Campaign"
