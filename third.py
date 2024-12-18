import requests


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "тестовый post запрос",
    "body" : "тестовый контент post запрос",
    "foo" : "ещё один тестовый запрос",
    "userId" : 2
}

response = requests.post(url, data=data)

print(response.status_code)

print(f"ответ - {response.json()}")