def first(input_file):
    with open(input_file, "r") as input:
        data = input.read().splitlines()
        gamma = ""
        epsilon = ""
        for bit in range(0, len(data[0])):
            count0 = 0
            count1 = 0
            for num in data:
                if num[bit] == '0':
                    count0 += 1
                else:
                    count1 += 1
            gamma += '0' if count0 > count1 else '1'
            epsilon += '0' if count0 < count1 else '1'
        return int(gamma, 2) * int(epsilon, 2)

def count(pos, nums):
    count0 = 0
    count1 = 0
    for num in nums:
        if num[pos] == '0':
            count0 += 1
        else:
            count1 += 1    
    return (count0, count1)

def second(input_file):
    with open(input_file, "r") as input:
        data = input.read().splitlines()
        oxygenrating = data.copy()
        co2scrub = data.copy()
        for bit in range(0, len(data[0])):
            o0, o1 = count(bit, oxygenrating)
            c0, c1 = count(bit, co2scrub)
            oxybit = '1' if o1 >= o0 else '0'
            co2bit = '0' if c0 <= c1 else '1'
            oxygenrating = list(filter(lambda num: num[bit] == oxybit or len(oxygenrating) == 1, oxygenrating))
            co2scrub = list(filter(lambda num: num[bit] == co2bit or len(co2scrub) == 1, co2scrub))
        return int(oxygenrating[0], 2) * int(co2scrub[0], 2)

if __name__ == "__main__":
    input = "./input.dat"
    print(f"First: {first(input)}\nSecond: {second(input)}")