from http import AuthenticatedRequest

class Reward(AuthenticatedRequest):

    def show(self, id):
        return self.request("GET", "rewards/{}".format(id))["reward"]

