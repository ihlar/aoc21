import time
from collections import defaultdict

def zero():
    return 0

def parseinput(indata):
    pairs = defaultdict(zero)
    chars = defaultdict(zero)
    template = indata[0].strip('\n') 
    for i in range(1, len(template)):
        c = template[i]
        p = template[i-1] + c 
        pairs[p] +=1
        chars[c] += 1
    rules = {}
    for line in indata[2:]:
        key, val = line.strip('\n').split(' -> ')
        rules[key] = val
    return (rules, pairs, chars)

def build_polymer(iterations, rules, pairs, chars):
    for _ in range(iterations):
        newpairs = defaultdict(zero)
        for pair in pairs:
            n = pairs[pair]
            c = rules[pair]
            newpair1 = pair[0]+c
            newpair2 = c+pair[1]
            for newpair in [newpair1, newpair2]:
                newpairs[newpair] += n
            chars[c] += n
        pairs = newpairs
    l = list(chars.values())
    l.sort()
    return l[-1] - l[0]
    
def first(inpath):
    with open(inpath, 'r') as indata:
        return build_polymer(10, *parseinput(indata.readlines()))

def second(inpath):
    with open(inpath, 'r') as indata:
        return build_polymer(40, *parseinput(indata.readlines()))

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")
    start = time.time()
    print(f"Second: {second(input)} - elapsed {time.time()-start}")