n=int(input())
m=int(input())
a=0
b=0
for i in range(1,n):
    if n%i==0:
        a=a+i
for j in range(1,m):
    if m%i==0:
        b=b+i
if n==b or m==a:
    print("Amicable")
else:
    print("Not Amicable")