"""
File: anagram.py
Name: Aaron Kao
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant.

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program shows the anagram game, which is a word or phrase formed by rearranging
    the letters of a different word.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        else:
            start = time.time()
            dic_lst = read_dictionary(word)
            find_anagrams(word, dic_lst)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    param s: input word
    Load the dictionary file and Store the word at DIC_LST.
    """
    dic_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            # Algorithm optimization1 - Store the same number of input word
            if len(line.strip()) == len(s):
                dic_lst.append(line.strip())
    dic_lst = set(dic_lst)     # Algorithm optimization2 : set {'aah', 'aal'...}   O(1)
    return dic_lst


def find_anagrams(s, dic_lst):
    """
    param s: input word
    return: the anagram words from dictionary.txt
    """
    print('Searching...')
    word_lst = []
    find_anagrams_helper(s, "", len(s), dic_lst, word_lst)
    print(str(len(word_lst)) + ' anagrams:', word_lst)


def find_anagrams_helper(s, current_s, len_s, dic_lst, word_lst):
    """
    param s: input word
    param current_s: the initial string
    param len_s: the length of input word
    return: the anagram words from dictionary.txt
    """
    if len(current_s) == len_s and current_s in dic_lst:  # Base Case - Anagram word form dictionary.txt
        if current_s not in word_lst:       # Avoid storing repeated permutations, ex: apple has two p letters.
            word_lst.append(current_s)
            print('Found:', current_s)
            print('Searching...')
    else:
        # Choose
        for i in range(len(s)):
            s_remain = s[:i]+s[i+1:]       # Unselected remaining letters.
            current_s += s[i]              # Pick the letter and store at the string
        # Explore
            #   if has_prefix(current_s, dic_lst):   # for loop is O(N)
            find_anagrams_helper(s_remain, current_s, len_s, dic_lst, word_lst)
                # Recursion - the next step of searching word.
        # Un-choose
            current_s = current_s[:-1]     # Back to previous step.


def has_prefix(sub_s, dic_lst):
    """
    :param sub_s: the current searching word
    :return: True/False ,whether the word exists in the DIC_LST
    """
    for line in dic_lst:
        if line.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
