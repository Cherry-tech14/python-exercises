first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number > second_number and first_number > third_number:
    print("First number is larger")
elif second_number > first_number and second_number > third_number :
    print("Second number is larger")
elif third_number > first_number and third_number > second_number :
    print("Third number is the largest")    
else:
    print("At least two numbers are equal.")         