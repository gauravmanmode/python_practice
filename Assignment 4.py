#1
for i in range(1000,2500):
	if i%7==0 and i%5==0:
		print(i)

#2
from random import randrange
x=randrange(1,9)
k=int(input("Enter num 1 to 9 "))
while(k!=x):  
    k=int(input("Enter again "))  
else:
     print("Well guessed")
    
   
#3
for i in range(1,6):
	print('*'*i)
for i in range(4):
	print('*'*(4-i))



#4
sum=0
n=int(input("Enter n  "))
for i in range(n):
    sum=sum+i
    i=i+1
print("sum is",sum)

#5
sum=0
n=int(input("Enter n  "))
for i in range(n):
	sum=sum+(i**2)
	i=i+1
print("sum is",sum)

#6
e=o=0
k=input("Enter sample numbers by , ")
l=k.split(',')
for i in l:
    if int(i)%2==0:
        e=e+1
    else:
        o=o+1
print("Even ",e,"\n Odd ",o)

#7
a=0
b=1
print('0','1',end=',')
for i in range(50):
	f=a+b
	a=b
	b=f
	print(f,end=',')

#8
for i in range(50):
    if i%15==0:
        print("fizzbuzz")
    elif i%5==0:
        print("Fizz")
    elif i%3==0:
        print("buzz") 
    else:
        print(i)

#9
sum=s=t=0
from math import sin,factorial
x=float(input("Calculate sin in radian "))
n=int(input("upto what "))
for i in range(1,n,2):
	s =((-1)**t)*(x**i)/factorial(i)
	t=t+1
	sum=sum+s
print("cal sin is",sum,"also sin from python func is  ",sin(x))


#10
sum=s=t=0
from math import cos,factorial
x=float(input("Calculate cos in radian "))
n=int(input("upto what "))
for i in range(0,n,2):
	s =((-1)**t)*(x**i)/factorial(i)
	t=t+1
	sum=sum+s
print("cal cos is",sum,"also cos from python func is  ",cos(x))
