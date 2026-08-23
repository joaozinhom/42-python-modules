from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lowered = ingredients.lower()
    is_valid = any(item.lower() in lowered for item in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {keyword}"
