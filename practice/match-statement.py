'''
day = "Friday"

match day:
    case "Monday":
        print("Start of the week")

    case "Friday":

        print("Weekend is near")

    case _:
        print("Regular day")


choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("Rice")
    case 2:
        print("Beans")
    case 3:
        print("Yam")
    case _:
        print("Invalid choice") 
 

command = input("Enter command: ")

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("stopping...")
    case "exit":
        print("Goodbye!...")
    case _:
        print("Unknown command...")  
'''

number = int(input("Enter a number (1-4): "))

match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")

    case _:
        print("Invalid day")                



