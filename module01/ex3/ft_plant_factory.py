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
	print("=== Plant Factory Output ===")
	plants = [
		Plant("rose",25.0,30,1,1),
		Plant("oak",200.0,365,1,1),
		Plant("cactus",5.0,90,1,1),
		Plant("sunflower",80.45,30,1,1),
		Plant("Fern",15.0,120,1,1)
		]
	for c in plants:
		print(f"Created:", end=" ")
		c.show()
	