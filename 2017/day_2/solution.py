def part_1(): 
	data = [line.strip() for line in open("2017/day_2/input.txt", "r").read().replace("\t", " ").split("\n")]
	s = 0
	for line in data: 
		l=[]
		for p in line.split(): 
			if p.isdecimal(): 
				l.append(int(p))
		for i in range(len(l)): 
			for j in range(len(l)): 
				if l[i]/l[j] == l[i]//l[j] and i!=j:
					s+= l[i]//l[j]
	print(s)
part_1()