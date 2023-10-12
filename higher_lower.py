import random
#from replit import clear
import HLgame_data

import os

def clear():
  os.system('cls')

#get number of elements
listOfData = HLgame_data.data
numOfElements = len(HLgame_data.data)


#functions to get data
def getData(randEl):
    data1 = HLgame_data.data[randEl]
    return data1


def printInfo(data):
    print(
        f"{data['name']}, {data['description']}, from {data['description']}.\n"
    )


playerScore = 0
randEl = random.randint(0, numOfElements - 1)
data1 = getData(randEl)

randEl = random.randint(0, numOfElements - 1)
data2 = getData(randEl)

gameOver = False
while gameOver == False:

    print(f"Compare A:", end=" ")
    printInfo(data1)
    print(f"\nAgainst B:", end=" ")
    printInfo(data2)

    score1 = data1["follower_count"]
    score2 = data2["follower_count"]
    choice = input("Who has more followers? Type 'A' or 'B':")

    if score1 > score2:
        moreFollowers = "A"
    elif score1 < score2:
        moreFollowers = "B"

    clear()
    if choice == moreFollowers:
        data1 = data2
        randEl = random.randint(0, numOfElements - 1)
        data2 = getData(randEl)
        playerScore += 1
        print(f"You are right. Current score is {playerScore}.")
    else:
        print(f"Sorry, that's wrong. Your final score is {playerScore}")
        gameOver = True

    print("\n")
