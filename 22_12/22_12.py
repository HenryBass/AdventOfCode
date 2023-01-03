map = list(map(lambda x: list(x), open("input.txt", "r").read().split("\n")))
found = False
import time

letters = ["S"]
for n in range(97,123):
    letters.append(chr(n))
letters.append("E")

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            start = [i, j]

t = 0
def printmap():
    print("\n" * 50)
    for i in map:
        s = ""
        for j in i:
            s += j.replace("#", "█")

        print(s)
    time.sleep(0.01)

tosearch = [[start[0], start[1]]]

while not found:
    printmap()
    extends = []
    print("\n", t)
    for cord in reversed(tosearch):

        for n in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x = cord[0] + n[0]
                y = cord[1] + n[1]
                if x >= 0 and y >= 0 and x < len(map) and y < len(map[0]):
                    pos = map[x][y]

                    if pos != "#" and map[cord[0]][cord[1]] != "#" and letters.index(map[cord[0]][cord[1]]) - letters.index(pos) >= -1:
                        if pos == "E":
                            found = True
                        tosearch.append([x, y])

        tosearch.remove(cord)
        map[cord[0]][cord[1]] = "#"
    t += 1
    input()

printmap()
print(t)