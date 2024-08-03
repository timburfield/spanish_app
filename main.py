import json
import random as r
from colorama import Fore

""" Main code for running program """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Load corpus data
    with open('Files/eng_to_spa.json') as json_file:
        dictionary = json.load(json_file)
        words_eng = list(dictionary.keys())

    # Statistics setup
    score = []
    correct_ans = []

    """   """

    # Ask user to specify how many of the words to include in the bag of words
    print('What range (1-X) do you want to select words from?')
    range = int(input())

    # TODO: write a function that checks if the answer is correct
    # TODO: mark as correct if one of several options was answered correct (e.g. "el, la")

    while True:

        # Show user a random spanish word and take answer
        word_eng = words_eng[r.randint(0, range)]
        # Make sure word has not been answered correctly already
        while word_eng in correct_ans:
            word_eng = words_eng[r.randint(0, range)]
        word_spa = dictionary[word_eng]
        print(f'\nTranslate this word: {word_eng}')
        ans = input('write here: ')

        # Check if answer is correct and present correct translation
        if ans.lower() == word_spa.lower():
            score.append(1)
            correct_ans.append(word_eng)
            print(Fore.GREEN + 'Correct!' + Fore.WHITE)
        else:
            score.append(0)
            print(Fore.RED + 'Wrong!' + Fore.WHITE)
            print(f'Correct answer was: {word_spa}')

        print(f'Current score: {int((score.count(1)/len(score))*100)}%')
