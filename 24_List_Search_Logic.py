# Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)
num=(1,4,9,16,25,36,49,64,81,100,81)
print(type(num))
x=int(input("enter number : "))
i=0
while i<len(num):
    if(num[i]==x):
        print("Find index = ",i)
        break    
    else:
        print("FINDING")
        i+=1
else:
    print("Sorry, number not found in the list")
