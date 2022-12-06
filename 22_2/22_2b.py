replacements = {"A":0,"B":1,"C":2,"X":0,"Y":3,"Z":6}
input = list(map(lambda x: x.split(" "),open("input", "r").read().split("\n")))

input = list(map(lambda x: [replacements.get(x[0]), replacements.get(x[1])], input))

score = 0

for i in input:
    score += i[1]
    if i[1] == 0:
        score += ((i[0] - 1) % 3) + 1
    if i[1] == 3:
        score += i[0] + 1
    if i[1] == 6:
        score += ((i[0] + 1) % 3) + 1


print(score)