def part_1(): 
	grid = [[0 for _ in range(1000)] for __ in range(1000)]
	with open("2015/day_6/input.txt", "r") as f: 
		lines = [line.replace(" through ", " ").replace("n o", "no").strip().split() for line in f.readlines()]
	for line in lines: 
		x1, y1 = [int(i) for i in line[1].split(",")]
		x2, y2 = [int(i) for i in line[2].split(",")]
		x1, x2 = min(x1, x2), max(x1, x2)
		y1, y2 = min(y1, y2), max(y1, y2)
		code = line[0]
		for i in range(x1, x2+1): 
			for j in range(y1, y2+1): 
				if code == "turnon":grid[i][j] += 1
				elif code == "turnoff":grid[i][j] = max(0, grid[i][j]-1)
				else: grid[i][j] += 2
	return sum(sum(row) for row in grid)
print(part_1())