inputf = open("input", "r").read().split("\n")[:-1]

def priority(item):
    return (ord(item.lower()) - 96) + (26 * (1 if (item.isupper()) else 0))

i = 0
k = []
while i < len(inputf):
    for j in inputf[i]:
        if j in inputf[i + 1] and j in inputf[i + 2]:
            k.append(priority(j))
            break
    i += 3

print(sum(k))