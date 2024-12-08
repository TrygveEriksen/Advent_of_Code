import networkx

def check_rules(update, rules): 
	for rule in rules: 
		if rule[0] in update and rule[1] in update and update.index(rule[1]) <= update.index(rule[0]): 
			return False
	return True
		
def fix(update, rules): 
	g = networkx.DiGraph()
	g.add_nodes_from(update)
	for ru in rules: 
		if ru in update: 
			g.add_edge(*ru)
	new = [ a for a in networkx.topological_sort(g)]
	return new


def part_1(): 
	with open("2024/day_5/input.txt", "r") as f: 
		lines = [line.strip() for line in f.readlines()]
	idx = lines.index("")
	rules = [tuple(map(int, line.strip().split("|"))) for line in lines[:idx]]
	updates = [list(map(int, line.strip().split(","))) for line in lines[idx+1:]]
	inc = []
	s=0
	new = []
	for up in updates: 
		if not check_rules(up, rules): 
			inc.append(up)
	for i in inc: 
		i2 = fix(i, rules)
		s+= i2[len(i2)//2]
	print(s)



#part_1()
def check(): 
	sha = "7a04b54830004e945c1eda6ed6ec8c57ff4b249de4b331bd021a849694f29b8f *linuxmint-22-cinnamon-64bit.iso"
	t = "7a04b54830004e945c1eda6ed6ec8c57ff4b249de4b331bd021a849694f29b8f *linuxmint-22-cinnamon-64bit.iso"
	if t == sha: 
		print("all good")
	else: 
		print(sha)
		print(t)
check()