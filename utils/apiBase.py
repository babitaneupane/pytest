import playwright.sync_api 
import playwright


ordersPayLoad={"orders":[{"country":"India","productorderid":"6581ca399fd99c85e8ee7f45"}]}

class APIUtils:


    def getToken(self, playwright, user_credentials):
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"},
        )

        assert response.ok
        print(response.json())
        responseBody = response.json()  
        return response.json().get("token")

def createOrder(self, playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                            data=ordersPayLoad,
                                            headers={"Authorization": token,
                                                     "content-type": "application/json"
                                                     })
        
        print(response.json())
        responseBody = response.json()
        orderId = responseBody["order"][0]

        return orderId


     