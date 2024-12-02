class Bot: 
	def __init__(self, id): 
		self.id = id
		self.nums=[]
		self.gives=[]
	
	def recieve(self, num): 
		self.nums.append(num)
		if len(self.nums) == 2:
			if sorted(int(i) for i in self.nums) == sorted([17, 61]):
				print(self.id)
				exit()
			else: 
				self.gives[0].recieve(str(min(int(i) for i in self.nums)))
				self.gives[1].recieve(str(max(int(i) for i in self.nums)))
	

bots = {}

with open("2016/day_10/input.txt", "r") as f: 
		lines = f.readlines()

todo = []

for line in lines: 
	line=line.strip()
	l = line.split(" ")
	if l[0] == "value": 
		todo.append(l)
	elif l[0] == "bot": 
		n = l[1]
		if l[6] not in bots: 
			bots[l[6]] = Bot(l[6])
		if l[11] not in bots: 
			bots[l[11]] = Bot(l[11])
		if n not in bots: 
			bots[n] = Bot(n)
			
		bots[n].gives = [bots[l[6]], bots[l[11]]]
	
for l in todo: 
	val = l[1]
	n = l[5]
	bots[n].recieve(val)
	
	