def find_index(list1, target_len, target_id): 
    idx = 0
    target_idx = list1.index(target_id)
    while idx < target_idx-target_len+1: 
        if all(a =="." for a in list1[idx:idx+target_len]): 
            return idx 
        idx += 1
    return None
    


def part_2(): 
    with open("2024/day_9/input.txt", "r") as f: 
        data = f.read().strip()
    out = []
    jdx = 0
    s = 0
    for idx in range(len(data)):  
        for _ in range(int(data[idx])): 
            if idx % 2: 
                out.append(".")
            else: 
                out.append(jdx)
        jdx += 1 if not idx % 2 else 0
    jdx -= 1

    while jdx > -1: 
        target_len = out.count(jdx)
        target_idx = out.index(jdx)
        if (idx:= find_index(out, target_len, jdx)) is not None:
            frag = out[target_idx: target_idx+target_len]
            out = out[:target_idx] + ["." for _ in " "*target_len]+ out[target_idx+target_len:]
            out = out[:idx] + frag + out[idx+target_len:]
        jdx -=1

    print()
    for pos in range(len(out)): 
        if out[pos] != ".": 
            s+= pos * out[pos]

    print(s)





part_2()
