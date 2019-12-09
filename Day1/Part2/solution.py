def compute_fuel(mass):
    total_fuel, current_mass = 0, mass
    
    while (current_mass := current_mass // 3 - 2 ) >= 0:
        total_fuel += current_mass

    return total_fuel

def get_total():
    with open("../data/input") as f:
        total = sum(map(lambda x: compute_fuel(int(x)), f.read().splitlines()))

    return total

print("Total amount of fuel: {}".format(get_total()))