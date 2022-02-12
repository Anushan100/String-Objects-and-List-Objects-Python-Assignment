a=5
for i in range(a):
    for j in range(i+1):
        print(".",end="")
    print("")
for x in range(a,0,-1):
    y=x
    for y in range(y-1):
        print(".",end="")
    print("")