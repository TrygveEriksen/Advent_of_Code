def apply(s):
	i = 0
	ret=""
	while i < len(s): 
		c = 1
		while i+c < len(s): 
			if s[i+c] == s[i]: 
				c+=1 
			else: 
				ret +=f"{c}{s[i]}"
				i+=c
				break
		else: 
			ret += f"{c}{s[i]}"
			return ret


	return ret


		

s="1113122113"
for i in range(50): 
	s=apply(s)

print(len(s))