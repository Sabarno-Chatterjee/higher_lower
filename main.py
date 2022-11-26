import random
#import replit
import art
import game_data

print(art.logo)
# first = random.choice(game_data.data)
# second = random.choice(game_data.data)
def select():
  """To pick a random list element from game_data.data"""  
  return random.choice(game_data.data)

first = select()
second = select()
print(first)
print(second)
# first_position = game_data.data.index(first)
# second_position = game_data.data.index(second)

# print(first["name"])

# print(
#     f"\n\nCompare A: {first['name']}, a {first['description']}, from {first['country']}.\n\n"
# )
# print(art.vs)
# print(
#     f"\n\nCompare B: {second['name']}, a {second['description']}, from {second['country']}.\n\n"
# )

# result = "b"

# if first["follower_count"] > second["follower_count"]:
#     result = "a"
#     first = first
# else:
#     first = second

# score = 0
# choice = input("Who has more followers? Type 'A' or 'B':").lower()
# if choice == result:
#     score += 1
#     print(f"\nYou are correct. Your score is {score}\n")
    
# else:
#     print(f"\n Sorry, you are wrong!. Your final score is {score}\n")

# print(first)
# print(second)
