import networkx as nx
def part_1(): 
    data = open("2024/day_18/input.txt", "r").readlines()
    
    for k in range(2990, len(data)): 
        try: 
            b = set()
            for d in data[:k]: 
                a,c =d.strip().split(",")
                b.add((int(a), int(c)))    

            nodes = set()
            for i in range(71): 
                for j in range(71): 
                    if (i,j) not in b: 
                        nodes.add((i,j))
            G = nx.DiGraph()
            for n in nodes:
                for n2 in [(n[0]+1, n[1]), (n[0]-1, n[1]), (n[0], n[1]+1), (n[0], n[1]-1)]: 
                    if n2 in nodes: 
                        G.add_edge(n, n2)
            path = nx.shortest_path(G, (0,0), (70,70)) 
        except: 
            print(data[k-1])
            break
        print(len(path))
part_1()