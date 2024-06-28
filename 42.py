#Write a Python program to print all unique values in a dictionary.

l = [{"A": "01"}, {"B": "02"}, {"C": "01"}, {"D": "05"}, {"E": "05"}, {"F": "09"}, {"F": "07"}]
print("Original List: ", l)

u_value = set(val for dic in l for val in dic.values())

print("Unique Values: ", u_value)