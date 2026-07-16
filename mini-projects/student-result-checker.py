name = input("Enter your student name: ")
score = int(input("Enter your score: "))

if (score < 0) or (score > 100):
    print("Invalid Score")
else:
    print("Student:", name)
if score >= 70:
    print("Grade: A")
    print("Status: Pass")

elif score >= 60:
    print("Grade: B")
    print("Status: Pass")
elif score >= 50:
    print("Grade: C")
    print("Status: Pass")
elif score >= 45:
    print("Grade: D")
    print("Status: Pass")
elif score >= 40:
    print("Grade: E") 
    print("Status: Pass")  
else:
    print("Grade: Fail") 
    print("Status: Fail")    


