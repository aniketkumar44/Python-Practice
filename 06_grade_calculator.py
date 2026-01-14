#grade_calculator

score=float(input("ENTER THE NUMBER"))
if score<0 or score>1:
    print("WRONG INPUT")
elif score>=0.9:
    print("YOUR GRADE IS A")
elif score>=0.8:
    print("YOUR GRADE IS B")
elif score>=0.7:
    print("YOUR GRADE IS C")
elif score>=0.6:
    print("YOUR GRADE IS D")
else:
    print("YOUR GRADE IS F")
