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
    dice1 = randint(1,6)            #Roll Dice 1 and produce a random number between 1 and 6
    dice2 = randint(1,6)            #Roll Dice 1 and produce a random number between 1 and 6
    print("%s and %s" %(dice1, dice2))          #Print the 2 dice number rolls
    totalroll = dice1+dice2                     #Add the 2 dice rolls
    return totalroll                            #Return total dice rolls
# 1 Marks 
def getplayers(): 
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
    numberofplayers=""                  #Initialize variable for numberofplayers
    playernames = []                    #Initialize list for playernames
    playerindex = 0                     #Initialize list index for referencing playernames list
    while numberofplayers == "":        #While loop to catch invalid number of players input
        numberofplayers=input("Please enter the number of players: ")
        if numberofplayers.isnumeric():                 #Catch if input is not numeric
            numberofplayers = int(numberofplayers)
            if numberofplayers < 1:                     #Catch if input is less than 1
                print("Invalid input please try again")
                numberofplayers = ""
            else:                                       #If number of players input is valid, proceed to save player names in list
                numberofplayers = int(numberofplayers)  #Convert input to integer
                for playerindex in range(numberofplayers):              #Save playernames in list
                    playernames.append(input("Please enter player #" +str(playerindex+1) + " name: "))
        else:
            print("Invalid input please try again")
            numberofplayers = ""
    return playernames              #Return playernames in a list

# 1 Marks 
def getrounds(): 
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """
    # Implement your function here
    gamerounds =""              #Initialize game rounds to blank
    while gamerounds == "":     #While loop to catch invalud number of game rounds
        gamerounds = input("Please enter how many rounds the players wish to play: ")
        if gamerounds.isnumeric():              #Catch if input is not numeric
            gamerounds = int(gamerounds)
            if gamerounds < 1:                  #Catch if input is less than 1
                print("Invalid input please try again")
                gamerounds = ""
            else:
                gamerounds = int(gamerounds)       #If input is valid, save it as number of rounds
        else:
            print("Invalid input please try again")
            gamerounds = ""
    return gamerounds                               #return number of rounds


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
    game = [[0 for i in range(roundcount)] for x in range(len(players))]
    #Initialize the games 2D list
    #Used for loop to create a list with the same number of elements as the number of rounds and initialized contents to 0 - eg: 2 rounds will have [0, 0]
    #Used another for loop to multiply that list ([0, 0]) into the number of players - eg: 3 players for a 2 round game will have [[0,0],[0,0],[0,0]]
    gameset = [game,players,roundcount]             #Return gameset as a nested list with the game, players, and roundcount in the list
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
    input ("%s! Hit enter once you are ready to roll your dices!" % player) #Takes player name as parameter and displays the name and prompts user to roll the dice
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
    highestscore=0              #Initialize highestscore to 0 for comparison later
    winners=[]                  #Initialize a list variable to accommodate for multiple winners
    #winnercount=0
    allwinners=''               #Initialize a string with all the winner names
    x=0
    for x in range (x,len(players)):            #Go through all the player's total scores and find the highest score
        if sum(game[x]) > highestscore:
            highestscore = sum(game[x])         #Save highestscore for later reference
    x=0
    for x in range (x,len(players)):            #With the highestscore of the game determined, find the player that has the highest score
        if sum(game[x]) == highestscore:    #Go through the scores of each player and save the player's name in the winners list if score matches the highest score
            winners.append(players[x])

    allwinners=','.join(map(str,winners))   #Join all winners names in one string variable
    return allwinners                       #Return string variable with all winners names


# 5 Marks 
def rungame():
    """
    function: This function runs the game 
    It sets the game first using setgame() function. It gets the game, players and roundcount from setgame
    It prints the header and Round 1 begining score card first with inital scores set to 0
    It then asks use to roll dices using asktoroll function for all rounds and players 
    When the game finish it prompts for continuation and if chose to continue run the game again otherwise terminate.
    """

    # The next 5 lines are to get you started 
    # Implement the rest of the code 
    gamestatus = 1          #Counter used to repeat or terminate the game - initialized to 1 or run game at first run
    while gamestatus == 1:
        gameset = setgame() # Calling the setgame to get game info 
        game = gameset[0] # Getting game list 
        players = gameset[1] # Getting playerlist 
        roundcount = gameset[2] # Getting roundcount 
        printgame(game, players, 0, roundcount) # Calling printgame to print the first score card. 
        roundnum = 0            #Initialize current round number to 0 for the first round
        for x in range(roundcount):     #Used for loop to loop through the number of rounds
            for y in range(len(players)):       #Used for loop to loop through the number of players and prompt them to roll the dice per round
                game[y][x]=asktoroll(players[y])
            roundnum += 1                       #Increment round number at the end of each round
            printgame(game, players, roundnum, roundcount)      #Print end of round score

        winningnames = findwinner(game,players)                 #Find the winning players
        print("Congratulations %s! You are our WINNER!" % winningnames)         #Display winning players names
        print("Would you like to play another game?")                           #Prompt user for a new game or to terminate game
        print("[1] Yes")
        print("[2] No")
        while gamestatus == 1:              #Used to catch invalid input for game restart or quit prompt
            gamestatus = input("Your choice: ")
            if gamestatus.isnumeric():          #Catch if non-numeric
                gamestatus = int(gamestatus)
                if gamestatus == 1:             #Catch if user wants to run the game again
                    break
                elif gamestatus == 2:           #Catch if user wants to quit
                    print("Thank you and see you later!")
                    break
                else:
                    print("Invalid input please try again")     #Catch any other input as invalid input
                    gamestatus = 1
            else:
                print("Invalid input please try again")
                gamestatus = 1

# 5 Marks
def printgame(game, players, roundnum, roundcount): 
    """
    This function takes in game list, players list, round number (aka which round is active), totalround count as input parameters
    The function prints left aligned pretty table of the game with Rounds in columns and players in rows 
    Sample Output:
    ****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Appla     8         7         4         19        
    Applb     11        5         8         24        
    Applc     9         3         5         17        
    Appld     8         8         7         23        
    ****************************************************
    The Stars and the Round title (End of Round) are calculated and aligned as number of rounds changes. 
    This function does not return anything
    """
    #game = [[4,2,7],[4,5,5],[3,5,5],[11,8,5]]
    topborder = ''              #String variable for top asterisk border
    bottomborder = ''           #String variable for bottom asterisk border
    if roundnum == 0:           #Catch if it is the beginning of the game - Print Round 1 if it's the beginning of the game
        roundstring = "Round 1" #Variable that will be combined later with other strings to print top and bottom header
        borderplus = 9
    else:                       #The rest of the score boards will have a heading of "End of Round"
        roundstring = "End of Round " + str(roundnum)
        borderplus = 16         #Variable that is used to count additional border characters needs to be printed
    for x in range ((roundcount*6)):        #Border is a total of 6 characters per round times 2 plus the number of characters of the top border header
        topborder = topborder + '*'         #Used for loop to create top border based on the number of rounds and number of header characters
    for x in range (((roundcount*6)*2)+borderplus): #Used for loop to create bottom border based on the number of rounds and number of header characters
        bottomborder = bottomborder + '*'
    print("%s %s %s" % (topborder, roundstring, topborder))     #Combine border and header variables to display top header
    for x in range (roundcount):            #Use for loop to display all rounds as Round N, that's aligned to the left by 10 spaces
        if x == 0:
            print("          {0:<10}".format("Round " + str(x+1)),end="")       #Use print end parameter to print in a continuous line
        else:
            print("{0:<10}".format("Round " + str(x+1)),end="")
    print("{0:<10}".format("Total"))                    #Print total with the same alignment
    for x in range (len(players)):                      #Use for loop to display player names as a row
        truncplayername=players[x][:9]                  #Truncate playername to 9 characters for a better score board view
        #print("{0:<10}".format(players[x]),end="")
        print("{0:<10}".format(truncplayername),end="") #Used for loop and print end parameter to display playername and score in a row
        for y in range (roundcount):                    #Display all scores in game list
            print("{0:<10}".format(game[x][y]),end="")
        print("{0:<10}".format(sum(game[x])))           #Display total score of a player in game list
    print(bottomborder)                                 #Print bottom border
    


def game():
    """
    function: Game function to run game 
    """
    rungame() # calling run game 

if __name__ == "__main__":
    """
    Main code block to run the code
    """
    game() # calling game in main block