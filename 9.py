"""Write a Python function that takes two lists and returns true if they have
at least one common member."""

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 2]

has_common_element = any(x in l1 for x in l2)

if has_common_element:
  print("The lists have at least one common member.")
else:
  print("The lists have no common members.")