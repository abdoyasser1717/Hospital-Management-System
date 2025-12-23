from backend.doctor import Doctor
from backend.patient import Patient
# from ..common.utilities import *
class hospital_manger:
    def __init__(self):
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
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2
        self.specializations =  {specialization : {"doctors" :[],"status":{self.NORMAL:[],self.URGENT:[],self.SUPER_URGENT:[]}} for specialization in specializations_name}
        self.MAX_QUE = 10

        # self.but_dummy_patient()

    def add_new_patient(self,specialization,name,status):
        spce = self.specializations[specialization]
        pat = Patient(name,status)
        spce["status"][status].append(pat)
        return 'adding new patient successfully'
    def can_add_patient(self,specialization):
        num_patients = 0
        for status in self.specializations[specialization]["status"].values():
            num_patients += len(status)
        if num_patients > self.MAX_QUE:
            return False
        return True
    def add_doctor(self,specialization,name):
        spce = self.specializations[specialization]
        doc = Doctor(name,specialization)
        spce["doctors"].append(doc)
    def remove_doctor(self,specialization,name):
        spce = self.specializations[specialization]
        if not spce["doctors"] :
            return "no doctors with such name"
        for doc in spce["doctors"]:
            if doc.name == name:
                spce["doctors"].remove(doc)
                return "removed doctor successfully"
        return  "no doctor with such name"
    def get_doctors_info(self):
        result = []
        for specialization_name in self.specializations.keys():
            current_doctors = []
            for doc in self.specializations[specialization_name]["doctors"]:
                current_doctors.append(doc)
            if not current_doctors:
                continue
            result.append((specialization_name,current_doctors))
        return result
    def get_patient_info(self):
        result = []
        for specialization_name  in self.specializations.keys():
            curr_patient = []
            for patients_list in self.specializations[specialization_name]["status"].values():
                for patient in patients_list:
                    curr_patient.append(patient)
            if not curr_patient:
                continue
            result.append((specialization_name,curr_patient))
        return result
    def get_next(self,specialization):
        spce = self.specializations[specialization]
        for status in spce["status"].values():
            if len(status) != 0:
               next_patient = status[0].name
               del status[0]
               return f'{next_patient} go to Dr please '
        return "there are no patients , have rest Dr "
    def remove_leaving_patient(self,specialization,patient):
        spce = self.specializations[specialization]
        for status in spce["status"].values():
            for idx,pat in enumerate(status):
                if pat.name == patient:
                    del status[idx]
                    return 'remove patient successfully'
        return 'there are no patients have such name '





if __name__ == '__main__':
    hospital_manger = hospital_manger()
    print(hospital_manger.specializations)