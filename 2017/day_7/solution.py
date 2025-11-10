from functools import cache
def make_dicts(): 
	data = open("2017/day_7/input.txt", "r").read().split("\n")
	parents, children, weights = dict(), dict(), dict()
	for line in data: 
		if " -> " in line: 
			par, childs = line.split(" -> ")
			parent = par.strip().split()[0]
			children[parent] = [c for c in childs.strip().split(", ")]
			weights[parent] = int(par.strip().split()[1][1:-1])
			for c in childs.strip().split(", "): 
				parents[c] = parent
		else: 
			weights[line.strip().split()[0]] = int(line.strip().split()[1][1:-1])
	return parents, children, weights

def DFS(parents, child):
	if child not in parents: 
		return child
	else: 
		return DFS(parents, parents[child])

def part_1(): 
	parents, *_ = make_dicts()
	print(DFS(parents, "wnwzo"))

def DFS_weights(children, weights, node): 
	s = weights[node]
	for c in children.get(node, []):
		s += DFS_weights(children, weights, c)
	return s

def balance_tree(children, weights, node, off): 
	w = []
	for c in children.get(node, []): 
		wei = DFS_weights(children, weights, c)
		w.append(wei)
	
	if len(w) > 0 and (len(set(w))) != 1: 
		#print(f"Balancing {node}, children: {children.get(node, [])}")
		if len(w) > 2: 
			d = {a: w.count(a) for a in set(w)}
			k, m = 0, 0
			for key, it in d.items(): 
				if it > m: 
					m = it
					k = key
			for i in range(len(w)): 
				if w[i] != k: 
					balance_tree(children, weights, children.get(node, [])[i], k - w[i])
		else: 
			pass


	elif off != 0: 
		print(f"Change node {node}, new weight: {weights[node] + off}")

		



def part_2(): 
	*_, children, weights = make_dicts()
	root = "ahnofa"

	balance_tree(children, weights, root, 0)

part_2()