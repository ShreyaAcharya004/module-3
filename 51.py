"""Write a Python function that checks whether a passed string is
palindrome or not"""

text = input("Enter a string: ")

cleaned_text = ''.join(c.lower() for c in text if c.isalnum())

reversed_text = cleaned_text[::-1]
if cleaned_text == reversed_text:
  print(f"'{text}' is a palindrome.")
else:
  print(f"'{text}' is not a palindrome.")