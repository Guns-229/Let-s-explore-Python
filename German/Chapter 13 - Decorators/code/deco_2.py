class Users(object):

    def __init__(self, name, passwd, filename):
        self.name = name
        self.password = passwd
        self.filename = filename

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = password





d = Users("a", "b", "c")
print(d.password)
