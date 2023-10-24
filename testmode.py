import sys
from random import randint

# 1 Marks
def rolldice():
    """
    function: rolldice prints two random numbers between 1 and 6 simulate two dices rolling. 
    The function should also print output of the numbers generated (Eg: 6 and 6) 
    return: int:total (total of two random numbers) 
    """
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print("%s and %s" %(dice1, dice2))
    totalroll = dice1+dice2
    return totalroll

def findwinner(game, players):
    """
    function: This function takes game list (2D list) and the player list as input parameters. Goes through the game and find the player that has the highest score
    Return the winning player name as string. If more than one player winning (eg: same score) return a winner string with all players comma seperated (Eg: John, Kate)
    :param list:game (Game list)
    :param list:players (Players list)
    :return string:winner (Winning players name as string)
    """ 
    # Implement your function here 
    highestscore=0
    winners=[]
    #winnercount=0
    allwinners=''
    x=0
    for x in range (x,len(players)):
        if sum(game[x]) > highestscore:
            highestscore = sum(game[x])
    x=0
    for x in range (x,len(players)):
        if sum(game[x]) == highestscore:
            winners.append(players[x])

    allwinners=', '.join(map(str,winners))
    return allwinners

numberofplayers=""
playernames = []
playerindex = 0
while numberofplayers == "":
    numberofplayers=input("Please enter the number of players: ")
    if numberofplayers.isnumeric():
        numberofplayers = int(numberofplayers)
        if numberofplayers < 1:
            print("Invalid input please try again")
            numberofplayers = ""
        else:
            numberofplayers = int(numberofplayers)
            for playerindex in range(numberofplayers):
                playernames.append(input("Please enter player #" +str(playerindex+1) + " name: "))
    else:
        print("Invalid input please try again")
        numberofplayers = ""
for playerindex in range(numberofplayers):
    print(playernames[playerindex])

gamerounds =""
while gamerounds == "":
    gamerounds = input("Please enter how many rounds the players wish to play: ")
    if gamerounds.isnumeric():
        gamerounds = int(gamerounds)
        if gamerounds < 1:
            print("Invalid input please try again")
            gamerounds = ""
        else:
            gamerounds = int(gamerounds)
    else:
        print("Invalid input please try again")
        gamerounds = ""
print(gamerounds)

#gameset = [[""]*gamerounds]*len(playernames)
game = [[0 for i in range(gamerounds)] for x in range(len(playernames))]
test2d=[[1,1,1],[4,4,4],[3,3,3],[4,4,4]]


#game[0][0]='A'
#game[0][1]='B'
#game[0][2]='C'

#game[1][0]='D'
#game[1][1]='E'
#game[1][2]='F'

#game[2][0]='G'
#game[2][1]='H'
#game[2][2]='I'

#game[3][0]='J'
#game[3][1]='K'
#game[3][2]='L'


gameset=[game,playernames,gamerounds]

print (test2d)

alltest2d=', '.join(map(str,playernames))
print(alltest2d)
print (game)
print (gameset)
x=0
input ("%s! Hit enter once you are ready to roll your dices!" % playernames[x])
dice=rolldice()
print(dice)

print(sum(test2d[x]))

newwinners=findwinner(test2d,playernames)

print(newwinners)

roundnum = 1

roundstring = "End of Round " + str(roundnum)