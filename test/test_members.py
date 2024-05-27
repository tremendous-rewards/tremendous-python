import os
from tremendous import Configuration, ApiClient, TremendousApi

class TestMembers:
  configuration = Configuration(
     server_index=Configuration.Environment["testflight"],
      access_token = os.environ["SANDBOX_API_TOKEN"]
  )

  api = ApiClient(configuration)
  client = TremendousApi(api)

  def test_list_members(self):
    members = self.client.list_members().members

    assert len(members) > 0

    for member in members:
        assert hasattr(member, "id")
        assert hasattr(member, "email")
        assert hasattr(member, "name")
        assert hasattr(member, "role")
