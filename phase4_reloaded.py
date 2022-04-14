#Information before using program
print('Welcome to the Efficiency Calculator.\n')
print('Here, you will enter the stats and information about a player and this program will determine if said player is efficient, is almost efficient, or not efficient yet.\n')
print('The determination for this is simply looking at the statistics. If the player is having between 45+ field goal percentage, 35+ three point percentage, and 80+ free throw percentage . We are not taking anything else into account, so do not be mad if your favorite player is not considered efficient.\n')
print('Enter the information of a player below.\n')

#variables that represent the players stats
#loop so user can keep entering players as they want
n = int(input('How many players are you entering?: ')) #determines how long the loop goes for
i = 0 
while i < n:
    player_name = input('Name of player: ')
    player_FG = int(input('Field Goal Percentage: '))
    player_TPP = int(input('Three Point Percentage: '))
    player_FT = int(input('Free Throw Percentage: '))
    
#Conditional statements nested inside the loop to determine which player goes into which file
    if 45 <= player_FG and 35 <= player_TPP and 80 <= player_FT :
        with open ('e.txt', 'a+') as file:
            print(player_name + ' is efficient! \n')
            file.write(player_name + '\n')
            
    elif 80 <= player_FT and player_FG < 45 and player_TPP < 35:
        with open ('GFT.txt', 'a+') as file:
            print(player_name + ' is a great free throw shooter! \n')
            file.write(player_name + '\n')
            
    elif 35 <= player_TPP and player_FG < 45 and player_FT < 80:
        with open ('G3P.txt', 'a+') as file:
            print(player_name + ' is a great 3P shooter! \n')
            file.write(player_name + '\n')
            
    elif 45 <= player_FG and player_TPP < 35 and player_FT < 80:
        with open ('GFG.txt', 'a+') as file:
            print(player_name + ' is a great in the paint/mid range area! \n')
            file.write(player_name + '\n')
            
    elif player_FG < 45 and player_TPP < 35 and player_FT < 80:
        with open ('non_e.txt', 'a+') as file:
            print(player_name + ' is NOT very efficient! \n')
            file.write(player_name + '\n')
    else:
        print('Seems this player is missing one or more of the requirements to fit into one of these caterogories')
        with open ('other_players.txt', 'a+') as file:
            file.write(player_name + '\n')
    i += 1

#reads the superstar file and prints all of the players who are efficient
f = open("e.txt", "r")
print('Here are all the superstars: \n' + f.read() + '\n')
