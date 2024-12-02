def part_1(): 
	with open("2015/day_14/input.txt", "r") as f: 
		lines = [line.strip().replace("can fly ", "").replace(" km/s for", "").replace("seconds, but then must rest for ", "").replace("seconds.", "").split() for line in f.readlines()]
	d = {line[0]: 0 for line in lines}
	for t5 in range(1, 2504): 
		d2 = {}
		m=0
		for l in lines: 
			t=t5
			s=0
			speed = int(l[1])
			t1 = int(l[2])
			t2 = int(l[3])
			t3 = t1+t2

			s+= speed*t1*(t//t3)
			t%=t3
			if t >= t1: 
				s+= speed*t1
			else: 
				s+= t * speed
			m= max(m, s)
			d2[l[0]] = s

		for key in d2.keys(): 
			if d2[key] == m: 
				d[key]= d[key]+1
	print(d[max(d)])
	print()
part_1()
