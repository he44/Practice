in_name = "i1_eg.txt"

with open(in_name, "r") as fp:
    lines = fp.readlines()


# mapping from ingredients to possible allergens
possible = dict()

for line in lines:
    ingredients, allergens = line.strip().split("contains ")
    ingredient_list = ingredients.split('(')[0].split()
    allergen_list = allergens.split(')')[0].split(", ")
    print("Ingredients: {}".format(ingredient_list))
    print("Allergens: {}".format(allergen_list))
    for ingredient in ingredient_list:
        if ingredient not in possible:
            possible[ingredient] = []
        for allergen in allergen_list:
            possible[ingredient].append(allergen)
print(possible)
    
