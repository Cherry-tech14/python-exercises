username = input("Enter a Username: ")

if username == "admin":
    password = input("Enter password: ")
    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Unknown User")        
    



