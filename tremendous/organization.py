from http import AuthenticatedRequest

class Organization(AuthenticatedRequest):

    def create(self, data):
      return self.request("POST", "organizations", data)["organization"]

    def list(self):
        return self.request("GET", "organizations")["organizations"]

    def show(self, id):
        return self.request("GET", "organizations/{}".format(id))["organization"]
