# print("HI")
# print("BYE")
# printt("hey")  #compile time error/

# a=10
# b=20
# print(a+a)  #logical error
#             #insted of putting a+b, we put a+a 

 
# a=int(input())
# b=int(input())#runtime error
# print(a+b)   #in int we use str means it will show a run time error

try:
    a=int(input())
    b=int(input())
# except ValueError as e:
#     print("ValurError",e)
except TypeError as e:
    print("TypeError",e)
except Exception:
    print("Somthing wrong")
finally:  #finally will work wether ther is a error and no error
    print("Done")