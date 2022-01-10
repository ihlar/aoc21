import time
from collections import Counter

def first():    
    p1_score = 0
    p2_score = 0
    p1_pos = 6
    p2_pos = 3
    d = 1 
    
    n_throws = 3

    board = [1,2,3,4,5,6,7,8,9,10]
    r = 0
    while p1_score < 1000 and p2_score < 1000:
        for n in range(n_throws):
            p1_pos += d
            d += 1
            if d > 100:
                d = 1
        for n in range(n_throws):
            p2_pos += d
            d += 1
            if d > 100:
                d = 1
        p1_pos %= 10
        p2_pos %= 10
        p1_score += board[p1_pos]
        p2_score += board[p2_pos] if p1_score < 1000 else 0
        r += 6 if p1_score < 1000 else 3
    
    return min(p1_score, p2_score) * r, p1_score, p2_score, r

B = [1,2,3,4,5,6,7,8,9,10]

def steps(step, p, score, scs):
    if score >= 21:
        scs[step] += 1
        return
    step += 1
    p1 = (p+1) % 10
    p2 = (p+2) % 10
    p3 = (p+3) % 10
    steps(step, p1, score + B[p1], scs)
    steps(step, p2, score + B[p2], scs)
    steps(step, p3, score + B[p3], scs)

def second():
    start1 = 3
    start2 = 7
    c1 = Counter()
    c2 = Counter()
    steps(0,3,0, c1)
    steps(0,7,0, c2)
    w1 = 1
    for i in range(max(c1.keys()) + 1):
        wi = c1[i]
        for j in range(i, max(c2.keys()) + 1):
            other = c2[j]
            if other > 0:
                wi *= other if other <= wi else wi
        if wi > 0:
            w1 *= wi 
    print(c1)
    print(c2)
    print(w1)



    return 0

if __name__ == "__main__":
    start = time.time()
    print(f"First: {second()} - elapsed {time.time()-start}")