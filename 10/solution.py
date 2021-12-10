from collections import deque

SYNTAX = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

CORRUPTED = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

COMPLETE = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

def first(inpath):
    with open(inpath, 'r') as indata:
        lines = [l.strip('\n') for l in indata.readlines()]
        score = 0
        for line in lines:
            expected = deque()
            for c in line:
                if c in SYNTAX:
                    expected.append(c)
                elif c != SYNTAX[expected.pop()]:
                    score += CORRUPTED[c]
                    break
        return score

def second(inpath):
    with open(inpath, 'r') as indata:
        lines = [l.strip('\n') for l in indata.readlines()]
        completed = []
        for line in lines:
            score = 0
            expected = deque()
            corrupted = False
            for c in line:
                if c in SYNTAX:
                    expected.appendleft(c)
                elif c != SYNTAX[expected.popleft()]: 
                    corrupted = True
                    break
            if not corrupted:
                for start in expected:
                    score *= 5
                    score += COMPLETE[SYNTAX[start]]
                completed.append(score)
        return sorted(completed)[len(completed)//2]

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")