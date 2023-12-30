# Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Usee proper functions to check for win.

#               S W G
# computer =    0 1 2
# player = S 0  D W L
        #  W 1  L D W
        #  G 2  W L D

import random
D = 'Game draw'
L = 'You loose'
W = 'You won'

def check(comp, user):
    if (comp == user):
        return D
    if (comp == 0 and user == 1):
        return L
    if (comp == 1 and user == 2):
        return L
    if (comp == 2 and user == 0):
        return L
    return W


comp = random.randint(0, 2)
user = int(input('0 for Snake, 1 for Water and 2 for Gun: '))

print("Your response", user)
print("Computer response", comp)

score = check(comp, user)
print(score)

while True:
    again_play = input('\nDo you want to play Again? Y/N ')