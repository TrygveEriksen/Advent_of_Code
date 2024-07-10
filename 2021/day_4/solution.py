
def get_input():
	with open("2021/day_4/input.txt", "r") as f:
		lines = f.read().replace("  "," ").replace("\n ","\n").split("\n\n")
	return lines

def check(num, a)->int:
	for i in range(len(num)):
		##check col
		if len(list(filter(lambda x: x in a,[num[b][i] for b in range(len(num))]))) == len(num) or len(list(filter(lambda x: x in a, num[i]))) == len(num[i]):
			return sum(sum(int(c) for c in b if c not in a) for b in num )
	return 0


def part_1():
	nums = get_input()
	a = nums[0].split(",")
	nums = [[b.split(" ") for b in c.split("\n")]for c in nums[1:]]
	m = 0
	for i in range(len(a)):
		b = a[i]
		if m: 
			break
		for num in nums:
			m = max(m, int(b)*check(num, a[:i+1]))
	return m

def part_2():
	nums = get_input()
	a = nums[0].split(",")
	nums = [[b.split(" ") for b in c.split("\n")]for c in nums[1:]]

	for i in range(len(a)):
		b = a[i]
		for num in nums[::-1]:
			temp = int(b)*check(num, a[:i+1])
			if temp and len(nums) > 1:
				nums.remove(num)
			elif temp :
				return temp
	return 0

print(part_2())