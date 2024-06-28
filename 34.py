"""Write a Python script to check if a given key already exists in a
dictionary."""

my_dict = {"apple": 10, "banana": 5, "cherry": 15}

keycheck = "apple"

if keycheck in my_dict:
  print(f"Key '{keycheck}' exists in the dictionary.")
else:
  print(f"Key '{keycheck}' does not exist in the dictionary.")