import requests 

url = "http://127.0.0.1:5000"

def test_post(): 
    payload = {
        "type": "car",
        "plate_id": "XX999YY",
        "model": "Fiat 500 Cabrio",
        "driver_name": "Mario Rossi",
        "registration_year": 2022,
        "status": "available",
        "doors": 3,
        "is_cabrio": True
    }

    response = requests.post(
        url = f"{url}/vehicles", 
        json = payload
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")


def test_put():
    payload = {
        "type": "car",
        "plate_id": "XX999YY",
        "model": "Fiat 500 Cabrio",
        "driver_name": "Alessandro Colella",
        "registration_year": 2026,
        "status": "available",
        "doors": 4,
        "is_cabrio": True
    }

    response = requests.put(
        url = f"{url}/vehicles/XX999YY", 
        json = payload
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

def test_patch(): 
    payload = {"status": "rented"}

    response = requests.patch(
        url = f"{url}/vehicles/XX999YY/status",
        json = payload
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")


def test_delete(): 
    response = requests.delete(
        url = f"{url}/vehicles/XX999YY"
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

    


if __name__ == '__main__': 
    
    test_post()
    test_put()
    test_patch()
    test_delete()