# soccer game: penalty shootout
# goal is printed every move of the game, along with the shot and goalkeeper
# goalkeeper will change position every move:
#    if the position matches the shot's (determined by the player's input), the player misses the shot, losing 1 point
#    if the shot's position differs from the goalkeeper's posisiton, a goal is scored 
# after missing 5 shots, the player loses and the game ends (with a message)
# The player wins by scoring 3 goals, which also ends the game (with a message)
import random
import math

def soccer_shootout():

    missed_shots = 0                           # increase by 1 every missed shot
    goals_scored = 0
    show_goal = 0
    show_miss = 0
    score_index = 0 # every move, substitute goals scored with 'O', otherwise substitute with 'X'
    center_save = [' []==================[]', ' ||  +     ⚫     +  ||', ' ||       /  \       ||', ' ||  +    \()/    +  ||', ' ||        }{        ||', ' ||  +     /\     +  ||', ' ||      _/  \_      ||', '////////////////////////']                              
    left_save = [' []==================[]', ' ||  ⚫     +     +  ||', ' || /  \             ||', ' || \()/    +     +  ||', ' ||  }{              ||', ' ||  /\     +     +  ||', ' ||_/  \_            ||', '////////////////////////']
    right_save = [' []===================[]', ' ||  +     +     ⚫   ||', ' ||             /  \  ||', ' ||  +     +    \()/  ||', ' ||              }{   ||', ' ||  +     +     /\   ||', ' ||            _/  \_ ||', '/////////////////////////']
    goal_center = [' []==================[]', ' ||  +   >>⚫<<   +  ||', ' ||                  ||', ' ||  +     ()     +  ||', ' ||      \/}{\/      ||', ' ||  +     /\     +  ||', ' ||      _/  \_      ||', '////////////////////////']
    goal_left = [' []==================[]', ' ||  +      +     +  ||', ' ||                  ||', ' ||  ()     +  >>⚫<<||', ' ||\/}{\/            ||', ' ||  /\     +     +  ||', ' ||_/  \_            ||', '////////////////////////']
    goal_right = [' []===================[]', ' ||  +   >>⚫<<       ||', ' ||            \   \  ||', ' ||  +     +    \()/  ||', ' ||              }{   ||', ' ||  +     +     /\   ||', ' ||            _/  \_ ||', '/////////////////////////']
    win = False                                                                         # for each position the goalie takes, theres a list that will print on the shell (separated by \n)
    print('Welcome to Soccer Shootout !')
    print('\n')
    level = input('Choose the number of shots to take (5, 7 or 9)')
    score_board = ['_']*int(level)
    victory_score = math.ceil(int(level)/2)

    while score_index < len(score_board) + 1:
        print('\n')
        play_direction = input('Choose the direction of the shot (left, center or right)')
        save_randomizer = random.randint(0,12)
        if save_randomizer in range (0,4):
            goalie_pos = 'left' 
        elif save_randomizer in range (5,8):
            goalie_pos = 'center'
        else:
            goalie_pos = 'right'                                                        #the random module passes an arbitrary integer which determines the goalie's position: if the number returned is between 0 - 33 (left); 34 - 66 (center); 67 -100 (right). 
        if play_direction in goalie_pos:
            missed_shots+=1
            score_board[score_index] = '[X]'
            score_index+=1
            print(' '.join(score_board))
            show_miss = '{}_save'.format(play_direction)
            if str(center_save) == show_miss:
                print('\n'.join(goal_center))
            elif str(left_save) == show_miss:
                print('\n'.join(left_save))
            else:
                print('\n'.join(right_save))
            print('MISSED SHOT!')
        else:
            score_board[score_index] = '[O]'
            goals_scored+=1
            score_index+=1
            print(' '.join(score_board))
            show_goal = 'goal_{}'.format(play_direction)
            if str(goal_center) == show_goal:
                print('\n'.join(goal_center))
            elif str(goal_left) == show_goal:
                print('\n'.join(goal_left))
            else:
                print('\n'.join(goal_right))
            print('GOAL !!!')
        if goals_scored == victory_score: 
            print('You won! Check out the final score!') 
            print('Goals scored: {}'.format(goals_scored))
            print('Shots missed: {}'.format(missed_shots))
            win = True
            break
        if missed_shots >= victory_score:
            print('You lost! Better luck next time!') 
            print('Goals scored: {}'.format(goals_scored))
            print('Shots missed: {}'.format(missed_shots))
            break

soccer_shootout()












        
        
        
        
        
