from backend.doctor  import Doctor
from backend.patient import Patient
import json
FILE = "specializations.json"
def save_data(data):
    with open(FILE , "w",encoding="utf-8") as f:
        json.dump(data, f,indent=4,ensure_ascii=False)
def load_data():

        try :
            with open(FILE, "r", encoding="utf-8") as f:
               return json.load(f)
        except FileNotFoundError:
            return {}

def default_specializations():
    specializations_name = [
        "General Medicine",
        "Emergency",
        "Cardiology",
        "Orthopedics",
        "Neurology",
        "Surgery",
        "Pediatrics",
        "ENT",
        "Dermatology",
        "Gynecology & Obstetrics",
        "ICU",
        "Radiology",
        "Laboratory"
    ]
    return {specialization : {"doctors" :[],"status":{0:[],1:[],3:[]}} for specialization in specializations_name}
def serialize_specializations(specializations):
    result = {}
    for sp_name,sp_data in specializations.items():
        result[sp_name] = {
            "doctors" : [doctor.to_dict() for doctor in sp_data["doctors"]],
            "status" : {}
        }
        for status , patients in sp_data["status"].items():
           result[sp_name]["status"][status] = [patient.to_dict() for patient in patients]
    return result

def deserialize_specializations(specializations):
    result = {}
    if not specializations:
        return default_specializations()
    for sp_name,sp_data in specializations.items():
        result[sp_name] = {
            "doctors" : [Doctor.from_dict(doctor) for doctor in sp_data["doctors"]],
            "status" : {}
        }
        for status , patients in sp_data["status"].items():
           result[sp_name]["status"][status] = [Patient.from_dict(p) for p in patients]
    return result