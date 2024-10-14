class teacher:
    def __init__(self,nam,regno):
        self.name=nam
        self.registernumber=regno

    def display(self):
        print("NAME:",self.name)
        print("REGNO:",self.registernumber)

t1=teacher("ramesh",7376232)
t2=teacher("suresh",7376213)

t1.display()
t2.display()
