import os
class_data={}
class_data.update({"Aniket":90})
class_data.update({"Raushan":60,"Rahul":50,"Manoj":80,"Rohan":85,"Arti":75,"Vaishnavi":95})
while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. ADD NEW STUDENT ")
    print("2. VIEW ALL STUDENT ")
    print("3. SEARCH STUDENT ")
    print("4. SAVING DATA ")
    print("5. EXIT ")
    choice=int(input("ENTER CHOICE : "))
    if choice==1:
        name=input("ENTER STUDENT NAME : ")
        marks=int(input("ENTER STUDENT MARKS : "))
        class_data[name]=marks
    elif choice==2:
        print("NAME    |    MARKS")
        print("-"*20)
        for key in class_data:
            print(key,"|",class_data[key])
            print("-"*30)
        #print("CLASS DATA : ",class_data)
    elif choice==3:
        name=input("ENTER STUDENT NAME : ")
        if name in class_data:
           print("MARKS : ",class_data[name])
        else:
            print("NOT FOUND NAME")
    elif choice==4:
        print("SAVING DATA....")
        file=open("marks.txt","w")
        for name in class_data:
            marks=class_data[name]
            line=name+","+str(marks)+"\n"
            file.write(line)
        file.close()
        print("DATA SAVED SUCCESSFULLY")
        print("PROGRAM CLOSING...")
        break
    elif choice==5:
        print("PROGRAM CLOSING... ")
        break
    else:
        print("PLEASE ENTER INVALID NUMBER ")
