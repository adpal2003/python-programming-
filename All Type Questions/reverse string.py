# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
firstname = input("What is your last name?:")
lastname = input("What is your last?")
print(firstname[::-1] + " " + lastname[::-1])