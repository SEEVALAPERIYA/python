a=int(input())
b=int(input())
t=max(a,b)
while(true):
     if(t%a==0 and t%b==0):
       break
     t=t+1
print(t)
