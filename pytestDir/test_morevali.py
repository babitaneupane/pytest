import time

from playwright.sync_api import sync_playwright, expect
from playwright.sync_api._generated import Page


def test_UIChecks(page: Page):

    #hude/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

#AlertBoxes
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="confirm").click()
    time.sleep(4)


   #mousehover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="top").click()
    

    #framehandling
    pageframe= page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link" , name="All Access plan").click()
    expect(pageframe.locator("body")).to_contain_text("happy subscribers")
   

    #Check the price of rice is equal to 37
    #identify the price column
    #identify rice row
    # extract the price of the rice.
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            pricecolValue = index
            print(f"Price column value is {pricecolValue}")
            break

    riceRow =page.locator("tr").filter(has_text="Rice")
    expect( page.locator("td").nth(pricecolValue)).to_have_text("37")