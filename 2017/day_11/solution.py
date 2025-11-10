def calc_dist(px, py): 
	nx, ny = abs(px), abs(py)
	dist = 0
	while nx > 0: 
		nx -= 1
		ny -= 0.5
		dist += 1
	while ny > 0:
		ny -= 1
		dist += 1
	return dist 
	




def part_1(): 
	data = open("2017/day_11/input.txt", "r").read().strip().split(",")
	px, py = 0,0
	m=0
	for d in data: 
		match d: 
			case "n": 
				py += 1
			case "ne": 
				px+=1
				py+=0.5
			case "nw": 
				px-=1 
				py +=0.5
			case "s": 
				py -= 1 
			case "se": 
				px += 1
				py -= 0.5
			case "sw": 
				px -=1
				py -=0.5
		m = max(m, calc_dist(px, py))
	print(m)
part_1()