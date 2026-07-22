class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{(self.name).title()}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 1, 25)
    rose.show()
    sunflower = Plant("Sunflower", 24, 27)
    sunflower.show()
    cactus = Plant("Cactus", 34, 1)
    cactus.show()
