def part_1(): 
	data = open("2016/day_2/input.txt", "r").read().split("\n")
	keypad = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
	x, y = 1,1
	out = ""
	for line in data: 
		for l in line: 
			match l: 
				case "U": 
					y -=1
				case "D": 
					y+=1
				case "R": 
					x+=1
				case "L": 
					x-=1
			x, y = max(x, 0), max(y, 0)
			x, y = min(x, 2), min(y, 2)
		out += str(keypad[y][x])
	print(out)

def part_2(): 
	data = open("2016/day_2/input.txt", "r").read().split("\n")
	keypad = [[None for _ in range(7)], 
		   [None for _ in range(3)] + [1] + [None for _ in range(3)], 
		   [None, None, 2, 3, 4, None, None], 
		   [None, 5, 6, 7, 8, 9, None], 
		   [None, None, "A", "B", "C", None, None], 
		   [None for _ in range(3)] + ["D"] + [None for _ in range(3)],
		   [None for _ in range(7)]]
	x, y = 1, 3
	out = ""
	for line in data: 
		for l in line: 
			match l: 
				case "U": 
					nx, ny = x, y-1
				case "D": 
					nx, ny = x, y+1
				case "R": 
					nx, ny = x+1, y
				case "L": 
					nx, ny = x-1, y
			if keypad[ny][nx] is not None: 
				x,y = nx, ny
		out += str(keypad[y][x])
	print(out)
part_2()