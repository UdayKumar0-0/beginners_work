x=int(input('x: '))
y=int(input('y: '))

for n in range(x,y+1):
    count=0
    for i in range(2,n):
        if n%i == 0:
            count = count+1
    if count==0:
        print(n)
    else:
        pass
