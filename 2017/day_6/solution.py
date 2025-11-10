def part_1(): 
	data = [int(i) for i in open("2017/day_6/input.txt", "r").read().strip().split()]
	seen = dict()
	l = len(data)
	m, i = 0, 0
	c=0 
	while " ".join(str(a) for a in data) not in seen: 
		seen[" ".join(str(a) for a in data)] = c
		c+=1
		for idx in range(l): 
			if data[idx] > m: 
				m = data[idx]
				i = idx
		data[i] = 0
		while m > 0: 
			i = (i+1)%l
			m-=1 
			data[i] += 1 
	print(c - seen[" ".join(str(a) for a in data)])
part_1()
 