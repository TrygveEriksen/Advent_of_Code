from itertools import combinations
def part_1(): 
	with open("2015/day_17/input.txt", "r") as f: 
		containers = list(map(int, f.read().split()))
	c=0
	containers = list(sorted(containers))
	for i in range(4, 12): 
		comb = combinations(containers, i)
		for p in comb: 
			c+= sum(p)==150
		if c: 
			break
	print(c)
part_1()