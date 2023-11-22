class teacher:
    def __init__(self,na,rn):
        self.name=na 
        self.regno=rn
    def display(self):
        print("name",self.name)
        print("regno",self.regno)    

t1=teacher("thomas","1")
t2=teacher("thara","20")

t1.display()
t2.display()