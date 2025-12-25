from backend.Person import Person
class Patient(Person) :
    STATUS =  ["Super Urgent",'Urgent','Normal']
    def __init__(self,name,status):
        super().__init__(name)
        self.status =status
    def to_dict(self):
        # convert from object to dict to stored
        return {
            "name" : self.name,
            "status" : self.status,
        }
    @staticmethod
    def from_dict(data):
        # convert from dict to object
        return Patient(data["name"],data["status"])

    def __str__(self):
        status_text = Patient.STATUS[self.status]
        return f'Patient : {self.name} is {status_text}'
    def __repr__(self):
        return F'Patient (id = {self.id} , name="{self.name}", status={self.status})'
if __name__ == '__main__':
    p1 = Patient("Ahmed", 0)
    p2 = Patient("Mona", 2)

    print(p1)
    print(repr(p1))
    print(p2)
