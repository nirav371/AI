import time
t = time.time()
a = int(input("a= "))
b = int(input("b= "))
d = int(input("d= "))
x=0
y=0
if(b>a):
    a, b = b, a

while(x+y!=d):
    print(f"{x} {y}")
    if(x==0):
        x=a
        continue
    if(y!=b):
        temp = min(x,b-y)
        x-= temp
        y+= temp
        continue
    if(y==b):
        y=0
        continue
print(f"{x} {y}")
end = time.time()-t
print("/n Time Taken: ", end)


 



        
    