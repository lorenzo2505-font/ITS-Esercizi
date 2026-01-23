from flask import Flask, url_for, request, jsonify
from abc import ABC, abstractmethod

class Device(ABC):

    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str):
        super().__init__()
        self.id = id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.setStatus(status)

    def setStatus(self, status: str): 
        self.status = status

    @abstractmethod
    def device_type(self) -> str: 
        pass

    @abstractmethod
    def base_diagnosis_time(self) -> int: 
        pass

    @abstractmethod
    def repair_complexity(self) -> int: 
        pass

    def info(self) -> dict: 
        return self.__dict__
    
    def estimated_total_time(self, factor: float = 1) -> int:

        return int((self.base_diagnosis_time() * factor) + (self.repair_complexity() * 30))

class Smartphone(Device): 

    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str, has_protective_case: bool, storage_gb: int):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb
    
    def device_type(self) -> str:
        return "smartphone"
    
    def base_diagnosis_time(self) -> int:
        return 20
    
    def repair_complexity(self):
        return 3

class Laptop(Device):

    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str, has_dedicated_gpu: bool, screen_size_inches: float):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches
    
    def device_type(self) -> str:
        return "laptop"
    
    def base_diagnosis_time(self) -> int:
        return 40 
    
    def repair_complexity(self) -> int:
        return 6
    

class ServiceCenter:

    def __init__(self):
        self.devices: dict[str, Device] = {}
    
    def add(self, device: Device) -> bool: 

        if device.id in self.devices:
            return False 
        
        self.devices[device.id] = device

        return True
    
    def get(self, device_id: str) -> Device | None: 

        if device_id not in self.devices: 
            return None 
        
        return self.devices[device_id]
    
    def update(self, device_id: str, new_device: Device):
        self.devices[device_id] = new_device
    
    def patch_status(self, device_id: str, new_status: str): 
        self.devices[device_id].setStatus(new_status)
    
    def delete(self, device_id: str) -> bool: 
        
        if device_id not in self.devices:
            return False 
        
        self.devices.pop(device_id)

        return True
    
    def list_all(self) -> list: 
        return list(self.devices.values())


iphone17: Smartphone = Smartphone("1a", "iphone17", "erald", 2025, "optimal", True, 256)
mackbook: Laptop = Laptop("2b", "mackbookpro", "esposito", 2025, "good", True, 15)
s: ServiceCenter = ServiceCenter()

s.add(iphone17)
s.add(mackbook)

app = Flask(__name__)

@app.route('/')
def home(): 
    return jsonify({"message": "Welcome to Service Center API", 
                    "links": {"devices": url_for("get_devices"), 
                               "device_by_id": url_for("get_device_by_id", id = "1a"), 
                               "estimate_factor": url_for("get_device_factor", id = "1a", factor = 1.5)}
                   })

@app.route('/devices', methods = ['GET'])
def get_devices():
    newdict: dict = {}

    for k in s.devices: 
        newdict[k] = s.devices[k].info()
    
    return jsonify(newdict), 200

@app.route('/devices/<string:id>', methods = ['GET'])
def get_device_by_id(id: str):

    if s.get(id) is None: 
        return jsonify({"error": "Device not found"}), 404
    
    return jsonify(s.devices[id].info()), 200

@app.route('/devices/<string:id>/estimate/<float:factor>', methods = ['GET'])
def get_device_factor(id: str, factor: float):

    if s.get(id) is None: 
        return jsonify({"error": "Device not found"}), 404
    
    return jsonify({"id": id, "device_type": s.devices[id].device_type(), "factor": factor, "estimated_total_minutes": s.devices[id].estimated_total_time(factor)})

@app.route('/devices', methods = ['POST'])
def post_devices():
    payload = request.get_json()

    if not payload or ("type" not in payload or (payload["type"] != "smartphone" and payload["type"] != "laptop")):
        return jsonify({"errore": "campo type obbligatorio, e deve essere uguale a smarthpone o laptop"}), 400
    
    smartphone_fields: list = ["id", "model", "customer_name", "purchase_year", "status", "has_protective_case", "storage_gb"]
    laptop_fields: list =  ["id", "model", "customer_name", "purchase_year", "status", "has_dedicated_gpu", "screen_size_inches"]

    if payload["type"] == "smartphone":

        for field in smartphone_fields:
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        smartphone: Smartphone = Smartphone(payload["id"], payload["model"], payload["customer_name"], payload["purchase_year"], payload["status"], payload["has_protective_case"], payload["storage_gb"])

        if not(s.add(smartphone)):
            return jsonify({"errore": "dispositivo già presente"}), 400
        
        
        newdict: dict = {"type": "smartphone"}
        newdict.update(smartphone.info())

        return jsonify(newdict), 201
    
    else:

        for field in laptop_fields:

            if field not in payload:
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        laptop: Laptop = Laptop(payload["id"], payload["model"], payload["customer_name"], payload["purchase_year"], payload["status"], payload["has_dedicated_gpu"], payload["screen_size_inches"])

        if not(s.add(laptop)):
            return jsonify({"errore": "dispositivo già presente"}), 400
        
        
        newdict: dict = {"type": "laptop"}
        newdict.update(laptop.info())

        return jsonify(newdict), 201

@app.route('/devices/<string:id>', methods = ['PUT'])
def put_devices(id: str):

    if s.get(id) is None:
        return jsonify({"errore": "il dispositivo non è presente"}), 404
    
    payload = request.get_json()

    if "type" not in payload or (payload["type"] != "smartphone" and payload["type"] != "laptop"):
        return jsonify({"errore": "campo type obbligatorio, e deve essere uguale a smarthpone o laptop"}), 400
    
    smartphone_fields: list = ["id", "model", "customer_name", "purchase_year", "status", "has_protective_case", "storage_gb"]
    laptop_fields: list =  ["id", "model", "customer_name", "purchase_year", "status", "has_dedicated_gpu", "screen_size_inches"]

    if payload["type"] == "smartphone":

        for field in smartphone_fields:
            
            if field not in payload: 
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        smartphone: Smartphone = Smartphone(payload["id"], payload["model"], payload["customer_name"], payload["purchase_year"], payload["status"], payload["has_protective_case"], payload["storage_gb"])
        
        s.update(id, smartphone)
        newdict: dict = {"type": "smartphone"}
        newdict.update(smartphone.info())

        return jsonify(newdict), 200
    
    else:

        for field in laptop_fields:

            if field not in payload:
                return jsonify({"errore": f"campo {field} non presente"}), 400
        
        laptop: Laptop = Laptop(payload["id"], payload["model"], payload["customer_name"], payload["purchase_year"], payload["status"], payload["has_dedicated_gpu"], payload["screen_size_inches"])
        
        s.update(id, laptop)
        newdict: dict = {"type": "laptop"}
        newdict.update(laptop.info())

        return jsonify(newdict), 200

@app.route('/devices/<string:id>/status', methods = ['PATCH'])
def patch_devices(id: str): 

    if s.get(id) is None: 
        return jsonify({"errore": "il dispositivo non esiste"}), 404
    
    payload = request.get_json()
    
    if "status" not in payload: 
        return jsonify({"errore": "campo status non presente"}), 404
    
    s.patch_status(id, payload["status"])

    return jsonify(s.devices[id].info()), 200

@app.route('/devices/<string:id>', methods = ['DELETE'])
def delete_devices(id: str):

    if s.get(id) is None: 
        return jsonify({"errore": "il dispositivo non esiste"}), 404
    
    s.devices.pop(id)

    return jsonify({"deleted": True, "id": id})




    
if __name__ == '__main__':
    app.run(debug=True)