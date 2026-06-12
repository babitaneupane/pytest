from .dashboard import Dashboardpage


class LoginPage:

    def __init__(self,page):
     self.page =page
     

    def navigate(self):
     self.page.goto("https://rahulshettyacademy.com/client")
                    

    def login(self,userEmail,userpassword):
     self.page.get_by_placeholder("email@example.com").fill(userEmail)
     self.page.get_by_placeholder("enter your passsword").fill(userpassword)
     self.page.get_by_role("button",name="Login").click()
     dashboardpage = Dashboardpage(self.page)
     return dashboardpage