finput = open("input.txt", "r").read().split("\n")

head = [0, 0]
tail = [0, 0]

msize = 16

nmap = [["." for i in range(msize)] for j in range(msize)]

def printmap():
    for i in reversed(nmap):
        print(" ".join(i))

print(nmap)

locs = set({})
locsl = []

t = 0


for i in finput:
    p = i.split(" ")
    
    for i in range(int(p[1])):
        t += 1

        if p[0] == "U":
            head[1] += 1
        if p[0] == "D":
            head[1] -= 1
        if p[0] == "R":
            head[0] += 1
        if p[0] == "L":
            head[0] -= 1
        
        if (abs(head[0] - tail[0]) > 1) or (abs(head[1] - tail[1]) > 1):
            
            if head[1] > tail[1]:
                tail[1] += 1
            if head[1] < tail[1]:
                tail[1] -= 1
            if head[0] > tail[0]:
                tail[0] += 1
            if head[0] < tail[0]:
                tail[0] -= 1
        
        locs.add(str(tail[0]) + " " + str(tail[1]))
        locsl.append(str(tail[0]) + " " + str(tail[1]))
        print(abs(head[0] - tail[0]) + abs(head[1] - tail[1]))
        nmap[head[1]][head[0]] = "@"
        nmap[tail[1]][tail[0]] = "#"
        printmap()
        print(head, tail, t)
        
print(locs, len(locs))