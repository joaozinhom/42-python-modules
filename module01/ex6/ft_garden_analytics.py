class Plant:
    class _Statistics:
        def __init__(self):
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def record_grow(self):
            self.__grow_calls += 1

        def record_age(self):
            self.__age_calls += 1

        def record_show(self):
            self.__show_calls += 1

        def display(self):
            print(f"  grow() calls: {self.__grow_calls}")
            print(f"  age() calls: {self.__age_calls}")
            print(f"  show() calls: {self.__show_calls}")

    def __init__(self, name, height, age):
        self._name = name
        self._height = 0.0
        self._age = 0
        self._stats = self._Statistics()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("anonymous", 0, 0)

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

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_stats(self):
        return self._stats

    def show(self):
        self._stats.record_show()
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


class Seed(Flower):
    def __init__(self, name, height, age, color, bloom_state, seed_count=0):
        super().__init__(name, height, age, color, bloom_state)
        self.seed_count = seed_count

    def bloom(self):
        super().bloom()
        self.seed_count = 12

    def show(self):
        super().show()
        if self.bloom_state:
            print(f"  Seeds produced: {self.seed_count}")
        else:
            print("  Seeds produced: none yet (not bloomed)")


class Tree(Plant):
    class _Statistics(Plant._Statistics):
        def __init__(self):
            super().__init__()
            self.__shade_calls = 0

        def record_shade(self):
            self.__shade_calls += 1

        def display(self):
            super().display()
            print(f"  produce_shade() calls: {self.__shade_calls}")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        self._stats.record_shade()
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
        self._stats.record_grow()
        print(f"[growing the {self._name}]")
        self.set_height(self.get_height() + 1.0)
        self.nutritional_value += 1

    def age(self):
        self._stats.record_age()
        print(f"[aging the {self._name}]")
        self.set_age(self.get_age() + 1)
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f"  Harvest season: {self.harvest_season}")
        print(f"  Nutritional value: {self.nutritional_value}")


def display_statistics(plant):
    print(f"Statistics for {plant.get_name().title()}:")
    plant.get_stats().display()


if __name__ == "__main__":
    print("Is 400 days older than a year?", Plant.is_older_than_year(400))
    print("Is 200 days older than a year?", Plant.is_older_than_year(200))
    print()

    unknown = Plant.anonymous()
    unknown.show()
    print()

    rose = Flower("rose", 4, 10, "red", False)
    rose.show()
    rose.bloom()
    rose.show()
    print()

    dandelion = Seed("dandelion", 15, 30, "yellow", False)
    dandelion.show()
    dandelion.bloom()
    dandelion.show()
    print()

    oak = Tree("oak", 500, 3650, 30)
    oak.show()
    oak.produce_shade()
    oak.produce_shade()
    print()

    carrot = Vegetable("carrot", 2, 5, "autumn")
    carrot.grow()
    carrot.age()
    carrot.show()
    print()

    print("===== ANALYTICS =====")
    for plant in (unknown, rose, dandelion, oak, carrot):
        display_statistics(plant)
