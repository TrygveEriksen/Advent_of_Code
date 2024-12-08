import re

def part_1(): 
	with open("2024/day_4/input.txt", "r") as f: 
		lines = [line.strip() for line in f.readlines()]
	s=0
	for i in range(1, len(lines)-1): 
		for j in range(1, len(lines[i])-1): 
			if lines[i][j] == "A": 
				s+= (lines[i-1][j-1] == "M" and lines[i+1][j+1]=="S" or lines[i-1][j-1]=="S" and lines[i+1][j+1]=="M") and (lines[i-1][j+1] == "M" and lines[i+1][j-1]=="S" or lines[i-1][j+1]=="S" and lines[i+1][j-1]=="M")
	print(s)
	






part_1()
