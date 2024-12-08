import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
#print(response)
#print(response.status_code)
if response.status_code == 200:
    print("Jupi! Strona jest OK")
    print("Dane uzytkownikow to: ", response.json())
else:
    print(f"Ups, cos poszło nie tak, kod błedu to: {response.status_code}")