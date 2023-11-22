def passorfail(mark):
    if mark < 35:
        print("fail")
    elif mark >= 35 and mark <= 100:
        print("pass") 
    else:
        print("enter valid mark")
    
m=(int(input("enter a mark")))
passorfail(m)
