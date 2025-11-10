def compare(d, reg, op, val)-> bool: 
	match op: 
		case ">": 
			return d.get(reg, 0) > val
		case ">=": 
			return d.get(reg, 0) >= val
		case "<=": 
			return d.get(reg, 0) <= val
		case "<": 
			return d.get(reg, 0) < val
		case "!=": 
			return d.get(reg, 0) != val
		case "==": 
			return d.get(reg, 0) == val
		case _: 
			raise Exception(f"Unsupported operand: {op}")

def apply(d, reg, op, val): 
	match op: 
		case "inc": 
			d[reg] = d.get(reg, 0) + val
		case "dec": 
			d[reg] = d.get(reg, 0) - val
		case _:
			raise Exception("Bad news")

def part_1(): 
	regs = {}
	m = 0
	data = [[a.split()[0], a.split()[1], int(a.split()[2]), a.split()[3], a.split()[4], a.split()[5], int(a.split()[6])] for a in open("2017/day_8/input.txt", "r").read().split("\n")]
	for instr in data: 
		if compare(regs, instr[4], instr[5], instr[6]): 
			apply(regs, instr[0], instr[1], instr[2])
		m = max(max(regs.values()), m)
	print(m)

part_1()