input = open("input22_1.txt", 'r').read().split("\n\n")[:-1]
elves = []
for i in range(len(input)):
    elves.append(0)
    for j in input[i].split("\n"):
            elves[i] += int(j)
elves.sort()
print(elves[-1] + elves[-2] + elves[-3])