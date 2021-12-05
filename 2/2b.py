with open("./input.dat", "r") as input:
    cmds = input.readlines()
    hpos = 0
    depth = 0
    aim = 0
    for cmd in cmds:
        l = cmd.split(" ")
        if l[0] == "forward":
            x = int(l[1])
            hpos += x
            depth += aim * x
        elif l[0] == "down":
            aim += int(l[1])
        else:
            aim -= int(l[1])
    print(hpos * depth)