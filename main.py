# expenses tracker

items = []

print("WELCOME TO EXPENSE TRACKER")

while True:
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





