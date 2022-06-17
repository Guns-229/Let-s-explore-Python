

class User_List():
    users = []

    def __init__(self, name, count):
        self.users.append(name)
        self.count = count


m = User_List("Mayank Johri", ["20 00 0"])
a = User_List("Mayank Johri a", ["20 00 0"])
b = User_List("Mayank Johri b", ["20 00 0"])
print(m.count, a.count, b.count)
print(id(m.count), id(a.count), id(b.count))
