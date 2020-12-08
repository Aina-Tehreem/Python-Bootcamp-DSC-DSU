name=input("enter your name: ")
print("diagonally, it will become:")
for i in range(len(name)):
    for j in range(i):
        print(" ", end="")
    print(name[i])

print("printing reverse diagonal:")
for i in range(len(name)):
    for j in range(len(name)-i):
        print(" ", end="")
    print(name[i])

