def addlist(lists):
    """
    Add lists of lists, recursively
    the result is global
    """
    global add2
    
    for item in lists:
        if isinstance(item, list): # If item type is list
            addlist(item)
        else:
            if 'add2' in globals():
                add2 += item
            else:
                print("Creating add")
                add2 = item

addlist([[1, 2], [3, 4, 5], 6])

print(add2)

