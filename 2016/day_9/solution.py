import re
from functools import cache

def process(line, depth):
    pattern = r'\((\d+[x]\d+)\)'
    matches = [(True, match) for match in re.finditer(pattern, line)]
    if len(matches) == 0 or depth == 0: 
        return line
    newline = ""
    last_idx = 0
    for idx in range(len(matches)): 
        use, match = matches[idx]
        if not use:
            continue
        length, repeat = [int(i) for i in re.findall(r'\d+', match.group())] 
        start, stop = match.span()
        for jdx, match2 in enumerate(matches[idx+1:]): 
            sa, so = match2[1].span()
            if sa > stop + length: 
                break
            elif sa < stop + length:
                matches[idx+1+jdx] = (False, match2[1])
        newline += line[last_idx: start] + line[stop: stop + length] * repeat
        last_idx = stop + length
    newline += line[last_idx:]
    return process(newline, depth - 1)

@cache
def process2(line):
    pattern = r'\((\d+[x]\d+)\)'
    matches = [(True, match) for match in re.finditer(pattern, line)]
    if len(matches) == 0: 
        return len(line) 
    newline = 0 
    last_idx = 0
    for idx in range(len(matches)): 
        use, match = matches[idx]
        if not use:
            continue
        length, repeat = [int(i) for i in re.findall(r'\d+', match.group())] 
        start, stop = match.span()
        for jdx, match2 in enumerate(matches[idx+1:]): 
            sa, so = match2[1].span()
            if sa > stop + length: 
                break
            elif sa < stop + length:
                matches[idx+1+jdx] = (False, match2[1])
        newline += start - last_idx + process2(line[stop: stop + length]) * repeat
        last_idx = stop + length
    newline += len(line) - last_idx
    return newline

def part_1():
    s = 0 
    with open("2016/day_9/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        l =  process(line, 1)
        print(f"{line} -> {l} , len = {len(l)}")
        s+= len(l)
    return s

def part_2():
    s = 0 
    with open("2016/day_9/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        l =  process2(line) 
        print(f"{line} -> {l}")
    return l

print(part_1())
print(part_2())
