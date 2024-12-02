def part_1(): 
	with open("2024/day_1/input.txt", "r") as f: 
		lines = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	l1 = [line[0] for line in lines]
	l2 = [line[1] for line in lines]
	l1.sort()
	l2.sort()
	s=0
	for i in range(len(l1)): 
		s+= l1[i]*l2.count(l1[i])
	print(s)
part_1()
