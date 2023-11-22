# class company():  #public -->access modifiver
#     def __init__(self):
#         self.companyName="Google"

# c1=company()
# c1.companyName="Goooogllllle"
# print(c1.companyName)

# class company():  #private -->access modifiver
#     def __init__(self):
#         self.__companyName="Google"
#     def companyName(self):  #private varabile accessed only inside the class
#         print(self.__companyName)
# c1=company()
# c1.companyName()
# print(c1.__companyName)

class company():  #protected -->access modifiver
    def __init__(self):
        self._companyName="Google" #protected variable can accessed using their class and also be accessed by using the child class
class b(company):
    pass        
b1=company()
print(b1._companyName)