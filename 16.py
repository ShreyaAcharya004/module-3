#Write a Python program to check whether a list contains a sub list

list1 = [1, 2, 3, 4, 5]
sublist = [2, 3]

is_sublist = any(sublist == list1[i:i + len(sublist)] for i in range(len(list1) - len(sublist) + 1))

if is_sublist:
  print("The sublist is present in the list.")
else:
  print("The sublist is not present in the list.")