print(max(map(lambda x:sum(map(int,x.split("\n"))),open("i",'r').read().split("\n\n")[:-1])))
print(sum(sorted(map(lambda x:sum(map(int,x.split("\n"))),open("i",'r').read().split("\n\n")[:-1]))[-3:]))