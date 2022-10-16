
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random, sys
print('Welcome to ROCK, PAPER, SCISSORS')
# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0
while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: r-rock , p-paper , s-scissors ,  q-quit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program. #import sys.exit from sys
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
             break  # Break out of the player input loop.
        else:
            print('Wrong Move , Choose again') #ask for input again
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
        
    nums = [1, 2, 3]
    randomchoice = random.choice(nums) #import random.choice from random
    if randomchoice == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomchoice == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomchoice == 3:
        computerMove = 's'
        print('SCISSORS')
# Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

