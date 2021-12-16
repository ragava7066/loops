num=int(input('enter a number : '))
temp = num
rev = 0
while (num>0):
    a=num%10
    rev=rev*10+a
    num=num//10
if (temp == rev): 
    print('the number is palindrome')
else:
    print('the number is not a palindrome')    