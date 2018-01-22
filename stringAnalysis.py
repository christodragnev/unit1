#Christo Dragnev
#1/19/18
#stringAnalysis.py

sentence = input("Enter a sentence:")
words=sentence.count(' ')
characters=len(sentence)
space=" "
letters=len(sentence)-sentence.count(space)

print('Your sentence has', words+1, 'words', 'and', characters, 'characters and', letters, 'letters')

characterSearch = input('Enter a character to search for: ')
print('Your sentence has',sentence.lower().count(characterSearch), ' of the character', characterSearch)

wordSearch = input('Enter a word to search for: ')
print('Your sentence has',sentence.lower().count(wordSearch), ' of the word', wordSearch)
