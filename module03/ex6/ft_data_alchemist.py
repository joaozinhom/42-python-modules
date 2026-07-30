import random

PLAYERS = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]

MIN_SCORE = 0
MAX_SCORE = 999


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")
    capitalized = [name.capitalize() for name in PLAYERS]
    already_capitalized = [name for name in PLAYERS if name[0].isupper()]
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {already_capitalized}")
    scores = {name: random.randint(MIN_SCORE, MAX_SCORE)
              for name in capitalized}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high_scores = {name: scores[name] for name in scores
                   if scores[name] > average}
    print(f"High scores: {high_scores}")
    return (None)


if __name__ == "__main__":
    main()
