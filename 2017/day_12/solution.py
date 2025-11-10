import networkx as nx

def part_1(): 
	data = [line.split(" <-> " ) for line in open("2017/day_12/input.txt", "r").read().split("\n")]
	G = nx.Graph()
	for line in data: 
		for target in line[1].split(", "): 
			G.add_edge(line[0], target)
	
	suc = nx.shortest_path(G, "0")
	print(len(suc))
	groups = nx.connected.number_connected_components(G)
	print(groups)