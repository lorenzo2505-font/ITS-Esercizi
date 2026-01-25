import requests 
import json 

url = 'http://127.0.0.1:5000'

if __name__ == '__main__':
    
    headers = {
        "Content-type": "application/json", 
        "Accept": "application/json"
    }
    # POST
    payload1 = {
        "type": "camera",
        "serial_number": "SN-3e67",
        "brand": "Philips",
        "room": "Living Room",
        "installation_year": 2022,
        "status": "online",
        "resolution": 3,
        "night_vision": True
    }

    response = requests.post(f"{url}/devices", headers = headers, json = payload1)
    print(f"POST: {response.status_code} {response.json()}")

    # PUT

    payload2 = {
        "type": "camera",
        "serial_number": "SN-3e67",
        "brand": "Canon",
        "room": "Kitchen",
        "installation_year": 2023,
        "status": "good",
        "resolution": 3,
        "night_vision": False
    }

    response = requests.put(f"{url}/devices/SN-3e67", headers = headers, json = payload2)
    print(f"PUT: {response.status_code} {response.json()}")

    # PATCH 

    payload3 = {"status": "mid"}

    response = requests.patch(f"{url}/devices/SN-3e67/status", headers = headers, json = payload3)
    print(f"PATCH: {response.status_code} {response.json()}")

    # DELETE

    response = requests.delete(f"{url}/devices/SN-3e67", headers = headers)
    print(f"DELETE: {response.status_code} {response.json()}") 



