inputf = list(map(lambda x: x.split("\n"), open("input.txt", "r").read().split("\n$ ")))

dirs = []

class Dir:
    def __init__(self, parent, children, name):
        self.parent = parent
        self.children = children
        self.name = name
        self.type = "Dir"
        self.size = 0
    def find(self, x):
        for i in self.children:
            if (i.name == x): return i 

class File:
    def __init__(self, parent, size, name):
        self.parent = parent
        self.size = size
        self.name = name
        self.type = "File"

ptr = Dir(None, [], "/")

for i in inputf:
    p = i[0].split(" ")
    if i[0] == "ls":
        for j in i[1:]:
            if j.split(" ")[0] == "dir":
                ptr.children.append(Dir(ptr, [], j.split(" ")[1]))
            else:
                ptr.children.append(File(ptr, int(j.split(" ")[0]), j.split(" ")[1]))
    elif p[0] == "cd":
        if p[1] == "..":
            ptr = ptr.parent
        else:
            ptr = ptr.find(p[1])

while ptr.name != "/":
    ptr = ptr.parent

def getsize(ptr):
    netsize = 0
    for i in ptr.children:
        if i.type == "File":
            netsize += i.size
        else:
            netsize += getsize(i)

    dirs.append(netsize)
    return netsize

size = getsize(ptr)

needed = (30000000 - (70000000 - size))

smf = []

for i in sorted(dirs):
    if i > needed:
        smf.append(i)

print(sorted(smf)[0])

while True:
    cmd = input("$ ")
    cmds = cmd.split(" ")
    if cmd == "ls":
        for i in ptr.children:
            if i.type == "File":
                print(i.name, "--", i.size)
            else:
                print("/" + i.name)
    elif cmds[0] == "cd":
        if cmds[1] == "..":
            ptr = ptr.parent
        else:
            ptr = ptr.find(cmds[1])
    print("\n")