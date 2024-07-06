"""Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30."""

numbers = list(range(1, 31))
squares = [num * num for num in numbers]

f_five = squares[:5]
l_five = squares[-5:]

print(f"First five elements: {f_five}")
print(f"Last five elements: {l_five}")
