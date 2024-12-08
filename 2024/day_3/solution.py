import re

def part_1(): 
	with open("2024/day_3/input.txt", "r") as f: 
		lines = f.read()
	o=True
	s=0
	while "do()"in lines or "don't()" in lines: 
		if o: 
			idx = lines.find("don't()")
			mul = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines[:idx])
			for m in mul: 
				m2=m.replace(")", "").replace("mul(", "").strip().split(",")
				s+= int(m2[0])*int(m2[1])
		else: 
			idx = lines.find("do()")
		lines = lines[idx:]
		o = not o
	print(s)
part_1()
