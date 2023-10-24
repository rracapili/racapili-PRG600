"""
Firstname: Ronald
Lastname: Capili
Username: radcapili
StudentID: 152344222
Email: radcapili@myseneca.ca
"""

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
# 1 Marks 
def getplayers(): 
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
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
    return playernames

# 1 Marks 
def getrounds(): 
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """
    # Implement your function here
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
    return gamerounds


# 4 Marks 
def setgame():
    """
    function: This functions use the getplayers() function and getrounds() function to get player list and round count
    Using the above values setup a two dimensional (2D) list called game. The game list will have lists elements for each round and player 
    Eg: [[score1_1, score1_2, score1_3], [score2_1, score2_2, score2_3], [score3_1, score3_2, score3_3]]
    In this above example score1_1 is player1's score for round 1. Score3_1 is player 3's score for round 1. Score 2_3 is player 2's score for round3 
    Hence each list element in game will represent a player
    Each score (int) element in the nested list element will represent a round for that player
    Finally return a gameset list which has the game list, players list, and number of rounds
    return: list:gameset (Eg gameset returned will be a list [game, players, roundcount]. In the gameset list game is lit, players is list and roundcount is integer)
    """ 
    players = getplayers() # Calling getplayers and getting player list 
    roundcount = getrounds() # Calling getrounds and getting roundcount 
    # Implement your function here 
    game = [["" for i in range(roundcount)] for x in range(len(players))]
    gameset = [game,players,roundcount]
    return gameset

# 1 Marks 
def asktoroll(player): 
    """
    function: This function takes player name and asks player to hit enter to roll the dice. 
    When user hit enter calls the rolldice function and returns a score 
    :param string:player (player input is string called player name)
    :return int:score (Returns score from roll dice)
    """
    # Implement your function here 
    input ("%s! Hit enter once you are ready to roll your dices!" % player)
    dice=rolldice()
    return dice

# 2 Marks 
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
    for x in range (x,len(players)):
        if sum(game[x]) > highestscore:
            highestscore = sum(game[x])
    for x in range (x,len(players)):
        if sum(game[x]) == highestscore:
            winners.append(players[x])

    allwinners=', '.join(map(str,winners))


if __name__ == "__main__":
    """
    Main code block to run the code
    """
    