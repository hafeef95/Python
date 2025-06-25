name=["karnan","nepolian","bagath singh","pritviraj"]
for name1 in name:
    print(name1)
for name1 in name:
    if name1[0]=='k':
        print(name1)
for name1 in name:
    if len(name1)>7:
        print(name1)
name=["karnan","nepolian","bagath singh","pritviraj"]
upper_words=[]
for name1 in name:
    upper_words.append(name1.upper())
print(upper_words)
list1=[]
list2=[]
for v in range(1,51):
    if v%3==0:
        list1.append(v)
    else:
        list2.append(v)
    
list1
list2

no1=[]
no2=[]
for m in range(1,61):
    if m%4==0:
        no1.append(m)
    else:
        no2.append(m)
        
no1     
no2

list3=[]
list4=[]
for k in range(1,91):
    if k%5==0:
        list3.append(k)
    else:
        list4.append(k)
list3
list4

no3=[]
no4=[]
for u in range(1,81):
    if u%8==0:
        no3.append(u)
    else:
        no4.append(u)
no3
no4

"*"*5

for t in range(1,6):
    print("*"*t)




for row in range(0,6,+1):
    for col in range(1,row):
        print(col,end="")
    print("")
#rigth down mirrer star pettarn

for row in range(1,8,+1):
    for col in range(1,row,+1):
        print("  ",end=" ")
    for col in range(row,8,+1):
        print("* ",end=" ")
    print("")
    
#equlatrial traingl pettarn
for row in range(8,1,-1):
    for col in range(1,row,+1):
        print(" ",end=" ")
    for col in range(row,8):
        print(" * ",end=" ")
    print("")  
        
#2 pyramid of stars  
         
for row in range(8,1,-1):
    for col in range(1,row,-1):
        print(" ",end=" ")
    for col in range(row,8,+1):
        print("*",end=" ")
    print("")
else:
    
 for row in range(1,8,+1):
    for col in range(8,row,+1):
        print(" ",end=" ")
    for col in range(row,8,+1):
        print("*",end=" ")
    print("")
#pattern to display lettar of the word

word="python"
for g in range(len(word),0,-1):
    print(word[:g])     
#pyramid of horizontal no tabels 
for row in range(1,11):
    for col in range(1,row+1):
        print(col*row,end=" ")
    print("")
#ingrising lettar
a=65
for row in range(1,7):
    
    for col in range(row):
        print(chr(a),end=" ")
        a=a+1
    print("")
    a=a+1

list8=[1,3.5,"pradeep",True,12-23j,56,345,"szfsdf"]
for value in range(0,8):
    print(list8[value])


for value in range(7,-1,-1):
    print(list8[value])


value=7
while value>-1:
    print(list8[value])
    value=value-1
#1-100 print in value
value=1
while value<=100:
    print(value)
    value+=1

list4=[2,7,18,39,56,27,89]
sum=0
for value in list4:
    sum=sum+value
    
sum=0
for index in range(0,len(list4)):
    sum=sum+list4[index]
print(sum)

#sum
total=0
value=0
while value<len(list4):
    total+=list4[value]
    value+=1    
print("sum:",total)
 #multiple   
list8=[1,2,3,4]
total=1
value=0
while value<len(list8):
    total*=list8[value]
    value+=1    
print("total:",total)
#horizontal no table
for row in range(1,11):
    for col in range(1,row+1):
        print(col*row,end=" ")
    print("")

row=1
while row<11:
    col=1
    while col<row+1:
        print(col*row,end=" ")
        col=col+1
    print()
    row=row+1


for row in range(0,6):
    for col in range(1,row):
        print(col,end="")
    print("")
 
row=0
while row<6:
    col=1
    while col<row:
        print(col,end="")
        col=col+1
    print()
    row=row+1
    
word="python"
for g in range(len(word),0,-1):
    print(word[:g])     
    

    
    
    
  
  
for row in range(0,6):
    for col in range(row,0,-1):
        print(col,end="")
    print("")
        
row=0
while row<6:
    col=row
    while col>0:
        print(col,end="")
        col=col-1
    print()
    row=row+1
    
for row in range(1,6):
    for col in range(6,row,-1):
        print(" ",end="")
    for col in range(1,row+1):
        print(col,end="")
    print("")
row=1
while row<6:
    col=6
    while col>row:
        print(" ",end="")
        col=col-1   
    col1=1
    while col1<row+1:
        print(col1,end="")
        col1=col1+1
    print()
    row=row+1
    
for a in range(1,10):
    for col in range(10,a,-1):
        print(a,end="")
    print("")

row=1
while row<6:
    col=6
    while col>row:
        print(row,end="")
        col=col-1
    print()
    row=row+1
    
for row in range(6,1,-1):
    for col in range(1,row,+1):
        print(col,end="")
    print("") 

row=6
while row>1:
    col=1
    while col<row:
        print(col,end="")
        col=col+1
    print()
    row=row-1
    
for row in range(1,6):
    for col in range(row,0,-1):
        print(col,end="")
    print(" ") 
row=1
while row<6:
    col=row
    while col>0:
        print(col,end="")
        col=col-1
    print()
    row=row+1
    
no3=[]
for u in range(1,10):
    no3.append(u)
#q1  
list1=[]
u=1
while u<10:
    list1.append(input())
    u=u+1
list1 

#q2
list1=[]
u=input("enter value or 0 for quit")
while u!='0':
    list1.append(u)
    u=input("enter value or 0 for quit")
    
list1
#Q3


list3=[]
u=int(input("enter value or 0 for quit"))
value=0
while u!=0:
        value=value+u
        list3.append(u)
        u=int(input("enter value or 0 for quit"))
list3
value
#q4
list1=[]
list2=[]
u=1
while u<=100:
    if (u%5==0)&(u%7==0):
        list1.append(u)
    u=u+1
list1
k=1
while k<=100:
    if k%7==0:
        list2.append(k)
    k=k+1
   
list1
list2


def func():
    list1=[]
    u=1
    while u<=100:
        if (u%5==0)&(u%7==0):
            list1.append(u)
        u=u+1
    print(list1)
func()

#q5
def func1():
    list3=[]
    u=int(input("enter value or 0 for quit"))
    value=0
    while u!=0:
        value=value+u
        list3.append(u)
        u=int(input("enter value or 0 for quit"))
    print(list3)
func1()
#q6
def func2():
    list1=[]
    u=1
    while u<10:
        list1.append(input(""))
        u=u+1
    return list1
d=func2()
#q7
def func3():
    g=input("enter a value")
    result=0
    for value in g:
        result=result+int(value)
    return result
d=func3()
def func4(g):
    result=0
    for value in str(g):
        result=result+int(value)
    return result
func4(24567)
#q8
def func4(k):
    list4=[] 
    for value in k:
        result=0 
        for value1 in str(value):
            result=result+int(value1)
        list4.append(result)
    return list4
func4([99876,987654,9787,6544])

def func5(*k):
    print(k)
    list4=[] 
    for value in k:
        result=0 
        for value1 in str(value):
            result=result+int(value1)
        list4.append(result)
    return list4
    
func5(99876,2345676,7890,4567)

def func6(*args):
    list6=[]
    for value2 in args:
        list6.append(value2.upper())
    return list6
func6("hafeef","pradeep","anjal")
def func7(*a):
    list8=[] 
    for value in a:
        result=0 
        for value1 in str(value):
            result=result+int(value1)
            for value2 in str(value1):
                result=result+int(value2)
        list8.append(result)
        return list8
func7()