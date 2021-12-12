import time
START = 'start'
END = 'end'

def build_graph(lines):
    graph = {}
    for line in lines:
        cave1, cave2 = line.strip('\n').split('-')
        if cave1 not in graph:
            graph[cave1] = [cave2]
        else:
            graph[cave1].append(cave2)
        if cave2 not in graph:
            graph[cave2] = [cave1]
        else:
            graph[cave2].append(cave1)
    return graph

def find_paths(start, path, graph):
    p = path.copy()
    if start == END:
        return 1 
    elif start.islower():
        if start in path:
            return 0
        p.append(start)
    npaths = 0
    for edge in graph[start]:
        npaths += find_paths(edge, p, graph)
    return npaths

def fp2(start, path, pair_in_path, graph):
    if start == END:
        return 1
    if start == START and len(path) > 0:
        return 0
    p = path
    if start.islower():
        if start in path:
            if pair_in_path:
                return 0 
            else:
                pair_in_path = True
        p = path.copy()
        p.append(start)
    npaths = 0
    for edge in graph[start]:
        npaths += fp2(edge, p, pair_in_path, graph)
    return npaths

def first(inpath):
    with open(inpath, 'r') as indata:
        graph = build_graph(indata.readlines())
        return find_paths('start', [], graph)

def second(inpath):
    with open(inpath, 'r') as indata:
        graph = build_graph(indata.readlines())
        return fp2('start', [], False, graph)

if __name__ == "__main__":
    input = "./input.dat"
    start = time.time()
    print(f"First: {first(input)} - elapsed {time.time()-start}")
    start = time.time()
    print(f"Second: {second(input)} - elapsed {time.time()-start}")