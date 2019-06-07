from campaign import Campaign
from funding_source import FundingSource
from member import Member
from order import Order
from organization import Organization
from product import Product
from reward import Reward

class Tremendous(object):

    def __init__(self, access_token, domain="https://testflight.tremendous.com"):
        if not access_token:
            raise Exception("Access token required for Tremendous API")

        self.campaigns = Campaign(access_token, domain)
        self.members = Member(access_token, domain)
        self.orders = Order(access_token, domain)
        self.organizations = Organization(access_token, domain)
        self.products = Product(access_token, domain)
        self.rewards = Reward(access_token, domain)
        self.funding_sources = FundingSource(access_token, domain)
