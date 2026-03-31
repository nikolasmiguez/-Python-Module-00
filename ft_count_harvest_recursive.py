def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))

    def counter(current, max_days):
        if current > max_days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        counter(current + 1, max_days)

    counter(1, harvest)
