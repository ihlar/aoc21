from functools import reduce

VISITED = -1
PEAK = 9

def parseinput(indata):
    return [[int(c) for c in l.strip()] for l in indata.readlines()]

def ismin(val, x, y, grid):
    line = grid[y]
    return (
        (y == 0 or grid[y-1][x] > val) and
        (y == len(grid)-1 or grid[y+1][x] > val) and
        (x == 0 or line[x-1] > val) and
        (x == len(line)-1 or line[x+1] > val)
    )

def getbasin(x, y, grid):
    line = grid[y]
    count = 1
    if grid[y][x] == PEAK or grid[y][x] == VISITED:
        return 0
    grid[y][x] = VISITED
    if x < len(line) - 1:
        count += getbasin(x+1,y, grid) 
    if x > 0:
        count += getbasin(x-1,y, grid) 
    if y < len(grid) - 1:
        count += getbasin(x,y+1, grid) 
    if y > 0:
        count += getbasin(x,y-1, grid) 
    return count

def sorted_insert(val, sorted):
    if val <= sorted[0]:
        return
    sorted[0] = val
    for i in range(1, len(sorted)):
        v = sorted[i]
        if v < sorted[i-1]:
            sorted[i] = sorted[i-1]
            sorted[i-1] = v
        else:
            return
            
def first(inpath):
    with open(inpath, 'r') as indata:
        grid = parseinput(indata)
        sum = 0
        for y, line in enumerate(grid):
            for x, val in enumerate(line):
                if ismin(val, x, y, grid):
                    sum += val+1
        return sum

def second(inpath):
    with open(inpath, 'r') as indata:
        grid = parseinput(indata)
        basins = [0,0,0]
        for y, line in enumerate(grid):
            for x, val in enumerate(line):
                if ismin(val, x, y, grid):
                    basin = getbasin(x, y, grid)
                    sorted_insert(basin, basins)
        return reduce(lambda a,b: a*b, basins, 1)

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")