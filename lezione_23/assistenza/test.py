import requests 

url = "http://127.0.0.1:5000"

def test_post(): 
    payload = {
        "type": "smartphone",
        "id": "d3",
        "model": "Galaxy S21",
        "customer_name": "Mario Rossi",
        "purchase_year": 2021,
        "status": "received",
        "has_protective_case": True,
        "storage_gb": 128
    }

    response = requests.post(
        f"{url}/devices",
        json = payload
    )

    print(f"Status code: {response.status_code}")
    print(f"response JSON: {response.json()}")


def test_put(): 
    payload = {
        "type": "smartphone",
        "id": "d3",
        "model": "Galaxy S22",
        "customer_name": "Alessandro Popa",
        "purchase_year": 2022,
        "status": "broken",
        "has_protective_case": False,
        "storage_gb": 200
    }

    response = requests.put(
        f"{url}/devices/d3",
        json = payload
    )

    print(f"Status code: {response.status_code}")
    print(f"response JSON: {response.json()}")

def test_patch(): 
    payload = {"status": "fixed"}

    response = requests.patch(
        f"{url}/devices/d3/status",
        json = payload
    )

    print(f"Status code: {response.status_code}")
    print(f"response JSON: {response.json()}")

def test_delete(): 
    response = requests.delete(
        f"{url}/devices/d3"
    )

    print(f"Status code: {response.status_code}")
    print(f"response JSON: {response.json()}")



if __name__ == '__main__': 
    
    test_post()
    test_put()
    test_patch()
    test_delete()

