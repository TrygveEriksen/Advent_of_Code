def part_2(): 
	with open("2015/day_3/input.txt", "r") as f: 
		directions = f.read().strip()
	cur1 = (0, 0)
	cur2 = (0, 0)
	visit = {(0, 0)}
	c1 = True 
	for d in directions: 
		if c1: 
			match d: 
				case "^": 
					cur1 = (cur1[0]+1, cur1[1])
				case ">": 
					cur1 = (cur1[0], cur1[1]+1)
				case "v": 
					cur1 = (cur1[0]-1, cur1[1])
				case "<": 
					cur1 = (cur1[0], cur1[1]-1)
		else: 
			match d: 
				case "^": 
					cur2 = (cur2[0]+1, cur2[1])
				case ">": 
					cur2 = (cur2[0], cur2[1]+1)
				case "v": 
					cur2 = (cur2[0]-1, cur2[1])
				case "<": 
					cur2 = (cur2[0], cur2[1]-1)
		visit.add(cur1)
		visit.add(cur2)
		c1 = not c1
	return len(visit)
print(part_2())