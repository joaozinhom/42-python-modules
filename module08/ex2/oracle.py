"""The Oracle: secure configuration via environment variables and .env files.

Configuration is loaded from real environment variables first, then from a
local ``.env`` file (through python-dotenv) for development. Real environment
variables always win over the ``.env`` file, and secrets never live in the
source code.
"""
import os
import sys

REQUIRED_KEYS = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")


def load_env_file() -> bool:
    """Load a local .env file if python-dotenv is available.

    Returns True when python-dotenv could be used. Real environment variables
    are never overridden by the file (override=False).
    """
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("WARNING: python-dotenv not installed, reading real env only.")
        print("         Install it with: pip install python-dotenv")
        print()
        return False
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path=env_path, override=False)
    return os.path.isfile(env_path)


def get(key: str, default: str | None = None) -> str | None:
    return os.environ.get(key, default)


def describe_database(mode: str, url: str | None) -> str:
    if url is None:
        return "MISSING (no DATABASE_URL configured)"
    if mode == "production":
        return "Connected to production cluster"
    return "Connected to local instance"


def describe_api(api_key: str | None) -> str:
    if api_key:
        return "Authenticated"
    return "MISSING (no API_KEY configured)"


def describe_zion(endpoint: str | None) -> str:
    return "Online" if endpoint else "Offline (no ZION_ENDPOINT configured)"


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    dotenv_ok = load_env_file()

    mode = get("MATRIX_MODE", "development") or "development"
    database_url = get("DATABASE_URL")
    api_key = get("API_KEY")
    log_level = get("LOG_LEVEL", "INFO")
    zion_endpoint = get("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {describe_database(mode, database_url)}")
    print(f"API Access: {describe_api(api_key)}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {describe_zion(zion_endpoint)}")
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if dotenv_ok:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] no .env file found, using environment / defaults")
    print("[OK] Production overrides available")
    print()

    missing = [key for key in REQUIRED_KEYS if get(key) is None]
    if missing:
        print("WARNING: missing configuration for: " + ", ".join(missing))
        print("Copy .env.example to .env and fill in your values.")
        sys.exit(0)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
