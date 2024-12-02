import hashlib

def part_1():
	key = "bgvyzdsv"
	c = 0
	while not all(a == "0" for a in ((hashlib.md5((key+str(c)).encode()).hexdigest()))[:6]): 
		c+=1
	return c
print(part_1())