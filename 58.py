#Write a Python program to read a random line from a file.

import random

filename = input("Enter the filename: ")

try:
  with open(filename, 'r') as file:
    lines = file.readlines() 

    if lines:
      random_line = random.choice(lines).strip()
      print(f"Random line from '{filename}': {random_line}")
    else:
      print(f"Error: File '{filename}' is empty.")

except FileNotFoundError:
  print(f"Error: File '{filename}' not found.")