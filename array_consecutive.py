def solution(statues):
    count = 0
    statues = sorted(statues)
    for i in range(statues[0],statues[-1]):
        if i not in statues:
            count += 1
    return count

#alternative
def solution2(statues):
    return max(statues) - min(statues) - len(statues) + 1

solution([6, 2, 3, 8])