import time
from functools import reduce
from collections import deque
import math
import re

digitpair = re.compile("\[\d+,\d+\]")
multidigit = re.compile("\d\d+")
number = re.compile("\d+")

def explode(pair):
    depth = 0
    match = re.search(digitpair, pair)
    pstart = 0
    while match:
        start, end = match.span()
        start += pstart
        end += pstart
        for pos in range(pstart, start+1):
            c = pair[pos]
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
        if depth > 4:
            n1, n2 = pair[start+1:end-1].split(',')
            leftmatch = None
            for m in re.finditer(number, pair[:start]):
                leftmatch = m
            if leftmatch:
                lns, lne = leftmatch.span()
                lnum = pair[lns:lne]
                newnum = str(int(lnum) + int(n1))
                pair = pair[:lns] + newnum + pair[lne:]
                start += len(newnum) - len(lnum)
                end += len(newnum) - len(lnum)
            rightmatch = re.search(number, pair[end:])
            if rightmatch:
                rns, rne = rightmatch.span()
                rnum = pair[end + rns : end + rne]
                pair = pair[:end + rns] + str(int(rnum) + int(n2)) + pair[end + rne:]
            pair = pair[:start] + '0' + pair[end:]
            return pair
        depth -= 1
        pstart = end
        match = re.search(digitpair, pair[pstart:])    
    return None

def split(pair):
    match = re.search(multidigit, pair)
    if match:
        start, end = match.span()
        num = float(pair[start:end])
        return pair[:start] + f"[{math.floor(num / 2)},{math.ceil(num / 2)}]" + pair[end:]
    else:
        return None

def reducepair(p):
    r = explode(p)
    while r != None:
        r1 = explode(r)
        if r1 != None:
            r = r1
            continue
        r1 = split(r)
        if r1 == None:
            return r
        r = r1
    return p

def addpairs(n1, n2):
    return reducepair(f"[{n1},{n2}]")

def magnitude(pair):
    p1, p2 = pair
    m = 0
    if isinstance(p1, list):
        m += 3 * magnitude(p1)
    else:
        m += 3 * p1
    if isinstance(p2, list):
        m += 2 * magnitude(p2)
    else:
        m += 2 * p2
    return m

def first(inpath):
    with open(inpath, 'r') as indata:
        nums = []
        for num in indata.readlines():
            nums.append(num.strip('\n'))
        maxmag = 0
        for i, n1 in enumerate(nums):
            for n2 in nums[i+1:]:
                maxmag = max(maxmag, max(magnitude(eval(addpairs(n1, n2))), magnitude(eval(addpairs(n2, n1)))))
        return (magnitude(eval(reduce(addpairs, nums))), maxmag)

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")