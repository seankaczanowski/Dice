'''
Dice 1.0
Developed By Sean Kaczanowski
Feb 2019
'''

import random

# Title Screen
print('')
print('     +-------------+   ')
print('     |   Dice 1.0  |   ')
print('     +-------------+   ')
print('   +-------+ +-------+ ')
print('   | o   o | | o   o | ')
print('   | o   o | | o   o | ')
print('   | o   o | | o   o | ')
print('   +-------+ +-------+ ')
print('')
print(' + Press \'r\' to Roll')
print(' + Press \'x\' to Exit')
print('')

# Dice Assign and Printing
def dice_assign():
  dice = random.randint(1, 6)
  if dice == 1:
    print('+-------+')
    print('|       |')
    print('|   o   |')
    print('|       |')
    print('+-------+')
    print('')
  if dice == 2:
    print('+-------+')
    print('| o     |')
    print('|       |')
    print('|     o |')
    print('+-------+')
    print('')
  if dice == 3:
    print('+-------+')
    print('| o     |')
    print('|   o   |')
    print('|     o |')
    print('+-------+')
    print('')
  if dice == 4:
    print('+-------+')
    print('| o   o |')
    print('|       |')
    print('| o   o |')
    print('+-------+')
    print('')
  if dice == 5:
    print('+-------+')
    print('| o   o |')
    print('|   o   |')
    print('| o   o |')
    print('+-------+')
    print('')
  if dice == 6:
    print('+-------+')
    print('| o   o |')
    print('| o   o |')
    print('| o   o |')
    print('+-------+')
    print('')
  return dice


i = 0
while i == 0:
  j = 0
  
  # Roll Input Loop
  while j == 0:
    roll = input('Roll: ')
    if roll == 'r':
      j = 1
    else:
      print('Error. Try Again. Press \'r\' to roll.')
  
  print('')
  print('Player Roll:')
  print('')
  player1 = dice_assign()
  player2 = dice_assign()
  print('Score: ' + str(player1 + player2))



