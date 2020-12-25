import string

def main():
    in_fname = "i1_eg.txt"
    in_fname = "valid_eg.txt"
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

ECLS = [
    "amb", 
    "blu",
    "brn",
    "gry", 
    "grn", 
    "hzl", 
    "oth"
]

def validator(field_name, content):
    if field_name == "byr":
        content = int(content)
        if content < 1920 or content > 2002:
            return False
    elif field_name == "iyr":
        content = int(content)
        if content < 2010 or content > 2020:
            return False
    elif field_name == "eyr":
        content = int(content)
        if content < 2020 or content > 2030:
            return False
    elif field_name == "hgt":
        unit = content[-2:]
        val = int(content[:-2])
        if unit == "cm":
            if val < 150 or val > 193:
                return False
        elif unit == "in":
            if val < 59 or val > 76:
                return False
        # unknown unit
        else:
            return False
    elif field_name == "hcl":
        # https://stackoverflow.com/questions/11592261/check-if-a-string-is-hexadecimal
        return content[0] == "#" and len(content) == 7 and all(c in string.hexdigits for c in content[1:])
    elif field_name == "ecl":
        return (content in ECLS)
    elif field_name == "pid":
        return len(content) == 9 and all(c in string.digits for c in content)
    elif field_name == "cid":
        return True

    return True


def check(passport):
    print("Checking passport: {}".format(passport))
    lines = passport.split('\n')
    seen_fields = dict()
    for line in lines:
        fields = line.split()
        for field in fields:
            field_name, content = field.split(':')
            seen_fields[field_name] = content
    print("Saw fields: {}".format([item for item in seen_fields]))
    for required_field in FIELDS[:-1]:
        if required_field not in seen_fields:
            return False
        if not validator(required_field, seen_fields[required_field]):
            return False
    return True


if __name__ == "__main__":
    main()

