factoraial =1
num = int(input('Enter a number: '))

if num<0:
    print('Factorial value must be greater than zero.')
elif num == 0:
    print('The factorail of 0 is 1')
else:
    for i in range (1,num+1):
        factoraial = factoraial * i
    print(factoraial)
    