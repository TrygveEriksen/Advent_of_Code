import time
import re

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def get_passports(): 
    ret = []
    l= ""
    with open("2020/day_4/input.txt","r") as f: 
        lines =  f.readlines()
    
    for line in lines: 
        line = line.strip()
        if line == "": 
            ret.append(l)
            l=""
        else: 
            l+= " " + line
    ret.append(l)
    return [[a.split(":") for a in p.strip().split(" ")] for p in ret]


def part_1() -> int: 
    passports = get_passports()
    c=0
    for p in passports: 
        c += len(fields) == len(p.intersection(fields))
    return c


def part_2() -> int: 
    passports = get_passports()
    c=0
    for p in passports: 
        f = {a[0] for a in p}
        status = 1
        if len(f.intersection(fields))==len(fields):
            for a in p: 
                match a[0]:
                    case "byr": 
                        status *= (int(a[1]) >= 1920) and (int(a[1])<= 2002) and len(a[1]) == 4
                    case "iyr": 
                        status *= (int(a[1]) >= 2010) and (int(a[1])<= 2020) and len(a[1]) == 4
                    case "eyr": 
                        status *= (int(a[1]) >= 2020) and (int(a[1])<= 2030) and len(a[1]) == 4
                    case "hgt": 
                        status *= (int(a[1][:-2])>=150 and int(a[1][:-2])<=193) if a[1][-2:] == "cm" else (int(a[1][:-2])>=59 and int(a[1][:-2])<=76) if a[1][-2:]=="in" else 0
                    case "hcl": 
                        status *= bool(re.fullmatch("#{1}[a-f0-9]{6}", a[1]))
                    case "ecl": 
                        status *= (a[1] in {"amb", "blu", "brn", "gry", "grn" ,"hzl", "oth"})
                    case "pid": 
                        status *= bool(re.fullmatch("[0-9]{9}", a[1]))
                    case "cid": 
                        status *= 1
            c+=status
    return c
                    
                    



def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")

main()