1.
i=0
while i<6:
	print((5-i)*' ','* '*i)
	i+=1
i=3
while i>0:
	print(' '*(5-i),'* ' *i)
	i-=1	

2.
from math import factorial
n=int(input("enter number "))
for i in range(1,n):
    for j in range(i):
        k=factorial(i)/(factorial(i-j)*factorial(j))
        print(int(k),end=',')
    print('1\n')

3.
for i in range(100,400):
    k=str(i)
    l=0
    for j in k:
        if int(j)%2!=0:
            l=1
            break
    if l==0:
        print(k)
       
4.
g=0
n=int(input("enter number "))
for i in range(1,n+1):
    k=n%i
    if (k==0):
        g=g+i
if (g==n):
    print(n," is perfect ")

5.
n=int(input("enter number "))
for i in range(1,n+1):
    k=0
    for j in range(2,i):
        if i%j==0:
            k=1
            break
    if k==0:
        print(i)

6.
news=s=0
n=int(input("enter n "))
for i in range(1,n+1):
    s=i*(i+1)/2
    news=news+s
print(int(news)," is sum ")

7.
sum=s=0
from math import exp,factorial
x=float(input("Calculate exp "))
n=int(input("upto what "))
for i in range(0,n):
	s =(x**i)/factorial(i)
	sum=sum+s
print("cal exp is",sum,"also exp func is  ",exp(x))

8.
a,d,n=(int(x) for x in input("enter a,d,n of ap  ").split(','))
s=(n/2)*(2*a+(n-1)*d)
print("sum of ap  ",s)

9.
a,r,n=(int(x) for x in input("enter a,r,n of gp  ").split(','))
s=a*((r**n)-1)/(r-1)
print("sum of gp  ",s)

10.
n=int(input("enter range "))
for i in range(n):
	k=str(i)
	if (k==k[::-1]):
print(k," is palindrome  ")
	



