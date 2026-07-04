import requests

base_url = "http://127.0.0.1:8000"

res = requests.get(f"{base_url}/getall")

if res.status_code == 200:
    b = res.json()
    
for i in b:
    print(i['ID'], i['Title'])