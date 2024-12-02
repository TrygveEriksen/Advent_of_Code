def part_2(): 
	with open("2015/day_1/input.txt", "r") as f: 
		_input = f.read()
	c=0 
	for i in range(len(_input)): 
		if c < 0: 
			return i
		c += _input[i] == "("
		c -= _input[i] == ")"


print(part_2())
