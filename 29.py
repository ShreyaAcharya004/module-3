#Write a Python program to unzip a list of tuples into individual lists.

my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
unzipped_lists = [list(i) for i in zip(*my_list)]

print(unzipped_lists)