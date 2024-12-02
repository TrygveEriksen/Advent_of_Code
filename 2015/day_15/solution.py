import json
def partition(): 
	for i1 in range(101): 
		for i2 in range(101-i1): 
			for i3 in range(101-i1-i2): 
				yield (i1, i2, i3, 100-i1-i2-i3)
				
def part_1(): 
	m=0
	with open("2015/day_15/input.txt", "r") as f: 
		d1 = json.loads(f.read())
	d2 = {0: "Frosting", 1: "Candy", 2:"Butterscotch", 3: "Sugar"}
	def score(p): 
		prod = 1
		for ing in ["capacity", "durability", "flavor", "texture"]: 
			s=0
			for i in range(len(p)): 
				s+= p[i]*d1[d2[i]][ing]
			prod*=max(s, 0)
		cal=0
		for i in range(len(p)): 
				cal+= p[i]*d1[d2[i]]["calories"]
		return prod if cal == 500 else -1


	m = max(score(p) for p in partition())
	print(m)
print(part_1())