import sys


def main() -> None:
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    args = sys.argv[1:]
    if (len(args) == 0):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i = i + 1
    print(f"Total arguments: {len(sys.argv)}")
    return (None)


if __name__ == "__main__":
    main()
