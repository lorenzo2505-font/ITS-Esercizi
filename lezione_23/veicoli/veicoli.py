from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str):
        super().__init__()
        self.plate_id = plate_id
        self.model = model 
        self.driver_name = driver_name 
        self.registration_year = registration_year
        self.setStatus(status)

    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    @abstractmethod
    def base_cleaning_time(self) -> int: 
        pass

    @abstractmethod
    def wear_level(self) -> int:
        pass

    def info(self) -> dict: 
        return self.__dict__
    
    def estimated_prep_time(self, factor: float = 1) -> int:
        return int((self.base_cleaning_time() * factor) + (self.wear_level() * 15))
    
    def setStatus(self, status: str):
        self.status = status 

class Car(Vehicle):
    
    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str, doors: int, is_cabrio: bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors 
        self.is_cabrio = is_cabrio
    
    def vehicle_type(self) -> str:
        return "car"
    
    def base_cleaning_time(self) -> int:
        return 30
    
    def wear_level(self) -> int:
        return 2
    

class Van(Vehicle):

    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str, max_load_kg: int, require_special_license: bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license
    
    def vehicle_type(self) -> str:
        return "van"
    
    def base_cleaning_time(self) -> int:
        return 60
    
    def wear_level(self) -> int:
        return 5


class FleetManager:

    def __init__(self):
        self.vehicles: dict[str, Vehicle] = {}
    
    def add(self, vehicle: Vehicle) -> bool: 
        
        if vehicle.plate_id in self.vehicles: 
            return False 
        
        self.vehicles[vehicle.plate_id] = vehicle

        return True
    
    def get(self, plate_id: str) -> Vehicle: 
        
        if plate_id not in self.vehicles: 
            return None 
        
        return self.vehicles[plate_id]
    
    def update(self, plate_id: str, new_veichle: Vehicle):
        self.vehicles[plate_id] = new_veichle
    
    def patch_status(self, plate_id: str, new_status: str):
        self.vehicles[plate_id].setStatus(new_status)
    
    def delete(self, plate_id) -> bool: 

        if plate_id not in self.vehicles: 
            return False 
        
        self.vehicles.pop(plate_id)

        return True
    
    def list_all(self) -> list: 
        mylist: list = [self.vehicles[v].info() for v in self.vehicles]

        return mylist 
    

    
    

        




