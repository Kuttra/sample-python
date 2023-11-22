class laptop:
    chargertype="C TYPE"

    def __init__(self):
        self.brand=""
        self.price="34"
    
    def setPrice(self,price): #instance variable
        self.price=price

    def getPrice(self): #instance variable
        print(self.price)

    @classmethod #decorators
    def changeChargerType(cls):
        cls.chargertype="B TYPE"
        print("Charger type changed to B")

    @staticmethod #decorators
    def info():
        print("This is laptop class")


hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType()

hp.info()