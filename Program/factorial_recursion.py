def factorail(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorail(n-1)

num = 5
print("Factorail of", num,"is",factorail(num))