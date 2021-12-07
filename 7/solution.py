import sys

def calcfuel(pos1, pos2):
    steps = abs(pos1-pos2)
    return steps * (1 + steps) // 2

def first(inpath):
    with open(inpath, 'r') as indata:
        positions = [int(x) for x in indata.read().split(',')]
        maxp = 0
        for p in positions:
            maxp = p if p > maxp else maxp
        total_fuel = sys.maxsize
        for pos in range(maxp+1):
            fuel = 0
            for pos2 in positions:
                fuel += abs(pos2-pos)
            if fuel < total_fuel:
                total_fuel = fuel
        return total_fuel

def second(inpath):
    with open(inpath, 'r') as indata:
        positions = [int(x) for x in indata.read().split(',')]
        maxp = 0
        for p in positions:
            maxp = p if p > maxp else maxp
        total_fuel = sys.maxsize
        for pos in range(0, maxp+1):
            fuel = 0
            for pos2 in positions:
                fuel += calcfuel(pos, pos2)
            if fuel < total_fuel:
                total_fuel = fuel
        return total_fuel

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")