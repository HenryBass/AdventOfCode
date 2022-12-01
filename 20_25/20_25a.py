input = [9033205, 9281649]

def transform(subj, loop):
    val = 1
    for _ in range(loop):
        val *= subj
        val = val % 20201227
    return val

# Given result, need to find loop size

def findloopsize(public):
    i = 0
    while True:
        t = transform(7, i)
        print(i, t)
        if t == public:
            return i
        i += 1

def findloopsizeadv(public):
    #public = transform(7, x)
    public = val % 20201227

loop1 = findloopsize(input[0])
loop2 = findloopsize(input[1])
print(loop1, loop2)


result1 = transform(input[0], loop2)
result2 = transform(input[1], loop1)

if result1 == result2:
    print("Succesfully found, key:", result1)