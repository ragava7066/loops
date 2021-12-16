num =int(input('enter a number : '))
temp=num
rev=0
while temp!=0:
    last_digit=temp%10
    rev=rev*10+last_digit
    print(last_digit)
    temp=temp//10
print(f'{num} reverse = {rev}')