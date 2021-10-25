# -*- coding: utf-8 -*-

"""
    File name: Hangman.py
    Author: Grégory LARGANGE
    Date created: 01/28/2021
    Last modified by: Grégory LARGANGE
    Date last modified: 10/25/2021
    Python version: 3.8.1

    Summary
    -------
    Play Hangman against a friend with this script!
"""


from os import system, path, name
from time import sleep
from termcolor import cprint
from random import randint

###############################
# ______
# |/  |
# |  (x)
# |  /|)
# |   |
# |  / )
# |_____
###############################

hangman = [
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
]

wordList = []
wordToGuess = []
currentGuess = []
triedLetters = []
maxTries = 5
triesCount = 0


def extractTxt():
    global wordList

    txtFilePath = path.join(
        path.dirname(path.realpath(__file__)), "resources", "commonEnglishWords.txt"
    )
    with open(txtFilePath, "r") as txtFile:
        for line in txtFile:
            currentLine = txtFile.readline().rstrip("\n")
            wordList.append(currentLine)
    txtFile.close()


def selectRandomWord():
    randIndex = randint(0, len(wordList) - 1)
    return wordList[randIndex]


def clear():
    # Windows
    if name == "nt":
        _ = system("cls")
    # Mac and Linux
    else:
        _ = system("clear")


def updateTerminal():
    clear()
    for line in range(len(hangman)):
        for column in range(len(hangman[0])):
            if column < len(hangman[0]) - 1:
                print(hangman[line][column], end="")
            else:
                print(hangman[line][column])
    print("")
    for index in range(len(currentGuess)):
        if index < len(currentGuess) - 1:
            print(currentGuess[index], end="")
        else:
            print(currentGuess[index])
    print("")
    print("Already tried letters:")
    print(triedLetters)


def startHangman(mode):
    global wordToGuess
    global currentGuess

    if mode == 1:
        valid_choice = False
        player_entry = ""

        while valid_choice is False:
            player_entry = input("Player1, enter a word to guess: ")
            if not player_entry.isalpha():
                print("You must enter a word, with letters only!")
            else:
                valid_choice = True

        for char in player_entry:
            if char == " ":
                wordToGuess.append(char)
                currentGuess.append(" ")
            else:
                char = char.lower()
                wordToGuess.append(char)
                currentGuess.append(".")
    else:
        extractTxt()
        wordToGuess = selectRandomWord()
        for char in wordToGuess:
            currentGuess.append(".")
    clear()


def updateHangman():
    if triesCount == 1:
        hangman[6] = ["|", "_", "_", "_", "_", "_"]
    if triesCount == 2:
        hangman[0] = ["_", "_", "_", "_", "_", "_"]
        hangman[1][0] = "|"
        hangman[1][1] = "/"
        for i in range(2, 6):
            hangman[i][0] = "|"
    if triesCount == 3:
        hangman[1][4] = "|"
        hangman[2] = ["|", " ", " ", "(", "x", ")"]
    if triesCount == 4:
        hangman[3] = ["|", " ", " ", "/", "|", ")"]
    if triesCount == 5:
        hangman[4][4] = "|"
        hangman[5] = ["|", " ", " ", "/", " ", ")"]


def playerTry():
    global wordToGuess
    global currentGuess
    global triedLetters
    global triesCount

    guessLetter = ""
    validEntry = False
    copyWord = True

    while validEntry is False:
        guessLetter = input("Player2, type the letter or word you yant to try: ")
        if guessLetter.isalpha():
            validEntry = True
            guessLetter = guessLetter.lower()
        else:
            cprint("Only letters !", "red")

    if len(guessLetter) == 1:
        if guessLetter in triedLetters:
            cprint("You have already tried this letter...", "red")
            triesCount += 1
            updateHangman()
        elif guessLetter in wordToGuess:
            cprint("Good choice, the letter is present in the word!", "green")
            for i, letter in enumerate(wordToGuess):
                if letter == guessLetter:
                    currentGuess[i] = guessLetter
            triedLetters.append(guessLetter)
        else:
            cprint("The letter is not in the word...", "red")
            triesCount += 1
            updateHangman()
            triedLetters.append(guessLetter)
    elif len(guessLetter) > 1:
        if len(guessLetter) != len(wordToGuess):
            cprint("This is not the world to guess, count the letters !", "red")
            triesCount += 1
            updateHangman()
        else:
            for i, letter in enumerate(guessLetter):
                if letter != wordToGuess[i]:
                    cprint("This is not the world to guess, try again !", "red")
                    triesCount += 1
                    copyWord = False
                    break
            if copyWord:
                currentGuess = guessLetter


def game():
    global triesCount
    global wordToGuess
    global currentGuess
    global maxTries
    wordFound = False

    print("=== GameMode selection ===")
    mode = 0
    validMode = False
    while validMode is False:
        mode = input(
            "Press '1' to play against a word choosen by another player, '2' to let the computer choose a word: "
        )
        if mode.isnumeric():
            mode = int(mode)
            if (mode == 1) or (mode == 2):
                validMode = True

    clear()
    startHangman(mode)
    updateTerminal()
    while (wordFound is False) and (triesCount < maxTries):
        playerTry()
        sleep(2)
        updateTerminal()
        wordFound = True
        for index in range(len(currentGuess)):
            if currentGuess[index] != wordToGuess[index]:
                wordFound = False

    if wordFound:
        cprint("*************************************************", "green")
        cprint("CONGRATULATIONS, YOU HAVE FOUND THE MYSTERY WORD!", "green")
        cprint("*************************************************", "green")
    if triesCount >= maxTries:
        cprint("*************************************************", "red")
        cprint("YOU HAVE LOST, BETTER LUCK NEXT TIME...", "red")
        cprint("The word was " + str(wordToGuess), "red")
        cprint("*************************************************", "red")


game()
