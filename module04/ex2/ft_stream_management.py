import sys
import typing


def print_error(message: str) -> None:
    """Send a message to the error stream instead of the standard one."""
    print(f"[STDERR] {message}", file=sys.stderr)
    return (None)


def ask_user(prompt: str) -> str:
    """Read one line from the standard input, without input()."""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line = sys.stdin.readline()
    return (line.strip())


def recover_archive(file_name: str) -> str | None:
    """Open a file, display its content like cat, then close it.

    Returns the content read, or None if the file could not be used.
    """
    file: typing.IO | None = None
    content: str | None = None
    try:
        file = open(file_name, "r")
        content = file.read()
        print(f"---\n\n{content}\n---")
    except Exception as error:
        print_error(f"Error opening file '{file_name}': {error}")
    if file is not None:
        file.close()
        print(f"File '{file_name}' closed.")
    return (content)


def transform_archive(content: str) -> str:
    """Append the 2087-compatible archive character to every line."""
    new_content = ""
    for line in content.splitlines():
        new_content += line + "#\n"
    return (new_content)


def save_archive(file_name: str, content: str) -> None:
    """Create the file (or replace it) and write the content in it."""
    file: typing.IO | None = None
    saved = False
    try:
        file = open(file_name, "w")
        file.write(content)
        saved = True
    except Exception as error:
        print_error(f"Error opening file '{file_name}': {error}")
    if file is not None:
        file.close()
    if saved:
        print(f"Data saved in file '{file_name}'.")
    else:
        print("Data not saved.")
    return (None)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return (None)
    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    content = recover_archive(file_name)
    if content is None:
        return (None)
    print("\nTransform data:")
    new_content = transform_archive(content)
    print(f"---\n\n{new_content}\n---")
    new_name = ask_user("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return (None)
    print(f"Saving data to '{new_name}'")
    save_archive(new_name, new_content)
    return (None)


if __name__ == "__main__":
    main()
