import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words = [
    "apple", "banana", "cherry", "date", "elephant", 
    "forest", "grape", "honey", "island", "jungle",
    "kitten", "lemon", "mountain", "notebook", "orange",
    "pencil", "quartz", "river", "sunflower", "tiger"
]

print("This is Hangman game\nYour Objective is to guess the word letter by letter ")
random_word = random.choice(words)
saved_words = []
display1 = ""
game_over = False
lives = 6

for each in random_word:
    display1 += "_ "

print(display1)


while game_over != True:
    display2 = ""
    letter_guessed = input("Guess your letter:\n")
    
    for alphabet in random_word:
        if alphabet == letter_guessed:
            display2 += letter_guessed
            saved_words.append(alphabet)
        elif alphabet in saved_words:
            display2 += alphabet
        else:
            display2 += "_"
    if letter_guessed not in random_word:
        lives -=1
        print(stages[lives])
    if "_" not in display2:
        game_over  = True
        print("You won")

   

    print(display2)