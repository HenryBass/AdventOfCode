inputf = list(map(lambda x: x.replace("  ", "").split("\n"), open("input.txt", "r").read().split("\n\n")))

monkeys = []

modval = 1

class Monkey():
    def __init__(self, id, items, op, mod, passif, passelse):
        self.id = id
        self.items = items
        self.op = op
        self.mod = mod
        self.passif = passif
        self.passelse = passelse
        self.count = 0

    def inspect(self):
        remove = []

        for j in range(len(self.items)):
            self.count += 1
            p = self.items[j]
            self.items[j] = int(eval(i.op)) % modval
            p = p % self.mod
            if int(eval(i.op)) % self.mod == 0:
                monkeys[self.passif].items.append(self.items[j])
            else:
                monkeys[self.passelse].items.append(self.items[j])
            
            remove.append(self.items[j])

        for k in remove:
            self.items.remove(k)

def parseint(txt):
    sint = ""
    for i in txt:
        if i.isdigit():
            sint += i
    return(int(sint))

for i in inputf:
    monkeys.append(Monkey(parseint(i[0]),
    (list(map(int, i[1].replace("Starting items: ", "").split(", ")))),
    i[2].replace("Operation: ", "").replace("new = ", "").replace("old", "p"),
    parseint(i[3]),
    parseint(i[4]),
    parseint(i[5])))
    modval *= parseint(i[3])

for h in range(0, 10_000):
    for i in monkeys:
        i.inspect()

activity = []

for i in monkeys:
    activity.append(i.count)

print(sorted(activity)[-1] * sorted(activity)[-2])