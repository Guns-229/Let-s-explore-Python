class Apple():
	def __init__(self, height, radius_range, color, weight):
		self.height = height
		self.largest_radius, self.smallest_radius = radius_range
		self.color = color
		self.weight = weight
		
a = Apple(10,[20,10], "red", 12)
print(a.largest_radius)
b = Apple(20,[20,10], "red", 12)
print(a==b)
b.heigh = 10
print(a==b)

        
