from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.onet.pl")
    page_title = page.title()
    print(f"Tytuł strony to {page_title}")

    assert "Onet – Jesteś na bieżąco" in page_title

    browser.close()