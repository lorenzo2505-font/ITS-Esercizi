import requests

url = ' http://127.0.0.1:5000'

if __name__ == '__main__':

    headers = {
        "Content-type": "application/json", 
        "Accept": "application/json"
    }

    # POST

    payload1 = {
        "type": "exam",
        "booking_id": "BK-3e67",
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Neri",
        "department": "Radiologia",
        "date": "2026-02-10",
        "time": "09:15",
        "status": "scheduled",
        "exam_type": "RMN",
        "requires_fasting": True
    }

    response = requests.post(f"{url}/bookings", headers = headers, json = payload1)

    print(f"POST: {response.status_code} {response.json()}")

    # PUT

    payload2 = {
        "type": "exam",
        "booking_id": "BK-3e67",
        "patient_name": "Alessandro Popa",
        "doctor": "Dr. Raponi",
        "department": "Radiologia",
        "date": "2026-02-11",
        "time": "09:16",
        "status": "scheduled",
        "exam_type": "RMN",
        "requires_fasting": False
    }

    response = requests.put(f"{url}/bookings/BK-3e67", headers = headers, json = payload2)
    print(f"PUT: {response.status_code} {response.json()}")

    # PATCH 

    payload3 = {"status": "bho"}

    response = requests.patch(f"{url}/bookings/BK-3e67/status", headers = headers, json = payload3)
    print(f"PATCH: {response.status_code} {response.json()}")

    response = requests.delete(f"{url}/bookings/BK-3e67", headers = headers)
    print(f"DELETE: {response.status_code} {response.json()}")