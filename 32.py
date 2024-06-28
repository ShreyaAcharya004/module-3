"""Write a Python script to sort (ascending and descending) a dictionary by
value."""

my_dict = {"apple": 10, "banana": 5, "cherry": 15}

sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", sorted_dict_asc)

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", sorted_dict_desc)