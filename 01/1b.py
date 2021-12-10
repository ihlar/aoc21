from typing import List

def count_larger(data: List[str], first: int) -> int:
    cnt = 0
    prev = first
    for e in data:
        if int(e) > prev:
            cnt += 1
        prev = int(e)
    return cnt

def suml(data: List[str]) -> int:
    sum = 0
    for e in data:
        sum += int(e)
    return sum

with open("input.dat", "r") as input:
    data = input.readlines()
    i = 0
    sums = []
    while i <= len(data) - 3:
        sums.append(suml(data[i:i+3]))
        i += 1
    first = int(sums[0])
    print(count_larger(sums[1:], first))

