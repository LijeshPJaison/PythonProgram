str = input('Enter the string: ')

revstr = (str[::-1])

if revstr == str:
    print('Palindrome string')
else:
    print('Not Palindrome string')