from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # browser = playwright.chromium.launch()  # running in background
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    page.goto("http://quotes.toscrape.com/")

    # Click text=Sign in
    ua = page.query_selector('//div/div/div/div/span')
    print(ua.inner_html())

    login = page.query_selector('[href="/login"]')
    login.click()

    username_input = page.query_selector('[id="username"]')
    username_input.type('lorem')

    password_input = page.query_selector('[id="password"]')
    password_input.type('admin123kkk')

    page.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
