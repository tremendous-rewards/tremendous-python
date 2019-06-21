from tremendous.campaign import Campaign
from tremendous.funding_source import FundingSource
from tremendous.member import Member
from tremendous.order import Order
from tremendous.organization import Organization
from tremendous.product import Product
from tremendous.reward import Reward
from tremendous.webhook import Webhook

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
        self.webhooks = Webhook(access_token, domain)
