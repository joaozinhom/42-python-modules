from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._rank, str(item)))
                self._rank += 1
        else:
            self._storage.append((self._rank, str(data)))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._rank, item))
                self._rank += 1
        else:
            self._storage.append((self._rank, data))
            self._rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str) for k, v in data.items())
        if isinstance(data, list):
            return all(
                isinstance(entry, dict) and
                all(isinstance(k, str) and isinstance(v, str) for k, v in entry.items())
                for entry in data
            )
        return False

    def ingest(self, data: dict | list) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for entry in data:
                formatted = f"{entry['log_level']}: {entry['log_message']}"
                self._storage.append((self._rank, formatted))
                self._rank += 1
        else:
            formatted = f"{data['log_level']}: {data['log_message']}"
            self._storage.append((self._rank, formatted))
            self._rank += 1


def main():
    print("=== Code Nexus - Data Processor ===")

    # --- NumericProcessor ---
    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()

    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore
    except TypeError as e:
        print(f"Got exception: {e}")

    numeric.ingest([1, 2, 3, 4, 5])
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    # --- TextProcessor ---
    print("\nTesting Text Processor...")
    text = TextProcessor()

    print(f"Trying to validate input '42': {text.validate(42)}")

    text.ingest(['Hello', 'Nexus', 'World'])
    print("Processing data: ['Hello', 'Nexus', 'World']")
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    # --- LogProcessor ---
    print("\nTesting Log Processor...")
    log = LogProcessor()

    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR',  'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
