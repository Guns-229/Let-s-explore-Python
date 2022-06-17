
class parent(object):
    def __init__(self, last_name, first_name, pay):
        self.last_name = last_name
        self.first_name = first_name
        self.pay = pay

    @property
    def full_name(self):
        return self.full_name

    @full_name.setter
    def full_name(self, full_name):
        self.full_name = full_name


class child(parent):
    def __init__(self, prog_lang, **kwargs):
        super().__init__(**kwargs)
        self.prog_lang = prog_lang


c1 = child(prog_lang="C", first_name="Meenu", last_name="Saxena", pay=1000)
print(c1.prog_lang)
