insts = list(map(lambda x: x.split(" "), open("input.txt", "r").read().split("\n")))

X = 1
i = 0
t = 0

sum = 0
skipnext = True

image = [["." for i in range(40)] for j in range(6)]

while i < len(insts):
    t += 1

    if skipnext == False:
        if insts[i][0] == "addx":
            X += int(insts[i][1])
            i += 1
            skipnext = True
        else:
            i += 1
    else:
        skipnext = False

    x = (t % 40)
    y = int(t / 40)

    if abs(X - x) < 2:
        image[y][x] = "#"
        print(X, x)

print("\n".join(list(map(lambda x: "".join(x), image))), "\n")