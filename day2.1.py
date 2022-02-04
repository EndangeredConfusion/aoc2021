values = [e for e in open("C:/aocinputs/aoc2.txt", "r").read().split("\n")]


horizontal = sum([int(word[-1]) for word in values if word[0] == "f"])
up = sum(int(word[-1]) for word in values if word[0] == "u")
down = sum(int(word[-1]) for word in values if word[0] == "d")

print(abs(horizontal * (up - down)))

