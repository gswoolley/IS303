"""
Name: Garett Woolley
Section: 003
Description: Prompts user for information and returns IS Application GPA, as well as chances to get into the program as a message
"""

def main():
    # I know we haven't learned dictionaries/maps yet, but I figured this was the most efficient way to do 
    # this rather than a bunch of if-else statements
    grade_to_gpa = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.4,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.4,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.4,
    'D': 1.0,
    'D-': 0.7,
    'F': 0
}
    # Get input and weight each input
    ACC_200 = .05 * grade_to_gpa[input("Enter ACC 200 Grade (e.g., A, B+, C-): ")];
    IS_201 = .3 * grade_to_gpa[input("Enter IS 201 Grade (e.g., A, B+, C-): ")]
    IS_303 = .3 * grade_to_gpa[input("Enter IS 303 Grade (e.g., A, B+, C-): ")]
    LAST_30_GPA = .18 * float(input("Enter Last 30 Credits GPA: "))
    OVERALL_GPA = .12 * float(input("Enter Overall GPA: "))
    ESSAY_SCORE = .05 * int(input("Essay score between 0 and 4: "))

    # Sum inputs and round them
    APP_GPA = round(sum([ACC_200, IS_201, IS_303, LAST_30_GPA, OVERALL_GPA, ESSAY_SCORE]), 3)

    MESSAGE = ""

    # Logic for display message
    if (APP_GPA >= 3.8):
        MESSAGE = "Chances are very good"
    elif (APP_GPA < 3.8 and APP_GPA >= 3.5):
        MESSAGE = "Chances are good"
    elif (APP_GPA < 3.5 and APP_GPA >= 3.2):
        MESSAGE = "Chances are so-so"
    else:
        MESSAGE = "You might want to retake IS 201 and/or IS 303"

    # Final print statement
    print("\nTotal Application GPA is " + str(APP_GPA) + "\n" + MESSAGE + "\n")


main()