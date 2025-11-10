def rot(d): 
	return (-d[1], d[0])


def part_1():
	dic = {(0,0):1} 
	num = 277678
	pos = (0,0)
	d = (1,0)
	idx = 1
	while  True: 
		idx += 1
		pos = (pos[0]+d[0], pos[1]+d[1])
		s=0
		for i in range(-1, 2): 
			for j in range(-1, 2): 
				if (pos[0]+i, pos[1]+j) in dic: 
					s+= dic.get((pos[0]+i, pos[1]+j))
		if s > num: 
			print(f"First over {num} is {s}")
			break
		dic[pos] = s
		if pos[0] == pos[1] or (pos[0] == -pos[1] and pos[0] < 0) or (pos[0] == -pos[1] + 1 and pos[0] > 0):
			d = rot(d)

part_1()

