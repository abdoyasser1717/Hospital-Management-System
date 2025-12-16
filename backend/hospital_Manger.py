from .patient import Patient
from common.utilities import *
class hospital_manger:
    def __init__(self,specialization_count):
        self.specialization_count = specialization_count
        self.specializations : list[dict[int, list[Patient]]]= [{0:[],1:[],2:[]} for _ in range(specialization_count)]
        self.MAX_QUE = 10
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2
        self.but_dummy_patient()
    def add_new_patient(self,specialization,name,status):
        spce = self.specializations[specialization]
        pat = Patient(name,status)
        spce[status].append(pat)
        return 'adding new patient successfully'
    def can_add_patient(self,specialization):
        num_patients = 0
        for status in self.specializations[specialization]:
            num_patients += len(status)
        if num_patients > self.MAX_QUE:
            return False
        return True
    def get_patient_info(self):
        result = []
        for idx,specialization in enumerate(self.specializations):
            if not specialization :
                continue
            curr_patient = []
            for status in specialization.values():
                for patient in status:
                    curr_patient.append(patient)
            result.append((idx,curr_patient))
        return result
    def get_next(self,specialization):
        spce = self.specializations[specialization]
        for status in spce.values():
            if len(status) != 0:
               next_patient = status[0].name
               del status[0]
               return f'{next_patient} go to Dr please '
        return "there are no patients , have rest Dr mostafa"

    def remove_leaving_patient(self,specialization,patient):
        spce = self.specializations[specialization]
        for status in spce.values():
            for idx,pat in enumerate(status):
                if pat.name == patient:
                    del status[idx]
                    return 'remove patient successfully'
        return 'there are no patients have such name '
    def but_dummy_patient(self):
        dummy_patient = [('specialization 1','dummyData',1),('specialization 2','AnotherDummyData',2),('specialization 3','thirdDummyData',0),('specialization 4','forthDummyData',1)]
        for  specialization,patient,status in dummy_patient :
            for i in range(10):
                count_patient = patient + str(i)
                spec = input_valid_int(specialization, 1, self.specialization_count )
                self.add_new_patient(spec,count_patient,status)
        another_dummy_data = [('specialization 5','ahmed',2),('specialization 5','saad',1),('specialization 5','hamdy',0),('specialization 5','yasser',2)]
        for  specialization,patient,status in another_dummy_data :
                spec = input_valid_int(specialization, 1, self.specialization_count )
                self.add_new_patient(spec,patient,status)






if __name__ == '__main__':
    hospital_manger = hospital_manger(5)
    print(hospital_manger.specializations)
