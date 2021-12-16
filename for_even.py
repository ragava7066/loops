start=int(input('enter starting number : '))
stop=int(input('enter ending number : '))
step =1
for var in range(start,stop,step):
    if var%2==0:
        print(var)