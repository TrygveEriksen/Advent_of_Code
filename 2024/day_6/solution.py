from copy import deepcopy



def part_1(): 
	with open("2024/day_6/input.txt", "r") as f: 
		m = [[[a] for a in line.strip()] for line in f.readlines()]
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	dir2 = ["U", "R", "D", "L"]
	i = 0
	px, py = 0,0
	
	for x in range(len(m)): 
		for y in range(len(m[0])): 
			if m[x][y]==["^"]: 
				px, py = x,y
				x2, y2 = x,y
	
	print(px, py)
	try: 
		m2 = deepcopy(m)
		m2[px][py] = ["X"]
		while 1: 
			px+= directions[i][0]
			py+= directions[i][1]
			assert px >= 0 
			assert py >= 0
			if m2[px][py] ==["#"]: 
				px -= directions[i][0]
				py -= directions[i][1]
				i += 1
				i %= 4
			else: 
				m2[px][py]=["X"]
	except: 
		xs = []
		for i in range(len(m)): 
			for j in range(len(m[0])): 
				if "X" in m2[i][j]: 
					xs.append((i, j))
	print(xs)
	s = 0
	for k, j in xs: 
		m2 = deepcopy(m)
		try: 
			if (k,j)==(x2, y2):
				continue
			i = 0
			m2[k][j] = ["#"]
			px, py = x2, y2
			##Game loop
			m2[px][py].append("U")
			while 1: 
				px += directions[i][0]
				py += directions[i][1]

				assert px >= 0 
				assert py >= 0

				if "#" in m2[px][py]: 
					if dir2[i] in m2[px][py]: 
						s+= 1
						break
					else: 
						m2[px][py].append(dir2[i])
						px-= directions[i][0]
						py-= directions[i][1]
						i += 1
						i %= 4
				else: 
					m2[px][py].append(dir2[i])
			print(s)

		except: 
			pass


print("9bcb6c30a80bfef9919f0a8b84e68e32f34412ea1df795d5c2b3a83b62cba2c9" == "9bcb6c30a80bfef9919f0a8b84e68e32f34412ea1df795d5c2b3a83b62cba2c9")


part_1()
