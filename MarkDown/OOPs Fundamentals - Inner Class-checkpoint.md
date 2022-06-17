
# The inner class
---
An inner class or nested class is a defined entirely within the body of another class  Let us do an example:


```python
class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
#         self.hand = self.Hand()

    class Head:
        def talk(self):
            return 'talking...'
    
    class Hand:
        def writing(self):
            print(Human.Head.talk(self))
            return "writing"

guido = Human()
print (guido.name)
print (guido.head.talk())
# Bad example misusing the methods
print (guido.Hand.writing(guido))
```

    Guido
    talking...
    talking...
    writing
    


```python

```
