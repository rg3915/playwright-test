from playwright.sync_api import Playwright, sync_playwright

# https://youtu.be/CK6MWehq7vI


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    # browser = playwright.chromium.launch()  # running in background
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    page.goto("http://quotes.toscrape.com/")

    login = page.query_selector('[href="/login"]')
    login.click()

    print('login...')
    username_input = page.query_selector('[id="username"]')
    username_input.type('lorem')

    password_input = page.query_selector('[id="password"]')
    password_input.type('admin123kkk')

    page.query_selector('input[type="submit"]').click()

    selector = '//*[@href="/logout"]'
    try:
        print('Prepare to logout...')
        page.wait_for_selector(selector, timeout=3000)
        print('logouted...')
    except:
        print('login failed')
        exit()

    ua = page.query_selector('//div/div/div/div/span')
    print(ua.inner_html())

    print('Waiting more 2 seconds...')
    page.wait_for_timeout(2000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
