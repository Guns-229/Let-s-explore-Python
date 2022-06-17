def user_name(x):
    x.append(['mayank', 'johri'])
    return id(x)


uname_list = ['mayank', 'johri']

print(id(uname_list) == user_name(uname_list))
print(id(uname_list) , user_name(uname_list))
