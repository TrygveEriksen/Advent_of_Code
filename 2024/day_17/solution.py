
def part_1(): 
    regs = [0, 0, 0]
    instr = [*map(int,open("2024/day_17/input.txt", "r").read().strip().split(","))]
    a = pow(8, 15)
    while 1: 
        ip = 0
        out = []
        regs = [0, 0, 0]
        regs[0]=a
        while 0 <= ip < len(instr): 
            match instr[ip]: 
                case 0: 
                    if instr[ip+1] < 4:
                        regs[0] = int(regs[0]/2**instr[ip+1])
                    else:
                        regs[0] = int(regs[0]//2**regs[instr[ip+1]-4])
                    ip+=2
                case 1: 
                    regs[1] = regs[1] ^ instr[ip+1]
                    ip+=2
                case 2: 
                    if instr[ip+1] < 4:
                        regs[1] = int(instr[ip+1])
                    else:
                        regs[1] = int(regs[instr[ip+1]-4] % 8)
                    ip+=2
                case 3: 
                    if not regs[0]: 
                        ip+=2
                    else: 
                        ip = instr[ip+1]
                case 4: 
                    regs[1] = regs[1] ^ regs[2]
                    ip+=2
                case 5: 
                    if instr[ip+1] < 4:
                        out.append(instr[ip+1])
                    else:
                        out.append(regs[instr[ip+1]-4] % 8)
                    #if len(out) == len(instr) or not out == instr[:len(out)]: 
                    #    break
                    ip+=2
                case 6: 
                    if instr[ip+1] < 4:
                        regs[1] = int(regs[0]/2**instr[ip+1])
                    else:
                        regs[1] = int(regs[0]/2**regs[instr[ip+1]-4])
                    ip+=2
                case 7: 
                    if instr[ip+1] < 4:
                        regs[2] = int(regs[0]/2**instr[ip+1])
                    else:
                        regs[2] = int(regs[0]/2**regs[instr[ip+1]-4])
                    ip+=2
        if out == instr: 
            print(a)
            break
        if len(out) != len(instr): 
            print("fail")
            break

        c=2
        for i in range(2,len(out)):
            if out[i] != instr[i]: 
                c = i
        a+= pow(8, c-2)
        print(out)

    #print(",".join(str(i) for i in out))


part_1()