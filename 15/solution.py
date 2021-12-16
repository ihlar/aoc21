import time
import math

def zero():
    return 0

def parseinput(indata):
    grid = [] #[[None] * len(indata[0].strip('\n'))] * len(indata)
    leny = len(indata)
    lenx = len(indata[0].strip('\n'))
    for y, line in enumerate(indata):
        l = []
        for x, d in enumerate(line.strip('\n')):
            l.append(node(int(d), x, y, lenx, leny))
        grid.append(l)
    return grid

def listincr(l):
    return [n + 1 if n < 9 else 1 for n in l]

def parseinput2(indata):
    grid = []
    leny = len(indata) * 5
    lenx = len(indata[0].strip('\n')) * 5
    for y, line in enumerate(indata):
        l = []
        for x, d in enumerate(line.strip('\n')):
            l.append(int(d))
        grid.append(l)
    for n in range(4):
        for i, line in enumerate(grid):
            grid[i] += listincr(line[(n*lenx)//5:(n+1)*lenx//5])
    for n in range(4):
        for i in range((n*lenx)//5, (n+1)*lenx//5):
            grid.append(listincr(grid[i]))
    for y in range(leny):
        for x in range(lenx):
            grid[y][x] = node(grid[y][x], x, y, lenx, leny)
    return grid

ADJ = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class node:
    def __init__(self, cost, x, y, lenx, leny) -> None:
        self.cost = cost
        self.path_cost = math.inf
        self.adjacent = []
        for dx, dy in ADJ:
            if x+dx >=0 and x+dx < lenx and y+dy >= 0 and y+dy < leny:
                self.adjacent.append((x+dx, y+dy))

def adjacent(x, y, lenx, leny):
    ad = []
    for dx, dy in ADJ:
        if x+dx >=0 and x+dx < lenx and y+dy >= 0 and y+dy < leny:
            ad.append((x+dx, y+dy))
    return ad

def get_cost(grid):
    current = grid[0][0]
    current.path_cost = 0
    y = 0
    x = 0
    while y < len(grid):
        ny = y + 1
        nnx = math.inf
        while x < len(grid[0]):
            cur = grid[y][x]
            nx = x + 1
            for c,r in cur.adjacent:
                next = grid[r][c]
                if cur.path_cost + next.cost < next.path_cost:
                    next.path_cost = cur.path_cost + next.cost 
                    if r < y:
                        ny = r
                        if c < nnx:
                            nnx = c
                    elif c < x:
                        nx = c
            x = nx
        y = ny
        x=0 if nnx == math.inf else nnx
    return grid[-1][-1].path_cost

def first(inpath):
    with open(inpath, 'r') as indata:
        grid = parseinput(indata.readlines())
        return get_cost(grid)

def second(inpath):
    with open(inpath, 'r') as indata:
        grid = parseinput2(indata.readlines())
        return get_cost(grid)

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")
    start = time.time()
    print(f"Second: {second(input)} - elapsed {time.time()-start}")