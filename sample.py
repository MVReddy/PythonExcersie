# Check given string is palindrome or not

s = input("Enter a string: ")
if s[::-1] == s:
    print("Palindrome")
else:
    print("Not palindrome")
