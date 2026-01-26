#print the mutiplication table of a num n.
n = int(input("ENTER ANY NUMBER : "))
for i in range(1,11):
        print(n,"x",i,"=",n*i)
print("-"*5)
# sum of n num (using while),(for)
#using while
n = 9
sum = 0
i = 1
while i <= n:
    sum += i
    i+=1
print("SUM OF NUMBER : ",sum)
print("-"*5)
#using for
n=10
sum=0
for i in range(1, n+1):
    sum+=i
print("SUM OF NUMBER : ",sum)
print("-"*5)
#factorial of n number. (using for and while)
#using for
n=5
f=1
for i in range(1, n+1):
    f*=i
print("factorial of number = ",f)
print("-"*5)
#using while
n=6
fact=1
i=1
while i <= n:
    fact *= i
    i+=1
print("factorial of number = ",f)
print("-"*5)

#print numbers from 1 to 100.
i=1
while i<=100:
    print(i)
    i+=1
print("-"*5)
#print numbers from 100 to 1.
i=100
while i>=1:
    print(i)
    i-=1
print("-"*5)
#print the multiplication table of a number 12.
num=12
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1
print("-"*5)
#print the elements of the following list using a loop:
list =[1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx<len(list):
    print(list[idx])
    idx+=1
print("-"*5)
sub=["python","foxpro","math","english","c"]
idx=0
while idx<len(sub):
    print(sub[idx])
    idx+=1
print("-"*5)
#using for
num=[1,4,9,16,25,36,49,81,100]
for el in num:
    print(el)
print("-"*5)

num=(1,4,9,16,25,36,49,81,100,49)
x=49
idx=0
for el in num:
    if(el == x):
        print(idx)
        found=True
        break
    idx +=1
else:
    print("end")
print("-"*5)
