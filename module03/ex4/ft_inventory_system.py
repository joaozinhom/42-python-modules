import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        parts = arg.split(":")
        if (len(parts) != 2):
            print(f"Error - invalid parameter '{arg}'")
            continue
        name = parts[0].strip()
        quantity = parts[1].strip()
        if (len(name) == 0):
            print(f"Error - invalid parameter '{arg}'")
            continue
        if (name in inventory.keys()):
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            value = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        if (value < 0):
            print(f"Quantity error for '{name}': quantity cannot be negative")
            continue
        inventory.update({name: value})
    return (inventory)


def print_percentages(inventory: dict[str, int], total: int) -> None:
    if (total == 0):
        print("Nothing to share: the inventory is empty")
        return (None)
    for item in inventory.keys():
        share = round(inventory[item] / total * 100, 1)
        print(f"Item {item} represents {share}%")
    return (None)


def print_extremes(inventory: dict[str, int]) -> None:
    items = list(inventory.keys())
    most = items[0]
    least = items[0]
    for item in items:
        if (inventory[item] > inventory[most]):
            most = item
        if (inventory[item] < inventory[least]):
            least = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    return (None)


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    if (len(inventory) == 0):
        print("Empty inventory. Usage: python3 "
              "ft_inventory_system.py <item_name>:<quantity> ...")
        return (None)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    print_percentages(inventory, total)
    print_extremes(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
    return (None)


if __name__ == "__main__":
    main()
