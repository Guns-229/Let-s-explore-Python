""" Example to validate the class variables and effects

"""


class ClassVariables(object):
    VAR_1 = ["This is a test"]

    def __init__(self, name, score=0):
        self.name = name
        self.VAR_1.append(name)
        self.score = score


mj_score = 14322
print(id(mj_score))
anuja_score = 14322
print(id(anuja_score))

mj = ClassVariables("mayank johri", mj_score)
aj = ClassVariables("Anuja johri", anuja_score)

print(id(mj.score))
print(id(aj.score))
