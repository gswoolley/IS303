import random

num1 = 0
num2 = 1

maxNum = int(input("Enter max number for range "))

while num1 != num2:
    num1 = random.randrange(0, maxNum)
    num2 = random.randrange(0 , maxNum)

print(num1, num2)
