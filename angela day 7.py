import random


list=["abebe","book","boots"]
display=[]
lives=6
stages= ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
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



choose_word=random.choice(list)
for i in choose_word:
    display.append("_")

# print(choose_word)
print(display)

end_game = False
# for i in range(0,len(choose_word)-1):
# a=0
# print(a)
# print(display[a])

no=-1

while end_game==False:

    guss=input ("guss the letter\n").lower()

    counter = -1


    for i in range(0,len(choose_word)):

        # counter=counter+1
        a=choose_word[i]
        if guss == a:
                display[i]=guss
                # break
    if guss not in choose_word:
            lives = lives - 1
            print("hello")
            # no=no+1
            print(stages[lives])


    print(lives)

    print(display)
    # print(a)
    if "_" not in display:
        end_game = True
        print("You Won")
    if lives == 0:
        print("you lose")
        end_game = True

