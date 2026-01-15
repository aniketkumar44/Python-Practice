t=('a','b','c','d','e')
print("t[0] = ",t[0])
print("t[1:3] = ",t[1:3])
t=('A',)+t[1:]
print("t*2 = ",t*2)
print("t = ",t)

num=int(input("enter any number"))
for i in range (1,11):
    print(num,"x",i,"=",num*i)
