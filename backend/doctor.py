from backend.Person import Person
class Doctor(Person):
    def __init__(self,name,speciality):
        super().__init__(name)
        self.speciality = speciality
    def to_dict(self):
        # convert from object to dict to stored
        return {"name":self.name,
                "speciality":self.speciality}
    @staticmethod
    def from_dict(data):
        # convert from dict to object
        return Doctor(data["name"],data["speciality"])
    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, speciality = {self.speciality}"
    def __str__(self):
        return f"DR : {self.name} specializes in {self.speciality} "