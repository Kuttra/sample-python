class Shape():
    def area(self):
        return 0
class Rectangle(Shape):
    def area(self):
        l=10
        b=20
        print(l*b)
# s1=Shape()
# print(s1.area())

r1=Rectangle()
r1.area()