import re

def part_1(): 
	data = open("2017/day_9/input.txt", "r").read().strip()
	data = re.sub(r'!{1}.{1}', "", data)
	s = 0
	for d in re.findall(r'<.*?>', data): 
		s += len(d)-2
	print(s)


part_1()