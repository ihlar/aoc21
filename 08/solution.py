def splitline(line):
    l = [e.strip().split(' ') for e in line]
    ss = [sorted(list(s)) for s in l[0]]
    ds = [sorted(list(s)) for s in l[1]]
    return [ss, ds]

def parseinput(lines):
    return [splitline(line.strip('\n').split('|')) for line in lines]

def uniquelen(dig):
    return len(dig) == 2 or len(dig) == 4 or len(dig) == 3 or len(dig) == 7

def first(inpath):
    with open(inpath, 'r') as indata:
        signals = parseinput(indata.readlines())
        count = 0
        for _, digs in signals:
            for dig in digs:
                if uniquelen(dig):
                    count += 1
        return count

def find_unique(signals, decoded):
    for sig in signals:
        if len(sig) == 7:
            decoded[8] = sig
        elif len(sig) == 3:
            decoded[7] = sig
        elif len(sig) == 2:
            decoded[1] = sig
        elif len(sig) == 4:
            decoded[4] = sig

def find3(signals, decoded):
    for sig in signals:
        if len(sig) == 5:
            found = True
            for w in decoded[7]:
                if w not in sig:
                    found = False
            if found:
                decoded[3] = sig
                break

def find069(signals, decoded):
    for sig in signals:
        if len(sig) == 6: # 0, 6, 9
            if decoded[6] == []:
                for w in decoded[1]:
                    if w not in sig:
                        decoded[6] = sig
            if sig != decoded[6] and (decoded[9] == [] or decoded[0] == []):
                find9 = True
                for w in decoded[3]:
                    if w not in sig:
                        find9 = False
                decoded[9 if find9 else 0] = sig

def find52(signals, decoded):
    for sig in signals:
        if len(sig) == 5 and sig != decoded[3]: # 2,5
            find5 = True
            for w in sig:
                if w not in decoded[9]:
                    find5 = False
            decoded[5 if find5 else 2] = sig

def second(inpath):
    with open(inpath, 'r') as indata:
        notes = parseinput(indata.readlines())
        sum = 0
        for signals, digs in notes:
            decoded=[[]]*10
            find_unique(signals, decoded)
            find3(signals, decoded)
            find069(signals, decoded)
            find52(signals, decoded)                    
            sum += decoded.index(digs[0])*1000 + decoded.index(digs[1]) * 100 + decoded.index(digs[2]) * 10 + decoded.index(digs[3])
        return sum

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")
