finput = open("input.txt", "r").read().split("\n")

knots = []

msize = 32

startx = 16
starty = 16

nmap = [["." for i in range(msize)] for j in range(msize)]

def printmap():
    for i in ((nmap)):
        print(" ".join((i)))

nmap[startx][starty] = "s"

locs = set({})
locsl = []

class Knot:
    def __init__(self, parent, cords):
        self.parent = parent
        self.cords = cords
    def follow(self):
        if (abs(self.parent.cords[0] - self.cords[0]) > 1) or (abs(self.parent.cords[1] - self.cords[1]) > 1):
            if self.parent.cords[1] > self.cords[1]:
                self.cords[1] += 1
            if self.parent.cords[1] < self.cords[1]:
                self.cords[1] -= 1
            if self.parent.cords[0] > self.cords[0]:
                self.cords[0] += 1
            if self.parent.cords[0] < self.cords[0]:
                self.cords[0] -= 1

t = 0

head = Knot(None, [startx, starty])

for i in range(9):
    if i == 0:
        knots.append(Knot(head, [startx, starty]))
    else:
        knots.append(Knot(knots[i-1], [startx, starty]))



for i in finput:
    p = i.split(" ")
    
    for i in range(int(p[1])):
        t += 1

        if p[0] == "U":
            head.cords[1] += 1
        if p[0] == "D":
            head.cords[1] -= 1
        if p[0] == "R":
            head.cords[0] += 1
        if p[0] == "L":
            head.cords[0] -= 1
        
        for i in knots:
            i.follow()
        
        print(knots[-1].cords, t)
        locs.add(str(knots[-1].cords[0]) + " " + str(knots[-1].cords[1]))
        #nmap[knots[-1].cords[0]][knots[-1].cords[1]] = "#"
        #nmap[knots[0].cords[0]][knots[0].cords[1]] = "@"
        #printmap()
        
print(len(locs))