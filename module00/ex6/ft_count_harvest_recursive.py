def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    iterative_loop(1, days)
    print("Harvest time!")


def iterative_loop(indice: int, day: int) -> None:
    if (indice > day):
        return
    else:
        print(f"Day {indice}")
    iterative_loop(indice+1, day)
