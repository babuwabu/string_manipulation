# ask user for input
name = input("Enter your name: ")
# manually convert the input to lowercase
lower_case = ""
for char in name:
    if "A" <= char <= "Z":
        lower_case += chr(ord(char) + 32)  # Convert uppercase to lowercase
    else:
        lower_case += char  # Keep other characters unchanged
# print output
print(lower_case)