"""Write a Python program to check whether an element exists within a
tuple."""

def element_in_tuple(element, my_tuple):
  return element in my_tuple

my_tuple = ("apple", "banana", "cherry")
element_to_find = "apple"

if element_in_tuple(element_to_find, my_tuple):
  print(f"{element_to_find} exists in the tuple")
else:
  print(f"{element_to_find} does not exist in the tuple")