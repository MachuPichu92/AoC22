# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:46:48 2022

@author: vaneb
"""


with open('02.txt') as f:
    
    games =  f.read().splitlines() 
    
#scores
rock = 1
paper = 2
scissors = 3

win = 6
tie = 3
loose = 0


#PART I
outcomes = {'A X': 4,
            'A Y': 8,
            'A Z': 3,
            'B X': 1,
            'B Y': 5,
            'B Z': 9,
            'C X': 7,
            'C Y': 2,
            'C Z': 6}


my_score = 0


for game in games:
    
    for k, v in outcomes.items():
        if game == k:
            my_score += v


print("Part I result is: {}".format(my_score))


#PART II

my_score = 0

for game in games:
    
    opp = game[0]
    me  = game[-1]
   
    if opp == 'A':# rock
        
        if me == 'X': #i need to lose , show scissors
            my_score += (scissors + loose)
            
        elif me == 'Y': #tie, show rock
            my_score += (rock + tie)
            
        else: #need to win
            my_score += (paper + win)
            
    elif opp == 'B': #paper
        
        if me == 'X': #loose
            my_score += (rock + loose) 
           
        elif me == 'Y': #draw
            my_score += (paper + tie)
            
        else:
            my_score += (scissors + win)
            
    else: # scissors
        
        if me == 'X': #lose
            my_score += (paper + loose) 
           
        elif me == 'Y': #draw
            my_score += (scissors + tie)
            
        else: #win
            my_score += (rock + win)


print("Part II result is: {}".format(my_score))

            
            
        