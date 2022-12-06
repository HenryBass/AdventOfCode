inputf = open("input.txt", "r").read()[:-1].split("\n\n")

setup, instructions = inputf[0].split("\n")[:-1], inputf[1].split("\n")

spots = []

for i in range(len(setup)+1):
    spots.append([])

for i in setup:
    i = i[1:-1].replace("[", "").replace("] ", " ").replace("  ", " ")
    for j in range(len(i)):
        if ord(i[j]) > 64 and ord(i[j]) < 91:
            print(int(j/2), i[j])
            spots[int(j/2)].append(i[j])

for n in range(len(spots)):
    spots[n].reverse()

for i in instructions:
    i = i.split(" ")
    print(i[1], i[3], i[5])
    picked = []

    for j in range(int(i[1])):
        picked.append(spots[int(i[3])-1].pop())

    picked.reverse()
    spots[int(i[5])-1].extend(picked)


output = ""

for i in spots:
    output += i.pop()

print(output)