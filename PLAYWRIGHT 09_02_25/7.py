from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    
    # Wysłanie zapytania GET
    response = request_context.get("https://jsonplaceholder.typicode.com/posts")
    
    # Sprawdzenie statusu odpowiedzi
    status = response.status
    print("Status odpowiedzi to: ", status)
    assert status == 200, f"Expected status 200, but got {status}"

    # Odczytanie odpowiedzi jako JSON
    result = response.json()
    
    # Sprawdzenie, ile elementów znajduje się w odpowiedzi
    num_elements = len(result)
    print(f"Liczba elementów w odpowiedzi: {num_elements}")
    assert num_elements > 0, "Expected more than 0 elements in the response"

    request_context.dispose()