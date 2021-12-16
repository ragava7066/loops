num = int(input('enter a number : '))
res = 0
div = 1

while div < num :
    if num%div == 0:
        res += div
    div+=1

if res == num:
    print(f'{num} is perfect')
else:
    print(f'{num} is not a perfect')    