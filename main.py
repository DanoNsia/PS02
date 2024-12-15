import requests
import pprint

r = requests.get("https://api.github.com")
print(r.status_code)
print(r.text)
r_json = r.json()
pprint.pprint(r_json)