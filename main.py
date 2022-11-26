import random
import replit
import art
import game_data


def select():
    """To pick a random list element from game_data.data"""
    return random.choice(game_data.data)


first = select()
second = select()

is_correct = True
score = 0
print(art.logo)
while is_correct:
  
  print(
      f"\n\nCompare A: {first['name']}, a {first['description']}, from {first['country']}.\n\n"
  )
  print(f"\nTest code: {first['follower_count']}\n")
  
  print(art.vs)
  print(
      f"\n\nCompare B: {second['name']}, a {second['description']}, from {second['country']}.\n\n"
  )
  print(f"\nTest code: {second['follower_count']}\n")
  
  
  result = "b"
  
  if first["follower_count"] > second["follower_count"]:
      result = "a"
      first = first
      second = select()
  else:
      first = second
      second = select()
  
  choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
  if choice == result:
      replit.clear()
      score += 1
      print(f"\n\n\nYou are correct. Your score is {score}\n")
      
  
  else:
      print(f"\n Sorry, you are wrong!. Your final score is {score}\n")
      is_correct = False
  
