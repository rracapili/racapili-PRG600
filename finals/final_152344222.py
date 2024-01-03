import sys
import os 
import random

"""
Firstname: Ronald
Lastname: Capili
Username: radcapili
StudentID: 152344222
Email: radcapili@myseneca.ca
"""

# This is my TicTacToe Class 
class TicTacToe:
    # Declare class variables 
    # players is a list of players (this game will have 2 players)
    # Winninggames is a list of all winning possibilities 
    # Player1entry is a list of entries of first players 
    # Player2 entry is a list of entries of second player 
    players = []
    winninggames = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]] #This is just sample 
    player1entry = []
    player2entry = []
    board = [1,2,3,4,5,6,7,8,9] #Based on infromation given in the Final Exam Problem Statement

    # This is a constructor 
    """
    This is a constructor that prints an initialization statement
    Then call the getplayernames method to get the names and configure the list of players 
    Also call the printboard method to print the board, since this is a constructor the printboard is called first time here 
    Therefore printboard in this constructor will print initial brand new board ready to be played.
    """
    def __init__(self) -> None:
        print ("Initializing a 3X3 TicTacToe")
    """
    This is getplayernames method 
    This method asks user to enter the name of the player 1 and 2 one by one and append the names to the players class variable
    """
    def getplayernames(self): 
        player1 = input("What is the name of the player 1: ")       #Ask user for player 1's name
        TicTacToe.players.append(player1)                           #Append player 1's name to players list
        player2 = input("What is the name of the player 2: ")       #Ask user for player 2's name
        TicTacToe.players.append(player2)                           #Append player 2's name to players list
    """
    This is a printboard method 
    This method prints current state of the board 
    """
    def printboard(self):
        for x in range (0,len(TicTacToe.board),3):                  #Iterate through the board in 3's. 
            row=TicTacToe.board[x:x+3]                              #Save elements of the board in another list
            formatted_row = "|" + "|".join(map(str,row)) + "|"      #Format the new list with the values to print in a box
            print(formatted_row)                                    #Print the values
    
    """
    This method gets all available numbers to be played at the time this method is called 
    It returns these available numbers 
    :return availablenumbers 
    """
    def getavailablenumbers(self):
        availablenumbers = []                                       #Initialize an empty list for the available numbers in the board
        for x in range(len(TicTacToe.board)):                       #Iterate through the board and check if there are remaining numbers
            if str(TicTacToe.board[x]).isdigit():
                availablenumbers.append(TicTacToe.board[x])         #Save remaining number in the new availablenumbers list and return it
        return availablenumbers
    
    """
    This function goes through all the winning games and compare them against the each individual players entries
    By comparing the entries against winning game this method identifies the winner if there is one 
    If there is a winner this method returns the winner otherwise return None
    """
    def getwinner(self,playername,playermoves):                         #Take current playername, and current playerentries as arguments
        for x in range(0,len(TicTacToe.winninggames)):                  #Iterate through all the winninggame combinations
            if set(TicTacToe.winninggames[x]).issubset(playermoves):    #If a winning game is a subset of the player's moves, return the player's name
                return playername
        return None                                                     #If no winning combination is found, return None

    """
    This is rungame method 
    This method continue to run a loop asking the user to enter the number to play and shows the available numbers as well
    If the user enter something otherthan the available number the prompt will continue to ask the same user to enter the correct values 
    This method assembles all the relevant method we have together, so that 
    First player one is asked to enter the number and then the second and then the first and it keep alternates 
    Until one player wins or the game finishes where there is no further numbers to enter. 
    Ultimately, if there is a winner it prints the winner. If ther eis no winner it prints No Winner. 
    """
    def rungame(self): 
        TicTacToe.getplayernames(self)                  #Call getplayernames to save player names
        TicTacToe.printboard(self)                      #Print first game board
        while True:                                     #While loop for the whole game - will be terminated by a break if a player wins or if all moves are used.
            while True:                                     #While loop for player input used to catch wrong input
                availablenumbers=TicTacToe.getavailablenumbers(self)            #Get available numbers for moves
                playermove=input("%s Enter the number to play your symbol X (Available Numbers %s): " % (TicTacToe.players[0], ','.join(map(str,availablenumbers))))
                if playermove.isdigit():                                        #If player input is digit, convert input to int
                    playermove=int(playermove)
                    if playermove < 1 or playermove > 9:                        #Check if input is within the moves allowed, print error message
                        print("Enter available Number")
                    elif playermove in availablenumbers:                        #Check if input is within the available moves, save it if it is
                        break
                    else:                                                       #Check if input is already used, print error message
                        print("Number already played, choose a different number from available numbers. (Available Numbers %s) " + (','.join(map(str,availablenumbers))))
                else:                                                           #If input is not a digit, print error message
                    print("Enter available Number")
            TicTacToe.player1entry.append(playermove)                           #Save player move
            for i in range(len(TicTacToe.board)):                               #Find the move number, and replace value in the board with X for player 1
                if TicTacToe.board[i] == playermove:
                    TicTacToe.board[i] = 'X'
                    break
            winner = TicTacToe.getwinner(self,TicTacToe.players[0],TicTacToe.player1entry)          #Check if this is a winning move
            availablenumbers=TicTacToe.getavailablenumbers(self)                                    #Get new available numbers
            if winner != None:                                                  #Check if there's a winner, print winner if there is, and end the game
                print("Player %s is the winner" % (winner))
                break
            elif len(availablenumbers) == 0:                                    #Check if no more moves are available
                TicTacToe.printboard(self)                                      #Print final board before terminating the game
                print("No one win!")
                print("End of the game",end='')
                break
            TicTacToe.printboard(self)                                          #Print board if it's not yet end of game
            while True:
                availablenumbers=TicTacToe.getavailablenumbers(self)            #Get available numbers for moves
                playermove=input("%s Enter the number to play your symbol O (Available Numbers %s): " % (TicTacToe.players[1], ','.join(map(str,availablenumbers))))
                if playermove.isdigit():                                        #If player input is digit, convert input to int
                    playermove=int(playermove)
                    if playermove < 1 or playermove > 9:                        #Check if input is within the moves allowed, print error message
                        print("Enter available Number")
                    elif playermove in availablenumbers:                        #Check if input is within the available moves, save it if it is
                        break
                    else:                                                       #Check if input is already used, print error message
                        print("Number already played, choose a different number from available numbers. (Available Numbers %s) " + (','.join(map(str,availablenumbers))))
                else:                                                           #If input is not a digit, print error message
                    print("Enter available Number")
            TicTacToe.player2entry.append(playermove)                           #Save player move
            for i in range(len(TicTacToe.board)):                               #Find the move number, and replace value in the board with O for player 2
                if TicTacToe.board[i] == playermove:
                    TicTacToe.board[i] = 'O'
                    break
            winner = TicTacToe.getwinner(self,TicTacToe.players[1],TicTacToe.player2entry)          #Check if this is a winning move
            availablenumbers=TicTacToe.getavailablenumbers(self)                                    #Get new available numbers
            if winner != None:                                                  #Check if there's a winner, print winner if there is, and end the game
                print("Player %s is the winner" % (winner))
                break
            elif len(availablenumbers) == 0:                                    #Check if no more moves are available
                TicTacToe.printboard(self)                                      #Print final board before terminating the game
                print("No one win!")
                print("End of the game",end='')
                break
            TicTacToe.printboard(self)         

# My main method to test this code locally
if __name__ == "__main__":
    game = TicTacToe()
    game.rungame()