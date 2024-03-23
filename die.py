import random

class Die:
  '''
  A singular die.\n
  Attributes:\n
  (int) _sides: The number of sides of the die\n
  (int) _value): The value of the die's roll\n
  Behaviors:\n
  roll() -> int: returns a value 1 to _sides
  '''

  def __init__(self, sides = 6):
    '''sides (int) is the number of sides on the die. Set to 6 by default.'''
    self._sides = sides
    self._value = 0

  def roll(self)->int:
    '''Sets _value to a random number 1-_sides, then returns _value'''
    self._value = random.randint(1,self._sides)
    return self._value

  def __str__(self):
    '''returns _value'''
    return str(self._value)

  def __lt__(self,other):
    '''Returns true if self._value < other._value. Returns false otherwise'''
    return self._value < other._value

  def __eq__(self,other):
    '''returns whether self._value is equal to other._value.'''
    return self._value == other._value

  def __sub__(self,other):
    '''returns the difference between self._value and other._value.'''
    return self._value - other._value