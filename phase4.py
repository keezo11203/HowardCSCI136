#Information before using program
print('Welcome to the Superstar Player Determinator.\n')
print('Here, you will enter the stats and information about a player and this program will determine if said player is a superstar, is close to superstardom, or not a superstar yet.\n')
print('The determination for this is simply looking at the statistics. If the player is averaging at least 20 points per game, having exactly or over 50% field goal percentage, 40% three-point field goal percentage, and 90% free throw percentage. We are not taking anything else into account, so do not be mad if your favorite player is not a superstar.\n')
print('Enter the information of a player below.\n')

#variables that represent the players stats
#loop so user can keep entering players as they want
n = int(input('How many players are you entering?: ')) #determines how long the loop goes for
i = 0 
while i < n:
    player_name = input('Name of player: ')
    player_PPG = int(input('Points per game: '))
    player_FG = int(input('Field Goal Percentage: '))
    player_TPP = int(input('Three Point Percentage: '))
    player_FT = int(input('Free Throw Percentage: '))
    
#Conditional statements to determine which player goes into which file
    if player_PPG >= 20 and player_FG >= 50 and player_TPP >= 40 and player_FT >=90: 
        with open ('superstars.txt', 'a+') as file:
            print(player_name + ' is a superstar! \n')
            file.write(player_name + '\n')
            
    elif 15 <= player_PPG < 20 and 45 <= player_FG < 50 and 35 <= player_TPP < 40 and 80 <= player_FT < 90:
        with open ('almost_super.txt', 'a+') as file:
            print(player_name + ' is almost a superstar! \n')
            file.write(player_name + '\n')
        
    elif player_PPG < 15 and player_FG < 45 and player_TPP < 35 and player_FT < 80:
        with open ('non_super.txt', 'a+') as file:
            print(player_name + ' is NOT a superstar! \n')
            file.write(player_name + '\n')
    else:
        print('Seems this player is missing one or more of the requirements to fit into one of these caterogories')
        with open ('other_players.txt', 'a+') as file:
            file.write(player_name + '\n')
    i += 1
#reads the superstar file and prints all of the players
f = open("superstars.txt", "r")
print('Here are all the superstars: \n' + f.read() + '\n')
