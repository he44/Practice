def rec_fuel(mass):
    total = 0
    while mass > 0:
        fuel = int(mass / 3) - 2
        if fuel > 0:
            total += fuel
        mass = fuel
    return total

"""
test_m = [14, 1969, 100756]
for m in test_m:
    print(rec_fuel(m))
"""

input_file = 'input.txt'

with open(input_file, 'r') as fp:
    lines = fp.readlines()

total_fuel = 0
for line in lines:
    mass = int(line)
    fuel = rec_fuel(mass)
    print(mass, fuel)
    total_fuel += fuel

print('Sum of the fuel requirements is %d'%total_fuel)
