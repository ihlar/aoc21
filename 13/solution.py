import time

def parseinput(indata):
    maxy = 0
    maxx = 0
    g = []
    folds = []
    for line in indata:
        if line.startswith('fold'):
            axis, value = line.strip('\n').split("fold along ")[-1].split('=')
            folds.append((axis, int(value)))
        elif line != '\n':
            # print(line)
            x, y = line.strip('\n').split(',')
            x = int(x)
            y = int(y)
            maxx = max(x, maxx)
            maxy = max(y, maxy)
            g.append((x, y))
    grid = []
    for _ in range(maxy+1):
        grid.append(['.'] * (maxx + 1))
    for x, y in g:
        grid[y][x] = '#'    
    return (grid, folds)

def foldgrid(lx, ly, axis, fold, grid):
    if axis == 'y':
        for y in range(ly-fold, ly):
            fy = fold - (y-fold)
            for x in range(lx):
                e = grid[y][x]
                if e == "#":
                    grid[fy][x] = e
        ly = fold 
    else:
        for y in range(ly):
            for x in range(lx - fold, lx):
                fx = fold - (x-fold)
                e = grid[y][x]
                if e == "#":
                    grid[y][fx] = e
        lx = fold
    return (lx, ly)

def first(inpath):
    with open(inpath, 'r') as indata:
        grid, folds = parseinput(indata)
        ly = len(grid)
        lx = len(grid[0])
        count = 0
        for i, (axis, fold) in enumerate(folds):
            lx, ly = foldgrid(lx, ly, axis, fold, grid)
            if i == 0:
                for y in range(ly):
                    for x in range(lx):
                        if grid[y][x] == '#':
                            count += 1
        for y in range(ly):
                for x in range(lx):
                    print(grid[y][x], end="")
                print("")
        return count

def second(inpath):
    with open(inpath, 'r') as indata:
        return 0

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")