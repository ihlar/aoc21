RESPAWNRATE = 7
INITIALAGE  = 8

def first(inpath): #SLOOOW
    with open(inpath , 'r') as input:
        SIMTIME = 80
        fishs = [int(t) for t in input.read().strip('\n').split(',')]
        for _ in range(0, SIMTIME):
            nnew = 0
            for i in range(0,len(fishs)):
                if fishs[i] == 0:
                    nnew +=1
                fishs[i] = (fishs[i]-1) % RESPAWNRATE if fishs[i] < RESPAWNRATE else fishs[i]-1
            for n in range(0, nnew):
                fishs.append(INITIALAGE)

        return len(fishs)
        
def second(inpath):
    with open(inpath , 'r') as input:
        SIMTIME = 256
        fishs = [int(t) for t in input.read().strip('\n').split(',')]
        simdata = [0]*(INITIALAGE+1)
        for f in fishs:     
            simdata[f] += 1 
        for _ in range(0, SIMTIME):
            first = simdata[0]
            for t in range(0, RESPAWNRATE):
                simdata[t] = simdata[t+1] if t+1 < RESPAWNRATE else first
            for t in range(RESPAWNRATE, INITIALAGE+1):
                simdata[t-1] += simdata[t]
                simdata[t] = 0
            simdata[INITIALAGE] = first
        return sum(simdata)

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")