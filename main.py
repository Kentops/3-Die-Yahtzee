'''
Yahtzee
2/28/2024
A 3 die version of Yahtzee
'''
import player
import check_input

def take_turn(player):

  ''' This function rolls the player's dice, displays the dice, checks for and displays any win types (pair, series, three)'''

  player.roll_dice()
  print(f"D1 = {player._dice[0]} D2 = {player._dice[1]} D3 = {player._dice[2]}")

  if player.has_three_of_a_kind():
    print("You got 3 of a kind!")

  elif player.has_pair():
    print("You got a pair!")

  elif player.has_series():
    print("You got a series of 3!")
  else:
    print("Aww. Too Bad.")

  print(f"Score = {player.get_points()}")

def main():
  '''Main function that runs the game'''
  print("-Yahtzee- \n")
  guy = player.Player()

  play_again = True
  while play_again:
    take_turn(guy)
    play_again = check_input.get_yes_no("Play again (Y/N)? ") 
    print()
    
  print("Game Over")
  print(f'Final Score = {guy.get_points()}')



main()