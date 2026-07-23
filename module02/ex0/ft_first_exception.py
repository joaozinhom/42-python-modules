def check_input(temp_str: str) -> int:
    try:
        value = int(temp_str)
    except ValueError:
        raise ValueError(
            f"Caught input_temperature error: invalid literal "
            f"for int() with base 10: '{temp_str}'")
    return (value)


def test_temperature_input(string_value: str) -> None:
    print(f"Input data is {string_value}")
    try:
        print(f"Temperature is now {check_input(string_value)}°C")
    except Exception as e:
        print(e)
    return (None)


print("=== Garden Temperature Checker ===")
test_temperature_input("25")
print("\n")
test_temperature_input("abc")
print("\n")
print("All tests completed - program didn't crash !")
