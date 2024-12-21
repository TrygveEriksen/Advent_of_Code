import networkx as nx 

directions = {(1,0), (-1,0), (0,1), (0,-1)}

def manhattan(p1, p2): 
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def get_graph(mat): 
    G = nx.DiGraph()
    nodes = set()
    for i in range(len(mat)): 
        for j in range(len(mat[0])): 
            if mat[i][j] != "#": 
                nodes.add((i,j))
    for node in nodes: 
        for d in directions: 
            if (node[0]+d[0], node[1]+d[1]) in nodes: 
                G.add_edge(node, (node[0]+d[0], node[1]+d[1]))
    return G
    

def get_len(mat, start, end):
    return len(nx.shortest_path(G, start, end))

def start_to_all(G, start): 
    paths = nx.single_source_shortest_path(G, start)
    lengths = {key:len(paths[key])-1 for key in paths.keys()}
    return lengths

def all_to_finish(G, finish): 
    paths = nx.single_target_shortest_path(G, finish)
    lengths = {key:len(paths[key])-1 for key in paths.keys()}

    return lengths

def part_1():
    data = open("2024/day_20/input.txt", "r").readlines()
    matrix_graph = [[a for a in line.strip()] for line in data]
    s, e = (0,0), (0,0)
    for i in range(len(matrix_graph)): 
        for j in range(len(matrix_graph[0])): 
            if matrix_graph[i][j] == "S": 
                s = (i,j)
            if matrix_graph[i][j] == "E": 
                e = (i,j)

    G = get_graph(matrix_graph)
    benchmark = get_len(G, s, e)
    su=0
    node_costs = start_to_all(G, s)
    goal_costs = all_to_finish(G, e)
    for n1 in node_costs.keys(): 
        for n2 in goal_costs.keys(): 
            if manhattan(n1, n2) <= 2 and benchmark -(node_costs[n1] + goal_costs[n2] + manhattan(n1, n2)) >= 100: 
                su += 1 
    print(su)

def part_2():
    data = open("2024/day_20/input.txt", "r").readlines()
    matrix_graph = [[a for a in line.strip()] for line in data]
    s, e = (0,0), (0,0)
    for i in range(len(matrix_graph)): 
        for j in range(len(matrix_graph[0])): 
            if matrix_graph[i][j] == "S": 
                s = (i,j)
            if matrix_graph[i][j] == "E": 
                e = (i,j)
    su = 0 
    G = get_graph(matrix_graph)
    benchmark = get_len(G, s, e)
    node_costs = start_to_all(G, s)
    goal_costs = all_to_finish(G, e)

    for n1 in node_costs.keys(): 
        for n2 in goal_costs.keys(): 
            if manhattan(n1, n2) <= 20 and benchmark - (node_costs[n1] + goal_costs[n2] + manhattan(n1, n2)) >= 100: 
                su += 1 
    print(su)

part_1()