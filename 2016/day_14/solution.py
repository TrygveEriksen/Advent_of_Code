import hashlib
from functools import lru_cache


salt = "ngcjuoqr"

@lru_cache(maxsize = 2048)
def hash_num(num):  
        h2 =  hashlib.md5((salt + str(num)).encode()).hexdigest()
        for _ in range(2016): 
            h2 = hashlib.md5(h2.encode()).hexdigest()
        return h2

def part_1(): 
    c = 0
    idx = 0
    while c < 64:
            h = hash_num(idx)
            triples = [5*h[i] for i in range(len(h)-2) if  h[i] == h[i+1] and h[i+1] == h[i+2]] 
            if len(triples): 
                for jdx in range(1, 1001):
                    abc =  hash_num(jdx + idx)
                    t = triples[0]
                    if t in abc:
                        print(f"Found {t[:3]} ({idx}) at {idx+jdx}")
                        c += 1
                        print(f"Counter at: {c}")
                        break
            idx += 1
    return idx - 1

print(part_1())
