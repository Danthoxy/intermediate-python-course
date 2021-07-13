def main():
  import random
  dice_sum = 0
  dice_rolls = int(input("How many dice would you like to roll ?")) 
  dice_sides = int(input("How many sides are the dice ?"))
  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_sides)
    if roll == 1 : 
      print(f"You rolled a {roll}! Critical Fail")
    elif roll == dice_sides :
      print(f"You rolled a {roll}! Critical Success ! ")
    else : 
      print(f'You rolled a {roll}')
    dice_sum += roll
  print(f'You have rolled a total of {dice_sum}')


if __name__== "__main__":
  main()