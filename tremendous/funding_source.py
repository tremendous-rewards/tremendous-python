from http import AuthenticatedRequest

class FundingSource(AuthenticatedRequest):

    def list(self):
        return self.request("GET", "funding_sources")["funding_sources"]

    def show(self, id):
        return self.request("GET", "funding_sources/{}".format(id))["funding_source"]
