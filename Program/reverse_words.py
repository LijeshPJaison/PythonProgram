
str = "welcome to python program"

words = str.split(" ")
words = words[-1::-1]

outputstr =' '.join(words)
print(outputstr)
