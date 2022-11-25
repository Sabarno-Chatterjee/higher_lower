import random
#import replit
import art
import game_data

print(art.logo)
first = random.choice(game_data.data)
second = random.choice(game_data.data)


first_position = game_data.data.index(first)
second_position = game_data.data.index(second)

print(first["name"])

print(f"\n\nCompare A: {first['name']}, a {first['description']}, from {first['country']}.\n\n")
print(art.vs)
print(f"\n\nCompare A: {second['name']}, a {second['description']}, from {second['country']}.\n\n")