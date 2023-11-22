class Vehicle():
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

s1=Car()
s1.start()