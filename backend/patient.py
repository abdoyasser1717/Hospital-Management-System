class Patient :
    def __init__(self,name,status):
        self.name,self.status =name,status
    def __str__(self):
        status = ["Super Urgent",'Urgent','Normal'][self.status]
        return f'Patient : {self.name} is {status}'
    def __repr__(self):
        return F'Patient (name="{self.name}", status={self.status}'