def part_1(): 
	
	with open("2015/day_7/input.txt", "r") as f: 
		d = {line.strip().split(" -> ")[1].strip(): line.strip().split(" -> ")[0].strip() for line in f.readlines()}
		d2 = d.copy()
	def DFS(node, c):
		try: 
			val = int(node)
			return val
		except: 
			pass
		ops = d[node]
		try: 
			val = int(ops)
			d[node] = val
			return val
		except: 
			pass

		if "NOT" in ops: 
			ops=ops.replace("NOT ", "")
			val =  ~DFS(ops, c)
			d[node] = val
			return val
		elif "OR" in ops: 
			ops = ops.split(" OR ")
			val =  DFS(ops[0], c) | DFS(ops[1], c)
			d[node] = val
			return val
		elif "AND" in ops: 
			ops= ops.split(" AND ")
			val = DFS(ops[0], c) & DFS(ops[1], c)
			d[node] = val
			return val
		elif "LSHIFT" in ops: 
			ops= ops.split(" LSHIFT ")
			val = DFS(ops[0], c) << int(ops[1])
			d[node] = val
			return val
		elif "RSHIFT" in ops: 
			ops= ops.split(" RSHIFT ")
			val = DFS(ops[0], c) >> int(ops[1])
			d[node] = val
			return val
		else: 
			val = DFS(ops, c)
			d[node] = val
			return val
	
	val = DFS("a", 0)
	d = d2.copy()
	d["b"] = str(val)
	return DFS("a",c=0)

print(part_1())