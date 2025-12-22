from .Person import Person
class Doctors(Person):
    def __init__(self,ID,name,speciality):
        super().__init__(ID,name)
        self.speciality = speciality
    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, speciality = {self.speciality}"
    def __str__(self):
        return f"DR : {self.name} specializes in {self.speciality} "