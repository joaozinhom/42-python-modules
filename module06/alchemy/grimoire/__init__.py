from .light_spellbook import (
    light_spell_allowed_ingredients,
    light_spell_record,
)

# Dark magic is intentionally NOT exposed here: ft_kaboom_1.py must reach
# into dark_spellbook directly to trigger the circular-import explosion.
__all__ = ["light_spell_allowed_ingredients", "light_spell_record"]
