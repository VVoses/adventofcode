import re

infile = open('PATHHERE', 'r')

lines = infile.read().split("\n\n")
infile.close()
passports = [line.split() for line in lines]
pports = [] #list of passports
valid = 0 #valid passports


def validate(key, val):
    if key == "byr" and int(val) >= 1920 and int(val) <= 2002:
        return True
    elif key == "iyr" and int(val) >= 2010 and int(val) <= 2020:
        return True
    elif key == "eyr" and int(val) >= 2020 and int(val) <= 2030:
        return True
    elif key == "hgt" and val[-2:] == "cm":
        return int(val[:-2]) >= 150 and int(val[:-2]) <= 193
    elif key == "hgt" and val[-2:] == "in":
        return int(val[:-2]) >= 59 and int(val[:-2]) <= 76
    elif key == "hcl":
        return not (re.match("#[0-9a-fA-F]{6}", val)) == None
    elif key == "ecl":
        return not (re.match("amb|blu|brn|gry|grn|hzl|oth", val)) == None
    elif key == "pid":
        return not (re.match("^\d{9}$", val)) == None
    elif key == "cid":
        return False
    else:
        return False

for passport in passports:
    pport = {}
    for field in passport:
        key, val = field.split(":")
        if validate(key, val):
            pport[key] = val

    fields = set(pport.keys())
    if fields == set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        pports.append(pport)
        valid += 1
