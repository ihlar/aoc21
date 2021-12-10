from functools import reduce
import sys

with open("input.dat", "r") as input:
    prev = int(input.readline())
    cnt = 0
    for l in input.readlines():
        if int(l) > prev:
            cnt += 1
        prev = int(l)   
    print(cnt)

with open("input.dat", "r") as input:
    data = input.readlines()
    print(
        sum(
            [int(x) > int(y) for x,y in zip(data[1:], data)]
        )
    )
    print(len(list(filter(lambda x,y: int(y)>int(x), data, data[1:]))))