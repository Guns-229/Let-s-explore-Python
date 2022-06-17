
def sum(a):
  if  a <= 2:
    return 1
  return sum(a-1) + sum(a-2)

v = sum(1)
print(v)
