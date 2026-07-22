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
        print(
            f"{self._name.title()}: {self.get_height()}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(self, name, height, age, color: str, bloom_state: bool):
        super().__init__(name, height, age)
        self.color = color
        self.bloom_state = bloom_state

    def bloom(self):
        print(f"[asking the {self._name} to bloom]")
        self.bloom_state = True

    def show(self):
        super().show()
        print(f"  Color: {self.color}")
        if self.bloom_state:
            print(f"{self._name.title()} is blooming beautifully!")
        else:
            print(f"{self._name.title()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name.title()} now produces a shade of "
            f"{self.get_height()}cm long and "
            f"{float(self.trunk_diameter)}cm wide."
        )

    def show(self):
        super().show()
        print(f"  Trunk diameter: {float(self.trunk_diameter)}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        print(f"[growing the {self._name}]")
        self.set_height(self.get_height() + 1.0)
        self.nutritional_value += 1

    def age(self):
        print(f"[aging the {self._name}]")
        self.set_age(self.get_age() + 1)
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f"  Harvest season: {self.harvest_season}")
        print(f"  Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    rose = Flower("rose", 4, 10, "red", False)
    rose.show()
    rose.bloom()
    rose.show()
    print()

    oak = Tree("oak", 500, 3650, 30)
    oak.show()
    oak.produce_shade()
    print()

    carrot = Vegetable("carrot", 2, 5, "autumn")
    carrot.show()
    carrot.grow()
    carrot.age()
    carrot.show()
