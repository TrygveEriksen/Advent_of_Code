import heapq
from math import inf 
import networkx

def part_1(): 
    with open("2024/day_16/input.txt") as f: 
        grid = [line.strip() for line in f.readlines()]

    visit = set()
    path = []
    start = (0,0)
    stop = (0,0)
    for idx in range(len(grid)): 
        for jdx in range(len(grid[0])): 
            if grid[idx][jdx] == "E": 
                stop = (idx, jdx)
            if grid[idx][jdx] == "S":
                start = (idx, jdx)

    heap = [(0, 1, start, (0,1))]
    min_cost = inf 
    while len(heap): 
        cost, amount, cur, d = heapq.heappop(heap)
        grid2 = ["".join("C" if (i,j) ==cur else grid[i][j] for j in range(len(grid[i]))) for i in range(len(grid))]
        if cost > min_cost: 
            continue
        if cur == stop: 
            min_cost = cost
            path.append(cur)

        if grid[cur[0]+d[0]][cur[1]+d[1]]!="#" and (cur[0]+d[0], cur[1]+d[1]) not in visit: 
            heapq.heappush(heap, (cost+1, (cur[0]+d[0], cur[1]+d[1]), d))
            visit.add((cur[0]+d[0], cur[1]+d[1]))

        if grid[cur[0]-d[1]][cur[1]+d[0]]!="#" and (cur[0]-d[1],cur[1]+d[0]) not in visit: 
            heapq.heappush(heap, (cost+1000, cur, (-d[1], d[0])))

        if grid[cur[0]+d[1]][cur[1]-d[0]]!="#" and (cur[0]+d[1],cur[1]-d[0]) not in visit: 
            heapq.heappush(heap,  (cost+1000,  cur, (d[1], -d[0])))

    print(path[0][1])


def part_2(): 
    d_dict = {0: (0, 1), 1:(-1, 0), 2:(0,-1), 3:(1, 0)}
    with open("2024/day_16/input.txt") as f: 
        grid = [line.strip() for line in f.readlines()]

    G = networkx.DiGraph()
    start = (0,0)
    stop = (0,0)
    nodes = set()
    edges = set()
    for idx in range(len(grid)): 
        for jdx in range(len(grid[0])): 
            if grid[idx][jdx] == "E": 
                stop = (idx, jdx)
                nodes.add((stop, 0))
            elif grid[idx][jdx] == "S":
                start = (idx, jdx)
                for i in range(4): 
                    nodes.add(((idx, jdx), i))
            elif grid[idx][jdx] == ".":
                for i in range(4): 
                    nodes.add(((idx, jdx), i))

    for node, d in nodes: 
        if (node[0]+d_dict[d][0], node[1]+d_dict[d][1])==stop: 
            edges.add(((node, d), (stop, 0)))
        if ((node[0]+d_dict[d][0], node[1]+d_dict[d][1]), d) in nodes: 
            edges.add(((node, d), ((node[0]+d_dict[d][0], node[1]+d_dict[d][1]), d)))
        for i in range(4): 
            if i != d and node!= stop and ((i+1)%4 == d or (d+1)%4 == i): 
                edges.add(((node, d), (node,i)))
    
    while len(edges): 
        a, b = edges.pop()
        if a[0] == b[0]: 
            G.add_edge(a,b, foo=1000)
        elif a[1] == b[1]:  
            G.add_edge(a,b,foo=1)
        else: 
            assert a[0]==stop or b[0] == stop
            G.add_edge(a,b,foo=1)
    
    path = networkx.all_shortest_paths(G, (start, 0), (stop, 0), weight="foo")
    a1 = []
    paths = [p for p in path]
    for p in paths: 
        a1.extend([a[0] for a in p])


    grid2 = ["".join("O" if (i,j) in a1 else grid[i][j] for j in range(len(grid[i]))) for i in range(len(grid))]
    for g in grid2: 
        print(g)

    print(len(set(a1)))


part_2()