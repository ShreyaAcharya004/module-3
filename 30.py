#Write a Python program to convert a list of tuples into a dictionary.

my_list = [("apple", "red"), ("banana", "yellow"), ("cherry", "red")]
my_dict = {key: value for key, value in my_list}

print(my_dict) 