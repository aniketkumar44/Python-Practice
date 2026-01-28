grand_total_sale = 0
while True:
    print("=" * 35)
    print("   BIBS CANTEEN SYSTEM (LIVE)     ")
    print("=" * 35)
    print("---- NEW CUSTOMER ORDER ----")
    name = input("Enter Customer Name: ")
    C = int(input("Qty of Cakes (Rs 30): "))
    D = int(input("Qty of Cold Drinks (Rs 25): "))
    S = int(input("Qty of Snacks (Rs 20): "))
    W = int(input("Qty of Water (Rs 10): "))
    total = (C * 30) + (D * 25) + (S * 20) + (W * 10)
    if total >= 1000:
        disc = total * 0.15
        print("Congrats" ,name, "You got 15% Discount.")
    elif total >= 500:
        disc = total * 0.10
        print(f"Congrats" ,name, "You got 10% Discount.")
    else:
        disc = 0
        print("No descount; better luck next time")
    final_bill = total - disc
    gst= total*(5/100)
    print("-" * 30)
    print("Customer Name : ",name)
    print("Total Amount  : ",total)
    print("Discount      : -",disc)
    print("GST@5%        : ",gst)
    print("To Pay        : ",final_bill+gst)
    print("-" * 30)
    grand_total_sale = grand_total_sale + final_bill
    choice = input("Next Customer? (yes/no): ")
    if choice == "no":
        print("Closing the Shop Software...")
        break
print("=" * 35)
print(" DAY END REPORT - TOTAL SALE: Rs",grand_total_sale)
print("=" * 35)
