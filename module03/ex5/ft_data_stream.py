import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]

ACTIONS = ["run", "eat", "sleep", "grab", "move",
           "climb", "swim", "release", "use"]

EVENT_COUNT = 1000
LIST_SIZE = 10

Event = tuple[str, str]


def gen_event() -> typing.Generator[Event, None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(events: list[Event]) -> typing.Generator[Event, None, None]:
    while (len(events) > 0):
        index = random.randrange(len(events))
        event = events[index]
        del events[index]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(EVENT_COUNT):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")
    events = [next(stream) for _ in range(LIST_SIZE)]
    print(f"Built list of {len(events)} events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
    return (None)


if __name__ == "__main__":
    main()
