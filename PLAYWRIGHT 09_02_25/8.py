from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    
    # Wysłanie zapytania GET
    response = request_context.get("https://jsonplaceholder.typicode.com/users/1")
    
    # Sprawdzenie statusu odpowiedzi
    status = response.status
    print("Status odpowiedzi to: ", status)
    assert status == 200, f"Expected status 200, but got {status}"

    # Odczytanie odpowiedzi jako JSON
    result = response.json()
    
    # Pobranie wartości z pola 'name'
    user_name = result["name"]
    print(f"Imię i nazwisko użytkownika: {user_name}")

    request_context.dispose()

    # Otworzenie strony wyszukiwarki Google i wyszukanie nazwiska użytkownika
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    
    page.click("button:has-text('Zaakceptuj wszystko')")
   

    page.locator("textarea").first.fill(user_name)
    page.click("input[value='Szukaj w Google']")

    page.wait_for_timeout(10000)
    browser.close()