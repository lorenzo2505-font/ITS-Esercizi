from abc import ABC, abstractmethod

class SmartDevice(ABC):

    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str):
        super().__init__()
        self.serial_number = serial_number
        self.brand = brand 
        self.room = room 
        self.installation_year = installation_year
        self.setStatus(status)
    
    def setStatus(self, status: str): 
        self.status = status
    
    @abstractmethod
    def device_type(self) -> str: 
        pass

    @abstractmethod
    def energy_consumption(self) -> float|int: 
        pass 

    @abstractmethod
    def connection_quality(self) -> int: 
        pass 

    def info(self) -> dict: 
        return self.__dict__
    
    def diagnostici_time(self, factor: float = 1.0) -> float:
        return (self.energy_consumption() * factor) + (self.connection_quality() * 10)


class SmartBulb(SmartDevice): 

    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str, brightness_lumens: int, color_capability: bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability
    
    def device_type(self) -> str:
        return "bulb"
    
    def energy_consumption(self) -> float|int:
        return 15
    
    def connection_quality(self) -> int:
        return 4

class SecurityCamera(SmartDevice): 

    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str, resolution: str, night_vision: bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision
    
    def device_type(self) -> str:
        return "camera"
    
    def energy_consumption(self) -> float|int:
        return 50
    
    def connection_quality(self) -> int:
        return 10

class IoTHub:

    def __init__(self):
        self.devices: dict[str, SmartDevice] = {}
    
    def add(self, device: SmartDevice) -> bool: 
        
        if device.serial_number in self.devices: 
            return False
        
        self.devices[device.serial_number] = device

        return True 
    
    def get(self, serial_number: str) -> SmartDevice | None:

        if serial_number not in self.devices: 
            return None 

        return self.devices[serial_number]

    def update(self, serial_number: str, new_device: SmartDevice): 
        self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str): 
        self.devices[serial_number].setStatus(new_status)

    def delete(self, serial_number: str) -> bool: 

        if serial_number not in self.devices: 
            return False 
        
        self.devices.pop(serial_number)

        return True
    
    def list_all(self) -> list: 
        mylist: list = [self.devices[d].info() for d in self.devices]

        return mylist



        
        


    