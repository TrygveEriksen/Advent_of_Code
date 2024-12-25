
def part_1(): 
	keys = []
	locks = []
	c = 0
	with open("2024/day_25/input.txt", "r") as f: 
		blocks = f.read().split("\n\n")
	for block in blocks: 
		block = block.split()
		if block[0].strip() == "#"*5: 
			locks.append([sum(block[i][j] == "#" for i in range(len(block))) for j in range(len(block[0]))])
		else: 
			keys.append([sum(block[i][j] == "#" for i in range(len(block))) for j in range(len(block[0]))])
	for key in keys: 
		for lock in locks: 
			c += not any(key[i] + lock[i] > 7 for i in range(5))
	print(c)
part_1()