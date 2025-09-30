import re
from playwright.sync_api import expect 
from playwright.sync_api import Page


def test_google_search(page: Page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("no popup to accept")
    page.get_by_role("combobox", name= "Search").fill("Playwright Python")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright1",re.IGNORECASE))
        
