"""Exercise 1: Higher Realm - functions operating on functions.

Spells all share the contract ``spell(target: str, power: int) -> str``.
The helpers below take spells and return brand-new spells, proving that
functions are first-class citizens in Python.
"""
from collections.abc import Callable

Spell = Callable[[str, int], str]


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power}"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power}"


def spell_combiner(
    spell1: Spell, spell2: Spell
) -> Callable[[str, int], tuple[str, str]]:
    """Return a spell that casts both spells and returns a tuple of results."""
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
    base_spell: Spell, multiplier: int
) -> Spell:
    """Return a spell identical to base_spell but with power multiplied."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Spell,
) -> Spell:
    """Return a spell that only casts when condition(*args) is truthy."""
    def guarded(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return guarded


def spell_sequence(
    spells: list[Spell],
) -> Callable[[str, int], list[str]]:
    """Return a spell that casts every spell in order, collecting results."""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result: " + ", ".join(combined("Dragon", 50)))

    print("\nTesting power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Goblin', 10)}")
    print(f"Amplified: {amplified('Goblin', 10)}")

    print("\nTesting conditional caster...")
    only_strong: Spell = conditional_caster(
        lambda target, power: power >= 20, fireball
    )
    print(only_strong("Slime", 5))
    print(only_strong("Slime", 40))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for result in sequence("Wraith", 30):
        print(result)


if __name__ == "__main__":
    main()
