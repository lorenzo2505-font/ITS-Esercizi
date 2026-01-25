from flask import Flask, url_for, request, jsonify
from veicoli import *

smart: Car = Car("p00pa", "smart", "lorenzo acomanni", 2025, "good", 2, False)
dante: Van = Van("vandant3", "wolks1982", "roberta cirillo", 2022, "destroyed", 3500, False)
f: FleetManager = FleetManager()

f.add(smart)
f.add(dante)

app = Flask(__name__)

@app.route('/')
def home(): 
    return jsonify({"message": "Welcome to Rent Service API", 
                    "links": {"vehicles": url_for("get_vehicles"), 
                              "vehicle_by_id": url_for("get_vehicles_by_id", id = "p00pa"), 
                              "prep_time": url_for("get_prep_time", id = "p00pa", factor = 1.5)}})

@app.route('/vehicles', methods = ['GET'])
def get_vehicles(): 
    newdict: dict = {}

    for v in f.vehicles: 
        newdict[v] = f.vehicles[v].info()
    
    return jsonify(newdict), 200 


@app.route('/vehicles/<string:id>', methods = ['GET'])
def get_vehicles_by_id(id: str): 
    
    if f.get(id) is None: 
        return jsonify({"errore": "veicolo non presente"}), 404
    
    return jsonify(f.vehicles[id].info())

@app.route('/vehicles/<string:id>/prep-time/<float:factor>', methods = ['GET'])
def get_prep_time(id: str, factor: float): 

    if f.get(id) is None: 
        return jsonify({"errore": "veicolo non presente"}), 404
    
    return jsonify({"estimated_prep_time": f.vehicles[id].estimated_prep_time(factor)}), 200

@app.route('/vehicles', methods = ['POST'])
def post_vehicles(): 
    payload = request.get_json()

    if not payload or ("type" not in payload or (payload["type"] != "car" and payload["type"] != "van")): 
        return jsonify({"errore": "il campo type è obbligatorio e deve essere uguale a car o van"}), 400
    
    car_fields: list = ["plate_id", "model", "driver_name", "registration_year", "status", "doors", "is_cabrio"]
    van_fields: list = ["plate_id", "model", "driver_name", "registration_year", "status", "max_load_kg", "require_special_license"]

    if payload["type"] == "car": 

        for field in car_fields: 
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        car: Car = Car(payload["plate_id"], payload["model"], payload["driver_name"], payload["registration_year"], payload["status"], payload["doors"], payload["is_cabrio"])
        
        if not(f.add(car)): 
            return jsonify({"errore": "veicolo già presente"})
        
        return jsonify(car.info()), 201
    
    else: 
        
        for field in van_fields: 

            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        van: Van = Van(payload["plate_id"], payload["model"], payload["driver_name"], payload["registration_year"], payload["status"], payload["max_load_kg"], payload["require_special_license"])
        
        if not(f.add(van)):
            return jsonify({"errore": "veicolo già presente"}), 400
        
        return jsonify(van.info()), 201 

@app.route('/vehicles/<string:id>', methods = ['PUT'])
def put_vehicle(id: str): 

    if f.get(id) is None: 
        return jsonify({"errore": "veicolo non presente"}), 404 
    
    payload = request.get_json()

    if not payload or ("type" not in payload or (payload["type"] != "car" and payload["type"] != "van")): 
        return jsonify({"errore": "il campo type è obbligatorio e deve essere uguale a car o van"}), 400
    
    car_fields: list = ["plate_id", "model", "driver_name", "registration_year", "status", "doors", "is_cabrio"]
    van_fields: list = ["plate_id", "model", "driver_name", "registration_year", "status", "max_load_kg", "require_special_license"]

    if payload["type"] == "car": 

        for field in car_fields: 
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        car: Car = Car(payload["plate_id"], payload["model"], payload["driver_name"], payload["registration_year"], payload["status"], payload["doors"], payload["is_cabrio"])
        
        if car.plate_id != id: 
            return jsonify({"errore": "l'id non può cambiare"}), 400
        
        f.update(id, car)

        return jsonify(car.info()), 200 
    
    else: 
        
        for field in van_fields: 

            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        van: Van = Van(payload["plate_id"], payload["model"], payload["driver_name"], payload["registration_year"], payload["status"], payload["max_load_kg"], payload["require_special_license"])
        
        if van.plate_id != id: 
            return jsonify({"errore": "l'id non può cambiare"})
        
        f.update(id, van)

        return jsonify(van.info()), 200

@app.route('/vehicles/<string:id>/status', methods = ['PATCH'])
def patch_vehicle(id: str): 

    if f.get(id) is None: 
        return jsonify({"errore": "veicolo non presente"}), 404 
    
    payload = request.get_json()

    if "status" not in payload: 
        return jsonify({"errore": "campo status non presente"})
    
    f.patch_status(id, payload["status"])

    return jsonify({"modifica effettuata": f"nuovo status: {payload['status']}"}), 200

@app.route('/vehicles/<string:id>', methods = ['DELETE'])
def delete_vehicle(id: str): 

    if f.get(id) is None: 
        return jsonify({"errore": "veicolo non presente"}), 404 
    
    f.vehicles.pop(id)

    return jsonify({"deleted": True, "id": id}), 200


        
    



    


if __name__ == '__main__':
    app.run(debug = True)



