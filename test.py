#1 reverse of the given number
n="codecode"
n=n[::-1]
print(n)

#2 prime number or not
num=int(input())
if num==1:
    print("not a prime")
if num>1:
    for i in range(2,num):
        if num%2==0:
            print(num,"not prime")
            break
    else:
        print(num,"prime")

#3 arrange way in forms largest value
import functools

class Solution:
    def printLargest(self,a):
        def comp(a, b):
            ab = a + b
            ba = b + a
            if ba > ab:
                return 1
            return -1
        
        a.sort(key=functools.cmp_to_key(comp))
        ans = "".join(a)
        return ans

solution = Solution()
input_numbers = [54, 546, 548, 60]
result = solution.printLargest([str(num) for num in input_numbers])
print(result)

#4 print reverse of number
num1 = 100
rev = 0
while(num1 > 0):
    a = num1 % 10
    rev = rev * 10 + a
    num1 = num1//10
print(rev)

#5 max and min element
a=[54,546,548,60]
print(max(a),end=" ")
print(min(a))