from smarthome import *
from flask import Flask, jsonify, url_for, request

pixar: SmartBulb = SmartBulb("nov95", "pixar", "bedroom", 1995, "good", 10, False)
fazbear_pizza: SecurityCamera = SecurityCamera("bite87", "fazbear entertainment", "r0", 1987, "optimal", "1080p", True)
iot_hub: IoTHub = IoTHub()

iot_hub.add(pixar)
iot_hub.add(fazbear_pizza)


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Smart Home Hub API", 
                    "links": {"devices": url_for("get_devices"), 
                              "devices_serial": url_for("get_devices_by_serial", serial = "nov95"), 
                              "diagnostic": url_for("get_diagnostic", serial = "bite87", factor = 1.5)}})

@app.route('/devices', methods = ['GET'])
def get_devices(): 
    newdict: dict = {}

    for d in iot_hub.devices: 
        newdict[d] = iot_hub.devices[d].info()
    
    return jsonify(newdict), 200

@app.route('/devices/<string:serial>', methods = ['GET'])
def get_devices_by_serial(serial: str): 
    
    if iot_hub.get(serial) is None: 
        return jsonify({"errore": "il dispositivo non esiste"}), 404
    
    return jsonify(iot_hub.devices[serial].info()), 200 

@app.route('/devices/<string:serial>/diagnostic/<float:factor>', methods = ['GET'])
def get_diagnostic(serial: str, factor: float):
    
    if iot_hub.get(serial) is None: 
        return jsonify({"errore": "Il dispositivo non esiste"}), 404
    
    return jsonify({"id": serial, "device_type": iot_hub.devices[serial].device_type(), "factor": factor, "diagnostic_seconds": iot_hub.devices[serial].diagnostici_time(factor)}), 200

@app.route('/devices', methods = ['POST'])
def post_devices(): 
    payload = request.get_json()

    if "type" not in payload or (payload["type"] != "bulb" and payload["type"] != "camera"): 
        return jsonify({"errore": "il campo type è obbligatorio e deve essere uguale a bulb o camera"}), 400
    
    bulb_fields: list = ["serial_number", "brand", "room", "installation_year", "status", "brightness_lumens", "color_capability"]
    camera_fields: list = ["serial_number", "brand", "room", "installation_year", "status", "resolution", "night_vision"]

    if payload["type"] == "bulb": 
        
        for field in bulb_fields: 
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        bulb: SmartBulb = SmartBulb(payload["serial_number"], payload["brand"], payload["room"], payload["installation_year"], payload["status"], payload["brightness_lumens"], payload["color_capability"])

        if not(iot_hub.add(bulb)): 
            return jsonify({"errore": "dispositivo già presente"}), 400 
        
        return jsonify(bulb.info()), 201
    
    else:

        for field in camera_fields: 
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        camera: SecurityCamera = SecurityCamera(payload["serial_number"], payload["brand"], payload["room"], payload["installation_year"], payload["status"], payload["resolution"], payload["night_vision"])

        if not(iot_hub.add(camera)): 
            return jsonify({"errore": "dispositivo già presente"}), 400 
        
        return jsonify(camera.info()), 201

@app.route('/devices/<string:serial>', methods = ['PUT'])
def put_devices(serial: str): 

    if iot_hub.get(serial) is None: 
        return jsonify({"errore": "il dispositivo non esiste"}), 404
    
    payload = request.get_json()
    
    if "type" not in payload or (payload["type"] != "bulb" and payload["type"] != "camera"): 
        return jsonify({"errore": "il campo type è obbligatorio e deve essere uguale a bulb o camera"}), 400
    
    bulb_fields: list = ["serial_number", "brand", "room", "installation_year", "status", "brightness_lumens", "color_capability"]
    camera_fields: list = ["serial_number", "brand", "room", "installation_year", "status", "resolution", "night_vision"]

    if payload["type"] == "bulb": 
        
        for field in bulb_fields: 
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        bulb: SmartBulb = SmartBulb(payload["serial_number"], payload["brand"], payload["room"], payload["installation_year"], payload["status"], payload["brightness_lumens"], payload["color_capability"])

        if serial != bulb.serial_number: 
            return jsonify({"errore": "serial_number è univoco e non può cambiare"}), 400
        
        iot_hub.update(serial, bulb)

        return jsonify(bulb.info()), 200
    
    else:

        for field in camera_fields: 
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        camera: SecurityCamera = SecurityCamera(payload["serial_number"], payload["brand"], payload["room"], payload["installation_year"], payload["status"], payload["resolution"], payload["night_vision"])

        if serial != camera.serial_number:
            return jsonify({"errore": "serial_number è univoco e non può cambiare"}), 400
        
        iot_hub.update(serial, camera)

        return jsonify(camera.info()), 200

@app.route('/devices/<string:serial>/status', methods = ['PATCH'])
def patch_devices(serial: str): 

    if iot_hub.get(serial) is None: 
        return jsonify({"errore": "il dispositivo non esiste"}), 404

    payload = request.get_json()

    if "status" not in payload: 
        return jsonify({"errore": "campo status non presente"}), 400
    
    iot_hub.patch_status(serial, payload["status"])
    
    return jsonify({"new status": payload["status"]}), 200

@app.route('/devices/<string:serial>', methods = ['DELETE'])
def delete_devices(serial: str): 

    if iot_hub.get(serial) is None: 
        return jsonify({"errore": "il dispositivo non esiste"}), 404 
    
    iot_hub.devices.pop(serial)
    
    return jsonify({"deleted": True, "serial_number": serial}), 200
    

    






if __name__ == '__main__': 

    app.run(debug = True)