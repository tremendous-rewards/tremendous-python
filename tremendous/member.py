from http import AuthenticatedRequest

class Member(AuthenticatedRequest):

    def create(self, data):
        return self.request("POST", "members", data)["member"]

    def list(self):
        return self.request("GET", "members")["members"]

    def show(self, id):
        return self.request("GET", "members/{}".format(id))["member"]
