class Rule:
	def __init__(self):
		self.visited = 0
		self.ruleset = ""
		self.nb = {}
		self.combinations = set()

	def visit(self, max_depth):
		if self.visited: 
			return self.combinations
		if not max_depth: 
			print("MAX DEPTH REACHED")
			return self.combinations
		else:
			for rule in self.ruleset:
				temp = set()
				for n in rule:
					comb = self.nb[n].visit(max_depth-len(rule))
					if len(temp) == 0:
						temp = comb
					else:
						temp2 = set()
						for c in comb:
							for t in temp:
								temp2.add(t+c)
						temp = temp2
				self.combinations = self.combinations.union(temp)
			self.visited = 1
			return self.combinations



def get_rules():
	with open("2020/day_19/input1.txt","r") as f:
		lines = f.readlines()
	rules = [line.strip().split(":") for line in lines]
	r_dict = {}
	for rule in rules:
		r_dict[rule[0]] = rule[1].strip()

	return r_dict

def get_input():
	with open("2020/day_19/input2.txt","r") as f:
		return [line.strip() for line in f.readlines()]




def part_2(): 
	messages = set(get_input())
	r_dict= get_rules()
	rules = {}
	for i in range(max(int(a) for a in r_dict)+1):
		rules[str(i)] = Rule()
	
	max_depth = max(len(l) for l in messages)

	for rule in rules:
		r = r_dict[rule]
		if r == "a" or r== "b":
			rules[rule].visited = 1
			rules[rule].combinations.add(r)
		else:
			rules[rule].ruleset = [ru.strip().split(" ") for ru in r.split("|")]
			for a in rules[rule].ruleset:
				for n in a:
					rules[rule].nb[n] = rules[n]
	print(f"MAX DEPTH: {max_depth}")
	print("RULE PARSING DONE")
	pos = rules["0"].visit(max_depth)
	print("Visit done")
	return len(pos.intersection(messages))

print(part_2())