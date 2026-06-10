from playwright.sync_api import  expect


fakePayloadOrderResponse = {"data": [], "message": "No Orders"}

def interceptRequest(route):
    route.continue_(url=" ")


def test_Network_2(page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role(  "button", name="Login").click()
    page.get_by_role(  "button", name="ORDERS").click()
    page.get_by_role(  "button", name="view").first.click()
    message = page.locator(".blink_me").ext_content()
    print(message)

    def test_session_storage(playwright):
     api_utils = api_utils()
     Token=api_utils.getToken(playwright)
     browser=playwright.chromium.launch(headless=False)
     context=browser.new_context()
     page=context.new_page()

   #script
     page.add_init_script("""localStorage.setItem('token','{getToken}')""")
     page.goto("https://rahulshettyacademy/client")
     page.get_by_role("button",name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
