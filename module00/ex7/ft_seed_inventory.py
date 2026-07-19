def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if (unit == "packets"):
        print(f"{seed_type.title()} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_type.title()} seeds: {quantity} {unit} available")
    elif (unit == "area"):
        print(f"{seed_type.title()} seeds: covers {quantity} square metters")
    else:
        print("Unknown unit type")
