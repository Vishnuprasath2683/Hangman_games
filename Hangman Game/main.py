import random
import stages_files
import words_files
lives=6
chosen_word=random.choice(words_files.words)
print(chosen_word) #display the word to guess
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display) #display lines based upon words
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!!")
    if '_' not in display:
        game_over=True
        print("You Win!!")
    print(stages_files.stages[lives])