import random
from datetime import datetime
from tracemalloc import start

maxNum = int(input("Enter max number "))
numGuess = 0
randomNum = random.randrange(0, maxNum)
startTime = datetime.now()
print (randomNum)
while numGuess != randomNum:
    numGuess = int(input("Guess a number "))
    if numGuess > randomNum:
        print("Too high, guess again")
    elif numGuess < randomNum:
        print("Too low, guess again")
    else:
        endTime = datetime.now()
        totalTime = endTime - startTime
        print("You guessed correctly! You took " + str(totalTime.seconds) + " seconds to guess correctly.")

