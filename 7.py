#Write a Python program to remove duplicates from a list.

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

dup_items = set()
uniq_items = []

for i in a:
 
    if i not in dup_items:

         uniq_items.append(i)

         dup_items.add(i)

print(dup_items) 