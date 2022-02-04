values = [int(e) for e in open("C:/aocinputs/aoc1.txt", "r").readlines()]

counter = 0
for i in range(len(values) - 1):
    if values[i + 1] > values[i]:
        counter += 1

print(counter)
