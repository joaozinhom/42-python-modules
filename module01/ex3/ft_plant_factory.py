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
    print("=== Plant Factory Output ===")
    plants = [
        Plant("rose", 25.0, 30, 1, 1),
        Plant("oak", 200.0, 365, 1, 1),
        Plant("cactus", 5.0, 90, 1, 1),
        Plant("sunflower", 80.45, 30, 1, 1),
        Plant("Fern", 15.0, 120, 1, 1),
    ]
    for c in plants:
        print("Created:", end=" ")
        c.show()
