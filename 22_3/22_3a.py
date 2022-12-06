inputf = open("input", "r").read().split("\n")[:-1]
def finditem(entry):
    s = int(len(entry)/2)
    first, last = entry[:s], entry[s:]
    for i in first:
        if i in last:
            item = i
            break
    return priority(item)

def priority(item):
    return (ord(item.lower()) - 96) + (26 * (1 if (item.isupper()) else 0))

k = sum(list(map(finditem, inputf)))
print(k)