import random
from functools import cache
import graphviz

def part_1(): 
	
	with open("2024/day_24/input.txt", "r") as f: 
		data = f.read().split("\n\n")

	d = {line.strip().split(" -> ")[1].strip(): line.strip().split(" -> ")[0].strip() for line in data[1].splitlines()}|{line.strip().split(": ")[0]:line.strip().split(": ")[1] for line in data[0].splitlines()}
	
	@cache
	def DFS(node):
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
			val =  ~DFS(ops)
			d[node] = val
			return val
		elif "XOR" in ops: 
			ops = ops.split(" XOR ")
			val = DFS(ops[0]) ^ DFS(ops[1])
			d[node] = val
			return val

		elif "OR" in ops: 
			ops = ops.split(" OR ")
			val =  DFS(ops[0]) | DFS(ops[1])
			d[node] = val
			return val
		elif "AND" in ops: 
			ops= ops.split(" AND ")
			val = DFS(ops[0]) & DFS(ops[1])
			d[node] = val
			return val
		else: 
			val = DFS(ops)
			d[node] = val
			return val
	
	out = ""
	for key in sorted(d.keys()): 
		if key[0] =="z":
			val = DFS(key)
			print(key, val)
			out += str(val)
	out = out[::-1]
	return out

#print(part_1())


def part_2(): 
	with open("2024/day_24/input.txt", "r") as f: 
		data = f.read().split("\n\n")
	for _ in range(2000): 
		x = bin(random.randint(0, 2**44 - 1))[2:].rjust(45, "0")
		y = bin(random.randint(0, 2**44 -1))[2:].rjust(45, "0")
		d1 = {}
		d2 = {line.strip().split(" -> ")[1].strip(): line.strip().split(" -> ")[0].strip() for line in data[1].splitlines()}
		for i in range(45):
			d1["x"+str(i).rjust(2, "0")] = x[44-i]
			d1["y"+str(i).rjust(2, "0")] = y[44-i]

		d = d1 | d2
		@cache
		def DFS(node):
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
				val =  ~DFS(ops)
				d[node] = val
				return val
			elif "XOR" in ops: 
				ops = ops.split(" XOR ")
				val = DFS(ops[0]) ^ DFS(ops[1])
				d[node] = val
				return val

			elif "OR" in ops: 
				ops = ops.split(" OR ")
				val =  DFS(ops[0]) | DFS(ops[1])
				d[node] = val
				return val
			elif "AND" in ops: 
				ops= ops.split(" AND ")
				val = DFS(ops[0]) & DFS(ops[1])
				d[node] = val
				return val
			else: 
				val = DFS(ops)
				d[node] = val
				return val
			
		a = bin(int(x, 2) + int(y, 2))[2:].rjust(45, "0")
		z = "".join(str(DFS("z"+str(44-j).rjust(2, "0"))) for j in range(45))
		wrong = [44-i for i in range(len(z)) if a[i] != z[i]]
		DFS.cache_clear()
		if len(wrong): 
			print(wrong)
			

		
	G = graphviz.Digraph(format="png", engine="dot")


	for key in d1: 
		G.node(key, key, shape="circle")
	
	c = 0 
	for out, input_ in d2.items(): 
		in1, gate, in2 = input_.split()
		G.node(gate+str(c), gate, shape="box")
		G.edge(in1, gate+str(c))
		G.edge(in2, gate+str(c))
		if out[0] == "z" and int(out[1:]) in wrong: 
			G.node(out, out, shape="circle", color="red")
		else: 
			G.node(out, out, shape="circle")
		G.edge(gate+str(c), out)
		c+=1


	out_path = "2024/day_24/output"
	G.render(out_path)
	#Manually change output nodes
	changes = ["z21", "shh", "vgs", "dtk", "z33", "dqr", "z39", "pfw"]
	print(",".join(sorted(changes)))
part_2()