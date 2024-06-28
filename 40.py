#Write a Python program to map two lists into a dictionary

keys = ["apple", "banana", "cherry"]
values = [10, 5, 15]

my_dict = {key: value for key, value in zip(keys, values)}

print(my_dict)