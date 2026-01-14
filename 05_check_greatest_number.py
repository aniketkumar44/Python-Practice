#check greatest number
a=int(input("enter first number : "))
b=int(input("enter second number : "))
c=int(input("enter third number : "))
if(a>=b and a>=c):
    print("A = ",a)
elif(b>=c and b>=a):
    print("B = ",b)
else:
    print("C = ",c)
