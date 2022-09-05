## Python Functions module first problem

def  find(n):
   su=0
   for i in range(1,n):
      if n%i==0:
        su=su+i
   if su==n:
      return 0
   elif su < n:
      return -1
   elif su > n:
      return 1

x=int(input())
find(x)
if find(x)==0:
   print("%d    is perfect number"%x)
elif find(x)==-1:
   print(" %d  is deficient  number"%x)
elif find(x)==1:
   print("%d  is abundant  number"%x)

