"""
Name: Garett Woolley
Section: 003
Description: Prompts user for information and returns BMI and BMI Category
"""


#Separate function for printing final statement
def printStatement(firstName, lastName, BMI, BMICategory):
    print(firstName + " " + lastName + "\n" + "has a BMI of " + str(BMI) + " and is " + str(BMICategory))

#Runs main chunk of code
def main():

    #Prompt user for input data
    firstName = input("Please enter first name: ")
    lastName = input("Please enter last name: ")
    heightFeet = input("Please enter first part of height in feet (e.g 5): ")
    heightInches = input("Please enter second part of height in inches (e.g 8): ")
    weight = input("Please enter the current weight pounds: ")

    #Calculate total height in inches
    totalHeight = (int(heightFeet) * 12) + int(heightInches)

    #Calculate BMI using this formula: [weight (lb)] / [total_height (in)]^2 x 703
    BMI = round(int(weight) / (totalHeight**2) * 703, 2)

    #Create BMICategory to store description of weight
    BMICategory = ""

    #Store description of weight in BMICategory
    if(BMI < 18.5):
        BMICategory = "Underweight"
    elif(BMI >= 18.5 or BMI < 25):
        BMICategory = "Normal Weight"
    elif(BMI >= 25 or BMI < 30):
        BMICategory = "Overweight"
    else:
        BMICategory = "Obese"

    #Print output
    printStatement(firstName=firstName, lastName=lastName, BMI=BMI, BMICategory=BMICategory);

main()

