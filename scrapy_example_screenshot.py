from playwright.sync_api import sync_playwright

# https://youtu.be/FK_5SQPq6nY

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com/')
    page.screenshot(path='/tmp/example.png')
    browser.close()
