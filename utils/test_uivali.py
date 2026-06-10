from playwright.sync_api import Page, expect

def test_uivalidationDynamicScript(page):
#iphone_x, Nokia_Edge
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone x")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")


    with page.expect_popup() as newpage_info:
      page.locator(".blinkingText").click()   #new page
      childPage = newpage_info.value
      text =childPage.locator(".red").text_content()
    print(text)
    words = text.split("at")
    email = words[1].strip().split("")[0]  
    assert email =="mentor@rahulshettyacademy.com"

