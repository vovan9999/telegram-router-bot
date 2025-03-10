import requests

def is_router_online():
    try:
        response = requests.get("http://37.53.93.0", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

if is_router_online():
    print("Роутер в мережі!")
else:
    print("Роутер не в мережі!")
