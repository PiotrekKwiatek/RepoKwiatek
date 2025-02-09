from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    request_context = p.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
    status = response.status

    print("Status odpowiedzi to: ", status)
    assert status == 200

    body = response.json()
    print(body)

    id = body["id"]
    userid = body["userId"]
    print("Id to: ", id)
    print("UserId to: ", userid)   

    assert id == 1
    assert userid == 1 

    title = body["title"]
    print("Typ title to string: ", isinstance(title,bool))
    assert isinstance(title, bool)