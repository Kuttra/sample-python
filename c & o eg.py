class calculater:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)

    def sub(self):
        print("sub",self.num1-self.num2)

    def mult(self):
        print("mult",self.num1*self.num2)

    def div(self):
        print("div",self.num1/self.num2)

   
obj1=calculater(10,2)
obj2=calculater(10,2)
obj3=calculater(10,2)
obj4=calculater(10,2)
obj1.add()
obj2.sub()
obj3.mult()
obj4.div()
