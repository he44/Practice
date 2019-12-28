input_file = 'input.txt'

with open(input_file, 'r') as fp:
    lines = fp.readlines()

total_fuel = 0
for line in lines:
    mass = int(line)
    fuel = int(mass / 3) - 2
    print(mass, fuel)
    total_fuel += fuel

print('Sum of the fuel requirements is %d'%total_fuel)
