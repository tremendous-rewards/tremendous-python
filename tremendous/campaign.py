from http import AuthenticatedRequest

class Campaign(AuthenticatedRequest):

    def list(self):
        return self.request("GET", "campaigns")["campaigns"]

    def show(self, id):
        return self.request("GET", "campaigns/{}".format(id))["campaign"]

