def update(l):
	c = [[0 for i in range(100)] for j in range(100)]
	for i in range(100): 
		for j in range(100): 
			c[i][j] += l[i-1][j]=="#" if i > 0 else 0
			c[i][j] += l[i+1][j]=="#" if i < 99 else 0
			c[i][j] += l[i-1][j-1]=="#" if i > 0 and j > 0 else 0
			c[i][j] += l[i-1][j+1]=="#" if i > 0 and j < 99 else 0
			c[i][j] += l[i+1][j+1]=="#" if i < 99 and j < 99 else 0
			c[i][j] += l[i+1][j-1]=="#" if i < 99 and j > 0 else 0
			c[i][j] += l[i][j+1]=="#" if j < 99 else 0
			c[i][j] += l[i][j-1]=="#" if j > 0 else 0

	c = [["#" if l[j][i] == "#" and (c[j][i]==3 or c[j][i]==2) or l[j][i] == "." and c[j][i]==3 else "." for i in range(100)] for j in range(100)]
	c[0][0] = "#"
	c[0][99] = "#"
	c[99][0] = "#"
	c[99][99] = "#"
	return c




def part_1(): 
	with open("2015/day_18/input.txt", "r") as f: 
		l1 = f.read().split()
	for i in range(100): 
		l1 = update(l1)
	print(sum(l.count("#") for l in l1))
part_1()