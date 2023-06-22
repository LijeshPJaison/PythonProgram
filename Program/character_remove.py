def remove_character(string,char):
    return string.replace(char,'')

input_string = input("Enter a string ")
character_to_remove = input("Enter charatcter to remove ")

result = remove_character(input_string,character_to_remove)
print(result)