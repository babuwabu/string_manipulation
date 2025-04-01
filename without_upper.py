# ask user for input
user = input("Enter your name: ")
# manually convert the input to uppercase
upper_case = ""

for char in user:
    if "a" <= char <= "z":
        upper_case += chr(ord(char) - 32)  # convert lowercase to uppercase
    else:
        upper_case += char  # unchanged char
# print the output
print(upper_case)