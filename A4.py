"""
Name: Garett Woolley
Section: 003
Description: python program that asks about a home women’s soccer team, how many games they played in a season, a
nd then displays the scores of each game as well as the overall record of the home team for the season.
"""

import random

def main():
    gamesWon = 0
    homeTeeam = input("Enter name of home team: ")
    gamesPlayed = int(input("Enter number of games home team plays in season: "))
    for count in range(0, gamesPlayed):
        awayTeam = input("Enter name of away team: ")
        homeScore = random.randrange(10)

        # Initialize awayScore with the same value as homeScore to enter the loop
        awayScore = homeScore

        # Continue generating awayScore until it is different from homeScore
        while homeScore == awayScore:
            awayScore = random.randrange(5)

        print(f"{homeTeeam}'s score: {homeScore} {awayTeam}'s score: {awayScore}")
        if(homeScore > awayScore):
            gamesWon += 1

    #Calculate games lost
    gamesLost = gamesPlayed - gamesWon
    
    #Print record
    print(f"{homeTeeam}'s record: {gamesWon} - {gamesLost}")

    winPercentage = gamesWon / gamesPlayed
    print(winPercentage)
    if(winPercentage >= .75):
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif(winPercentage >= .50):
        print("You had a good season")
    else:
        print("Your team needs to practice!")

main()
        
    

        


