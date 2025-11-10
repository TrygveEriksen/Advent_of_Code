bots = {}

class Bot: 
    def __init__(self, num): 
        self.num = num
        self.vals = []
        self.to = ["", ""]
        self.hasgiven = False

    def give(self):
        self.hasgiven = True
        if self.num[:3] == "out" or self.to == ["", ""]: 
            return
        global bots
        print("Giving in bot: " + self.num)
        b0 = bots.get(self.to[0])    
        b0.vals.append(self.vals[0])
        if len(b0.vals) == 2 and not b0.hasgiven: 
            b0.vals.sort()
            b0.give()

        b1 = bots.get(self.to[1])
        b1.vals.append(self.vals[1])
        if len(b1.vals) == 2 and not b1.hasgiven: 
            b1.vals.sort()
            b1.give()

def part_1(): 
    part_1.has_been_called = True
    with open("2016/day_10/input.txt") as f: 
        lines = [line.strip().split() for line in f.readlines()]
    for line in lines: 
        if line[0] == "value": 
            num = line[-2] + line[-1]
            val = int(line[1])
            if num not in bots: 
                b0 = Bot(num)
                bots[num] = b0
            else: 
                b0 = bots[num]
            b0.vals.append(val)
            bots[num] = b0
        if line[0] == "bot": 
            num_from = line[0] + line[1]
            low = line[5] + line[6]
            high = line[-2] + line[-1]
            if num_from not in bots: 
                b0 = Bot(num_from)
            else: 
                b0 = bots[num_from]
            bots[num_from] = b0 
            b0.to = [low, high]
            if low not in bots: 
                bots[low] = Bot(low)
            if high not in bots: 
                bots[high] = Bot(high)
    change = True
    #breakpoint()
    while change:
        print("New round")
        change = False
        for num, bot in sorted(bots.items()):
            print(f"{bot.num} -> {bot.to}, {bot.vals}")
            if len(bot.vals) == 2 and not bot.hasgiven: 
                bot.give()
                change = True
    for bot in bots.values():
        if bot.vals == [17, 61]:
            print("yey lets go")
            print(bot.num)

def part_2():
    assert part_1.has_been_called, "oh no so bad!"
    print(bots['output0'].vals[0]*bots['output1'].vals[0]*bots['output2'].vals[0])

part_1.has_been_called = False
part_1()        
part_2()
