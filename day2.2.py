values = [e for e in open("C:/aocinputs/aoc2.txt", "r").read().split("\n")]

horizontal = 0
depth = 0
aim = 0

for value in values:
    if value[0] == "d":
        aim += int(value[-1])
    elif value[0] == "u":
        aim -= int(value[-1])
    elif value[0] == "f":
        horizontal += int(value[-1])
        depth += aim * int(value[-1])

print(horizontal * depth)
