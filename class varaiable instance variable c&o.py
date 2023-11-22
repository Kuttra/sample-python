class phone():
    chargetype="C-TYPE"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        # self.chargetype=chargetype
    def display(self):
        print("Brand",self.brand)
        print("Price",self.price)
        print("Chargetype",self.chargetype)

#phone.chargetype="B-TYPE"

samsung = phone("Samsung","10000")
samsung.display()

redme = phone("Redme","5000")
redme.display()

google = phone("Pixel","3000")
google.display()