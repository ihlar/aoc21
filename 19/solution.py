import time
from collections import Counter

def x_rotate(vec):
    x, y, z = vec
    return (x, -z, y)

def y_rotate(vec):
    x, y, z = vec
    return (z, y, -x)

def z_rotate(vec):
    x, y, z = vec
    return (-y, x, z)

def alignments(vec):
    als = []
    v = None
    while v != vec:
        if not v:
            v = vec
        v1 = y_rotate(v)
        while v1 != v:
            v2 = z_rotate(v1)
            while v2 != v1:
                als.append(v2)
                v2 = z_rotate(v2)
            als.append(v1)
            v1 = y_rotate(v1)
        als.append(v)
        v = x_rotate(v)
    return als

def distance(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return (x1-x2, y1-y2, z1-z2)

def repos(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return (x1+x2, y1+y2, z1+z2)

def manhattan(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

def first(inpath):
    with open(inpath, 'r') as indata:
        scanners = []
        s = []
        for l in indata.readlines():
            if l.startswith("---"):
                scanners.append(s)
            elif l == "\n":
                s = []
            else:
                x,y,z = l.strip('\n').split(',')
                s.append((int(x), int(y), int(z)))
        beacons = set(scanners[0])
        scpos = [(0,0,0)]
        als = [[alignments(b1) for b1 in s] for s in scanners[1:]]
        unmapped = als
        while unmapped:
            scanners = unmapped
            for s in als:
                found = False
                for i in range(0, len(s[0])):
                    distances = Counter()
                    for b in beacons:
                        for b2a in s:
                            distances[distance(b, b2a[i])] += 1
                    for d, c in distances.items():
                        if c >= 12:
                            found = True
                            for b2a in s:
                                beacons.add(repos(b2a[i], d))
                            print(d, len(beacons))
                            scpos.append(d)
                            unmapped.remove(s)
                            break
                    if found: break
        maxman = 0
        for i in range(len(scpos)):
            for j in range(i, len(scpos)):
                maxman = max(manhattan(scpos[i], scpos[j]), maxman)
        return len(beacons), maxman

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")