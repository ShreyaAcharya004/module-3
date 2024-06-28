#Write a Python function to check whether a number is perfect or not

number = int(input("Enter a positive integer: "))

if number <= 0:
  print("Please enter a positive integer.")
else:
  sum_of_divisors = 1
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      sum_of_divisors += i
      if i * i != number:
        sum_of_divisors += number // i

  if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
  else:
    print(f"{number} is not a perfect number.")