import os
from tremendous import Configuration, ApiClient, TremendousApi

class TestInvoices:
  configuration = Configuration(
     server_index=Configuration.Environment["testflight"],
      access_token = os.environ["SANDBOX_API_TOKEN"]
  )

  api = ApiClient(configuration)
  client = TremendousApi(api)

  def test_list_invoices(self):
    invoices = self.client.list_invoices().invoices

    assert len(invoices) > 0

    for invoice in invoices:
        assert hasattr(invoice, "id")
        assert hasattr(invoice, "po_number")
        assert hasattr(invoice, "amount")
        assert hasattr(invoice, "created_at")
