def part_1(): 
	jumps = [int(i) for i in open("2017/day_5/input.txt", "r").read().split()]
	l = len(jumps)
	idx = 0
	c = 0
	while -1 < idx < l: 
		c += 1
		if jumps[idx] > 2: 
			jumps[idx] -= 1 
			idx += jumps[idx] + 1
		else: 
			jumps[idx] += 1 
			idx += jumps[idx] - 1
	print(c)
part_1()