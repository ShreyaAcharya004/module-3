#Write a Python program to find the highest 3 values in a dictionary

d = {'a': 10, 'b': 20, 'c': 70, 'd': 17, 'e': 27}

sorted_values = sorted(d.values(), reverse=True)
highest_3 = sorted_values[:3]

print("Highest 3 values in the dictionary:", highest_3)