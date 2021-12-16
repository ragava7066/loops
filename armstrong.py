num=int(input('enter a number : '))
temp = num
sum = 0
while (num>0):
    a=num%10
    sum+=a**3
    num=num//10
if (temp == sum): 
    print('the number is an armstrong')
else:
    print('the number is not an armstrong')    