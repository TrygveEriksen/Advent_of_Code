from itertools import combinations
from functools import reduce
def part_1(): 
	with open("2015/day_24/input.txt", "r") as f: 
		l = list(map(int, f.read().split()))

	
	comb = combinations(l, 5)
	m = 99999999999999999
	for c in comb: 
		try: 
			if sum(c) == 387: 
				l2 = set(l)
				for i in range(5, len(l)-5): 
					comb2 = combinations(l2.difference(set(c)), i)
					for c2 in comb2: 
						if sum(c2) == 387: 
							for j in range(5, len(l)-5-i): 
								comb3 = combinations(l2.difference(set(c)).difference(set(c2)), j)
								for c3 in comb3: 
									if sum(c3) == 387: 
										m = min(m, reduce(lambda x, y: x*y, c, 1))
										raise Exception("Found")
		except Exception as e: 
			print(e)
	print(m)

part_1()