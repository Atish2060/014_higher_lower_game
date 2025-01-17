import random
from data import Data
from logo import Logo
from logo import Vs

game = True
score = 0
person_A = random.choice(Data)
while game:
    print(Logo)
    print(f"Compare A: {person_A['name']},{person_A['description']},{person_A['country']}")
    print(Vs)
    person_B = random.choice(Data)
    while person_A['name'] == person_B['name']:
        person_B = random.choice(Data)
        print(f"Compare B: {person_B['name']},{person_B['description']},{person_B['country']}")
    print(f"Against B: {person_B['name']},{person_B['description']},{person_B['country']}")
    ans = input("Who has more followers:Type 'a' or 'b': ").lower()
    if ans == "a":
        if person_A["follower_count"] > person_B["follower_count"]:
            score += 1
            print(f"Your score is: {score}")
            person_A["name"] = person_A["name"]
        else:
            print(f"Your final score is: {score} ")
            print("Game Over")
            game = False
    if ans == "b":
        if person_B["follower_count"] > person_A["follower_count"]:
            score += 1
            print(f"Your score is: {score}")
            person_A["name"] = person_B["name"]
        else:
            print(f"Your final score is: {score} ")
            print("Game Over")
            game = False






