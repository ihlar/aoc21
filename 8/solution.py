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

def second(inpath):
    with open(inpath, 'r') as indata:
        notes = parseinput(indata.readlines())
        sum = 0
        for signals, digs in notes:
            tmpdigs=[[]]*10
            for sig in signals:
                if len(sig) == 7:
                    tmpdigs[8] = sig
                elif len(sig) == 3:
                    tmpdigs[7] = sig
                elif len(sig) == 2:
                    tmpdigs[1] = sig
                elif len(sig) == 4:
                    tmpdigs[4] = sig
            while [] in tmpdigs:
                for sig in signals:
                    if len(sig) == 5: # 2,3, 5
                        if tmpdigs[3] == []:
                            find3 = True
                            for w in tmpdigs[7]:
                                if w not in sig:
                                    find3 = False
                            if find3:
                                tmpdigs[3] = sig
                        elif tmpdigs[9] != [] and sig != tmpdigs[3]:
                            find5 = True
                            for w in sig:
                                if w not in tmpdigs[9]:
                                    find5 = False
                            tmpdigs[5 if find5 else 2] = sig
                    if len(sig) == 6: #6, 0, 9
                        if tmpdigs[6] == []:
                            for w in tmpdigs[1]:
                                if w not in sig:
                                    tmpdigs[6] = sig
                        elif sig != tmpdigs[6] and (tmpdigs[9] == [] or tmpdigs[0] == []):
                            find9 = True
                            for w in tmpdigs[3]:
                                if w not in sig:
                                    find9 = False
                            tmpdigs[9 if find9 else 0] = sig
            val = 0
            val = tmpdigs.index(digs[0])*1000 + tmpdigs.index(digs[1]) * 100 + tmpdigs.index(digs[2]) * 10 + tmpdigs.index(digs[3])
            sum += val    
        return sum

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")
