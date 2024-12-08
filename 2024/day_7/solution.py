def evaluate(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        match ops[i]: 
            case '+':
                result += nums[i+1]
            case'*':
                result *= nums[i+1]
            case _ :
                result = int(str(result) + str(nums[i+1]))
    return result

def can_match(target, nums):
    if len(nums) == 1:
        return target == nums[0]
    
    operators = ['+', '*', '||']
    n = len(nums) - 1
    
    for op_combo in range(3**n):
        ops = []
        curr = op_combo
        for _ in range(n):
            ops.append(operators[curr % 3])
            curr //= 3
            
        if evaluate(nums, ops) == target:
            return True
            
    return False

def part_1(): 
    data = [line.strip().split(": ") for line in open("2024/day_7/input.txt", "r").readlines()]
    s = 0
    for line in data:
        target, nums = line
        target = int(target)
        nums = [int(x) for x in nums.split()]
        
        if can_match(target, nums):
            s+= target

    print(s)
part_1()
