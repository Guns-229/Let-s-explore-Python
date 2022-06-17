# Assination effects on mutable data types,  

a = [10]

def test(a_par):
    print(a_par)
    a_par = ["hyderabad Rocks"]
    print(locals())
    print(globals())
    
test(a)

print(a)
print("locals:", len(locals()))
print("globals", len(globals()))