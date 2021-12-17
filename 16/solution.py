import time
import math
from enum import IntEnum

class sizes(IntEnum):
    version = 3
    type = 3
    literal = 5

class types(IntEnum):
    sum = 0
    product = 1
    min = 2
    max = 3
    literal = 4
    greater = 5
    less = 6
    equal = 7

length_types = {'0' : 15, '1' : 11}

def hextobin(hex):
    return format(int(hex, 16), "04b")

def unit(a, _): 
    return a

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def gt(a, b):
    if b == math.inf:
        return a
    return 1 if a < b else 0

def lt(a, b):
    if b == math.inf:
        return a
    return 1 if a > b else 0

def eq(a, b):
    if b == math.inf:
        return a
    return 1 if a == b else 0

def min(a, b):
    return a if a < b else b

def max(a, b):
    return a if a > b else b

def parse_packet(pos, packet_length, n, pval, operation, binstr):
    versionsum = 0
    packetvalue = pval
    while pos < packet_length or n > 0:
        if packet_length > 0 and packet_length - pos < sizes.version + sizes.type + 5:
            pos = packet_length
            break 
        versionsum += int(binstr[pos:pos+sizes.version], 2)
        pos += sizes.version
        T = int(binstr[pos:pos+sizes.type], 2)
        pos += sizes.type
        print(T, packetvalue)
        if T == types.literal:
            value = ""
            done = False
            while not done:
                L = binstr[pos:pos+sizes.literal]
                value += L[1:]
                if L[0] == '0':
                    done = True
                pos += sizes.literal
            v = int(value, 2)
            packetvalue = operation(v, packetvalue)    
            n -= 1
        else:
            op = unit
            if T == types.sum:
                oval = 0
                op = add
            elif T == types.product:
                oval = 1
                op = mult
            elif T == types.min:
                oval = math.inf
                op = min
            elif T == types.max:
                oval = -999999
                op = max
            elif T == types.greater:
                oval = math.inf
                op = gt
            elif T == types.less:
                oval = math.inf
                op = lt
            elif T == types.equal:
                oval = math.inf
                op = eq

            lentype = length_types[binstr[pos]]
            pos += 1
            lenval = int(binstr[pos:pos+lentype], 2)
            pos += lentype
            plen = pos + lenval if lentype == 15 else 0
            npackets = lenval if lentype == 11 else 0
            pval, vsum, p = parse_packet(pos, plen, npackets, oval, op, binstr)
            versionsum += vsum
            packetvalue = operation(pval, packetvalue)
            pos = p
            n -= 1
    return (packetvalue, versionsum, pos)

def first(inpath):
    with open(inpath, 'r') as indata:
        data = indata.read()
        hexstr = data
        binstr = "" 
        for hex in hexstr:
            binstr += hextobin(hex)
        value, sum, _ = parse_packet(0, len(binstr), 0, 0, unit, binstr)
        return (sum, value)

def second(inpath):
    with open(inpath, 'r') as indata:
        return 0

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")