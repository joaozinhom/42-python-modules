def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        value = int("abc")
        print(value)
    elif (operation_number == 1):
        result = 10 / 0
        print(result)
    elif (operation_number == 2):
        file = open("/non/existent/file")
        print(file)
    elif (operation_number == 3):
        message = "Temperature: " + 25
        print(message)
    return (None)


def test_error_types() -> None:
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            if (operation_number >= 4):
                print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    return (None)


print("=== Garden Error Types Demo ===")
test_error_types()
print("\nAll error types tested successfully!")
