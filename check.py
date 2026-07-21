'''x=int(input("enter the number 1"))
y=int(input("enter the number 2"))
if x>y:
    print("x is bigger")
else:
    print("y is bigger")'''
'''x=int(input("enter the number 1"))
y=int(input("enter the number 2"))
z=int(input("enter the number 3"))
if(x>y and x>z):
    print("x is bigger number")
elif(y>z):
    print("y is bigger number")
else:
    print("z is bigger number")'''
'''a, b, c = 10, 20, 30
minimum = a if a < b and a < c else (b if b < c else c)
print(minimum)'''
'''x=1
while x<=5:
    print(x)
    x+=1
print("end")'''
'''x=10
while(x>=10 and x<=20):
    print(x)
    x+=2
print("end")'''
'''x=[10,20,30,"python"]
for i in x:
    print(i)'''
'''x="python"
for ch in x:
    print(ch)'''
'''item_cost=[10,20,30]
gst =2
for x in item_cost:
    print(x+gst)'''
'''for x in range(1,5):
    print(x)'''
'''item=[1,2,3,4,5]

x=0
for i in item:
    x+=i
print(x)'''
'''rows=range(4,0,-1)
for x in rows:
    for star in range(1,x+1):
        print('*',end='')
    print()
'''
'''x=range(10,1,-3)
for i in x:
    print(i,end=" ")'''
'''group=[1,2,3,4]
search=int(input("enter the element in search:-"))
for element in group:
    if search == element:
        print("element found in group")
        break
else:
    print("element not found in group")'''
'''total=0
while True:
    num=int(input("enter the number"))
    if num==0:
        break
    total +=num
print("total:-",total)'''
'''def process(a,b):
    c=a+b
    d=a-b
    return c,d
y=process(40,40)
print(y)'''
'''def m1():
    print("this function is returning nothing ")
m1()
x=m1()
print(x)'''
'''def add():
    print("we have assigned function to the variable")
    sum = add
    sum()
'''
'''def display(x):
    print("this is display function")
def message():
    print("this is message function")
display(message())
'''
'''def first():
    print("this the outer function")
    def second():
            print("this is the second function")
    second()
first()
'''
'''def cart(item,price=20):
    print(item,"cost is:-",price)
cart(item="bangles")
cart(item="handbag",price=10000)
cart(price=1200,item="bangles")'''
'''def total_cost(x,*y):
    #using * this becomes a collection
    sum=0
    for i in y:
        sum+=i
    print(x+sum)
total_cost(100,200)
total_cost(110,226,311)
total_cost(100,200,311)
total_cost(11)'''
'''def m1(**x):
    def print_kwargs(**kwargs):
        print(kwargs)
    print_kwargs(id=1,name="jack",qualification="MBA")
def m1(**x):
    for k,v in x.items():
        print(k,"=",v)
m1(id=100,name="subh")'''
'''a=11
b=12
def m():
    a=10
    print("a from function m():-",a)
    print(globals()["a"])
    print("b from function m():-",b)
def n():
    print("a from function n():-",a)
    print("b from function n():-",b)
m()
n()
'''
'''def fac(n):
    if n==0:
        result = 1
    else:
        result=n*fac(n-1)
    return result
x=fac(5)
print("factorial is :-",x)'''
'''s=lambda a:a*a
x=s(4)
print(x)'''
'''items_cost=[199,188,11,1200,130,77]
gt_thou=filter(lambda x: 100<=x<200,items_cost)
x=list(gt_thou)
print("eligible for discount :-",x)
'''
'''from functools import reduce
each_it_costs=[111,222,333,444]
total_cost=reduce(lambda x,y: x if x>y else y,each_it_costs)
print(total_cost)'''
'''def m():
    yield'mahesh'
    yield'suresh'
g=m()
print(g)
print(type(g))
for y in g:
    print(y)'''
'''def m(x,y):
    while x<=y:
        yield x
        x+=1
g=m(5,10)
for y in g:
    print(y)'''
'''from add import sum,prod
sum(4,10)
prod(4,10)'''
'''import add
add.sum(10,10)
add.prod(10,10)'''
'''
import add as a
print(a.sum(10,10))
print(a.prod(10,10))
'''
'''x=10
y=20
def f1():
    print("hello")
print(dir('add'))
'''
'''x=0
while(x<len(n)):
    print(n[x],end=" ")
    x+=1

print(" while loop ended")
for i in range(0,len(n)):
    print(n[i],end=" ")
    i+=1'''
'''names=["mohan","prasad","ramesh","mohan",10,20,True,None]
names.append("suresh")'''
'''s=range(1,20,3)
m=[x for x in s if x%5==0]
print(m)'''
'''name=("rajat",)
print(name)
print(type(name))'''
'''p=[10,20,30,40,50,60,]
x=sorted(t,reverse=True)
print(max(x))
print(min(x))'''
'''z=(10,20,30,40,50,60,)
a,b,c,d,e,f=10,20,30,40,50,60
x=a,b,c,d
p=[100,"suresh",196227]
roll,name,sal=p
t=(x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)'''
'''d={
    1:"ramesh",
    2:"arjun",
    3:"neel"
}
if 2 in d:
    print(d[2])
else:
    print("NOT FOUND")'''
'''d={}
n=int(input("enter the number of the employee"))
i=1
while i<=n:
    name=input("enter name:-")
    salary=input("enter the salary :-")
    d[name]=salary
    i+=1
for x in d:
    print("the name is",x,"with salary is ",d[x])
'''
'''
print(d)
for k in d.keys():
    print(k)
for k in d.values():
    print(k)
    '''
'''
d2=d.copy()
print(d2)
print(id(d))
print(id(d2))

'''
'''d={
    1:"ramesh",
    2:"arjun",
    3:"neel"
}
s={a:a*a for a in range(1,6)}
print(s)'''
'''s=set(range(5))
print(type(s))
print(s)'''
'''s=set()
l=[40,50,60,10]
#s.add(10,20,30)#type error
s.update(range(1,10,2),range(0,10,2))
print(s)'''
'''s={x*x for x in range(5)}
print(s)'''
'''vowels=('a','e','i','o','u')
fSet=frozenset(vowels)
print(fSet)
print(type(fSet))
'''
'''print('one')
print('two')
try:
    print(10/0)
except ZeroDivisionError as z:
    print("exception passed:",z)
print('four')
print('five')'''
'''try:
    x=int(input("enter the number:-"))
    y=int(input("enter the number:-"))
    print(x/y)
except ZeroDivisionError as e:
    print("invalid input",e)'''
'''try:
    print("outer block")
    try:
        print("inner try block")
        print(10/0)
    except:
        print("inner except block")
    else:
        print("inner else block")
    finally:
        print("finally block")
except:
    print("outer block")
finally:
    print("outer finally block")'''
'''try:
    x=int(input("enter the number between +ve integer"))
    if x<0:
        raise ValueError(x)
except ValueError as e:
    print("you provided {}.please provide interger values only".format(e))
'''
'''f=open("abc.txt",'w')
print("file name:",f.name)
print("file mode:",f.mode)
print()'''
'''f=open("abc.txt",'a')
f.write("welcome\n")
f.write("to\n")
f.write("python world\n")
print("data written to the file successfully")
f.close()'''
'''f=open("abc.txt",'r')
data=f.read()
print(data)
f.close()'''
'''f=open("abc.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())'''
'''data="python language is excellent"
f=open("abc.txt","w")
f.write(data)
with open("abc.txt","r+")as f:
    text=f.read()
    print(text)
    print("the current position is :-",f.tell())
    f.seek(24)
    print("the current positon:-",f.tell())
    f.write(" britania biscuit")
    f.seek(0)
    text=f.read()
    print("data after modification:-")
    print(text)'''
'''import os,sys
fname=input("enter the file name:-")
if os.path.isfile(fname):
    print("file exits:",fname)
    f=open(fname,"r")
else:
    print("file does not exist:",fname)
    sys.exit(0)
print("the content of the file is :-")'''
import csv
with open("emp.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["emp no","emp name","emp sal","emp addr"])
    n=int(input("enter the number of the employes"))
    for i in range(n):
        eno=input("enter employe number:-")
        ename=input("enter name")
        esal=input("enter the salary")
        eaddr=input("enter addres")
        w.writerow([eno,ename,esal,eaddr,])
print("total employess data written to csv file succesfully")