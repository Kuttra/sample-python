s_username="EMC"
s_password="123"

username=input("enter username:")
password=input("enter password:")

def validate():
    if(s_username==username and s_password==password):
        return True
    else:
        return False

a=validate() 
print(a)  