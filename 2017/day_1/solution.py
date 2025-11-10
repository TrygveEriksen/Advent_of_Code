def part_1(): 
	data = open("2017/day_1/input.txt", "r").read().strip()
	l = len(data)
	s = 0
	for i in range(l): 
		if data[i] == data[(i+l//2)%l]: 
			s+= int(data[i])
	print(s)
part_1()