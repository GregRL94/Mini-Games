# -*- coding: utf-8 -*-

from termcolor import colored

"""
File name : Connect4.py
Author: Grégory LARGANGE
Date of creation : 01/15/2021
Date of last modification : 10/28/2021

Summary:
Play connect 4 against a friend with this script!
"""


def rules():
    print(
        " ======================== WELCOME TO CONNECT 4 ! ================================"
    )
    print(
        "Connect 4 consist of a 6 * 7 board. To win a player must align 4 of its pieces, either vertically,"
    )
    print(
        "horizontaly or diagonaly. Players cannot choose their playing row but only the column."
    )
    print(
        "The only way to play on a row is by stacking pieces until the next piece land on the desired row."
    )
    print("")
    print("Playable columns from 0 to 6 included")
    print("PLAYER 1 PIECE: O")
    print("PLAYER 2 PIECE: X")
    print(
        "=============================== GOOD LUCK ! ====================================="
    )
    print("")
    print("")


def drawBoard(field):
    columns = 15
    rows = 12
    #############################
    # The connect 4 board is made of 7 columns and 6 rows.
    # That's what i want it to look like:
    #    1 3 5 7 9 11 13     # Indexes of playable columns
    #   | | | | | | | |   0  # Playable row
    #   ---------------   1
    #   | | | | | | | |   2  # Playable row
    #   ---------------   3
    #   | | | | | | | |   4  # Playable row
    #   ---------------   5
    #   | | | | | | | |   6  # Playable row
    #   ---------------   7
    #   | | | | | | | |   8  # Playable row
    #   ---------------   9
    #   | | | | | | | |   10 # Playable row
    #   ---------------   11
    #############################
    for row in range(rows):
        # If row is even it is a playable row and we do the process "| | | ..."
        if row % 2 == 0:
            # Only one out of two rows is really playable, so we divide by two
            # to get the playable rows. We cast the result to int to avoid errors.
            playableRow = int(row / 2)
            for column in range(columns):
                # If colum is odd it is a playable column and we print a space
                if column % 2 != 0:
                    # Only one out of two columns is really playable, so we divide by two
                    # to get the playable columns. We cast the result to int to avoid errors.
                    playableColumn = int(column / 2)
                    colored_piece = (
                        colored(
                            field[playableRow][playableColumn], "green", attrs=["bold"]
                        )
                        if field[playableRow][playableColumn] == "O"
                        else colored(
                            field[playableRow][playableColumn], "red", attrs=["bold"]
                        )
                    )
                    print(colored_piece, end="")
                else:
                    if column != (columns - 1):
                        print("|", end="")
                    else:
                        print("|")
            else:
                print("-" * 15)


def checkWin(board, line, column):
    piece = board[line][column]
    minColumn = column
    minLine = line
    counter = 0
    pieceStreakCounter = 0
    winner = None

    ############## Check horizontal ##############
    # Go to the left most contiguous same piece #
    counter = column
    while True:
        # If counter is less than 0 we are not in the board anymore
        if counter < 0:
            break
        # Test if the piece at the location is the same as the played piece
        if board[line][counter] == piece:
            minColumn = counter
        # If it is not we exit the loop, as we found the left most contiguous same piece
        else:
            break
        # Moves to the previous column
        counter -= 1
    ## Counts the number of contiguous same pieces from the left most piece ##
    counter = minColumn
    while True:
        # If counter is more than 6 we are not in the board anymore
        if counter > 6:
            break
        # Test if the piece at the location is the same as the played piece
        if board[line][counter] == piece:
            pieceStreakCounter += 1
            # Win condition of connect 4
            if pieceStreakCounter >= 4:
                winner = determineWinner(piece)
                return winner
        # If it is not we exit the loop, the streak is broken
        else:
            break
        # Moves to the next column
        counter += 1
    #############################################
    # Resets the piece streak counter
    pieceStreakCounter = 0

    ############## Check vertical ##############
    ## Go to the top most contiguous same piece ##
    counter = line
    while True:
        # If counter is less than 0 we are not in the board anymore
        if counter < 0:
            break
        # Test if the piece at the location is the same as the played piece
        if board[counter][column] == piece:
            minLine = counter
        # If it is not we exit the loop, as we found the top most contiguous same piece
        else:
            break
        # Moves to the previous line
        counter -= 1
    ## Counts the number of contiguous same pieces from the top most piece ##
    counter = minLine
    while True:
        # If counter is more than 5 we are not in the board anymore
        if counter > 5:
            break
        # Test if the piece at the location is the same as the played piece
        if board[counter][column] == piece:
            pieceStreakCounter += 1
            # Win condition of connect 4
            if pieceStreakCounter >= 4:
                winner = determineWinner(piece)
                return winner
        # If it is not we exit the loop, the streak is broken
        else:
            break
        # Moves to the next line
        counter += 1
    #############################################
    # Resets the piece streak counter
    pieceStreakCounter = 0

    ########## Check diagonal TL -> BR ##########
    ## Go to the top-left most contiguous same piece ##
    counterC = column
    counterL = line
    while True:
        if counterC < 0 or counterL < 0:
            break
        if board[counterL][counterC] == piece:
            minColumn = counterC
            minLine = counterL
        else:
            break
        counterC -= 1
        counterL -= 1
    ## Counts the number of contiguous same pieces from the top left most piece ##
    counterC = minColumn
    counterL = minLine
    while True:
        if counterC > 6 or counterL > 5:
            break
        if board[counterL][counterC] == piece:
            pieceStreakCounter += 1
            if pieceStreakCounter >= 4:
                winner = determineWinner(piece)
                return winner
        else:
            break
        counterC += 1
        counterL += 1
    #############################################
    pieceStreakCounter = 0

    ########## Check diagonal BL -> TR ##########
    ## Go to the bottom-left most contiguous same piece ##
    counterC = column
    counterL = line
    while True:
        if counterC < 0 or counterL > 5:
            break
        if board[counterL][counterC] == piece:
            minColumn = counterC
            minLine = counterL
        else:
            break
        counterC -= 1
        counterL += 1
    ## Counts the number of contiguous same pieces from the bottom left most piece ##
    counterC = minColumn
    counterL = minLine
    while True:
        if counterC > 6 or counterL < 0:
            break
        if board[counterL][counterC] == piece:
            pieceStreakCounter += 1
            if pieceStreakCounter >= 4:
                winner = determineWinner(piece)
                return winner
        else:
            break
        counterC += 1
        counterL -= 1
    #############################################
    return winner


def determineWinner(piece):
    if piece == "O":
        return "PLAYER 1"
    return "PLAYER 2"


def play():
    currentField = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
    ]
    player = 1
    filledTreshold = 7

    while True:
        playRow = None
        playColumn = None
        validColumn = False
        filledCounter = 0

        print("TURN: PLAYER", player)
        while validColumn is False:
            try:
                playColumn = int(input("Choose a column to play at: "))
                if playColumn < 0 or playColumn > 6:
                    print("The column does not exist, you can not play here!")
                elif currentField[0][playColumn] != " ":
                    print("This column is full, you can not play here!")
                else:
                    validColumn = True
            except ValueError as ve:
                print(ve, "Please enter a numeric value.")
            except:
                print("Encountered unexpected exception")

        if player == 1:
            for row in range(5, -1, -1):
                if currentField[row][playColumn] == " ":
                    currentField[row][playColumn] = "O"
                    playRow = row
                    break
            player = 2
        else:
            for row in range(5, -1, -1):
                if currentField[row][playColumn] == " ":
                    currentField[row][playColumn] = "X"
                    playRow = row
                    break
            player = 1

        drawBoard(currentField)
        # Determine if there is a winner after each play
        winner = checkWin(currentField, playRow, playColumn)
        if winner:
            print(winner, " WINS !")
            break
        # Determine if the game is a draw due to board being filled after each play
        for column in range(7):
            if currentField[0][column] == " ":
                break
            else:
                filledCounter += 1
        if filledCounter == filledTreshold:
            print("BOARD IS FILLED, IT'S A DRAW!")
            break


rules()
play()
