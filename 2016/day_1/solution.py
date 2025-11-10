def right_turn(d): 
	return (d[1], -d[0])

def part_2(): 
	data = open("2016/day_1/input.txt", "r").read().split(", ")
	pos = (0,0)
	direction = (1,0)
	visit = {pos}
	for d in data: 
		match d[0]: 
			case "R": 
				direction = right_turn(direction)
			case "L": 
				for i in range(3): 
					direction = right_turn(direction)
		for _ in range(int(d[1:])): 
			pos = (pos[0] + direction[0], pos[1] + direction[1])
			if pos in visit: 
				print(abs(pos[0]) + abs(pos[1]))
				exit(0)
			visit.add(pos)
	
part_2()