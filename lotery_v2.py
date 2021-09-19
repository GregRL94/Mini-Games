# -*- coding: utf-8 -*-

"""
Author: Gregory Largange
Date of Creation: 16/09/2021
Summary: Lotery script distributing
tickets among players and choosing
at random a winning ticket
"""

import random
import time
import os


clear = lambda: os.system("cls")


class Lotery:
    def __init__(self):
        self.welcome_text = [
            " _-_-_ Helper Lotery script _-_-_",
            "by #ThunderChief",
            "Please checkout my GitHub page below!",
            "https://github.com/GregRL94",
            "",
        ]
        self.disclaimer_text = (
            "WARNING: huge number of tickets (>10^6) WILL slow down the script."
        )
        self.valid_choices = ["s", "e"]
        self.players = {}
        self.all_tickets = []
        self.nb_tickets = 0
        self.winning_ticket = None
        self.winning_player = None

    def test_player_name(self, player_name):
        if len(player_name) == 0:
            print("Invalid name. Enter at least 1 character")
            return False
        return True

    def add_player(self, player_name, player_tickets):
        # Tests if player name is already registered
        if player_name in self.players.keys():
            print("The player already exists ! Use another name !")
            return False

        # Tests if player has bought at least 1 ticket
        if player_tickets <= 0:
            print("player must buy at least 1 ticket to participate !")
            return False

        # Registers the player and the number of tickets he bought
        self.players[player_name] = [player_tickets]
        self.nb_tickets += player_tickets
        return True

    def register_players(self):
        clear()
        user_entry = None
        print(
            "Enter the name of the player followed by a coma followed by the number of tickets\nExample: John,85"
        )
        print("Enter 'x' at any time to exit players registration.")
        while user_entry != "x":
            user_entry = input()
            if user_entry != "x":
                try:
                    player_name, player_tickets = user_entry.split(",")
                    try:
                        player_tickets = int(player_tickets)
                        if self.test_player_name(player_name):
                            if self.add_player(player_name, player_tickets):
                                print(
                                    "Sucessfully registered",
                                    player_name,
                                    "with",
                                    player_tickets,
                                    "tickets",
                                )
                    except ValueError as v_e:
                        print(v_e, "You must enter a number")
                except Exception as e:
                    print(e, "Your entry does not fit required format")

    def generate_tickets(self):
        # Generates the ticket pool.
        for i in range(0, self.nb_tickets):
            self.all_tickets.append(i)
        # Shuffles the tickets in the ticket pool.
        random.shuffle(self.all_tickets)
        # Chooses at random which ticket is the winning ticket.
        self.winning_ticket = random.randint(0, self.nb_tickets - 1)

    def distribute_tickets(self):
        for player, player_tickets in self.players.items():
            tmp = player_tickets[0]
            player_tickets.clear()
            # Distribute as many tickets as player bought from ticket pool.
            # The ticket is choosen from the pool at random.
            for _ in range(0, tmp):
                ticket_index = random.randint(0, len(self.all_tickets) - 1)
                ticket = self.all_tickets.pop(ticket_index)
                player_tickets.append(ticket)
                # Determines if player has received the winning ticket.
                if ticket == self.winning_ticket:
                    self.winning_player = player

    def check_registered(self):
        disp_tickets = input("Would you like to display players and their tickets [y]?")
        if disp_tickets == "y":
            for player, ticket_list in self.players.items():
                print(player, "registered with:", str(len(ticket_list)))
                print(ticket_list, "\n")
        else
            return
        _ = input("Press Enter to proceed with the loterw results")

    def announce_winner(self):
        clear()
        print("------------ THE LOTERY HAS ENDED !! -------------")
        time.sleep(1)
        print("THE WINNING TICKET IS: TICKET N°" + str(self.winning_ticket))
        print("--------------------------------------------------")
        time.sleep(1)
        print("........ AND THE WINNER OF THE LOTTERY IS ........")
        time.sleep(3)
        print(self.winning_player)
        print("*************** CONGRATULATIONS !!! **************")

    def lotery_menu(self):
        print(
            "Welcome to the lotery !\nEnter all participants and the number of tickets they bought. When you are done, the lotery will begin."
        )
        print(self.disclaimer_text)
        user_choice = None
        while user_choice not in self.valid_choices:
            user_choice = input(
                "Press 's' to start registering players,\nPress 'e' to exit the lotery\n"
            )
        if user_choice == "s":
            self.register_players()
            if len(self.players) > 1:
                self.generate_tickets()
                self.distribute_tickets()
                self.check_registered()
                self.announce_winner()
            else:
                print("Not enough players to perform a lotery")
        print("\nThanks for using lotery !")


if __name__ == "__main__":
    clear()
    lotery = Lotery()
    for text in lotery.welcome_text:
        print(text)
    lotery.lotery_menu()
