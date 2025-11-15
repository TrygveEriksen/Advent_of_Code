from collections import deque
def part_1(): 
    q = deque([(idx + 1, 1) for idx in range(3017957)])
    while len(q) > 1: 
        cur = q.popleft()
        eat = q.popleft()
        q.append((cur[0], cur[1] + eat[1]))
    return q.popleft()


def part_2():
    left = deque()
    right = deque()
    for i in range(1,  3017957+1):
        if i < ( 3017957// 2) + 1:
            left.append(i)
        else:
            right.append(i)
    while left and right:
        if len(left) > len(right): 
            left.pop()
        else: 
            right.popleft()
        right.append(left.popleft())
        left.append(right.popleft())
    return left[0] or right[0]
print(part_2())
