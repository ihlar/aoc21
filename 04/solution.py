
def wraprange(start, wrap):
    for i in range(1, wrap):
        yield (start + i) % wrap

def bingo(draw, board):
    found = None
    bingo = False
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            v, _ = board[y][x]
            if v == draw:
                board[y][x] = (v, True)
                found = (x, y)
    if found != None:
        bingo = True
        x, y = found
        for yy in wraprange(y, len(board)):
            _, b = board[yy][x]
            bingo = b
            if not bingo:
                break
        if not bingo:
            bingo = True
            for xx in wraprange(x, len(board)):
                _, b = board[y][xx]
                bingo = b
                if not bingo:
                    break
    return bingo

def bingoval(draw, board):
    us = 0
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            v, b = board[y][x]
            us += v if not b else 0
    return us * draw

def first(inpath):
    with open(inpath, "r") as input:
        draws = [int(x) for x in input.readline().strip('/n').split(',')]
        boarddata = input.readlines()
        boards = []
        board = []
        for l in boarddata:
            if l == '\n':
                if board != []:
                    boards.append(board)
                board = []
            else:
                board.append([(int(v), False) for v in l.strip().replace('  ', ' ').strip('\n').split(' ')])
        boards.append(board)
        for draw in draws:
            for b in boards:
                if bingo(draw, b):
                    return bingoval(draw, b)
    return 0

def second(inpath):
    with open(inpath, "r") as input:
        wins = []
        draws = [int(x) for x in input.readline().strip('/n').split(',')]
        boarddata = input.readlines()
        boards = []
        board = []
        for l in boarddata:
            if l == '\n':
                if board != []:
                    boards.append(board)
                board = []
            else:
                board.append([(int(v), False) for v in l.strip().replace('  ', ' ').strip('\n').split(' ')])
        boards.append(board)
        for draw in draws:
            for b in boards:
                if bingo(draw, b):
                    addwin = True
                    for w, _ in wins:
                        if b == w:
                            addwin = False
                    if addwin:
                        wins.append((b, draw))
                        if len(wins) == len(boards):    
                            return bingoval(draw, b) 
    return 0

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")