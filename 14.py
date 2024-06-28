# Write a Python program to find the second smallest number in a list.

def find_second_smallest(number_list):

  if len(number_list) < 2:
    return None
  smallest = second_smallest = float('inf')
  for num in number_list:
    if num < smallest:
      second_smallest = smallest
      smallest = num
    elif num > smallest and num < second_smallest:
      second_smallest = num
  return second_smallest

number_list = [5, 1, 9, 2, 5]
second_smallest_num = find_second_smallest(number_list)

if second_smallest_num is not None:
  print(f"Second smallest number: {second_smallest_num}")
else:
  print("List has less than 2 elements or contains only duplicates")