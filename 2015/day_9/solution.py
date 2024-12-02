from itertools import permutations


def part_1(): 
	with open("2015/day_9/input.txt", "r") as f: 
		edges = [line.replace(" to ", ",").replace(" = ", ",").strip().split(",") for line in f.readlines()]

	e_dict = {(e[0], e[1]): int(e[2]) for e in edges}|{(e[1], e[0]): int(e[2]) for e in edges}
	places = set(a[0] for a in edges)
	places.add("Arbre")
	perm = permutations(places, 8)
	
	m = 0
	for p in perm: 
		s=0
		for i in range(len(p)-1): 
			if (p[i], p[i+1]) in e_dict: 
				s+= e_dict[(p[i], p[i+1])]
			else: 
				s+= e_dict[(p[i+1], p[i])]

		m= max(m, s)
	print(m)
part_1()

