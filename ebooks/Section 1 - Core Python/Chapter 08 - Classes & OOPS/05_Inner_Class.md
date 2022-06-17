
# The inner class
---
An inner class or nested class is a defined entirely within the body of another class  Let us do an example:


```python
class Human(object):

    def __init__(self, writing_hand):
        self.name = 'Guido'
        self.head = self.__Head()
        self.left_hand = self.__Hand()
        self.right_hand = self.__Hand()
        self.writing_hand = writing_hand

    class __Head(object):
        """
        Make them private classes to avoid abuse
        """
        def talk(self):
            return 'talking...'
    
    class __Hand(object):
        def writing(self, txt):
            print(txt)

    def lets_talk(self):
        return self.head.talk();
    
    def lets_write(self, txt):
        if(self.writing_hand.lower() == 'left'):
            self.left_hand.writing(txt)
        else:
            self.right_hand.writing(txt)
```


```python
guido = Human("right")
print(guido.name)
print(guido.head.talk())
# Bad example misusing the methods
try:
    guido.__Hand.writing(guido, "hello")
except Exception as e:
    print(e)
# guido.Hand.writing(guido, "hello")
print("*"*20)
guido.right_hand.writing("Ja")
guido.lets_write("World")
```

    Guido
    talking...
    'Human' object has no attribute '__Hand'
    ********************
    Ja
    World


### when to use 

- When you want to hide the implenetation from objects
- When inner classes has no independent functionality.
