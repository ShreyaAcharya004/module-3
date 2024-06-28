#Write a Python script to merge two Python dictionaries

d1={'a':10,'b':20}
d2={'c':30,'d':40}

d=d1.copy()
d.update(d2)
print(d)