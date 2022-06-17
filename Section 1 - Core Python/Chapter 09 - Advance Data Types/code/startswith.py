s = "Murthy "
# Strings are objects
if s.startswith('M'): print(s.upper())

name = s.lower()

print(name, id(name), s, id(s))
print("~"*79)

# what will happen? 
print(3*s) 

# print(dir(s))