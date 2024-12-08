def part_1(): 
	with open("2024/day_2/input.txt", "r") as f: 
		ints = list(list(map(int, line.strip().split()))for line in f.readlines())
	c=0
	for i in ints: 
		a1 = [i[j] == i[j+1]+1 or i[j] == i[j+1]+2 or i[j] == i[j+1]+3 for j in range(len(i)-1)]
		a2 = [i[j]+1 == i[j+1] or i[j]+2 == i[j+1] or i[j]+3 == i[j+1] for j in range(len(i)-1)]
		if all(a1) or all(a2): 
			c+=1
		else: 
			for j in range(len(i)): 
				a= i.pop(j)
				a1 = [i[j] == i[j+1]+1 or i[j] == i[j+1]+2 or i[j] == i[j+1]+3 for j in range(len(i)-1)]
				a2 = [i[j]+1 == i[j+1] or i[j]+2 == i[j+1] or i[j]+3 == i[j+1] for j in range(len(i)-1)]
				if all(a1) or all(a2): 
					c+=1
					break
				i.insert(j, a)

	print(c)
part_1()