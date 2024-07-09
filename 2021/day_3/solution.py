def get_input():
	with open("2019/day_3/input.txt", "r") as f:
		return [line.strip() for line in f.readlines()]

def part_1():
	lines = get_input()
	g = ""
	e= ""
	comp = len(lines)/2
	for i in range(len(lines[0])):
		c = 0
		for line in lines:
			c+= line[i] == "1"
		g += ("1" if c > comp else "0")
		e += ("0" if c > comp else "1")

	g = int(g,2)
	e = int(e,2)
	return g*e

def part_2():
	ox = get_input()
	co = get_input()
	l = len(ox[0])
	for i in range(l):
		c1 = 0
		c2 = 0
		for o in ox:
			c1 += o[i] == "1"
		for c in co:
			c2 += c[i] == "0"

		mc = "1" if c1 >= len(ox)/2 else "0"
		lc = "0" if c2 <= len(co)/2 else "1"
		if len(ox) != 1:
			ox = list( filter(lambda x: x[i]==mc, ox))
		if len(co) != 1:
			co = list( filter(lambda x: x[i]==lc, co))
	return int(ox[0],2) * int(co[0],2)

print(part_2())