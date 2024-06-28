#Write a Python program to check multiple keys exists in a dictionary

my_dict = {"apple": 10, "banana": 5, "cherry": 15}

c_keys = {"apple", "banana", "grape"}

all_keys_exist = all(key in my_dict for key in c_keys)

if all_keys_exist:
  print("All keys exist in the dictionary.")
else:
  print("Not all keys exist in the dictionary.")