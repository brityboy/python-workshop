from datetime import datetime
import os
import sys


def read_game_info(filename):
    '''
    INPUT: string
    OUTPUT: tuple of string, string, string, int, int

    Given the filename of a game, return the time, team names and score for the
    game. Return these values:

        time: string representing time of game
        team1: first team name
        team2: second team name
        score1: score of first team
        score2: score of second team
    '''
    with open(filename, 'r') as file:
        data = file.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].replace('\n', '')
    return (data[0], data[3][0:data[3].find('-')-1], data[3][data[3].find('-')+2:], int(data[4][0:data[4].find('-')]), int(data[4][data[4].find('-')+1:]))


def display_game(time, team, other, team_score, other_score):
    '''
    INPUT: string, string, string, int, int
    OUTPUT: string

    Given the time, names of the teams and score, return a one line string
    presentation of the results.
    expected1 = '22 MAR 2015 - 19:00: Barbados (0) - US Virgin Islands (1)'
    expected2 = 'Mar 22: Barbados (0) - US Virgin Islands (1)'
    '''
    print_string = '{}: {} ({}) - {} ({})'
    #return time+": "+team+' ('+str(team_score)+') - '+other+' ('+str(other_score)+')'
    return print_string.format(time, team, team_score, other, other_score)


def display_summary(team, data, detailed=False):
    '''
    INPUT: string, list of tuples, bool
    OUTPUT: string

    Given the data (list of tuples of game data), return a string containing
    the summary of results for the given team. This includes # games played,
    # wins, # losses, # ties, and # goals scored.

    If detailed is True, also include in the string all the games for the given
    team.
    '''

    games_played = 0
    wins = 0
    losses = 0
    ties = 0
    goals = 0

    for line in data:
        if team == line[1] or team == line[2]:
            games_played += 1
        if team == line[1]:
            if line[3] > line [4]:
                wins += 1
            elif line[3] == line[4]:
                ties += 1
            elif line[3] < line[4]:
                losses += 1
            goals += line[3]
        if team == line[2]:
            if line[4] > line[3]:
                wins += 1
            elif line[4] == line[3]:
                ties += 1
            elif line[4] < line[3]:
                losses += 1
            goals += line[4]

    #return team+' played a total of '+str(games_played)+' games '+'str(wins)+ ' win(s), '+str(losses)+' loss(es) '+str(ties)+' tie(s), '+str(goals)+' total goal(s)'
    printstring = '{} played a total of {} games.\n{} win(s), {} loss(es), {} tie(s), {} total goal(s)'
    if detailed==True:
        games = []
        for line in data:
            if team in line:
                games.append(line)
    return printstring.format(team, games_played, wins, losses, ties, goals), games



def run(directory, team):
    '''
    INPUT: string, string
    OUTPUT: None

    Given the directory where the data is stored and the team name of interest,
    read the data from the directory and display the summary of results for the
    given team.
    '''
    data = []
    for filename in os.listdir(directory):
        data.append(read_game_info(os.path.join(directory, filename)))
    print display_summary(team, data, detailed=True)


def main():
    '''
    INPUT: None
    OUTPUT: None

    Get the directory name and team name from the arguments given. If arguments
    are valid, display the summary of results. Otherwise, exit the program.
    '''
    error_message = "Usage: python worldcup.py directory team\n" \
                    "       e.g. python worldcup.py worldcup USA"
    if len(sys.argv) != 3:
        print error_message
        exit()
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print "{0} is not a valid directory.".format(directory)
        print error_message
        exit()
    team = sys.argv[2]
    run(directory, team)


if __name__ == '__main__':
    main()
