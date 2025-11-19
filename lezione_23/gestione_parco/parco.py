from flask import Flask, jsonify, url_for
from abc import ABC, abstractmethod

class Ride(ABC):
    
    def __init__(self, id: str, name: str, min_height_cm: int):
        super().__init__()
        self.id = id
        self.name = name 
        self.min_height_cm = min_height_cm
    
    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def base_wait(self):
        pass

    def info(self) -> dict:
        return {"id": self.id, "name": self.name, "min height cm": self.min_height_cm}
    
    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return int(self.base_wait() * crowd_factor)

class RollerCoaster(Ride):

    def __init__(self, id: str, name: str, min_height_cm: int, inversions: int):
        super().__init__(id, name, min_height_cm)
        self.inversions = inversions
    
    def category(self) -> str:
        return "roller coaster"
    
    def base_wait(self) -> int:
        return 40 
    
    def info(self) -> dict:
        return super().info() | {"inversions": self.inversions}


class Carousel(Ride):

    def __init__(self, id: str, name: str, min_height_cm: int):
        super().__init__(id, name, min_height_cm)
        self.animals: list[str] = ["horse", "swan", "tiger"]
    
    def category(self) -> str:
        return "family"
    
    def base_wait(self) -> int:
        return 10
    
    def info(self):
        return super().info() | {"animals": self.animals}

class Park:
    
    def __init__(self):
        self.rides: dict[str, Ride] = {}
    
    def add(self, ride: Ride):
        
        if ride.id in self.rides:
            raise ValueError("l'attrazione è già presente all'interno del parco")
        
        self.rides[ride.id] = ride
    
    def get(self, ride_id: str) -> Ride|None:

        if ride_id not in self.rides:
            return None
        
        return self.rides[ride_id]
    
    def list_all(self):
        mylist: list[str] = []
        
        for k in self.rides:
            mylist.append(self.rides[k].name)


p: Park = Park()
r: RollerCoaster = RollerCoaster("1", "shock", 150, 4)
c: Carousel = Carousel("2", "bioparco", 110)
p.add(r)
p.add(c)



app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"description": "Welcome to API Park", 
                    "attrazzioni": url_for("get_rides"), 
                    "attrazione specifica": url_for("get_ride_id", id = "1"), 
                    "tempi di attesa": url_for("get_waiting", id = "1", crowd = 1.0)})

@app.route('/rides', methods = ['GET'])
def get_rides():
    newdict: dict[str, dict[str, str|int]] = {}

    for k in p.rides:
        newdict[k] = p.rides[k].info()
    
    return jsonify(newdict), 200

@app.route('/rides/<string:id>', methods = ['GET'])
def get_ride_id(id: str):
    
    if p.get(id) is None:
        return None
    
    return jsonify(p.get(id).info())

@app.route('/rides/<string:id>/wait', defaults = {"crowd": 1.0})
@app.route('/rides/<string:id>/wait/<float:crowd>', methods = ['GET'])
def get_waiting(id: str, crowd: float):
    return jsonify({"wait": p.get(id).wait_time(crowd)})


    


if __name__ == '__main__':
    app.run(debug=True)


    



