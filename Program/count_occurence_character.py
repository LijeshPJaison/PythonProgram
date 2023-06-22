string = "abcdeaa"
char = input("Enter character: ")

i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1
print("total number of", char, "is", count)