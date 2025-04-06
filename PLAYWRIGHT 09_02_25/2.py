from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")
    page.wait_for_url("**/logged-in-successfully/")
    success_message = "Logged In Successfully"
    messege = page.text_content("h1")
    print(f"Wiadomość o sukcesie to: {messege}")

    page_url = page.url
    assert page.url in "https://practicetestautomation.com/logged-in-successfully/"

    assert success_message in messege, f"Expected '{success_message}' to be in '{messege}'"

    locator_logout = page.locator("text=Log out")
    is_visible = locator_logout.is_visible()
    print(f"Element 'Log out' widoczny: {is_visible}")
    assert is_visible, "Element 'Log out' nie jest widoczny"

    browser.close()