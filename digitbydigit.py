num =int(input('enter a number : '))
temp=num
while temp!=0:
    last_digit=temp%10
    print(last_digit)
    temp=temp//10