def part_1(): 
	data = [ord(i) for i in open("2017/day_10/input.txt", "r").read().strip()] + [17, 31, 73, 47, 23]
	l = [*range(256)]
	pos = 0
	skip = 0
	for _ in range(64): 
		for d in data: 
			first, last = pos, (pos + d-1)%256
			for _ in range(d//2): 
				l[first], l[last] = l[last], l[first]
				first = (first + 1)%256
				last = (last-1)%256
			pos = (pos+d+skip)%256
			skip += 1
	new = []
	for i in range(0, 256, 16): 
		ap = 0
		for j in range(16): 
			ap ^= l[i+j]
		new.append(str(hex(ap))[2:])
	print("".join(new))
part_1()
		
