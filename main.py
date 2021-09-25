#import logo art
from art import logo

import random
# data range = range(0,49)

#import vs art
from art import vs

#import game data
from game_data import data

print(logo)

random1 = random.randint(0,49)
random2 = random.randint(0,49)

#pick two instagrammers to compare

influencer_a_name = data[random1]["name"]
influencer_a_description = data[random1]["description"]
influencer_a_country = data[random1]["country"]

influencer_b_name = data[random2]["name"]
influencer_b_description = data[random2]["description"]
influencer_b_country = data[random2]["country"]

print(f"Compare A: {influencer_a_name}, {influencer_a_description}, from {influencer_a_country}.")

print(vs)

print(f"Compare B: {influencer_b_name}, {influencer_b_description}, from {influencer_b_country}")

guess = input("Who has more followers? Type 'A' or 'B': ")
 
#Check guess against follower count

#Ask user to make a guess

#recycle person b to compare new person against

