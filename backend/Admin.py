from backend.Person import Person


class Admin(Person) :
    def __init__(self,name,role="system management "):
        super().__init__(name)
        self.role = role
    def __repr__(self):
        return f"Id = {self.id}, name = {self.name}, role = {self.role}"
    def __str__(self):
        return f"{self.name} is a {self.role}"

