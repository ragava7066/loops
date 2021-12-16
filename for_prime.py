num=int(input('enter a number : '))
count_of_factors=0
for div in range(1, num+1):
    if num%div==0:
        count_of_factors+=1
if count_of_factors == 2:
    print('the number is prime : ')
else :
    print('the number is not prime : ')