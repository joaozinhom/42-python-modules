def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    iterative_loop(1, days)
    print("Harvest time!")


def iterative_loop(indice, day):
    if (indice > day):
        return 0
    else:
        print(f"Day {indice}")
    iterative_loop(indice+1, day)
