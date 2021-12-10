def parseline(l):
    return [
        tuple(map(
            lambda c: int(c), 
            p.strip().split(',')
            )) 
        for p in l.split('->')
        ]

def is_diagonal(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1-x2) == abs(y1-y2)

def diagonal_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    yield (x1, y1)
    while y1 != y2:
        y1 += 1 if y2 > y1 else -1
        x1 += 1 if x2 > x1 else -1
        yield (x1, y1)

def first(inpath):
    with open(inpath, "r") as input:
        data = input.readlines()
        grid = []
        largestx = 0
        largesty = 0
        avoid = 0
        danger = 2
        lines = [parseline(l) for l in data]
        for line in lines:
            x1, y1 = line[0]
            x2, y2 = line[1]
            largestx = max(largestx, max(x1, x2))
            largesty = max(largesty, max(y1, y2))
        for _ in range(0, largesty+1):
            grid.append([0 for _ in range(0, largestx+1)])
        for line in lines:
            x1, y1 = line[0]
            x2, y2 = line[1]
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x1] += 1
                    if grid[y][x1] == danger:
                        avoid += 1
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    grid[y1][x] += 1
                    if grid[y1][x] == danger:
                        avoid += 1
        return avoid

def second(inpath):
    with open(inpath, "r") as input:
        data = input.readlines()
        grid = []
        largestx = 0
        largesty = 0
        avoid = 0
        danger = 2
        lines = [parseline(l) for l in data]
        for line in lines:
            x1, y1 = line[0]
            x2, y2 = line[1]
            largestx = max(largestx, max(x1, x2))
            largesty = max(largesty, max(y1, y2))
        for _ in range(0, largesty+1):
            grid.append([0 for _ in range(0, largestx+1)])
        for line in lines:
            x1, y1 = line[0]
            x2, y2 = line[1]
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x1] += 1
                    if grid[y][x1] == danger:
                        avoid += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    grid[y1][x] += 1
                    if grid[y1][x] == danger:
                        avoid += 1
            elif is_diagonal(*line):
                for x, y in diagonal_line(*line):
                    grid[y][x] += 1
                    if grid[y][x] == danger:
                        avoid += 1
        return avoid

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")