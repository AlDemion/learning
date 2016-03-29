#!/usr/bin/env python
import random


def get_user_choice(game_pool, choices_count):
    user_choice = []
    for choice in range(1, choices_count + 1):
        selection = raw_input("Please choose \"" + str(choice) + "\" number: ")
        verified_selection = verify_user_choice(game_pool, choice, choices_count, selection, user_choice)
        user_choice.append(verified_selection)

    return user_choice


def verify_user_choice(game_pool, choice, choices_count, selection, user_choice):
    try:
        selection = int(selection)
        if selection in game_pool and selection not in user_choice:
            return selection
        elif selection in user_choice:
            print "You already picked this number. Please choose another one."
            raise ValueError
        else:
            raise ValueError

    except (TypeError, ValueError):
        selection = raw_input("Wrong selection. Please choose \"" + str(choice) + "\" number again: ")
        selection = int(selection)
        verify_user_choice(game_pool, choice, choices_count, selection, user_choice)

    finally:
        return selection


def verify_init(game_type):
    try:
        game_type = int(game_type)
        if game_type in range(1, 4):
            if game_type == 1:
                game_pool = range(1, 37)
                choices_count = 5
                return game_pool, choices_count
            elif game_type == 2:
                game_pool = range(1, 46)
                choices_count = 6
                return game_pool, choices_count
            elif game_type == 3:
                game_pool = range(1, 48)
                choices_count = 7
                return game_pool, choices_count
        else:
            raise ValueError

    except (TypeError, ValueError):
        print "Wrong selection, please choose again."
        main()


def game(game_pool, choices_count):
    winning_pool = []
    while len(winning_pool) < choices_count:
        rand = random.choice(game_pool)
        if rand not in winning_pool:
            winning_pool.append(rand)

    return winning_pool


def main():
    print "Please choose type of game: "
    print "\t 1) 5 from 36"
    print "\t 2) 6 from 45"
    print "\t 3) 7 from 48"
    game_type = raw_input("Your choice: ")
    game_pool, choices_count = verify_init(game_type)
    user_choice = get_user_choice(game_pool, choices_count)
    winning_pool = game(game_pool, choices_count)
    match_pool = []
    for i in user_choice:
        if i in winning_pool:
            match_pool.append(i)

    print "\nOk. Game is finished."
    print "Your selection was: " + str(user_choice)
    print "Winning numbers is: " + str(winning_pool)
    print "Matching numbers is: " + str(match_pool)
    print "You guess " + str(len(match_pool)) + " numbers."
    print "Thanks for playing. Bye."

if __name__ == "__main__":
    main()

