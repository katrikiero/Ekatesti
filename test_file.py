from playwright.sync_api import Page
def test_method(page:Page):
    page.goto("https://google.com")