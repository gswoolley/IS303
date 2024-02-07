"""
Name: Garett Woolley
Description: Write a program that accepts a student’s full name and their final grade average (i.e. 95). 
Then using an IF ELIF ELSE statement, display the letter grade using the following legend
"""

# Prompt for student's full name
FullName = input("Enter student's full name: ")

# Prompt for student's grade average
gradeAverage = int(input("Enter student's grade average "))

letterGrade = ""

if(gradeAverage >= 94 and gradeAverage <= 100):
    letterGrade = "A"
elif(gradeAverage >= 90 and gradeAverage <= 93):
    letterGrade = "A-"
elif(gradeAverage >= 87 and gradeAverage <= 89):
    letterGrade = "B+"
elif(gradeAverage >= 83 and gradeAverage <= 86):
    letterGrade = "B"
elif(gradeAverage >= 80 and gradeAverage <= 82):
    letterGrade = "B-"
else:
    letterGrade = "C"

print(FullName + " had a final average of " + str(gradeAverage) + " which resulted in an " + letterGrade + " for the course. ")