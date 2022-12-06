inputf = open("input.txt", "r").read()[:-1].split("\n\n")

setup, instructions = inputf[0].split("\n")[:-1], inputf[1].split("\n")

spots = []

for i in range(len(setup)):
    spots.append([])

for i in setup:
    i = i[1:-1].replace("[", "").replace("] ", " ").replace("  ", " ")
    for j in range(len(i)):
        if ord(i[j]) > 64 and ord(i[j]) < 91:
            spots[int(j/2)].append(i[j])

for i in instructions:
    i = i.split(" ")
    for j in range(int(i[1])):
        spots[int(i[5])-1].append(spots[int(i[3])-1].pop())


output = ""

for i in spots:
    output += i.pop()

print(output)