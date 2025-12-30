
from backend  import hospital_manger
from common.utilities import *

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
            choice = int(input('Enter your choice(from 1 to 9): '))

        except ValueError:
            print('Please enter a number.')
        else:
            return choice

    def run(self):
        while True:
            print('--'*20)
            choice = self.execute_menu()
            if choice >  9 or choice < 1 :
                print('--' * 20)
                print('Please enter a number from 1 to 9.')
            elif choice == 1 :
                print('--' * 20)
                specialization = check_input_specialization(input('Enter specialization: '))
                if not specialization:
                    continue
                patient = input_valid(input('Enter the patient: '))
                if not patient:
                    continue
                status = int(input('Enter the status(0 : normal , 1 :urgent ,2 : super_urgent): ): '))
                if status not in [0, 1, 2]:
                    print("Invalid status! Must be 0, 1, or 2")
                    continue
                self.backend.add_new_patient(specialization,patient,status)
            elif choice == 2 :
                print('--' * 20)
                self.print_all_patients()
            elif choice == 3 :
                print('--' * 20)
                specialization = check_input_specialization(input('Enter specialization: '))
                if not specialization:
                    continue
                self.get_next_patient(specialization)
            elif choice == 4 :
                print('--' * 20)
                specialization = check_input_specialization(input('Enter specialization: '))
                if not specialization:
                    continue
                patient = input_valid(input('Enter the patient: '))
                if not patient:
                    continue
                result = self.backend.remove_leaving_patient(specialization,patient)
                print(result)
                # print('-' * 10)
            elif choice == 5 :
                print("--"*20)
                specialization = check_input_specialization(input('Enter specialization: '))
                if not specialization:
                    continue
                doctor =input_valid(input('Enter the doctor name : '))
                if not doctor:
                    continue
                self.backend.add_doctor(specialization,doctor)
                # print('-' * 10)
            elif choice == 6 :
                print('--'*20)
                specialization = check_input_specialization(input('Enter specialization: '))
                if not specialization:
                    continue
                doctor = input_valid(input('Enter the doctor name : '))
                if not doctor:
                    continue
                print(self.backend.remove_doctor(specialization,doctor))
                # print('-' * 10)
            elif choice == 7 :
                print('--'*20)
                specialization = check_input_specialization(input('Enter specialization: '))
                if not specialization:
                    continue
                doctor = input_valid(input('Enter the doctor name : '))
                if not doctor:
                    continue
                update_choice = input('Do you want to update the doctor specialization? (y/n): ')
                if update_choice == 'y':
                   specialization = check_input_specialization(input('Enter specialization: '))
                   if not specialization:
                        continue
                   self.backend.remove_doctor(specialization, doctor)
                   self.backend.add_doctor(specialization,doctor)
                elif update_choice == 'n':
                      update_choice = input('Do you want to update the doctor name ? (y/n): ')
                      if update_choice == 'y':
                            doctor = input_valid(input('Enter the doctor name : '))
                            if not doctor:
                                continue
                            self.backend.remove_doctor(specialization, doctor)
                            self.backend.add_doctor(specialization, doctor)
                else:
                    print('Please enter a valid input.')
                # print('-' * 10)

            elif choice == 8 :
                print('--'*20)
                self.print_all_doctors()
                # print('-' * 10)
            elif choice == 9 :
                print("exit program")
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