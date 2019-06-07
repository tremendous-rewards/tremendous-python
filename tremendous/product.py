from http import AuthenticatedRequest

class Product(AuthenticatedRequest):

    def list(self):
        return self.request("GET", "products")["products"]

