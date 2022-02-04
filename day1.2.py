def sum_three(index: int, ints: list[int]) -> int | None:
    try:
        return ints[index] + ints[index + 1] + ints[index + 2]
    except IndexError:
        print("index error")
        return None


values = [int(e) for e in open("C:/aocinputs/aoc1.txt", "r").readlines()]
counter = 0

for i in range(len(values)):
    if sum_three(i + 1, values) is not None:
        if sum_three(i, values) < sum_three(i + 1, values) and sum_three(i + 1, values) is not None:
            counter += 1
    else:
        break

print(counter)
