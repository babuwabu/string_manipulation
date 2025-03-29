# ask user's input to add spaces in the beginning
inputs = str(input("Enter your input and add spaces in the beginning: "))
# remove spaces without using lstrip
inputs = inputs.replace(" ", "")
# print output
print(inputs)
