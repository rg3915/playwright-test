from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=50)
    browser = playwright.chromium.launch()  # running in background
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://github.com/
    page.goto("https://github.com/")

    # Click text=Sign in
    page.locator("text=Sign in").click()
    page.wait_for_url("https://github.com/login")

    # Click input[name="login"]
    page.locator("input[name=\"login\"]").click()

    # Fill input[name="login"]
    page.locator("input[name=\"login\"]").fill("lorem")

    # Click input[name="password"]
    page.locator("input[name=\"password\"]").click()

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("lorem")

    # Click input:has-text("Sign in")
    # page.locator("input:has-text(\"Sign in\")").click()
    # page.wait_for_url("https://github.com/session")

    # ua = page.query_selector('input[name=login_field]')
    # print(ua.inner_html())
    # print(ua.inner_text())

    ua = page.query_selector('input[name="login"]')
    print(ua.input_value())

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
