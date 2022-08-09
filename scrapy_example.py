from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://example.com/')

    # Click text=More information...
    page.locator("text=More information...").click()
    page.wait_for_url("https://www.iana.org/domains/reserved")
    # ---------------------
    browser.close()
