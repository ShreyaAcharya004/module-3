"""Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30."""

numbers = list(range(1, 31))
squares = [num * num for num in numbers]

first_five = squares[:5]
last_five = squares[-5:]

print(f"First five elements: {first_five}")
print(f"Last five elements: {last_five}")