import time

def shoot(xvel, yvel, left, right, bottom, top):
    x, y = 0, 0
    hit = False
    maxy = 0
    while x <= right and y >= bottom:
        x += xvel
        y += yvel
        if bottom <= y <= top and left <= x <= right:
            hit = True
        if y > maxy:
            maxy = y
        xvel -= 1 if xvel > 0 else 0
        yvel -= 1
    return hit, maxy

def first():
    area = ((60, 94), (-171, -136))
    maxy = 0
    (left, right), (bottom, top) = area 
    count = 0
    mx = 0
    while mx * (mx+1) // 2 < left:
        mx+=1
    for yvel in range(bottom, abs(bottom) + 1):
        for xvel in range(mx, right + 1):
            hit, my = shoot(xvel, yvel, left, right, bottom, top)
            if hit:
                count += 1 
                if my > maxy:
                    maxy = my
    return count, maxy 

if __name__ == "__main__":
    start = time.time()
    print(f"First: {first()} - elapsed {time.time()-start}")