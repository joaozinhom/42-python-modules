def check_temperature(temp_str: str) -> int:
    try:
        value = int(temp_str)
    except ValueError:
        raise ValueError(f"Error : '{temp_str}' is not a valid number")
    if (value < 0):
        raise ValueError(f"Error: {value}°C is too cold for plants (min 0°C)")
    if (value > 40):
        raise ValueError(f"Error: {value}°C is too hot for plants (max 40°C)")
    return (value)


def test_temperature_input(string_value: str) -> None:
    print(f"Testing temperature: {string_value}")
    try:
        print(
            f"Temperature {check_temperature(string_value)}°C "
            f"is perfect for plants!")
    except Exception as e:
        print(e)
    return (None)


print("=== Garden Temperature Checker ===")
test_temperature_input("25")
print("\n")
test_temperature_input("abc")
print("\n")
test_temperature_input("100")
print("\n")
test_temperature_input("-50")
print("\n")
print("All tests completed - program didn't crash !")
