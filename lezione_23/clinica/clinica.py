from abc import ABC, abstractmethod

class Booking(ABC): 
    
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str):
        super().__init__()
        self.booking_id = booking_id
        self.patient_name = patient_name 
        self.doctor = doctor
        self.department = department 
        self.date = date 
        self.time = time 
        self.setStatus(status)
    
    def setStatus(self, status: str):
        self.status = status 
    
    @abstractmethod
    def booking_type(self) -> str:
        pass

    @abstractmethod
    def base_duration(self) -> int: 
        pass

    @abstractmethod
    def priority_level(self) -> int:
        pass

    def info(self) -> dict: 
        return self.__dict__
    
    def estimated_wait(self, factor: float = 1.0) -> int: 
        return (self.base_duration() * factor) + (self.priority_level() * 5)


class MedicalVisit(Booking): 
    
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, visit_reason: str, first_time: bool):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = first_time 
    
    def booking_type(self) -> str:
        return "visit"
    
    def base_duration(self) -> int:
        return 30
    
    def priority_level(self) -> int: 
        return 5

class DiagnosticExam(Booking): 

    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, exam_type: str, requires_fasting: bool):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.exam_type = exam_type
        self.requires_fasting = requires_fasting
    
    def booking_type(self) -> str:
        return "exam"
    
    def base_duration(self) -> int:
        return 60
    
    def priority_level(self) -> int:
        return 8

class ClinicHub: 

    def __init__(self):
        self.bookings: dict[str, Booking] = {}
    
    def add(self, booking: Booking) -> bool: 

        if booking.booking_id in self.bookings: 
            return False 
        
        self.bookings[booking.booking_id] = booking 

        return True
    
    def get(self, booking_id: str) -> Booking|None: 

        if booking_id not in self.bookings: 
            return None 
        
        return self.bookings[booking_id]
    
    def update(self, booking_id: str, new_booking: Booking): 
        self.bookings[booking_id] = new_booking
    
    def patch_status(self, booking_id: str, new_status: str): 
        self.bookings[booking_id].setStatus(new_status)
    
    def delete(self, booking_id: str) -> bool: 
        
        if booking_id not in self.bookings: 
            return False
        
        self.bookings.pop(booking_id)

        return True
    
    def list_all(self) -> list: 
        return [self.bookings[b].info() for b in self.bookings]
    
