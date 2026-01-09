#check odd or even
num=int(input("enter the number : "))
if(num%2==0):
    print("even")
else:
    print("odd")
    
#check greatest number
a=int(input("enter first number : "))
b=int(input("enter second number : "))
c=int(input("enter third number : "))
if(a>=b and a>=c):
    print("A",a)
if(b>=c and b>=a):
    print("b",b)
if(c>=a and c>=b):
    print("C",c)
    
#multiple of 5

num=int(input("enter number : "))
if(num%5==0):
    print("multiple of 5")
else:
    print("not multiple")
