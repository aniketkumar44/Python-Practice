#dictionary
report_card = {}
py_marks = int(input("Enter Python Marks: "))
report_card.update({"Python": py_marks})

math_marks = int(input("Enter Math Marks: "))
report_card.update({"Math": math_marks})

eng_marks = int(input("Enter English Marks: "))
report_card.update({"English": eng_marks})
print("-" * 30)
print("Final Report Card:", report_card)
print("Marks in Python:", report_card["Python"])
