# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]

# for i in items:
#     if items.count(i) > 1:
#         print(i)
#         break
# else:
#     print("No duplicate found!!")

# using set 
unique_item = set()

for item in items:
    if item in unique_item:
        print(f"Dublicate {item}")
        break
    unique_item.add(item)