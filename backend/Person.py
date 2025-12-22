class Person :
    _id_counter = 1
    def __init__(self,name):
        self.id = Person._id_counter
        Person._id_counter += 1
        self.name = name
    def __str__(self):
        return f"{self.name} (id: {self.id})"
    def __repr__(self):
        return f"id={self.id}, name={self.name}"