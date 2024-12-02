import re

def part_1(): 
	with open("2015/day_12/input.txt", "r") as f: 
		file = f.read()
	while "red" in file: 
		idx = bi = file.index("red")
		bc = fc = 1
		lfi = lbi = fi = bi 
		lbc = lfc = 1
		while bc > 0: 
			bi -= 1
			bc += file[bi]=="}"
			bc -= file[bi]=="{"
		while fc > 0: 
			fi += 1

			fc -= file[fi]=="}"
			fc += file[fi]=="{"

		while lbi >= 0 and lbc > 0: 
			lbi -= 1
			lbc += file[lbi]=="]"
			lbc -= file[lbi]=="["				
		while lfi < len(file)-1 and lfc > 0: 
			lfi += 1
			lfc -= file[lfi]=="]"
			lfc += file[lfi]=="["						


		if lbi > bi and lfi < fi: 
			file = file[:idx] + file[idx+3: ]
		else: 
			file = file[:bi] + file[fi+1: ]
		


	l = re.split(r"[{},:\[\]]", file)
	s = 0
	for i in l: 
		try: 
			s+= int(i)
		except: pass
	print(s)
part_1()
