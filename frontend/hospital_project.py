
from backend  import hospital_manger
from common.utilities import *

class Frontend_Manger :
    def __init__(self,specialization_count=20):
        self.specialization_count = specialization_count
        self.backend = hospital_manger(self.specialization_count)

    def execute_menu(self):
        menu = [
            "Program Options:",
            '1) Add new patient',
            '2) Print all patients',
            '3) Get next patient',
            '4) Remove a leaving patient',
            '5) End a program',
        ]
        display = '\n'.join(menu)
        print(display)
        try :
            choice = int(input('Enter your choice(from 1 to 5): '))

        except ValueError:
            print('Please enter a number.')
        else:
            return choice

    def run(self):
        while True:
            choice = self.execute_menu()
            if choice > 5 or choice < 1 :
                print('Please enter a number from 1 to 5.')
            elif choice == 1 :
                specialization = input_valid_int(input('Enter specialization: '), 1, self.specialization_count )
                patient = input('Enter the patient: ')
                status = int(input('Enter the status(0 : normal , 1 :urgent ,2 : super_urgent): ): '))
                self.backend.add_new_patient(specialization,patient,status)
            elif choice == 2 :
                self.print_all_patients()
            elif choice == 3 :
                specialization = input_valid_int(input('Enter specialization: '), 1, self.specialization_count )
                self.get_next_patient(specialization)
            elif choice == 4 :
                specialization = input_valid_int(input('Enter specialization: '), 1, self.specialization_count )
                patient = input('Enter the patient: ')
                result = self.backend.remove_leaving_patient(specialization,patient)
                print(result)
            elif choice == 5 :
                exit()
    def print_all_patients(self):
        patient_info = self.backend.get_patient_info()
        for specialization,patients in patient_info :
            print(f'specialization: {specialization}')
            for patient in patients:
                print(patient)
    def get_next_patient(self,specialization):
        next_patient = self.backend.get_next(specialization)
        print(next_patient)





if __name__ == '__main__' :
    frontend = Frontend_Manger()
    frontend.run()