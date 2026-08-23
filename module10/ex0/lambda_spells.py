"""Exercise 0: Lambda Sanctum - mastering anonymous functions.

Every transformation below is expressed with a lambda passed to a built-in
higher-order function (sorted, filter, map, min, max), never a named helper.
"""
from typing import Any


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by their 'power' level, descending."""
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Keep only the mages whose 'power' is at least min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name with a '* ' prefix and a ' *' suffix."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return the strongest, weakest and average power of the mages."""
    strongest = max(mages, key=lambda mage: mage["power"])
    weakest = min(mages, key=lambda mage: mage["power"])
    total = sum(map(lambda mage: mage["power"], mages))
    average = round(total / len(mages), 2)
    return {
        "max_power": strongest["power"],
        "min_power": weakest["power"],
        "avg_power": average,
    }


def main() -> None:
    artifacts: list[dict] = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Ice Wand", "power": 70, "type": "wand"},
    ]
    mages: list[dict[str, Any]] = [
        {"name": "Lex", "power": 60, "element": "arcane"},
        {"name": "Jordan", "power": 95, "element": "fire"},
        {"name": "Riley", "power": 80, "element": "water"},
    ]

    print("Testing artifact sorter...")
    ranked = artifact_sorter(artifacts)
    print(f"{ranked[0]['name']} ({ranked[0]['power']} power) comes before "
          f"{ranked[1]['name']} ({ranked[1]['power']} power)")

    print("\nTesting power filter...")
    strong = power_filter(mages, 80)
    print(f"Mages with power >= 80: "
          f"{', '.join(mage['name'] for mage in strong)}")

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(["fireball", "heal", "shield"])))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
