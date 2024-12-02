def part_2(): 
		with open("2015/day_2/input.txt", "r") as f: 
			p = [[int(i) for i in a.strip().split("x")] for a in f.readlines()]
		
		s = 0

		for a in p: 
			l = [a[0]+a[1], a[1]+a[2], a[2]+a[0]]
			v = a[0] * a[1] * a[2]

			s+= 2*min(l) + v
		return s
print(part_2())