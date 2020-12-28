import os

pair=[]
directory=input("enter the  folder path: ")
directory=directory+'/'
files=os.listdir(directory)
print("before sorting:\n",files)

for i in files:
    location=os.path.join(directory,i)
    size=os.path.getsize(location)
    pair.append((size,i))

print()
pair.sort(reverse=True)
#for j in pair:
print("After sorting:\n",pair)

