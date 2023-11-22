class student:
    def __init__(self):
        self.name="bhgutr"
        self.regno="1234"
    def display(self):
        print("name", self.name)
        print("regno", self.regno)

s1=student()
s2=student()

s1.name="manoj"
s1.regno="1"

s2.name="tharun"
s2.regno="2"

s1.display()
s2.display()