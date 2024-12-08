def part_1(): 
	r2 = row = 3010
	col = 3019
	s=0
	while col > 0: 
		s+= row
		row+= 1
		col -= 1
	r2 -= 2
	while r2 > 0: 
		s+= r2
		r2-= 1

	print(s)
	num = 20151125
	mul = 252533
	div = 33554393
	for i in range(s-1): 
		num = (num * mul) % div
	print(num)
part_1()