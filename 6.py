"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
"""

data = ["abc", "xyz", "aba", "1221"]

count = 0
for word in data:
  if len(word) >= 2 and word[0] == word[-1]:
    count += 1

print(count)