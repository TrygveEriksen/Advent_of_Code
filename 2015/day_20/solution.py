from sympy import factorint
from itertools import product

def factor_sum(n): 
    factors = factorint(n)

    primes = list(factors.keys())
    powers = [list(range(factors[p] +1)) for p in primes]

    # Generate all combinations of powers
    divisors = []
    for combination in product(*powers):
        divisor = 1
        for p, power in zip(primes, combination):
            divisor *= p**power
        divisors.append(divisor)
    s = 0
    for d in divisors: 
        if d*50 >= n: 
            s+= d
    return s


def part_1(): 
    target = 33100000
    i = 1
     
    while factor_sum(i)*11 < target: 
        i+=1

    print(i)



#print(factor_sum(65520))
part_1()