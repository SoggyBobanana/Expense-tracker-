# expenses tracker

items = []

print("WELCOME TO EXPENSE TRACKER")

while True:
    item = input("\nenter item (put 0 to stop)\n")
    
    if item == "":
        print("empty input not allowed")
        continue
    
    if not item.replace(" ", "").isalpha():
        print("only word allowed")
        continue
    
    if item == "0":
        break
    
    items.append(item) # store item in the list

print("\nitems :")
for i in items:
    print("-",i)
print("\nTotal items:", len(items))


