"""Loading Programs: a data-analysis tool built on pip / Poetry deps.

The program checks that its scientific dependencies are available, then uses
numpy to *generate* the dataset, pandas to manipulate it and matplotlib to
render a visualization. Missing dependencies are reported gracefully with
installation instructions for both pip and Poetry.
"""
import importlib
import importlib.metadata
from types import ModuleType
from typing import Optional

REQUIRED: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}

OUTPUT_IMAGE = "matrix_analysis.png"
DATA_POINTS = 1000


def version_of(package: str) -> str:
    """Return the installed version of a package, or 'unknown'."""
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def load_module(name: str) -> Optional[ModuleType]:
    """Import a module by name, returning None when it is not installed."""
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def print_install_help(missing: list[str]) -> None:
    """Explain how to install the missing packages with pip and Poetry."""
    print()
    print("MISSING DEPENDENCIES:")
    for package in missing:
        print(f"[MISSING] {package} is not installed")
    print()
    print("Install with pip:")
    print("    pip install -r requirements.txt")
    print()
    print("Install with Poetry:")
    print("    poetry install")
    print()
    print(
        "pip reads requirements.txt and installs into the active "
        "environment;"
    )
    print(
        "Poetry reads pyproject.toml, resolves a locked dependency tree "
        "and"
    )
    print("manages its own isolated environment for you.")


def check_dependencies() -> list[str]:
    """Print the status of every required dependency, return the missing."""
    print("Checking dependencies:")
    missing: list[str] = []
    for package, message in REQUIRED.items():
        if load_module(package) is None:
            print(f"[MISSING] {package} - {message}")
            missing.append(package)
        else:
            print(f"[OK] {package} ({version_of(package)}) - {message}")
    return missing


def run_analysis() -> None:
    """Generate Matrix data with numpy, process it and plot it."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print()
    print("Analyzing Matrix data...")
    rng = np.random.default_rng(42)
    signal = np.cumsum(rng.normal(0, 1, DATA_POINTS))
    noise = rng.normal(0, 0.5, DATA_POINTS)
    frame = pd.DataFrame({"signal": signal, "noise": noise})
    frame["rolling"] = frame["signal"].rolling(window=25).mean()

    print(f"Processing {DATA_POINTS} data points...")
    print("Generating visualization...")
    figure, axis = plt.subplots(figsize=(10, 5))
    axis.plot(frame.index, frame["signal"], color="#00ff41", label="signal")
    axis.plot(
        frame.index, frame["rolling"], color="white", label="trend (rolling)"
    )
    axis.set_title("Matrix Data Analysis")
    axis.set_xlabel("data point")
    axis.set_ylabel("value")
    axis.legend()
    figure.savefig(OUTPUT_IMAGE)
    plt.close(figure)

    print()
    print("Analysis complete!")
    print(f"Results saved to: {OUTPUT_IMAGE}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    missing = check_dependencies()
    if missing:
        print_install_help(missing)
        return
    run_analysis()


if __name__ == "__main__":
    main()
