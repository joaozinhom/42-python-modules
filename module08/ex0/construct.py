import os
import site
import sys


def in_virtual_environment() -> bool:
    """Return True when the interpreter runs inside a virtual environment.

    A virtual environment sets ``sys.prefix`` to the venv directory while
    ``sys.base_prefix`` keeps pointing at the base installation. Legacy
    ``virtualenv`` sets ``sys.real_prefix`` instead.
    """
    if hasattr(sys, "real_prefix"):
        return True
    return sys.prefix != sys.base_prefix


def site_packages_path() -> str:
    """Best-effort location where packages get installed for this Python."""
    try:
        packages = site.getsitepackages()
        if packages:
            return packages[0]
    except AttributeError:
        pass
    return str(site.getusersitepackages())


def report_inside() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(site_packages_path())


def report_outside() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


def main() -> None:
    if in_virtual_environment():
        report_inside()
    else:
        report_outside()


if __name__ == "__main__":
    main()
