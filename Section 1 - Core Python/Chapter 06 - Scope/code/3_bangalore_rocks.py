# Gotchas with mutable data types,  

a = [10]

def test(a_par):
    print(a_par)
    a_par.append("Bangalore Rocks")
    print(locals())
    print(globals())
    
test(a)

print(a)
print("locals:", len(locals()))
print("globals", len(globals()))