#ASK THE USER TO ENTER NAMES OF THEIR 3FAVORITE MOVIES & STORE THEM IN LIST.
'''movies=[]
movie1=input("ENTER 1st MOVIE : ")
movie2=input("ENTER 2st MOVIE : ")
movie3=input("ENTER 3st MOVIE : ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)'''
#check if a list contains a palindrome of elements.
'''list=[1,2,3,2,1]
copy_list=list.copy()
list.reverse()
if (copy_list==list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
#Checking for a word
list=['A','n','i','k','e','t']
copy_list=list.copy()
list.reverse()
if (copy_list==list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")'''
#Store the above values in a list & sort them from "A" to "D".
list=["A","C","B","D"]
print(type(list))
list.sort()
print("Sorted list = ",list)
