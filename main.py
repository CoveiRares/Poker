import random
import os
from poker_hand import is_pair, is_flush, is_straight

DECK = [f"{i} of {j}" for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] for j in range(4)]
SUIT_SYMBOLS = ['\u2660', '\u2665', '\u2666', '\u2663']
MOVES = {"fold", "check", "call", "bet"}


def main():
    # print cool title
    welcome()
    # inset an amount of cash
    while True:
        try:
            cash = int(input("How much would you like to spend today?: $"))
        except ValueError:
            print("You must enter a number!")
        else:
            if cash>2000000000:
                print("Cash must be lower than 2 billion!")
            else:
                break

    # Initiate first game
    input("Press enter to start the first game!")
    game(cash)


def welcome():
    with open(os.getcwd()+"\\ASCII_DRAWINGS\\PokerTitle.txt", "r") as file:
        print(file.read())


def game(cash):
    print(f"Current cash: {cash}")
    bot_quit_current = False
    quit_current = False

    player_hand = random.sample(DECK, k=2)
    enemy_hand = random.sample([x for x in DECK if x not in player_hand], k=2)

    table = random.sample([x for x in DECK if x not in player_hand and x not in enemy_hand], k=5)
    table_cards = 2
    enemy_bet= random.randint(0,cash)
    player_bet = 0
    while True:
        idk_how_to_do_this_so_it_exits_the_other_while_loop = False
        print_cards(player_hand, table, table_cards, enemy_hand)
        print()
        print(f"Enemy bet: {enemy_bet} | Player bet: {player_bet}")
        # Calculate available moves
        available_moves = "Fold | "
        if player_bet == enemy_bet:
            available_moves += "Check | "
        if player_bet < enemy_bet:
            available_moves += "Call | "
        available_moves += "Bet"

        # Choose move
        while True:
            print("What's your move?")
            answer = input(available_moves + "   ").lower()
            if answer not in MOVES:
                print("Not a valid move")
                continue

            if answer == "fold":
                quit_current = True
                break

            if answer == "check":
                break

            if answer == "call":
                player_bet = enemy_bet
                break

            if answer == "bet":
                if player_bet >= cash:
                    print("You don't have enough money to bet and you have to choose something else!")
                    continue
                bet = 0
                while bet < max(enemy_bet, player_bet):
                    try:
                        bet = int(input("How much do you want to bet?: $"))
                    except ValueError:
                        print("You must enter a number!")
                    else:
                        if bet > cash - player_bet:
                            print(f"You must enter less than how much money you've got left ({cash - player_bet}).")
                            bet = 0
                        elif bet < 0:
                            print(f"Invalid bet ({bet})")
                            bet = 0
                        else:
                            player_bet += bet
                            if enemy_play(enemy_hand, table):
                                enemy_bet = player_bet
                                idk_how_to_do_this_so_it_exits_the_other_while_loop = True
                                break
                            bot_quit_current = True
                            break
                if idk_how_to_do_this_so_it_exits_the_other_while_loop:
                    break

        print()
        table_cards += 1
        # If the bot decided to quit, the player gets the pot money
        if bot_quit_current:
            cash += enemy_bet
            break
        # If the bot decided to quit, the player loses the pot money
        if quit_current:
            cash -= player_bet
            break
        # At the end calculate the winner
        if table_cards == 6:
            print_cards(player_hand, table, table_cards, enemy_hand)
            print()
            winner = calculate_winner(player_hand, enemy_hand, table)
            if winner=="player":
                cash += enemy_bet
            elif winner=="enemy":
                cash -= player_bet
            else:
                pass
            print(winner)
            break
    play_again(cash)

def calculate_winner(player, enemy, table):
    player = calculate_hand_strength(player, table)
    enemy = calculate_hand_strength(enemy, table)
    if player > enemy:
        return "player"
    elif player == enemy:
        return "tie"
    else:
        return "enemy"


def play_again(cash):
    print(f"Current cash: {cash}")
    if input("Do you want to play again (y/n)?: ") != "y":
        print("It was great having you!")
    else:
        game(cash)


def enemy_play(enemy, table):
    strength = calculate_hand_strength(enemy, table)
    if strength>1:
        return True
    else:
        return False


def calculate_hand_strength(hand, table):
    strength = max(is_straight(hand, table), is_flush(hand, table), is_pair(hand, table))
    return strength

def print_cards(player_cards, table, table_cards_num,enemy_cards):
    print("Enemy:", end=" ")
    if table_cards_num == 6:
        with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{enemy_cards[0]}.txt", "r") as f1:
            with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{enemy_cards[1]}.txt", "r") as f2:
                for i in range(9):
                    first = f1.readline()[:-1]
                    second = f2.readline()[:-1]
                    if i == 8:
                        print("       " + first + " " + second, end="")
                    elif i == 4:
                        print("       " + change_symbol(first) + " " + change_symbol(second))
                    elif i == 0:
                        print(first + " " + second)
                    else:
                        print("       " + first + " " + second)
    else:
        with open(os.getcwd()+f"\\ASCII_DRAWINGS\\hovered card.txt", "r") as f1:
            with open(os.getcwd()+f"\\ASCII_DRAWINGS\\hovered card.txt", "r") as f2:
                for i in range(9):
                    if i == 8:
                        print("       " + f1.readline() + " " + f2.readline(), end="")
                    elif i == 0:
                        print(f1.readline()[:-1] + " " + f2.readline()[:-1])
                    else:
                        print("       " + f1.readline()[:-1] + " " + f2.readline()[:-1])
    print()
    print("Table:", end=" ")
    if table_cards_num == 2:
        print()
    else:
        with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{table[0]}.txt", "r") as f1:
            with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{table[1]}.txt", "r") as f2:
                with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{table[2]}.txt", "r") as f3:
                    with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{table[3]}.txt", "r") as f4:
                        with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{table[4]}.txt",
                                  "r") as f5:
                            first = second = third = fourth = fifth = ""
                            for i in range(9):
                                if table_cards_num >= 2:
                                    first = f1.readline()[:-1]
                                    second = f2.readline()[:-1]
                                    if table_cards_num >= 3:
                                        third = f3.readline()[:-1]
                                        if table_cards_num >= 4:
                                            fourth = f4.readline()[:-1]
                                            if table_cards_num >= 5:
                                                fifth = f5.readline()[:-1]
                                if i == 0:
                                    print(first + " " + second + " " + third + " " + fourth + " " + fifth)
                                elif i == 4:
                                    print("       " + change_symbol(first) + " " + change_symbol(
                                        second) + " " + change_symbol(third) + " " + change_symbol(
                                        fourth) + " " + change_symbol(fifth))
                                else:
                                    print("       " + first + " " + second + " " + third + " " + fourth + " " + fifth)

    print()
    print("Player:", end=" ")
    with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{player_cards[0]}.txt", "r") as f1:
        with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{player_cards[1]}.txt", "r") as f2:
            for i in range(9):
                first = f1.readline()[:-1]
                second = f2.readline()[:-1]
                if i == 8:
                    print("        " + first + " " + second, end="")
                elif i == 4:
                    print("        " + change_symbol(first) + " " + change_symbol(second))
                elif i == 0:
                    print(first + " " + second)
                else:
                    print("        " + first + " " + second)


def change_symbol(line):
    # changing the line to a list so you can change the character in the middle to the suit
    if len(line) == 0:
        return ""
    l = list(line)
    l[7] = SUIT_SYMBOLS[int(line[7])]
    return "".join(l)

main()