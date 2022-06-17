# 1. at module level both locals and globals will return same values. 

a = 10

def test(a_par):
    print(a_par)
    a_par = "Pune Rocks"
    print(locals())
    print(globals())


test(a)
print(a)
print("locals:", len(locals()))
print("globals", len(globals()))