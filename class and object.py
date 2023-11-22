class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("lets enjoy beach")

ramesh = goa()
suresh = goa()

ramesh.name="ramesh"
suresh.name="suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)
print(suresh.name)
print("drink:",suresh.drink)

ramesh.party()
suresh.beach()

