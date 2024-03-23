import die
class Player:
  '''
  Creates dice then converts dice rolls into points.\n
  Attributes:\n
  (Die[]) _dice: A list of die objects.\n
  (int) _points: A value dependent on dice rolls.\n
  Behaviors:\n
  get_points() -> int: Accessor method for _points\n
  roll_dice(): Rolls each die in _dice and sorts them.\n
  has_pair() -> bool: Returns whether two die values in _dice are the same.\n
  has_three_of_a_kind() -> bool: Returns whether all three dice share the same value.\n
  has_series() -> bool: Returns whether the three dice values are in sequence.
  '''

  def __init__(self):
    '''Constructs and sorts three die objects and initializes _points to 0'''
    self._dice = []
    for i in range(3):
      self._dice.append(die.Die())

    self._points = 0

  def get_points(self):
    '''Accessor method for _points'''
    return self._points

  def roll_dice(self):
    '''Calls the roll method of each die in _dice, then _dice is sorted by die value.'''
    for i in range(0,3):
      self._dice[i].roll()

    #Organize dice order
    self._dice.sort()

  def has_pair(self) -> bool:
    '''Returns whether two die values in _dice are the same. Increments points by 1.'''
    for i in range (0,2):
      for j in range(i+1,3):
        if(self._dice[i] == self._dice[j]):
          self._points += 1
          return True

    #Loop done, no pair found
    return False
    

  def has_three_of_a_kind(self) -> bool:
    '''Returns whether all three die values in _dice are the same. Increments points by 3.'''
    for i in range(1,3):
      if(self._dice[0] != self._dice[i]):
        return False

    #Loop done, die 0 equals die 1 and 2
    self._points += 3
    return True

  def has_series(self) -> bool:
    '''Returns whether the three dice values are in sequence. Increments points by 2.'''
    for i in range (1,3):
      if(self._dice[i] - self._dice[0] != i):
        return False
    #Loop done, the dice are in sequence
    self._points += 2
    return True