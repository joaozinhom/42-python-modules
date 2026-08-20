class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float, jump: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age
        self.growth = growth
        self.jump = jump

    def show(self) -> None:
        print(
            f"{(self.name).title()}: {self.height}cm, "
            f"{self.age_days} days old"
        )

    def grow(self) -> None:
        self.height += self.jump

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    cactus = Plant("Cactus", 42, 42, 0, 0.5)
    c = 0
    cactus.show()
    for c in range(0, 7):
        cactus.grow()
        cactus.age()
        cactus.show()
