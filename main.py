from gamedata import data
import random
from art import logo, vs
score=0
def get_random_data():
    return random.choice(data)

def print_result(point):
    print(f"You lose | Score : {point}")

def compare_data(player_one,player_two):
    print(f"A :{player_one['name']} who is a {player_one['description']} from {player_one['country']}")
    print(vs)
    print(f"B :{player_two['name']} who is {player_two['description']} from {player_two['country']}")
    choice = input("Who has the more followers A or B :")
    return choice.lower(),player_one,player_two

def find_follower(player_one,player_two):
    return player_one['follower_count'],player_two['follower_count']
 
def input_choice_loop(choice,player_one,player_two,flag,point):
    player_one_follower,player_two_follower = find_follower(player_one,player_two)
    flag=False
    if choice=='a':
        if player_one_follower > player_two_follower:
            player_two = get_random_data()
            point+=1
            return player_one,player_two,flag,point
        else:
             #exit statement
            print_result(point)
            flag=True
            return player_one,player_two,flag,point
            
    elif choice=='b':
        if player_one_follower < player_two_follower:
            player_one = get_random_data()
            point+=1
            return player_one,player_two,flag,point
        else:
            print_result(point)
            flag=True
            return player_one,player_two,flag,point
             #exit statement
    else:
        print("Its a invalid choice")

print(logo)
flag=False
p_one = get_random_data()
p_two = get_random_data()
while not flag:
    input_choice,p_one, p_two = compare_data(p_one,p_two)
    p_one,p_two,flag,score =input_choice_loop(input_choice,p_one,p_two,flag,score)
    #p_one,p_two=select_winner(p_one,p_two)
