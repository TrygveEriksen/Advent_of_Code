
import re

def get_input():
    with open("2020/day_18/input.txt","r") as f:
        lines = f.readlines()
    return [line.strip().replace("(","( ").replace(")"," )").split(" ") for line in lines]

apply = lambda x,y,o : x+y if o =="+" else x*y

def ex_reduce(expression):
    operator="+"
    s=int(expression[0])
    for e in expression[1:]:
        match e: 
            case "+":
                operator = "+"
            case "*":
                operator = "*"
            case _ :
                s= apply(s, int(e), operator)
    return str(s) 


def part_1():
    k=0
    s=0
    ex = get_input()
    for e in ex:
        while ")" in e: 
            i = e.index(")")
            j=i
            k+=1
            while j>0: 
                j-=1
                if e[j] =="(":
                    #reduce
                    temp = e[j+1:i]
                    insert = ex_reduce(temp)
                    temp = e[:j] if j >0 else []
                    temp.append(insert)
                    if i < len(e)-1:
                        temp.extend(e[i+1:])
                    e = temp
                    break
        if len(e) > 1:
            e = [ex_reduce(e)]
        s+= int(e[0])
    return s

def ex_reduce_2(expression):
    while "+" in expression:
        i = expression.index("+")
        insert = str(int(expression[i-1])+int(expression[i+1]))
        temp = expression[:i-1] if i > 1 else []
        temp.append(insert)
        if i < len(expression)-2:
            temp.extend(expression[i+2:])
        expression=temp
    return str(eval("".join(expression)))     

def part_2():
    k=0
    s=0
    ex = get_input()
    for e in ex:
        while ")" in e: 
            i = e.index(")")
            j=i
            k+=1
            while j>0: 
                j-=1
                if e[j] =="(":
                    #reduce
                    temp = e[j+1:i]
                    insert = ex_reduce_2(temp)
                    temp = e[:j] if j >0 else []
                    temp.append(insert)
                    if i < len(e)-1:
                        temp.extend(e[i+1:])
                    e = temp
                    break
        if len(e) > 1:
            e = [ex_reduce_2(e)]
        s+= int(e[0])
    return s        
            
            
        
    


print(part_2())