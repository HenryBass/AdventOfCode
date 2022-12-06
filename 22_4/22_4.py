inputf = open("input", "r").read().split("\n")[:-1]

def anysubset(x):
    x = x.split(",")
    x0 = set(range(int(x[0].split("-")[0]), int(x[0].split("-")[1]) + 1))
    x1 = set(range(int(x[1].split("-")[0]), int(x[1].split("-")[1]) + 1))
    print(x0, x1)
    return 1 if x1 & x0 else 0
    
print(sum(list(map(anysubset, inputf))))