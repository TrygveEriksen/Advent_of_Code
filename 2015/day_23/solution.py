def part_1(): 
	with open("2015/day_23/input.txt", "r") as f: 
		instructions = [line.strip().split() for line in f.readlines()]
	reg_dict = {"a": 0, "b": 1}
	regs = [1, 0]
	i = 0 
	try: 
		instr = instructions[0]
		while True: 
			match instr[0]: 
				case "hlf": 
					regs[reg_dict[instr[1]]] = regs[reg_dict[instr[1]]] // 2
					i+= 1
					instr = instructions[i]
				case "tpl": 
					regs[reg_dict[instr[1]]] = regs[reg_dict[instr[1]]] * 3
					i+= 1
					instr = instructions[i]
				case "inc": 
					regs[reg_dict[instr[1]]] = regs[reg_dict[instr[1]]] + 1
					i+= 1
					instr = instructions[i]
				case "jmp": 
					i+= int(instr[1])
					instr = instructions[i]
				case "jie": 
					if not int(regs[reg_dict[instr[1]]]) % 2: 
						i+= int(instr[2])
					else: 
						i+= 1
					instr = instructions[i] 
				case "jio": 
					if int(regs[reg_dict[instr[1]]])==1: 
						i+= int(instr[2])
					else: 
						i+= 1
					instr = instructions[i] 
			assert i >= 0
	except Exception as e: 
		print(e)
		print(regs[1])
	
part_1()