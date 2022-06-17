import math

class Circle():
    _area = None
    _radius = None

    def __init__(self, radius):
        self.set_radius(radius)

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius
        self._area = 3.14*radius*radius

    radius = property(get_radius, set_radius)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area
        self._radius = math.sqrt(self._area)/3.14


c = Circle(10)
print(c.radius)
print(c.area)

print("---")
c.radius=222

print(c.radius)
print(c.area)

c.area=154751

print(c.radius)
print(c.area)
