# ask user for input
user = input("Enter text: ")
char_find = input("Enter the character to find: ")
# find the last occurrence manually
index = -1
for i in range(len(user) - 1, -1, -1):
    if user[i] == char_find:
        index = i
        break
# print the output
if index != -1:
    print(f"The character '{char_find}' last appears at index {index}.")
else:
    print(f"The character '{char_find}' is not found in the string.")