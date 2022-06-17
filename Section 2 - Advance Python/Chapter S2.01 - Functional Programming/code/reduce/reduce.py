from functools import reduce

vals = [[10.592503862004378, 10.381575625004189, 10.195353463001084],
        [0.7834748989989748, 0.7892336399963824, 0.786548912001308],
        [0.82304873400426, 0.7867131360035273, 0.7751070890008123]]

def my_sum(val, a):
    print(val, a)
    val.append(sum(a))
    return val

sum_val = reduce(my_sum, vals, [])
print("*"*10)
print(sum_val)
