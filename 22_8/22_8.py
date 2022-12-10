finput = list(map(lambda x: list(map(int, list(x))), open("input.txt", "r").read().split("\n")))

count = (pow(len(finput[0]), 2) - pow(len(finput) - 2, 2))

scores = []

for x in range(len(finput[0:-1]))[1:]:
    for y in range(len(finput[x][0:-1]))[1:]:
        k = finput[x][y]
        dirs = [list(reversed(finput[x][:y])),
        finput[x][y:][1:],
        list(reversed([i[y] for i in finput[:x]])),
        list(([i[y] for i in finput[1+x:]]))]

        score = 1

        for i in range(len(dirs)):
            for j in range(len(dirs[i])):
                if dirs[i][j] >= k:
                    print(j+1, dirs[i], k)
                    score = score * (j+1)
                    break
                elif j == len(dirs[i]) - 1:
                    print(j+1, dirs[i])
                    score = score * (j+1)

        print(score)
        scores.append(score)
        mdirs = list(map(max, dirs))

        for i in mdirs:
            if i >= k:
                0
            else:
                count += 1
                break

        #print(total, max(total), finput[x][y])
        #count += (0 if max(total) <= finput[x][y] else 1)

print("max:", max(scores))
#print(count)