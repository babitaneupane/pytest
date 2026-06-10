
from playwright.sync_api import Playwright, expect


class APIUtils:

 def getToken(self, playwright):
  api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
  response = api_request_context.post("/api/ecom/auth/login",
                                     data={"userEmail": "test@example.com",
                                           "userPassword": "Test@123"})
  assert response.ok
  print(response.text())
  responseBody = response.json()  
  return responseBody.get("token")

 def create_order(self, playwright, ordersPayLoad):
    token = self.getToken(playwright)
    api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
    response = api_request_context.post(url="/api/ecom/order/create-order",
                                      data={"orders": ordersPayLoad},
                                      headers={"Authorization": token,
                                               "content-type": "application/json"})
    print(response.json())
    response_body=response.json()
    if "orders" in response_body:
        orderId=response_body["orders"][0]
    else:
        print(f"Error creating order: {response_body}")
        return None
    return orderId


def test_e2e_web_api(playwright):
 browser=playwright.chromium.launch(headless=False)
 context=browser.new_context()
 page=context.new_page()


 #create order
 api_utils=APIUtils()
 ordersPayLoad = [{"country": "India", "productOrderedId": "6262e95dfa7f514aac6721cd"}]
 orderId=api_utils.create_order(playwright, ordersPayLoad)

 if not orderId:
    print("Order creation failed, skipping test")
    return

 #login
 page.goto("https://rahulshettyacademy.com/client")
 page.wait_for_load_state()
 page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
 page.get_by_placeholder("password").fill("Iamking@000")
 page.get_by_role("button",name="login").click()

 page.get_by_role("button",name="orders").click()

 #orders history page
 row = page.locator("tr").filter(has_text=orderId)
 row.get_by_role("button",name="view").click()
 expect(page.locator(".tagline")).to.contain_text("thankyou for choosing us")
 context.close()