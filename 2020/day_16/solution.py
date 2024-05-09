import time
import networkx as nx

def get_input_1():
    with open("2020/day_16/input.txt", "r") as f: 
        lines = [line.strip().split(",") for line in f.readlines()]
    return [[int(i) for i in line] for line in lines]


def get_input_2(): 
    with open("2020/day_16/input2.txt", "r") as f: 
        lines = f.readlines()
    rules = [line.strip().split(":")[0] for line in lines]
    lines = [line.strip().split(":")[1] for line in lines]
    lines = [line.strip().replace("-", " or ").split(" or ") for line in lines]
    return lines, rules

def get_input_3():
    with open("2020/day_16/input3.txt", "r") as f: 
        lines = [line.strip().split(",") for line in f.readlines()]
    return [int(i) for i in lines[0]]




def check_rule(num, rule): 
    return num >= int(rule[0]) and num <= int(rule[1]) or num >= int(rule[2]) and num <= int(rule[3])



def part_1(): 
    tickets = get_input_1()
    rules = get_input_2()[0]
    s = 0
    for t in tickets: 
        for num in t: 
            foo = True
            for rule in rules: 
                if check_rule(num, rule): 
                    foo = False
            if foo : 
                s+= num

    return s

def part_2(): 
    tickets = get_input_1()
    rules, rulenames = get_input_2()
    my_ticket = get_input_3()
    r=[]
    d = {name:[] for name in rulenames}
    for t in tickets: 
        for num in t: 
            foo = True
            for rule in rules: 
                if check_rule(num, rule): 
                    foo = False
            if foo : 
                r.append(t)
    for re in r: 
        tickets.remove(re)

    for i in range(len(rules)):
        for j in range(len(tickets[0])): 
            foo = True
            for t in tickets:
                foo = foo and check_rule(t[j], rules[i])
            if foo: 
                d[rulenames[i]].append(j)
    
    G= nx.Graph(d)
    res = nx.max_weight_matching(G, maxcardinality=True)
    n=[]
    for r in res: 
        if isinstance(r[0], int): 
            n.append((r[1], r[0]))
        else: 
            n.append(r)

    p=1
    for r in n: 
        if r[0][:9] =="departure": 
            p*= my_ticket[r[1]]
    return p
    






    
def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()

