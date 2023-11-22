# class dad(): #multiple inheritance
#     def phone(self):
#         print("dads phone")

# class mom():
#     def sweet(self):
#         print("moms sweet")

# class son(dad,mom):
#     def laptop(self):
#         print("sons laptop")

# ram=son()
# ram.phone()
# ram.sweet()

# class grandpa(): #multileval inheritance
#     def phone(self):
#         print("granpas phone")

# class dad(grandpa):
#     def money(self):
#         print("dada money")

# class son(dad):
#     def laptop(self):
#         print("sons laptop")

# ram=son()
# ram.laptop()
# ram.money()

# # d1=dad()
# # d1.phone()

# ram.phone()

class dad(): #hybrid inheritance
    def money(self):
        print("dads money")
class land():
    def important(self):
        print("important land")
class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s2=son2()
s2.money()
s1=son1()
s1.money()
s1.important()