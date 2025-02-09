from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    # Wpisanie niepoprawnej nazwy użytkownika
    page.fill("#username", "student1")
    
    # Wpisanie hasła
    page.fill("#password", "Password123")
    
    # Kliknięcie przycisku "Submit"
    page.click("#submit")

    # Sprawdzenie, czy pojawia się komunikat o błędzie
    error_message_locator = page.locator("#error")
    error_message = error_message_locator.text_content()
    print(f"Wiadomość o błędzie to: {error_message}")

    # Sprawdzenie, czy komunikat o błędzie jest zgodny z oczekiwaniami
    expected_error_message = "Your username is invalid!"
    assert expected_error_message in error_message, f"Expected '{expected_error_message}' to be in '{error_message}'"

    browser.close()