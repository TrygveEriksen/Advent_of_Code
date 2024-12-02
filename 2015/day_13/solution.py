from itertools import permutations

def part_1(): 
	with open("2015/day_13/input.txt", "r") as f: 
		lines = [line.strip().replace("would lose ", "-").replace(".", "").replace("would gain ", "").replace("happiness units by sitting next to ", "").split() for line in f.readlines()]
	names = set(line[0] for line in lines)
	names.add("me")
	perm = permutations(names, 9)
	w = {(l[0], l[2]): int(l[1]) for l in lines}|{("me", name): 0 for name in names}|{(name, "me"): 0 for name in names}
	m=0
	for p in perm: 
		s=0
		for i in range(len(p)): 
			r = p[i]
			l = p[(i+1)%len(p)]
			s+=w[(r, l)] +w[(l, r)]
		m=max(m, s)
	print(m)


	
part_1()
