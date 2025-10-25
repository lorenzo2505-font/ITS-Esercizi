class AppointmentScheduler:

    def __init__(self):
        self.appointments: dict[str, dict] = {}
    
    def  schedule_appointment(self, app_id: str, data: str) -> dict | str:
        
        if app_id in self.appointments:
            return "Errore: appuntamento esiste già"
        
        self.appointments[app_id] = {'data': data, 'programmato': True}

        return self.appointments[app_id]
    
    def reschedule_appointment(self, app_id: str, nuova_data: str) -> dict | str:

        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato."
        
        self.appointments[app_id]['data'] = nuova_data

        return self.appointments[app_id]
    
    def cancel_appointment(self, app_id: str) -> dict | str:
        
        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato."
        
        self.appointments[app_id]['programmato'] = False

        return self.appointments[app_id]
    
    def remove_appointment(self, app_id: str) -> dict | str:

        if app_id not in self.appointments:
            return  "Errore: appuntamento non trovato."
        
        return self.appointments.pop(app_id)
    
    def list_appointments(self) -> list[str]:
        return self.appointments.keys()
    
    def get_appointment(self, app_id: str) -> dict | str:
        
        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato."
        
        return self.appointments[app_id]
    




if __name__ == '__main__':

    a: AppointmentScheduler = AppointmentScheduler()
    print(a.schedule_appointment('1', '5/11/2025'))
    print(a.reschedule_appointment('1', '9/5/2025'))
    print(a.cancel_appointment('1'))
    #print(a.remove_appointment('1'))
    print(a.list_appointments())
    print(a.get_appointment('1'))
    


