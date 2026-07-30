import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        entry = input("Enter new coordinates as floats "
                      "in format 'x,y,z': ")
        parts = entry.split(",")
        if (len(parts) != 3):
            print("Invalid syntax")
            continue
        coords: list[float] = []
        for part in parts:
            value = part.strip()
            try:
                coords.append(float(value))
            except ValueError as e:
                print(f"Error on parameter '{value}': {e}")
                break
        if (len(coords) == 3):
            return (coords[0], coords[1], coords[2])


def get_distance(first: tuple[float, float, float],
                 second: tuple[float, float, float]) -> float:
    return (math.sqrt((second[0] - first[0]) ** 2
                      + (second[1] - first[1]) ** 2
                      + (second[2] - first[2]) ** 2))


def main() -> None:
    print("=== Game Coordinate System ===")
    print("")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    center = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(get_distance(center, first), 4)}")
    print("")
    print("Get a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(get_distance(first, second), 4)}")
    return (None)


if __name__ == "__main__":
    main()
