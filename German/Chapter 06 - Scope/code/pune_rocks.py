# 1. at module level both locals and globals will return same values. 

a = 10

def test(a_par):
    print(a_par)
    a_par = "Pune Rocks"
    print('a_par1' in locals())


test(a)
