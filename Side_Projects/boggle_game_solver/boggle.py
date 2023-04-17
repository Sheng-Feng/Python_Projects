"""
File: boggle.py
Name: Aaron Kao
----------------------------------------
This program is Boggle Game.
The player enters 4x4 numbers of English letters and program will try to find as many words as it can.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	step 1. read dictionary and store at list.
	step 2. input 4x4 letters
	step 2-1. if input wrong format(space, not alpha, or two letters), show 'Illegal input'.
	step 2-2. Store letters to word list.
	step 3. find boggle from dictionary list.
	step 4. Show the results.
	"""
	#start = time.time()
	word = []
	# word = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	dic_lst = read_dictionary()
	for i in range(1, 5):
		input_word = input(str(i) + ' row of letters: ').lower()    # Case-Insensitive.
		for j in range(0, 7, 2):									# Avoid input space, not alpha, or two letters.
			if len(input_word) != 7 or not input_word[j].isalpha():
				print('Illegal input')
				return												# If input wrong format, terminate double for-loop.
		word.append(input_word.split())								# Store at list of list.
	find_boggle(word, len(word), len(word[0]), dic_lst)
	#end = time.time()
	#print('----------------------------------')
	#print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic_lst = []
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:				# Only store >=4 length words at dic.list
				dic_lst.append(line.strip())
	return dic_lst


def find_boggle(word, row_max, column_max, dic_lst):
	"""
	:param word: input 4x4 letters
	:param row_max: 4
	:param column_max: 4
	:param dic_lst: dic.list.
	"""
	word_lst = []								    # Store found boggle words.
	for x in range(row_max):
		for y in range(column_max):
			letter_lst = [(x, y)]					# Store the first letter coordinates.
			find_boggle_helper(word, word[x][y], row_max, column_max, x, y, dic_lst, letter_lst, word_lst)
	print('There are '+str(len(word_lst)) + ' words in total.')


def find_boggle_helper(word, current_s, row_max, column_max, x, y, dic_lst, letter_lst, word_lst):
	"""
	:param word: input 4x4 letters
	:param current_s: the first letter
	:param row_max: 4
	:param column_max: 4
	:param x:  x coordinate of the first letter
	:param y:  y coordinate of the first letter
	:param dic_lst: dic.list.
	:param letter_lst: the coordinates of letters.
	:param word_lst: found words list
	"""
	if len(current_s) >= 4 and current_s in dic_lst:   # Base Case - Boggle word form dictionary.txt
		if current_s not in word_lst:				   # Avoid store same words at word list.
			word_lst.append(current_s)
			print('Found "'+current_s+'"')
	if has_prefix(current_s, dic_lst):			       # If find one boggle word, still search next word.
		# Choose										# ex: room  -> roomy
		for i in range(-1, 2):
			for j in range(-1, 2):					   # Set boundary and avoid the same coordinate word.
				if 0 <= x+i < row_max and 0 <= y+j < column_max and (x+i, y+j) not in letter_lst:
					letter_lst.append((x+i, y+j))	   # Store coordinate.
					current_s += word[x+i][y+j]		   # Store letter.
		# Explore
					if has_prefix(current_s, dic_lst):
						find_boggle_helper(word, current_s, row_max, column_max, x+i, y+j, dic_lst, letter_lst, word_lst)
		# Un-choose
					letter_lst.pop()
					current_s = current_s[:-1]


def has_prefix(sub_s, dic_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for line in dic_lst:
		if line.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
