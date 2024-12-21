from functools import cache


    
    
def part_1(): 
    with open("2024/day_19/input.txt", "r") as f: 
        data = f.read().split("\n\n")
    sub = data[0].strip().split(", ")

    @cache
    def check(string:str): 
        if not string: 
            return 1
    
        foo = 0
        for s in sub:
            if string.startswith(s):
                foo += check( string[len(s):])
        return foo
    
    s = 0
    strings = data[1].splitlines()
    for string in strings: 
        s+= check(string)
    print(s) 
    
    
part_1()