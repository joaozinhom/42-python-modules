import random

ACHIEVEMENTS = [
    "First Steps", "Speed Runner", "Master Explorer", "Treasure Hunter",
    "Boss Slayer", "Survivor", "Collector Supreme", "Untouchable",
    "Sharp Mind", "Strategist", "World Savior", "Crafting Genius",
    "Unstoppable", "Hidden Path Finder", "Dragon Tamer", "Night Owl",
    "Perfect Landing", "Lock Picker", "Potion Brewer", "Beast Whisperer",
    "Silent Blade", "Storm Chaser", "Gold Hoarder", "Map Maker",
    "Puzzle Breaker", "Loyal Companion", "Arena Champion", "Deep Diver",
    "Star Gazer", "Trap Dodger", "Rune Reader", "Ghost Hunter",
    "Iron Will", "Quick Draw", "Peace Keeper", "Legend Born",
]

PLAYER_NAMES = ["Alice", "Bob", "Charlie", "Dylan"]

MIN_PICKED = 16
MAX_PICKED = 20


def gen_player_achievements() -> set[str]:
    picked = random.randint(MIN_PICKED, MAX_PICKED)
    return (set(random.sample(ACHIEVEMENTS, picked)))


def get_union(players: list[tuple[str, set[str]]],
              skipped: str = "") -> set[str]:
    union: set[str] = set()
    for name, owned in players:
        if (name != skipped):
            union = union.union(owned)
    return (union)


def get_common(players: list[tuple[str, set[str]]]) -> set[str]:
    common = set(ACHIEVEMENTS)
    for _, owned in players:
        common = common.intersection(owned)
    return (common)


def main() -> None:
    print("=== Achievement Tracker System ===")
    players: list[tuple[str, set[str]]] = []
    for name in PLAYER_NAMES:
        players.append((name, gen_player_achievements()))
    for name, owned in players:
        print(f"Player {name}: {owned}")
    print(f"All distinct achievements: {get_union(players)}")
    print(f"Common achievements: {get_common(players)}")
    for name, owned in players:
        others = get_union(players, name)
        print(f"Only {name} has: {owned.difference(others)}")
    catalog = set(ACHIEVEMENTS)
    for name, owned in players:
        print(f"{name} is missing: {catalog.difference(owned)}")
    return (None)


if __name__ == "__main__":
    main()
