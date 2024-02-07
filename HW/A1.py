"""
Name: Garett Woolley
Section: 003
Description: This program prompts the user 
             to enter the cost of a an average 4 bedroom 
             house in Bentonville Arkansas and displays 
             the cost in Taiwanese New Dollars
"""

def dollarsToTaiwanese():
    try:
        print('\n');
        houseCost = float(input("Enter the cost of a an average 4 bedroom house in Bentonville Arkansas: "))
    except ValueError:
        print("Must be a number!")
    else:
        print('\n')
        taiwaneseAmount = "{:.2f}".format(round(houseCost * 31.54, 2))
        print("The cost of a $" + str(houseCost) + " 4 bedroom home in Arkansas in Taiwanese dollars is" + '\n' + "$" + taiwaneseAmount + '\n');

dollarsToTaiwanese()



