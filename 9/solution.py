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

def gb(x,y,grid):
    line = grid[y]
    count = 0  
    if grid[y][x] == 9 or grid[y][x] == -1:
        return 0
    grid[y][x] = -1
    count = 1
    if x < len(line) - 1:
        count += gb(x+1,y, grid) 
    if x > 0:
        count += gb(x-1,y, grid) 
    if y < len(grid) - 1:
        count += gb(x,y+1, grid) 
    if y > 0:
        count += gb(x,y-1, grid) 
    return count
        
def getbasin(x, y, grid):
    return gb(x,y,grid)

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
                    if basin > basins[0]:
                        basins[0] = basin
                        basins.sort()
        print(basins)
        return basins[0]*basins[1]*basins[2]

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")