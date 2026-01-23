import requests 

url = "http://127.0.0.1:5000"

payload1 = {
    "type": "dog",
    "id": "3c", 
    "name": "scooby", 
    "age_years": 5,
    "weight_kg": 21, 
    "breed": "alano", 
    "is_trained": True
}

response = requests.post(
    f"{url}/animals/add",
    json = payload1
)

print(f"Status code: {response.status_code}")
print(f"Response JSON: {response.json()}")

payload2 = {
    "adopter_name": "Clark Kent"
}

second_response = requests.post(
    f"{url}/animals/1a/adopt", 
    json = payload2
)

print(second_response.status_code)
print(second_response.json())