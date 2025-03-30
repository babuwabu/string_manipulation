# ask user for input
user = input("Enter your name: ")
suffix = input("Enter the suffix to check: ")
# check if the input ends with the given suffix manually and print output
if len(user) >= len(suffix) and user[-len(suffix):] == suffix:
    print("True")
else:
    print("False")