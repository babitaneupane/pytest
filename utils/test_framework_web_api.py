import pytest
import json
import requests

from playwright.sync_api import Playwright, expect
from pageobjects.login import LoginPage
from pageobjects.dashboard import Dashboardpage
from utils.apiBaseFramework import APIUtils

BASE_URL = "https://rahulshettyacademy.com"

# Load credentials for parametrization
def load_credentials():
    with open("data/credentials.json") as f:
        test_data = json.load(f)
        return test_data.get('user_credentials', [])

user_credentials_list = load_credentials()


class APIUtils:


    def getToken(self, user_credentials):
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]

        response = requests.post(
            f"{BASE_URL}/api/ecom/auth/login",
            data={
                "userEmail": user_email,
                "userPassword": user_password,
            },
        )

        print(response.json())
        return response.json().get("token")

    def create_order(self, user_credentials, orders_payload):
        token = self.getToken(user_credentials)

        response = requests.post(
            f"{BASE_URL}/api/ecom/order/create-order",
            data=json.dumps(orders_payload),
            headers={
                "Authorization": token,
                "Content-Type": "application/json",
            },
        )

        responseBody = response.json()
        print(responseBody)
        return responseBody.get("orders")[0]


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright, page, user_credentials):

    userName = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    # Define the order payload
    orders_payload = [
         {
                "country": "India",
                "productOrderedId": "6960eae1c941646b7a8b3ed3"
            }
    ]
           
        

    # Create order via API
    api_utils = APIUtils()
    orderId = api_utils.create_order(
        user_credentials,
        orders_payload,
    )

    print(f"[INFO] Created order with ID: {orderId}")

    # Navigate to login page
    loginpage = LoginPage(page)
    loginpage.navigate()
    dashboardpage = loginpage.login(userName, password)

    # Navigate to Orders and view the specific order
    page.wait_for_load_state("networkidle")
    orderHistoryPage = dashboardpage.selectOrdersNavLink()
    page.wait_for_load_state("networkidle")
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)

    page.wait_for_load_state("networkidle")

    # Verify success message
    success_element = page.locator(".tagline")
    expect(success_element).to_contain_text("Thank you for Shopping With Us")

    print("[SUCCESS] Test passed! Found thank you message")
