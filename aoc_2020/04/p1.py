def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    passports = open(in_fname).read().strip().split('\n\n')

    valid_num = 0
    for passport in passports:
        if check(passport):
            valid_num += 1

    print(valid_num)

FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl", 
    "ecl",
    "pid",
    "cid"
]

def check(passport):
    lines = passport.split('\n')
    seen_fields = set()
    for line in lines:
        fields = line.split()
        for field in fields:
            field_name, _ = field.split(':')
            seen_fields.add(field_name)
    for required_field in FIELDS[:-1]:
        if required_field not in seen_fields:
            return False
    return True


if __name__ == "__main__":
    main()

