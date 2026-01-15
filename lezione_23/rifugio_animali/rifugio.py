from flask import Flask, jsonify, url_for
from abc import ABC, abstractmethod
import requests 
import json

class Animal(ABC):
    
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float):
        super().__init__()
        self.id = id 
        self.name = name 
        self.age_years = age_years
        self.weight_kg = weight_kg

    
    @abstractmethod
    def species(self) -> str:
        pass


    @abstractmethod
    def daily_food_grams(self) -> float:
        pass

    def info(self) -> dict:
        return {"id": self.id, "name": self.name, "age_years": self.age_years, "weight_kg": self.weight_kg}
    
    def bmi_like(self) -> float:
        return self.weight_kg / (self.age_years + 1)


class Dog(Animal):

    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool):
        super().__init__(id, name, age_years, weight_kg)
        self.breed = breed 
        self.is_trained = is_trained
    
    def species(self) -> str:
        return "dog"
    
    def daily_food_grams(self) -> float:
        return 200 + self.age_years * 50 
    
    def info(self) -> dict:
        return super().info() | {"breed": self.breed, "is_trained": self.is_trained}


class Cat(Animal):

    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, indoor_only: bool, favorite_toy: str):
        super().__init__(id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy
    
    def species(self) -> str:
        return "cat"
    
    def daily_food_grams(self) -> float:
        return 100 + self.age_years * 30
    
    def info(self) -> dict:
        return super().info() | {"indoor_only": self.indoor_only, "favorite_toy": self.favorite_toy}


class Shelter:

    def __init__(self):
        self.animals: dict[str, Animal] = {}
        self.adoptions: dict[str, str] = {}
    
    def add(self, animal: Animal):
        
        if animal.id in self.animals: # se l'animale è già presente nel dizionario, non sovrascrivo, ma semplicemente ignoro il fatto
            pass

        else:
            self.animals[animal.id] = animal
    
    def get(self, animal_id: str) -> Animal | None:
        
        if animal_id not in self.animals:
            return None
        
        return self.animals[animal_id]
    
    def list_all(self) -> list[Animal]:
        return list(self.animals.values())
    
    def is_adopted(self, animal_id: str) -> bool:
        
        if animal_id in self.adoptions:
            return True
        
        return False 
    
    def set_adopted(self, animal_id: str, adopter_name: str):

        if not(self.is_adopted(animal_id)):
            self.adoptions[animal_id] = adopter_name
        
        else:
            pass


d: Dog = Dog("1A", "Krypto", 5, 10, "cane kryptoniano", True)
c: Cat = Cat("2A", "Romeo", 10, 4, True, "tiragraffi")
s: Shelter = Shelter()

#payload: dict = { "type": "cat", "id": "c5", "name": "Silvestro", "age_years": 3, "weight_kg": 4.2, "indoor_only": True, "favorite_toy": "ball" }

s.add(d)
s.add(c)


app = Flask(__name__) 

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Animal Shelter API", 
                    "animali": url_for("get_animals"),
                    "animale specifico": url_for("get_animal_by_id", id = "1A"),
                    "cibo giornaliero": url_for("get_animal_food", id = "1A"),
                    "è adottato ?": url_for("get_animal_adoption", id = "1A")})

@app.route('/animals', methods = ['GET'])
def get_animals():
    newdict: dict = {}

    for k in s.animals:
        newdict[k] = s.animals[k].info()
    
    return jsonify(newdict), 200

@app.route('/animals/<string:id>', methods = ['GET'])
def get_animal_by_id(id: str):

    if s.get(id) is None:
        return None 
    
    return jsonify(s.get(id).info())

@app.route('/animals/<string:id>/food', methods = ['GET'])
def get_animal_food(id: str):

    if s.get(id) is None:
        return None 
    
    return jsonify({"id": s.get(id).id, "daily_food_grams": s.get(id).daily_food_grams()})

@app.route('/animals/<string:id>/adoption', methods = ['GET'])
def get_animal_adoption(id: str):

    if s.get(id) is None: 
        return None 
    
    if s.is_adopted(id):
        return jsonify({"id": s.get(id).id, "adopted": True, "adopter_name": s.adoptions[s.get(id)]})
    
    return jsonify({"id": s.get(id).id, "adopted": False})


@app.route('/animals/add', methods = ['POST'])
def add_animals():

    payload = requests.get_json()

    if ("type" in payload) and (payload["type"] == "dog" or payload["type"] == "cat"): 

        if (payload["type"] == "dog"):
            dog_fields: list = ["id", "name", "age_years", "weight_kg", "breed", "is_trained"]

            for el in dog_fields:
                
                if el not in dog_fields:
                    raise KeyError(f"campo: {el} non presente")
            
            dog: Dog = Dog(payload["id"], payload["name"], payload["age_years"], payload["weight_kg"], payload["breed"], payload["is_trained"])

            s.add(dog)

            return jsonify({"status": "ok", "added": dog.info()})
        
        elif (payload["type"] == "cat"):
            cat_fields: list = ["id", "name", "age_years", "weight_kg", "indoor_only", "favorite_toy"]

            for el in cat_fields:

                if el not in cat_fields:
                    raise KeyError(f"campo: {el} non presente ")
            
            cat: Cat = Cat(payload["id"], payload["name"], payload["age_years"], payload["weight_kg"], payload["indoor_only"], payload["favorite_toy"])

            s.add(cat)

            return jsonify({"status": "ok", "add": cat.info()})
    
    raise KeyError("tipo non presente o non valido")


    

    





    



if __name__ == '__main__':
    app.run(debug=True)







    
    

    

    

        
    
