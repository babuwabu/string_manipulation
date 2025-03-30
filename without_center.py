# ask user for input
user = input("Enter your name: ")
width = int(input("Enter the total width: "))

# check left and right padding
padding = max(0, width - len(user))
left_padding = padding // 2
right_padding = padding - left_padding

total_space = " " * left_padding + user + " " * right_padding

# print the output
print(f'"{total_space}"')