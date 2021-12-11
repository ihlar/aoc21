SIMTIME = 100

def parseinput(input):
    return [[int(c) for c in l.strip('\n')] for l in input]

def increase_or_flash(x, y, grid):
    if x < 0 or y < 0 or y > len(grid) - 1 or x > len(grid[y]) - 1:
        return 0
    e = grid[y][x]
    if e == 0:
        return 0
    if e < 9:
        grid[y][x] += 1
        return 0
    else: # e == 9
        grid[y][x] = 0
        return (
            1 + 
            increase_or_flash(x-1, y, grid)   +
            increase_or_flash(x+1, y, grid)   +
            increase_or_flash(x, y-1, grid)   +
            increase_or_flash(x, y+1, grid)   +
            increase_or_flash(x-1, y-1, grid) +
            increase_or_flash(x-1, y+1, grid) +
            increase_or_flash(x+1, y-1, grid) +
            increase_or_flash(x+1, y+1, grid)        
        )

def first(inpath):
    with open(inpath, 'r') as indata:
        grid = parseinput(indata.readlines())
        count = 0
        for _ in range(SIMTIME):
            flashes = []
            for y, row in enumerate(grid):
                for x, e in enumerate(row):
                    grid[y][x] += 1 if e < 9 else 0
                    if e == 9:
                        flashes.append((x,y))
            for x, y in flashes:
                count += increase_or_flash(x, y, grid)
        return count

def second(inpath):
    with open(inpath, 'r') as indata:
        grid = parseinput(indata.readlines())
        all = len(grid) * len(grid[0])
        count = 0
        step = 0
        while count != all:
            count = 0
            flashes = []
            for y, row in enumerate(grid):
                for x, e in enumerate(row):
                    grid[y][x] += 1 if e < 9 else 0
                    if e == 9:
                        flashes.append((x,y))
            for x, y in flashes:
                count += increase_or_flash(x, y, grid)
            step += 1
        return step

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")