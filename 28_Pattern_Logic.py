
rows = int(input("Enter Number of Rows: "))
print("="*30)
for i in range(1, rows + 1):
    print("*" * i)
print("="*30)
for i in range(rows, 0, -1):
    print("*" * i)
print("="*30)
for i in range(rows):
    print("*" * rows)

print("-" * 30)

