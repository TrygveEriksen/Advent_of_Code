import networkx as nx

def part_1(): 
    G = nx.Graph()
    for line in open("2024/day_23/input.txt", "r").readlines(): 
        line = line.strip().split("-")
        G.add_edge(line[0], line[1])
    cycles = nx.cycles.simple_cycles(G, length_bound=3)
    cycles = [c for c in cycles if len(c)==3]
    cycles = [c for c in cycles if any([c1[0]=="t" for c1 in c])]
    print(len(cycles))

def part_2(): 
    G = nx.Graph()
    for line in open("2024/day_23/input.txt", "r").readlines(): 
        line = line.strip().split("-")
        G.add_node(line[0], weight=1)
        G.add_node(line[1], weight=1)
        G.add_edge(line[0], line[1])
    clique = nx.clique.max_weight_clique(G, weight="weight")
    clique = [*sorted(clique[0])]
    print(",".join(clique))
part_2()