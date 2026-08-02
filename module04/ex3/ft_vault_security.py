def secure_archive(file_name: str,
                   action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    """Safely read from or write to a vault using a context manager.

    The 'with' statement closes the file even when an error is raised,
    so no file descriptor ever leaks out of this function.

    Returns (True, content read or success message) on success,
    or (False, error message) on failure.
    """
    if action not in ("read", "write"):
        return (False, f"Unknown action '{action}'")
    try:
        if action == "read":
            with open(file_name, "r") as file:
                return (True, file.read())
        with open(file_name, "w") as file:
            file.write(content)
        return (True, "Content successfully written to file")
    except Exception as error:
        return (False, f"{error}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    status, data = secure_archive("ancient_fragment.txt")
    print((status, data))
    if not status:
        return (None)
    print("\nUsing 'secure_archive' to write previous content "
          "to a new file:")
    print(secure_archive("vault_copy.txt", "write", data))
    return (None)


if __name__ == "__main__":
    main()
