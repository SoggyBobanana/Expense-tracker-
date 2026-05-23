# expenses tracker

items = []

print("WELCOME TO EXPENSE TRACKER")

while True:
    print("""
Choose :
1. Add item
2. View items
3. Delete item
4. Exit
""")
    
    choice = input("Enter choice : ")

    # 1. Add item
    if choice == "1":
        item = input("\nenter item (put x to stop)\n") # enter item name
    
        if item == "":
            print("empty input not allowed, please insert your item again")
            continue
    
        if not item.replace(" ", "").isalpha():
            print("only word allowed, please insert your item again")
            continue
    
        if item == "x" or item == "X":
            break
    
        try: 
            price = float(input("Enter price : RM ")) # user input price
        except ValueError:
            continue
    
        items.append((item, price)) # store item in the list

print("\n======= Item List =======")

total = 0 

for item, price in items:
    print(f" - {item} : RM {price:.2f}")
    total += price
    
print("\nTotal items:", len(items))
print(f"Total spent : RM {total: .2f}")


# future add on : category, category summary / total, save data to file, receipt style UI, add delete edit feature, search item


# to adjust
# 2. View items
    elif choice == "2":
        print("\n======= Item List =======")

        total = 0

        for item, price in items:
            print(f" - {item} : RM {price:.2f}")
            total += price

        print("\nTotal items:", len(items))
        print(f"Total spent : RM {total:.2f}")

    # 3. Delete item
    elif choice == "3":
        del_item = input("Enter item name to delete: ")

        for i in items:
            if i[0].lower() == del_item.lower():
                items.remove(i)
                print("Item deleted!")
                break
        else:
            print("Item not found.")

    # 4. Exit
    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, try again.")



