import pytest
from playwright.sync_api import expect
#for chrome
def test_playwright_basics(playwright):
 browser=playwright.chromium.launch(headless=False)
 context=browser.new_context()
 page=context.new_page()
 #page.goto("https://rahulshettyacademy.com")

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # visible browser
    page = browser.new_page()

 #page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #page.click("sign in")"""
#page.wait_for_url("**/dashboard")

def test_playwrightshortcut(page):
 
 page.goto("https://rahulshettyacademy.com/loginpagepractise/") 


#locators
#page.get_by_role() to locate by explicit and implicit accessibility attributes.
#page.get_by_text() to locate by text content.
#page.get_by_label() to locate a form control by associated label's text.
#page.get_by_placeholder() to locate an input by placeholder.
#page.get_by_alt_text() to locate an element, usually image, by its text alternative.
#page.get_by_title() to locate an element by its title attribute.
#page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).

def test_corelocators(page):

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    
    expect(page.get_by_text("incorrect username/password")).to_be_visible()
    page.click("text=Sign In")
    page.wait_for_url("**/dashboard")
    
  
    #for firefox
"""def test_firefoxBrowser(playwright):
      
      firefoxBrowser = playwright.firefox.launch(headless=False)
      page = firefoxBrowser.new_page()
      page.goto("https://rahulshettyacademy.com/loginpagePractise/")
      
      page.get_by_label("Username").fill("rahulshettyacademy")
      page.get_by_label("Password").fill("learning")
      page.get_by_role("combobox").select_option("teach")
      page.locator("#terms").check()
      page.get_by_role("link", name="terms and conditions").click()
      page.get_by_role("button", name="Sign In").click()
    
      expect(page.get_by_text("incorrect username/password")).to_be_visible()
      page.wait_for_timeout(3000)   

"""
             