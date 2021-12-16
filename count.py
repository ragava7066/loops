num=int(input('enter a number : '))
temp=num
count = 0
while temp!=0:
    count+=1
    temp = temp//10
print(f'{num} has {count} digits')    