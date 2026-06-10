from .orderHistory import orderHstorypage

class Dashboardpage:
    
    def __init__(self,page):
     self.page=page


    def selectOrdersNavLink(self):
      self.page.get_by_role("button", name="ORDERS").click()
      orderHistoryPage = orderHstorypage(self.page)
      return orderHistoryPage