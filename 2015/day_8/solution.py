import re

def part_1(): 
	with open("2015/day_8/input.txt", "r") as f: 
		lines = [line.strip() for line in f.readlines()]
	l1 = sum(len(l) for l in lines)
	l2 = 0
	for line in lines: 
		line = re.sub(r"\\", "XX", line)
		line = re.sub(r"\"", "XX", line)
		print(line.encode())
		l2 += len(line) +2
	print(l1)
	print(l2)
	print(-l1 +l2)
part_1()