def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    # Deferred so the prints above run first; this import triggers the
    # circular dependency between dark_spellbook and dark_validator and
    # raises ImportError on purpose.
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    spell = dark_spell_record("Necromancy", "Bats and frogs")
    print(f"Testing record dark spell: {spell}")


if __name__ == "__main__":
    main()
