from playwright.sync_api import expect

class OrderDetailsPage:
    

    def __init__(self,page):
       self.page=page

    def verifyOrderMessange(self,page):
        expect(self.page.locator(".tagline")).to_contain_text("Thankyou for choosing us")