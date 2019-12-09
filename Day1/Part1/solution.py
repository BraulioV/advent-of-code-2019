def get_total():
    with open("../data/input") as f:
        total = sum(map(lambda x: int(x)//3 - 2, f.read().splitlines()))

    return total

print("Total amount of fuel: {}".format(get_total()))