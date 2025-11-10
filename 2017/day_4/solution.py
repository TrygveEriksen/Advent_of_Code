def part_1(): 
	data = open("2017/day_4/input.txt", "r").read().split("\n")
	s = 0
	for l in data: 
		l2 = l.split()
		s += len(l2) == len(set(["".join(sorted(a)) for a in l2]))
	print(s)
part_1()