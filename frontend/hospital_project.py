
from backend  import hospital_manger
# from common.utilities import *

class Frontend_Manger :
    def __init__(self):
        self.backend = hospital_manger()

    def execute_menu(self):
        menu = [
            "Program Options:",
            '1) Add new patient',
            '2) Print all patients',
            '3) Get next patient',
            '4) Remove a leaving patient',
            "5) Add doctor",
            "6) Remove doctor",
            "7) Update doctor",
            "8) print all doctors",
            '9) End a program',
        ]
        display = '\n'.join(menu)
        print(display)
        try :
            choice = int(input('Enter your choice(from 1 to 10): '))

        except ValueError:
            print('Please enter a number.')
        else:
            return choice

    def run(self):
        while True:
            choice = self.execute_menu()
            if choice > 10 or choice < 1 :
                print('Please enter a number from 1 to 5.')
            elif choice == 1 :
                specialization = input('Enter specialization: ')
                patient = input('Enter the patient: ')
                status = int(input('Enter the status(0 : normal , 1 :urgent ,2 : super_urgent): ): '))
                self.backend.add_new_patient(specialization,patient,status)
            elif choice == 2 :
                self.print_all_patients()
            elif choice == 3 :
                specialization = input('Enter specialization: ')
                self.get_next_patient(specialization)
            elif choice == 4 :
                specialization = input('Enter specialization: ')
                patient = input('Enter the patient: ')
                result = self.backend.remove_leaving_patient(specialization,patient)
                print(result)
            elif choice == 5 :
                specialization = input('Enter specialization: ')
                doctor = input('Enter the doctor name : ')
                self.backend.add_doctor(specialization,doctor)
            elif choice == 6 :
                specialization = input('Enter specialization: ')
                doctor = input('Enter the doctor name : ')
                print(self.backend.remove_doctor(specialization,doctor))
            elif choice == 7 :
                specialization = input('Enter specialization: ')
                doctor = input('Enter the doctor name : ')
                self.backend.remove_doctor(specialization,doctor)
                update_choice = input('Do you want to update the doctor specialization? (y/n): ')
                if update_choice == 'y':
                   specialization = input('Enter nem specialization: ')
                   self.backend.add_doctor(specialization,doctor)
                elif update_choice == 'n':
                      update_choice = input('Do you want to update the doctor name ? (y/n): ')
                      if update_choice == 'y':
                            doctor = input('Enter the doctor name : ')
                            self.backend.add_doctor(specialization, doctor)
                else:
                    print('Please enter a valid input.')
            elif choice == 8 :
                self.print_all_doctors()
            elif choice == 9 :
                exit()
    def print_all_patients(self):
        patient_info = self.backend.get_patient_info()
        for specialization,patients in patient_info :
            print(f'specialization: {specialization}')
            for patient in patients:
                print(patient)
    def print_all_doctors(self):
        doctors_info = self.backend.get_doctors_info()
        for specialization,doctors in doctors_info :
            print(f'specialization: {specialization}')
            for doctor in doctors:
                print(doctor)
    def get_next_patient(self,specialization):
        next_patient = self.backend.get_next(specialization)
        print(next_patient)

if __name__ == '__main__' :
    frontend = Frontend_Manger()
    frontend.run()