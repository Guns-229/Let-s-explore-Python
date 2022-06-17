class Company:
    d = 1
    a = d


c = Company()
a = Company()
print(c.d, c.a)
print(a.d, a.a)
a.d = "God is Good"
print(c.d, c.a)
print(a.d, a.a)
Company.d = "God is Great"
print(a.d, a.a)
print(c.d, c.a)
Company.a = 3
print(a.d, a.a)
print(c.d, c.a)
