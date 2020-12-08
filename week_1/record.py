L=[]
D={}
num=[]
sum=0
for i in range(5):
    roll=input("enter roll number: ")
    name=input("enter name: ")
    age=input("enter age: ")
    marks=int(input("enter your marks out of 100: "))
    if(marks>100 or marks<0):
        marks=input(int("enter your marks out of 100: "))
    num.append(marks)
    sum=sum+marks
    D.update({'roll_num':roll,'name':name,'age':age,'marks':marks})

    L.append(D)
print(L)
print("highest marks in class are: ",max(num))
print("lowest marks in class are: ",min(num))
print("average marks of class are: ",sum/5)
