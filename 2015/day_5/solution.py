def part_1():
	with open("2015/day_5/input.txt", "r") as f: 
		inp = [line.strip() for line in f.readlines()]
	s = 0
	v="aeiou"
	for line in inp: 
		l1 = [line[i]==line[i+2] for i in range(len(line)-2)]

		l2 = any([line.count(line[i:i+2])>1 for i in range(len(line)-2)])

		s+=any(l1) and l2 

	return s

print(part_1())