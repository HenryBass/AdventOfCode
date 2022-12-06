replacements = {"A":0,"B":1,"C":2,"X":0,"Y":1,"Z":2}
input = list(map(lambda x: x.split(" "),open("input", "r").read().split("\n")))

input = list(map(lambda x: [replacements.get(x[0]), replacements.get(x[1])], input))

score = 0

for i in input:
    score += i[1] + 1
    if i[1] == (i[0] + 1) % 3:
        score += 6
    elif i[0] == i[1]:
        score += 3


print(score)