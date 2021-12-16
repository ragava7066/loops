string = 'abcd....xyz'
# in is the membership operator
print('a' in string) # simple use of membership operator
print('this is operatop of previous exp')

# simple linear search prog
string = input('enter your string -> ')
char = input('enter the char to be searched in the given string -> ')

if char in string:
    print('"{}" is present in the given "{}'.format(char,string))
else:
    print(char, 'is not present in the given string')    