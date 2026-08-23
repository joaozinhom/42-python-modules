def validate_ingredients(ingredients: str) -> str:
    # Deferred import breaks the circular dependency: light_spellbook is
    # only imported when this function runs, not at module load time.
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    is_valid = any(item.lower() in lowered for item in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {keyword}"
