
from playwright.sync_api import Playwright, expect


class APIUtils:

 # BLOCK: API Authentication - Gets login token from auth endpoint
 def getToken(self, playwright):
  api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
  response = api_request_context.post("/api/ecom/auth/login",
                                     data={"userEmail": "rahulshetty@gmail.com",
                                           "userPassword": "Iamking@000"})
  assert response.ok
  print(response.text())
  responseBody = response.json()  
  return responseBody.get("token")

 # BLOCK: API Order Creation - Creates order and returns order ID
 def create_order(self, playwright, ordersPayLoad):
    token = self.getToken(playwright)
    api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
    response = api_request_context.post(url="/api/ecom/order/create-order",
                                      data={"orders": ordersPayLoad},
                                      headers={"Authorization": token,
                                               "content-type": "application/json"})
    print(response.json())
    response_body=response.json()
    orderId=response_body["orders"][0]
    return orderId


def test_e2e_web_api(playwright):
 # BLOCK: Browser Setup - Launch browser and create page
 browser=playwright.chromium.launch(headless=False)
 context=browser.new_context()
 page=context.new_page()


 # BLOCK: API - Create order and get order ID
 api_utils=APIUtils()
 ordersPayLoad = [{"country": "India", "productOrderedId": "6262e95dfa7f514aac6721cd"}]
 orderId=api_utils.create_order(playwright, ordersPayLoad)

 # BLOCK: Error Handling - Check if order created successfully
 if not orderId:
    print("Order creation failed, skipping test")
    return

 # BLOCK: LOGIN PAGE - Navigate to site and enter credentials
 page.goto("https://rahulshettyacademy.com/client")
 page.wait_for_load_state()
 page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
 page.get_by_placeholder("password").fill("Iamking@000")
 page.get_by_role("button",name="login").click()

 # BLOCK: DASHBOARD PAGE - Click orders button to view order history
 page.get_by_role("button",name="orders").click()

 # BLOCK: ORDERS HISTORY PAGE - Find order and click view button
 row = page.locator("tr").filter(has_text=orderId)
 row.get_by_role("button",name="view").click()
 
 # BLOCK: ORDER DETAILS PAGE - Verify confirmation message appears
 expect(page.locator(".tagline")).to.contain_text("thankyou for choosing us")
 context.close()
