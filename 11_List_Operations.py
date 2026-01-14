stringlist=["mahesh","ranesh","suresh","kamlesh","vishnu"]
print(type(stringlist))
for names in stringlist:
    print(names)
numlist=[4,67,10,15,13]
for i in range(len(numlist)):
    numlist[i]=numlist[i]*2
print(numlist)
numlist.append(50)
print("after append 50 = ",numlist)
nlist=[25,35,45]
print("nlist = ",nlist)
numlist.extend(nlist)
print("After extend nlist = ",numlist)
numlist.sort()
print("After sort = ",numlist)
numlist.pop(5)
print("After pop =" ,numlist)
del numlist[0]
print("After del = ",numlist)
print("Len = ",len(stringlist))
print("Sum = ",sum(numlist))
print("Max = ",max(numlist))
print("Minimum = ",min(numlist))
sorted_stringlist=sorted(stringlist)
print(sorted_stringlist)
