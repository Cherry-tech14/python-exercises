'''
count = 1

while count <= 5:
    print(count)
    count += 1
    

number = 3

while number > 0:
    print(number)
    number -= 1
    

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access Granted")   


for i in range(3):
    password = input("Enter password: ")
    

while True:
    password = input("Enter password: ")

    if password == "python123":
        break

        print("Access Granted")
        

count = 1

while count <= 5:
    print(count)

    break
    
count = 1

while count <= 5:
    print(count)

    if count == 3:
        break

    count += 1
    

for i in range(1, 6):
    if i == 3:
        continue

    print(i)
    

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)


age = 18

if age >= 18:
    pass
print("program finished")
'''

for i in range(5):
    if i == 2:
        pass
    print(i)

    
