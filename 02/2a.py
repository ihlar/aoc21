with open("./input.dat", "r") as input:
    cmds = input.readlines()
    hpos = 0
    depth = 0
    for cmd in cmds:
        l = cmd.split(" ")
        if l[0] == "forward":
            hpos += int(l[1])
        elif l[0] == "down":
            depth += int(l[1])
        else:
            depth -= int(l[1])
    print(hpos * depth)