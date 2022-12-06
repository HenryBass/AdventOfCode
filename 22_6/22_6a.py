inputf = open("input", "r").read()
for i in range(14, len(inputf)):
    if len(set(inputf[i-14:i])) == len(inputf[i-14:i]):
        print(i)
        break