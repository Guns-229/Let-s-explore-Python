import dumm
from importlib import reload


print(dumm.getval())
print(dumm.reverse("Python Ruby"))
print(dumm.getval())

reload(dumm)

print("~"*20)
print(dumm.getval())
print(dumm.reverse("Java is a Programming Language"))
print(dumm.getval())
