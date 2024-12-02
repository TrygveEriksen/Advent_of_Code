import json, re
def part_1(): 
	with open("2015/day_16/input.txt", "r") as f: 
		lines = f.readlines()
	d ={
		"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,"akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2,"perfumes": 1}
	lines = [re.sub(r"(\d+):", r'"\1":{', line)+"}" for line in lines]
	lines = ",".join(lines)
	aunts = json.loads(lines)
	for k in d.keys(): 
		l = []
		for a in aunts.keys(): 
			if k in aunts[a]: 
				if k in ["cats", "trees"]: 
					if aunts[a][k] <= d[k]: 
						l.append(a)
				elif k in ["pomeranians", "goldfish"]: 
					if aunts[a][k] >= d[k]: 
						l.append(a)
				else: 
					if aunts[a][k] != d[k]: 
						l.append(a)
		for a in l: 
			aunts.pop(a) 
	print(aunts)



part_1()
