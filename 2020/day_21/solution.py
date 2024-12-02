

def get_input(): 
	with open("2020/day_21/input.txt","r") as f: 
		return [line.replace(")", "").strip().split(" (") for line in f.readlines()]
	


def part_1(): 
	ingredients = get_input()

	ingredients = [(set(a.split()), set(b.replace("contains ", "").split(", "))) for a,b in ingredients]
	print(ingredients)

part_1()