from tremendous.http import AuthenticatedRequest

class Invoice(AuthenticatedRequest):
    def create(self, data):
        return self.request("POST", "invoices", data)["invoice"]

    def list(self):
        return self.request("GET", "invoices")["invoices"]

    def show(self, id):
        return self.request("GET", "invoices/{}".format(id))["invoice"]

    def destroy(self, id):
        return self.request("DELETE", "invoices/{}".format(id))["invoice"]
