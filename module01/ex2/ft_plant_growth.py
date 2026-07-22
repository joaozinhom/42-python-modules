class Plant:
	def __init__(self, name, height, age, growth, jump):
		self.name = name
		self.height = height
		self.age = age
		self.growth = growth
		self.jump = jump
	def show(self):
		print(f"{(self.name).title()}: {self.height}cm, {self.age} days old")

	def grow(self):
		self.height += self.jump

	def grow_age(self):
		self.age += 1
	
if __name__ == "__main__":
	print("=== Garden Plant Growth ===")
	cactus = Plant("Cactus", 42, 42, 0, 0.5)
	c = 0
	cactus.show()
	for c in range(0,7):
		cactus.grow()
		cactus.grow_age()
		cactus.show()