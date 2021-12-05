def find(num, color, seen, match, path):
    if not seen and (color == match or color in path):
        return (num, color, True)
    return (num, color, False)

def count(rule, rule_map):
    n, col = rule
    print(f"{n}, {col}")
    if col == None:
        return 1
    else: 
        return n, rule_map[col] 

def check_rule(n, rule):
    _,c,_ = rule[0] 
    if c == None:
        return 0
    else:
        return n

def count_bags_impl(rules, rule_map):
    if rules == None:
        return 1
    rule, *rest = rules
    n, col, _ = rule
    print(f"{n}, {col}")
    if col == None:
        return 1
    else:
        s1 = check_rule(n, rule_map[col])
        s2 =  n * count_bags_impl(rule_map.get(col), rule_map)
        s3 = count_bags_impl(rest, rule_map) if rest != [] else 0
        return s1 + s2 + s3

def count_bags(color, rule_map):
    return count_bags_impl(rule_map[color], rule_map)

with open("./input.dat", "r") as input:
    cmap = {}
    data = input.readlines()
    for rule in data:
        split = rule.split("contain")
        color = split[0].split('bags')[0].strip()
        contents = []
        for r in split[1].split(','):
            elts = r.strip().split(' ')
            num = elts[0]
            if num == "no":
                contents.append((0, None, False))
            else:
                col = " ".join(elts[1:-1])
                contents.append((int(num), col, False))
        cmap[color] = contents
    
    scol = 'shiny gold'
    res = set()
    rest = list(cmap.keys())
    found = True
    while found:
        found = False
        for col in rest:
            rule = cmap[col]
            cmap[col] = [find(n, c, f, scol, res) for n, c, f in rule]
            for n,c,f in cmap[col]:
                if f:
                    res.add(col)
                    found = True
                    try:
                        rest.remove(col)
                    except:
                        pass
    print(len(res))

    print(count_bags("shiny gold", cmap))


