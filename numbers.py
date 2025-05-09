#nivens/harshads
n=int(input())
temp=n
sum=0
while n>0:
    d=n%10
    sum+=d
    n=n//10
if temp%sum==0:
    print("yes")
else:
    print("no")
output:
123
no
152
yes
--------------------------------------------------------
#automorphic
n=int(input())
temp=n
sq=n**2
l=len(str(n))
d=sq%10**l
if temp==d:
    print("yes")
else:
    print("no")

output:
 25
yes
---------------------------------
#automorphic upto given range
n=int(input())
for i in range(1,n+1):
    temp=i
    sq=i**2
    l=len(str(i))
    d=sq%10**l
    if i==d:
        print(i)
output:
50
1
5
6
25
---------------------------------------
#adams number
n=int(input())
sq=n**2
rsq=int(str(sq)[::-1])
n1=int(str(n)[::-1])
sq1=n1**2
if rsq==sq1:
    print("yes")
else:
    print("no")
output:
 3
yes
 25
no
-----------------------------------------------
#magic number
n=int(input())
visit=set()
while n!=1 and n not in visit:
    visit.add(n)
    sum=0
    while n>0:
        d=n%10
        sum+=d
        n//=10
    n=sum
if n==1:
    print("yes")
else:
    print("no")
output:
3
no
19
yes
------------------------------------------------
