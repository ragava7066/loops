num=int(input('enter a number : '))
count_of_factors=0
div=1

while div<=num:
    if num%div==0:
        count_of_factors+=1
    div+=1
if count_of_factors == 2:
    print('the number is prime : ')
else :
    print('the number is not prime : ')