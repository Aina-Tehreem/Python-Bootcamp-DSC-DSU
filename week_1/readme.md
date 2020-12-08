# DSC-DSU | Python Bootcamp 2020 | Week 1

QUESTION NO.1 Define a function to print a string diagonally.


For this question's condition I set the range to the length of whatever the input string we will get and then nested another for loop in which will run according to the outer for loop. the outer for loop prints string character meanwhile the inner forloop prints spaces

for i in range(len(name)):
    for j in range(i):
        print(" ", end="")
    print(name[i])
    
To reverse the diagonal I simply changed the range value in inner loop to (length - i) so for the first time it will print 4-4=0 spaces, for second run it will be 4-3=1 space and so on.   
for i in range(len(name)):
    for j in range(len(name)-i):
        print(" ", end="")
    print(name[i])
  
  
QUESTION NO.2 Create a program to take as input 5 student records in the following format:
**roll_num** | **name** | **age** | **marks**(out of 100)
And then output the records in a tabular form with class average, class highest and class lowest at end in the following format.
Use dictionaries (list of dictionaries in exact)
Insert atleast 5 records
Input must be user-given
(Optional) validate the user input, i.e marks aren't greater 100 and other such validations you think there might be    


L=[]              *I took list L for the record and list num for marks. Dictionary D is for the records that we will input. Each dictionary is equal to one record.
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
    sum=sum+marks                                               *we are appending marks and the whole record (including marks) separately for the ease of calculating max. min                                                                  and average of class marks 
    D.update({'roll_num':roll,'name':name,'age':age,'marks':marks})

    L.append(D)
print(L)
print("highest marks in class are: ",max(num))                     * function max and min is used to find the highest and lowest marks of the class.
print("lowest marks in class are: ",min(num))                      
print("average marks of class are: ",sum/5)                         * dividing the sum by 5 which is the total number of records, we get average.


QUESTION NO.3 A function that will print lyrics of given song with 1 second delay between each line.


After importing time and writing the song with escape sequence \n , I used splitlines to split each line of the song and then with the range set to number of verses I started to print the lines with one sec delay with the help of time.sleep(sec)

line=song.splitlines()
for i in range(len(line)):
    print(line[i])
    time.sleep(1)
