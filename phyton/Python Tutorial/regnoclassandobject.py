class student:
    def __init__(self):
        self.name=""
        self.regno=""
    def display(self):
        print("NAME :",self.name)
        print("REG NO :",self.regno)

raja=student()
sachin=student()
saran=student()

raja.name="RAJAGOPAL"
raja.regno="CB139"

sachin.name="SACHINSURESH"
sachin.regno="CB140"

saran.name="SARAN"
saran.regno="CB144"

raja.display()
sachin.display()
saran.display()
        
