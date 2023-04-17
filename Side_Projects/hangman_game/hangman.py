"""
File: hangman.py
Name: Aaron Kao
-----------------------------
This program plays hangman game.Users see a dashed word, trying to correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the updated word on console. Players have N_TURNS chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. set up initial variable and boundary condition
    2. input letter to variable
    3. determine whether the input letter meet the requirement
    4. function - case_insensitive
    5. function - left times count
    6. function - judge whether input is correct
    7. function - if input letter is correct, change the letter at current status
    8. game over setting
    9. print out the words at different conditions
    """
    answer = 'STANCODE'
    turns = N_TURNS
    word = initial(answer)
    print('The word looks like ' + initial(answer))
    print('You have ' + str(turns) + ' wrong guesses left.')
    while True:
        letter = str(input('Your guess: '))
        if letter.isalpha() and len(letter) < 2:     # if input is number or over 2 letters, print 'Illegal format.'
            letter = case_insensitive(letter)
            turns = left_time(answer, letter, turns)
            word = guess(answer, letter, word)
            judge(answer, letter)
            if turns == 0 or word == answer:        # if chances is running out or guess correct word, terminate loop
                break
            print('The word looks like ' + word)
            print('You have ' + str(turns) + ' wrong guesses left.')
        else:
            print('Illegal format.')
    if turns == 0:
        print('You are completely hung : (')
    elif word == answer:
        print('You win!!')
    print('The word was: ' + answer)


def case_insensitive(letter):
    """
    if input letter is lower-case, change it to upper-case
    """
    if letter.islower():
        letter = letter.upper()
    return letter


def judge(answer, letter):
    """
    1. if input is correct, print...
    2. if input is wrong, print...
    """
    if answer.find(letter) == -1:
        print('There is no ' + letter.upper() + "'s in the word.")
    else:
        print('You are correct!')


def left_time(answer, letter, turns):
    """
    if input letter is wrong, reduce one time left to guess word.
    """
    if answer.find(letter) == -1:
        turns -= 1
    return turns


def guess(answer, letter, word):
    """
    1. input-answer, letter, word(current status)
    2. if input letter in the answer word, change '-' to input letter.
    3. update current word
    """
    ch = ''
    if answer.find(letter) != -1:
        for i in range(len(answer)):
            if answer[i] == answer[answer.find(letter)]:   # multiple letters
                ch += letter
            else:
                ch += word[i]
    else:
        for i in range(len(answer)):
            ch += word[i]
    return ch


def initial(answer):
    """
    initial word - EX:answer = apple, and initial word = '-----'
    """
    ch = ''
    for i in range(len(answer)):
        ch += '-'
    return ch


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
