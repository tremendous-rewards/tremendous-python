from tremendous.http import AuthenticatedRequest

class Webhook(AuthenticatedRequest):

    def create(self, url, data={}):
        return self.request("POST", "webhooks", {
          "url": url
        })["webhook"]

    def list(self):
        return self.request("GET", "webhooks".format(id))["webhooks"]

    def show(self, id):
        return self.request("GET", "webhooks/{}".format(id))["webhook"]

    def events(self, id):
        return self.request("GET", "webhooks/{}/events".format(id))["events"]


