"""Exercise 3: Ancient Library - the functools module's treasures.

Demonstrates reduce, partial, lru_cache and singledispatch, combined with
the operator module, to build powerful functional artifacts.
"""
import functools
import operator
from collections.abc import Callable
from typing import Any

# Binary operations for the reducer, keyed by their spell name.
REDUCE_OPS: dict[str, Callable[[int, int], int]] = {
    "add": operator.add,
    "multiply": operator.mul,
    "max": lambda left, right: left if left > right else right,
    "min": lambda left, right: left if left < right else right,
}


def spell_reducer(spells: list[int], operation: str) -> int:
    """Combine all spell powers with functools.reduce and the operator module.

    Returns 0 for an empty list and raises ValueError for an unknown
    operation.
    """
    if operation not in REDUCE_OPS:
        raise ValueError(f"Unknown operation: {operation}")
    if not spells:
        return 0
    return functools.reduce(REDUCE_OPS[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    """Build three specialized enchantments pre-filling power=50 and element.

    functools.partial freezes the leading ``power`` and ``element`` arguments,
    leaving only the ``target`` to be provided at call time.
    """
    return {
        element: functools.partial(base_enchantment, 50, element)
        for element in ("fire", "ice", "lightning")
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, cached via functools.lru_cache."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a functools.singledispatch spell system, keyed on type."""

    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _cast_damage(spell: int) -> str:
        return f"{spell} damage"

    @cast.register(str)
    def _cast_enchantment(spell: str) -> str:
        return spell

    @cast.register(list)
    def _cast_multi(spell: list[Any]) -> str:
        return f"{len(spell)} spells"

    return cast


def enchant_target(power: int, element: str, target: str) -> str:
    return f"{element.title()} enchantment ({power}) on {target}"


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(enchant_target)
    print(enchanters["fire"]("Sword"))

    print("\nTesting memoized fibonacci...")
    for index in (0, 1, 10, 15):
        print(f"Fib({index}): {memoized_fibonacci(index)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(f"Damage spell: {cast(42)}")
    print(f"Enchantment: {cast('fireball')}")
    print(f"Multi-cast: {cast(['fireball', 'heal', 'shield'])}")
    print(cast(3.14))


if __name__ == "__main__":
    main()
