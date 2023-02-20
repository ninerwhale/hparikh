string = input("HeLLO woRLD: ")

lowercase_letters = ""
uppercase_letters = ""

# Separate the lowercase and uppercase letters
for char in string:
    if char.islower():
        lowercase_letters += char
    elif char.isupper():
        uppercase_letters += char

# Combine the letters and remove spaces
modified_string = lowercase_letters + uppercase_letters
modified_string = modified_string.replace(" ", "")

print(modified_string)