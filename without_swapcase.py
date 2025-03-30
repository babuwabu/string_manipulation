# ask user for input
user = input("Enter your name: ")
# reverse the casing of each character
swapped_case = ""
for char in user:
    if "a" <= char <= "z":
        swapped_case += chr(ord(char) - 32)  # convert lowercase to uppercase
    elif "A" <= char <= "Z":
        swapped_case += chr(ord(char) + 32)  # convert uppercase to lowercase
    else:
        swapped_case += char  # unchanged
# print output
print(swapped_case)
