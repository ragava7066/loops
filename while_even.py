start=int(input('enter starting number : '))
stop=int(input('enter ending number : '))
step =2

while start<stop:
    if start%2==0:
        print(start)
    start=start+step
