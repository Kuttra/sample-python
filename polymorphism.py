# def add(a,b,c=0): #polymorphism
#     print(a+b+c)
# add(10,20)    
# add(10,20,12)

# def add(a=10):
#     print(a)
# add(50) 

class Animal():
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(Self):
        print("Dog barks") #overridding
class Bird(Animal):
    def sound(self):
        print("Birds sing") #overridding
d1=Dog()
d1.sound()

e1=Bird()
e1.sound()