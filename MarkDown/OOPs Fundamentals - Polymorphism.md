
# Polymorphism
---
The polymorphism is the process of using an operator or function in different ways for different data input. In practical terms, polymorphism means that if class B inherits from class A, it doesn’t have to inherit everything about class A; it can do some of the things that class A does differently. (wikipedia)


```python
class Animal:
    def __init__(self, name=''):
        self.name = name

    def talk(self):
        pass
    
    def getHeadCount(self):
        return 1

class Cat(Animal):
   def talk(self):
      print ("Meow!")


class Dog(Animal):
   def talk(self):
      print ("Woof!")


a = Animal()
a.talk()

cat = Cat("Missy")
cat.talk()
print(cat.getHeadCount())

dog = Dog("Rocky")
dog.talk()
print(dog.getHeadCount())
```

    Meow!
    1
    Woof!
    1
    


```python

```
