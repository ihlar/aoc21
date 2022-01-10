import time

def enhance(image, enhancement, oob):
    out = []
    for y in range (-1, len(image) + 1):
        r = ""
        for x in range (-1, len(image[0]) + 1):
            num = ""
            for gy in range(y-1, y+2):
                for gx in range(x-1, x+2):
                    if 0 <= gy < len(image) and 0 <= gx < len(image[0]):
                        num += '1' if image[gy][gx] == "#" else '0'
                    else:
                        num += '0' if oob == '.' else '1'
            r += enhancement[int(num, 2)]
        out.append(r)
    return out, enhancement[0 if oob == '.' else -1]

def n_lit(img):
    sum = 0
    for r in img:
        for c in r:
            if c == '#':
                sum += 1
    return sum

def first(inpath):
    with open(inpath, 'r') as indata:
        lns = indata.readlines()
        estr = lns[0].strip('\n')
        inputimage = [l.strip('\n') for l in lns[2:]]
        outputimage, oob = enhance(inputimage, estr, '.')
        for _ in range(49):
            outputimage, oob = enhance(outputimage, estr, oob)
        return n_lit(outputimage)

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")