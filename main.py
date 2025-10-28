import requests

response = requests.get("https://api.github.com")
print("Статус:", response.status_code)
print("Тип данных:", response.headers["Content-Type"])
print("Первые 200 символов ответа:")
print(response.text[:200])
