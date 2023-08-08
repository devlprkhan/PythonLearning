'''
Snake Water Gun
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors"
where players use hand gestures to represent a snake, water, or a gun. 
The gun beats the snake, the water beats the gun, and the snake beats the water. 
Write a python program to create a Snake Water Gun game in Python using if-else statements. 
Do not create any fancy GUI. Use proper functions to check for win.


                              Computer's Choices
                              | Snake | Water | Gun |
                        -------------------------------
                        Your   |   D   |   W   |  L   |
                        Choice |-----------------------
                              |   L   |   D   |  W   |
                        -------------------------------
                              |   W   |   L   |  D   |
       
D=draw
L=lose
W=win
'''

#? Solution
'''
1: Initialize the matrix to represent the possible outcomes of the game.
2: Convert the gestures entered by the player and computer into their respective matrix indices.
3: Retrieve the result from the matrix based on the player's and computer's gestures.
4: Display the result of the game.
'''

import random

# Computer list
computer_gestures = ['S', 'W', 'G']
# Outcome matrix
outcome_matrix = [
    # S    W    G
    ['D', 'W', 'L'],  # S
    ['L', 'D', 'W'],  # W
    ['W', 'L', 'D'],  # G
]

# Get the gesture from Matrix
def get_gesture(gesture):
  gestures = {'S': 0, 'W': 1, 'G': 2}
  return gestures[gesture]

def display_result(result):
    if result == 'D':
        print("It's a draw!")
    elif result == 'W':
        print("Congratulations! You win!")
    elif result == 'L':
        print("Sorry, you lose!")


player_gesture = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()

if(player_gesture in ['S', 'W', 'G']):
  computer_gesture = random.choice(computer_gestures)

  player_index = get_gesture(player_gesture)
  computer_index = get_gesture(computer_gesture)

  result = outcome_matrix[player_index][computer_index]

  display_result(result)
else:
  raise ValueError("Invalid input!")