class Plant:
	def __init__(self, name, height, age):
		self._name = name
		self._height = 0.0
		self._age = 0
		self.set_height(height)
		self.set_age(age)

	def set_height(self, value):
		if value < 0:
			print(f"{self._name.title()}: Error, height can't be negative")
			return False
		self._height = float(value)
		return True

	def set_age(self, value):
		if value < 0:
			print(f"{self._name.title()}: Error, age can't be negative")
			return False
		self._age = value
		return True

	def get_height(self):
		return self._height

	def get_age(self):
		return self._age

	def show(self):
		print(f"{self._name.title()}: {self.get_height()}cm, {self.get_age()} days old")


if __name__ == "__main__":
	print("=== Garden Security System ===")

	rose = Plant("rose", 15.0, 10)
	print("Plant created:", end=" ")
	rose.show()

	if rose.set_height(25):
		print("Height updated: 25cm")
	if rose.set_age(30):
		print("Age updated: 30 days")

	if not rose.set_height(-5):
		print("Height update rejected")
	if not rose.set_age(-3):
		print("Age update rejected")

	print("Current state:", end=" ")
	rose.show()