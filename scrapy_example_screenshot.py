from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com/')
    page.screenshot(path='/tmp/example.png')
    browser.close()
