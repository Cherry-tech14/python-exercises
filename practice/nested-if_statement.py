'''
age = 20

if age >= 18:
    print("You are an adult.")

if age >= 21:
    print("You can enter the VIP section.")


username = input("Username: ")
password = input("Password: ")

if username == "Mariam":
    if password == "Python123":
        print("Login successful.")
'''

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")

    if age >= 60:
        print("Senior Citizen")
    else:
        print("Working Age")
else:
    print("Minor")