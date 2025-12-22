from backend.Person import Person


class Staff(Person) :
    def __init__(self, name, shift, role ="employee"):
        super().__init__( name)
        self.role = role
        self.shift = shift
    def __repr__(self):
        return f"name = {self.name} , shift = {self.shift} , role = {self.role } id =  {self.id}"
    def __str__(self):
        return f"{self.name} is a {self.role} working in {self.shift} shift "
if __name__ == "__main__":
    s1 = Staff("Hassan", "Night")
    print(s1)
    print(repr(s1))