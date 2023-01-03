inputf = list(map(lambda x: list(x), open("input.txt", "r").read().split("\n")))

times = {
    
}

map = inputf.copy()
found = False
import time

letters = ["S"]
for n in range(97,123):
    letters.append(chr(n))
letters.append("E")

starts = []

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            start = [i, j]
        if map[i][j] == "a":
            starts.append([i, j])

t = 0
def printmap():
    print("\n" * 10)

    for i in map:
        s = ""
        for j in i:
            s += j.replace("#", "█")

        print(s)
    time.sleep(0.05)

tosearch = [[start[0], start[1]]]
print(starts)
for z in starts:
    map = inputf.copy()
    t = 0
    tosearch = [[z[0], z[1]]]
    while not found:
        #printmap()
        extends = []
        for cord in reversed(tosearch):

            for n in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    x = cord[0] + n[0]
                    y = cord[1] + n[1]
                    if x >= 0 and y >= 0 and x < len(map) and y < len(map[0]):
                        pos = map[x][y]

                        if pos != "#" and map[cord[0]][cord[1]] != "#" and letters.index(map[cord[0]][cord[1]]) - letters.index(pos) >= -1:
                            if pos == "E":
                                print(t)
                                found = True
                            tosearch.append([x, y])

            tosearch.remove(cord)
            map[cord[0]][cord[1]] = "#"
        t += 1