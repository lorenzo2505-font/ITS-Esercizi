from flask import Flask, url_for, request, jsonify
from clinica import *

m: MedicalVisit = MedicalVisit("1a", "luca marchetti", "campitelli", "majorana", "2026-02-01", "18:00", "scheduled", "certificato agonistico", False)
d: DiagnosticExam = DiagnosticExam("2b", "cane pazzo", "john dorian", "bho", "2026-08-05", "09:00", "scheduled", "esame della prostata", True)
c: ClinicHub = ClinicHub()

c.add(m)
c.add(d)

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Clinic Booking Hub API", 
    "links": {"bookings": url_for("get_bookings"), 
    "bookings_by_id": url_for("get_bookings_by_id", id = "1a"), 
    "wait": url_for("get_wait", id = "2b", factor = 1.5)}})

@app.route('/bookings', methods = ['GET'])
def get_bookings():
    newdict: dict = {}
    
    for b in c.bookings: 
        newdict[b] = c.bookings[b].info()
    
    return jsonify(newdict), 200

@app.route('/bookings/<string:id>', methods = ['GET'])
def get_bookings_by_id(id: str): 

    if c.get(id) is None: 
        return {"errore": "la prenotazione non esiste"}, 404
    
    return jsonify(c.get(id).info()), 200

@app.route('/bookings/<string:id>/wait/<float:factor>', methods = ['GET'])
def get_wait(id: str, factor: float): 

    if c.get(id) is None: 
        return jsonify({"errore": "la prenotazione non esiste"}), 404
    
    return jsonify({"booking_id": id, "booking_type": c.get(id).booking_type(), "factor": factor, "estimated_wait_minutes": c.get(id).estimated_wait(factor)}), 200

@app.route('/bookings', methods = ['POST'])
def post_booking(): 
    payload = request.get_json()

    if not(payload) or "type" not in payload or (payload["type"] != "visit" and payload["type"] != "exam"): 
        return jsonify({"errore": "Il campo type è obbligatorio e deve essere uguale a visit o exam"}), 400
    
    fields: list = ["booking_id", "patient_name", "doctor", "department", "date", "time", "status"]

    for f in fields: 
        
        if f not in payload: 
            return jsonify({"errore": f"campo {f} non presente"}), 400
    
    if payload["type"] == "visit":

        if "visit_reason" not in payload or "first_time" not in payload: 
            return jsonify({"errore": "i campi visit_reason e first_time sono obbligatori"}), 400
        
        visit: MedicalVisit = MedicalVisit(payload["booking_id"],
                                            payload["patient_name"],
                                            payload["doctor"], 
                                            payload["department"], 
                                            payload["date"], 
                                            payload["time"], 
                                            payload["status"], 
                                            payload["visit_reason"], 
                                            payload["first_time"])
        
        if not(c.add(visit)): 
            return jsonify({"errore": "la richiesta esiste già"}), 400
        
        return jsonify(visit.info()), 201
    
    else:

        if "exam_type" not in payload or "requires_fasting" not in payload: 
            return jsonify({"errore": "i campi exam_type e requires_fasting sono obbligatori"}), 400
        
        exam: DiagnosticExam = DiagnosticExam(payload["booking_id"],
                                            payload["patient_name"],
                                            payload["doctor"], 
                                            payload["department"], 
                                            payload["date"], 
                                            payload["time"], 
                                            payload["status"], 
                                            payload["exam_type"], 
                                            payload["requires_fasting"])
        
        if not(c.add(exam)): 
            return jsonify({"errore": "la prenotazione esiste già"}), 400
        
        return jsonify(exam.info()), 201

@app.route('/bookings/<string:id>', methods = ['PUT'])
def put_bookings(id: str): 
    
    if c.get(id) is None: 
        return jsonify({"errore": "la prenotazione non esiste"}), 404
    
    payload = request.get_json()

    if not(payload) or "type" not in payload or (payload["type"] != "visit" and payload["type"] != "exam"): 
        return jsonify({"errore": "Il campo type è obbligatorio e deve essere uguale a visit o exam"}), 400
    
    fields: list = ["booking_id", "patient_name", "doctor", "department", "date", "time", "status"]

    for f in fields: 
        
        if f not in payload: 
            return jsonify({"errore": f"campo {f} non presente"}), 400
    
    if payload["type"] == "visit":

        if "visit_reason" not in payload or "first_time" not in payload: 
            return jsonify({"errore": "i campi visit_reason e first_time sono obbligatori"}), 400
        
        visit: MedicalVisit = MedicalVisit(payload["booking_id"],
                                            payload["patient_name"],
                                            payload["doctor"], 
                                            payload["department"], 
                                            payload["date"], 
                                            payload["time"], 
                                            payload["status"], 
                                            payload["visit_reason"], 
                                            payload["first_time"])
        
        if id != visit.booking_id: 
            return jsonify({"errore": "l'id è univoco e non può essere cambiato"}), 400
        
        c.update(id, visit)

        return jsonify(visit.info()), 200
    
    else:

        if "exam_type" not in payload or "requires_fasting" not in payload: 
            return jsonify({"errore": "i campi exam_type e requires_fasting sono obbligatori"}), 400
        
        exam: DiagnosticExam = DiagnosticExam(payload["booking_id"],
                                            payload["patient_name"],
                                            payload["doctor"], 
                                            payload["department"], 
                                            payload["date"], 
                                            payload["time"], 
                                            payload["status"], 
                                            payload["exam_type"], 
                                            payload["requires_fasting"])
        
        if id != exam.booking_id: 
            return jsonify({"errore": "l'id è univoco e non può essere cambiato"}), 400
        
        c.update(id, exam)
        
        return jsonify(exam.info()), 200

@app.route('/bookings/<string:id>/status', methods = ['PATCH'])
def patch_bookings(id: str): 
    
    if c.get(id) is None: 
        return jsonify({"errore": "la prenotazione non esiste"}), 404 
    
    payload = request.get_json() 

    if not payload or "status" not in payload: 
        return jsonify({"errore": "campo status non presente"})
    
    c.patch_status(id, payload["status"])

    return jsonify({"new status": payload["status"]}), 200
    
@app.route('/bookings/<string:id>', methods = ['DELETE'])
def delete_booking(id: str):

    if not(c.delete(id)): 
        return jsonify({"errore": "la prenotazione non esiste"}), 404
    
    return jsonify({"deleted": True, "booking_id": id}), 200
    
    

if __name__ == '__main__':
    app.run(debug = True)