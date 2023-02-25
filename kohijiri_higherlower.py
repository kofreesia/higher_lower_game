print("hello, world~")
import random
from database import data

def vs(sel_opt, unsel_opt):
  return (sel_opt is None) or (sel_opt['follower_count'] > unsel_opt['follower_count'])


data_shuffled = random.sample(data, len(data)) # shuffle data (but keep the order of original data)
score = -1   # add 1 every times
a = b = None # options
i = 0        # random number for sampling "B"
x = ''       # user input
keep_game = True


# This algorithm only allow user to input "A", "B", "Q", or "X", otherwise the game will not over.
while keep_game:
  score += 1
  x = ''

  # The first one should always be the option "A".
  a = data_shuffled[0]
  # Random select an element between the first and the last elements.
  # (The first one is always be the option "A" and the last one was selected as "B" in previous time.)
  i = random.randrange(1, len(data_shuffled) - 1)
  b = data_shuffled[i]

  print('A: {} ({}, {}) vs B: {} ({}, {})'.format(
      a['name'], a['description'], a['country'],
      b['name'], b['description'], b['country']))
  print('A {} \t B {}'.format(a['follower_count'], b['follower_count']))
  
  while x not in ['a', 'b', 'q', 'x']:
    x = input('Type A or B: ').lower()
    if x in ['a', 'b']:
      if x == 'b':
        a, b = b, a
        data_shuffled[0], data_shuffled[i] = data_shuffled[i], data_shuffled[0]
      keep_game = vs(a, b)
    elif x.lower() == 'x' or x.lower() == 'q':
      keep_game = False
    else:
      print('Type "x" or "q" to finish.')

  # Move the option "B" to the last element of a list to avoid seleting again next time.
  data_shuffled[i], data_shuffled[len(data_shuffled) - 1] = data_shuffled[len(data_shuffled) - 1], data_shuffled[i]
  

print('Game Over; Your score is {}.'.format(score))

