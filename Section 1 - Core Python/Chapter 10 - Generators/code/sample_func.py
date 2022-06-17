
def get_list(st_no, end_no):
    lst = []
    no = st_no
    while(no < end_no):
        print(no)
        lst.append(no)
        no += 1
    return lst

print(get_list(1,5))
