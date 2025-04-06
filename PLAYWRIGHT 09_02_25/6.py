from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    request_context = p.request.new_context()
    new_post = {"userId": 9, "title": "sample", "body": "body sample"}
    print("Wysyłamy nowy post", new_post)
    response = request_context.post("https://jsonplaceholder.typicode.com/posts", data=new_post)
    
    status = response.status
    print("Status odpowiedzi to: ", status)
    assert status == 201

    result = response.json()
    print(result)


    assert result["userId"] == 9
    assert result["title"] == "sample"
    assert result["body"] == "body sample"