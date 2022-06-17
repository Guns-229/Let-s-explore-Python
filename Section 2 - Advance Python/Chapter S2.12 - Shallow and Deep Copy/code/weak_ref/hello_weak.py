import weakref
import sys


class MayaHello:
    def __init__(self, lang):
        self.lang = lang

    def hello(self):
        if(self.lang == 'hi'):
            return "नमस्ते"
        elif(self.lang == 'de'):
            return "Hallo"
        else:
            return ("Hello")

    def __del__(self):
        print("self destruct initiated")
        del self.lang

a = MayaHello('hi')
print(a.hello())
b = weakref.ref(a)
print(b().hello())
sys.stdout.flush()
#del(a)

print(dir(b()))
print(b())
