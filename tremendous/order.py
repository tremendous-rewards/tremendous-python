from http import AuthenticatedRequest

class Order(AuthenticatedRequest):

    def create(self, data):
        return self.request("POST", "orders", data)["order"]

    def show(self, id):
        return self.request("GET", "orders/{}".format(id), data)["order"]

