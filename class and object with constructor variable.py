class laptop:
    def __init__(self):
        self.processor=""
        self.ram=""
    def display(self):
        print("processor", self.processor)
        print("ram", self.ram)

hp=laptop()
dell=laptop()

hp.processor="i5"
hp.ram="8gb"

dell.processor="i7"
dell.ram="12gb"

hp.display()
dell.display()
