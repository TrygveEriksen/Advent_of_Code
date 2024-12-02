

alphabet = "abcdefghijklmnopqrstuvwxyz"
i, o, l = alphabet.index("i"), alphabet.index("o"), alphabet.index("l")

def increment(s):
	s[-1]+=1
	for j in range(len(s)-1, 0, -1):
		s[j-1]+= s[j]//len(alphabet)
		s[j]%=len(alphabet)
	return s
	

def part_1(): 
	s = [alphabet.index(a) for a in "hxbxxyzz"]
	increment(s)
	while 1: 
		l1 = any(s[i]+2 == s[i+1]+1 and s[i]+2== s[i+2] for i in range(len(s)-2))
		l2 = i not in s and o not in s and l not in s
		c=0
		j=0
		while  j< len(s)-1: 
			if s[j] == s[j+1]: 
				c+=1 
				j+=2
			else: 
				j+=1

		l3 = c > 1
		print("".join(alphabet[i] for i in s))
		if l1 and l2 and l3: 
			break
		else: 
			s=increment(s)
	return "".join(alphabet[i] for i in s)
print(part_1())