class animal():
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class bird(animal):
    def sound(self):
        print("Birds sing")

a1=bird()
a1.sound()

