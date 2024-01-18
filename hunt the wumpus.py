"""This program utilizes dictionaries to track caves available to the player along with locations of items/characters in the game. All locations of items/characters in the game are randomized but will never overlap. The player will encounter up to two bats, two pits, two floating potions, and the wumpus. To win the player must kill the wumpus with one of their grenades. A floating potion can save a player if they walk into a cave with a pit, but if the player does not leave the cave or kill the wumpus in the next turn if the player has no more potions they will fall into the pit."""

import random

win = False
player_cave = random.randint(1,20)
grenades = 5
wumpus_alive = True
float_potion = 0
caves = {
    1 : 'nothing',
    2 : 'nothing',
    3 : 'nothing',
    4 : 'nothing',
    5 : 'nothing',
    6 : 'nothing',
    7 : 'nothing',
    8 : 'nothing',
    9 : 'nothing',
    10 : 'nothing',
    11 : 'nothing',
    12 : 'nothing',
    13 : 'nothing',
    14 : 'nothing',
    15 : 'nothing',
    16 : 'nothing',
    17 : 'nothing',
    18 : 'nothing',
    19 : 'nothing',
    20 : 'nothing'
}
cave_connections = {
    1 : '2 5 8',
    2 : '1 3 10',
    3 : '2 4 12',
    4 : '3 5 14',
    5 : '1 4 6',
    6 : '5 7 15',
    7 : '6 8 17',
    8 : '1 7 9',
    9 : '8 10 18',
    10 : '2 9 11',
    11 : '10 12 19',
    12 : '3 11 13',
    13 : '12 14 20',
    14 : '4 13 15',
    15 : '6 14 16',
    16 : '15 17 20',
    17 : '7 16 18',
    18 : '9 17 19',
    19 : '11 18 20',
    20 : '13 16 19',
}

def check_senses(current_cave):
    global cave_connections
    global caves
    
    #connected_caves variable is only what the player's cave is connected to and is put into a list
    connected_caves = cave_connections[current_cave].split()
    for i in range(len(connected_caves)):
        #iterates through list checking each number for anything the player could encounter
        if caves[int(connected_caves[i])] != 'nothing':
            if caves[int(connected_caves[i])] == 'wumpus':
                print('You smell something terrible nearby.')
            elif caves[int(connected_caves[i])] == 'bat':
                print('You hear a rustling.')
            elif caves[int(connected_caves[i])] == 'pit':
                print('You feel a cold wind blowing from a nearby cavern.')

def bat_cave():
    global player_cave
    player_cave = random.randint(1,20)
    print('A bat picked you up and brought you to a random cave.')
    flow_control = input('(press enter to continue)')
    
def throw_move():
    global throw_or_move
    global player_cave
    global cave_connections
    global caves
    global win
    global grenades
    global float_potion
    
    if throw_or_move.upper() == 'T':
        grenades = grenades - 1
        while True:
            try:
                grenade_cave = int(input('Which cave? '))
            except ValueError or TypeError:
                print('Please enter a number.')
            else:
                #checking if the cave the player entered is connected to player's current cave
                if str(grenade_cave) in cave_connections[player_cave]:
                    break
                else:
                    print('No current tunnels lead to that cave.')
        if caves[grenade_cave] == 'wumpus':
            print('You hit the wumpus! You win!')
            wumpus_alive == False
            win = True
        else:
            print('Missed.')
    elif throw_or_move.upper() == 'M':
        while True:
            try:
                move_cave = int(input('Which cave? '))
            except ValueError or TypeError:
                print('Invalid input.')
            else:
                if str(move_cave) in cave_connections[player_cave]:
                    break
                else:
                    print('No current tunnels lead to that cave.')
        player_cave = move_cave
        if caves[move_cave] == 'bat':
            bat_cave()
        elif caves[move_cave] == 'potion':
            print('You found a floating potion! It can help you in times of trouble.')
            flow_control = input('(press enter to continue)')
            float_potion = float_potion + 1
            #takes potion off of map and will not replenish
            caves[move_cave] = 'nothing'
    else:
        print('Invalid input.')

def reset():
    global grenades
    global caves
    global win
    global wumpus_alive
    global float_potion
    
    grenades = 5
    caves = {
        1 : 'nothing',
        2 : 'nothing',
        3 : 'nothing',
        4 : 'nothing',
        5 : 'nothing',
        6 : 'nothing',
        7 : 'nothing',
        8 : 'nothing',
        9 : 'nothing',
        10 : 'nothing',
        11 : 'nothing',
        12 : 'nothing',
        13 : 'nothing',
        14 : 'nothing',
        15 : 'nothing',
        16 : 'nothing',
        17 : 'nothing',
        18 : 'nothing',
        19 : 'nothing',
        20 : 'nothing'
    }
    win = False
    wumpus_alive = True
    float_potion = 0

def set_positions():
    global wumpus
    global pit1
    global pit2
    global bat1
    global bat2
    global potion_pos1
    global potion_pos2
    
    #while true loops are used to ensure there is no overlapping of items/characters
    while True:
        wumpus = random.randint(1,20)
        if wumpus != player_cave:
            break
        else:
            wumpus = random.randint(1,20)
    while True:
        pit1 = random.randint(1,20)
        if pit1 != wumpus and pit1 != player_cave:
            break
        else:
            pit1 = random.randint(1,20)
    while True:
        pit2 = random.randint(1,20)
        if pit2 != wumpus and pit2 != player_cave and pit2 != pit1:
            break
        else:
            pit2 = random.randint(1,20)
    while True:
        bat1 = random.randint(1,20)
        if bat1 != wumpus and bat1 != pit1 and bat1 != pit2 and bat1 != player_cave:
            break
        else:
            bat1 = random.randint(1,20)
    while True:
        bat2 = random.randint(1,20)
        if bat2 != wumpus and bat2 != pit1 and bat2 != pit2 and bat2 != bat1 and bat2 != player_cave:
            break
        else:
            bat2 = random.randint(1,20)
    while True:
        potion_pos1 = random.randint(1,20)
        if potion_pos1 != wumpus and potion_pos1 != pit1 and potion_pos1 != pit2 and potion_pos1 != bat1 and potion_pos1 != player_cave and potion_pos1 != bat2:
            break
        else:
            potion_pos = random.randint(1,20)
    while True:
        potion_pos2 = random.randint(1,20)
        if potion_pos2 != wumpus and potion_pos2 != pit1 and potion_pos2 != pit2 and potion_pos2 != bat1 and potion_pos2 != player_cave and potion_pos2 != bat2 and potion_pos2 != potion_pos1:
            break
        else:
            potion_pos = random.randint(1,20)
    caves[wumpus] = 'wumpus'
    caves[pit1] = 'pit'
    caves[pit2] = 'pit'
    caves[bat1] = 'bat'
    caves[bat2] = 'bat'
    caves[potion_pos1] = 'potion'
    caves[potion_pos2] = 'potion'



def main():
    global throw_or_move
    global player_cave
    global cave_connections
    global caves
    global win
    global grenades
    global float_potion
    
    while True:
        reset()
        set_positions()

        
        while True:
            print('\nYou are in cave', player_cave, '\nTunnels lead to caves:', cave_connections[player_cave], '\n',)
            check_senses(player_cave)
            
            while True:
                try:
                    throw_or_move = input('Would you like to throw a grenade or move?(T or M) ')
                except ValueError or TypeError:
                    print('Invalid input.')
                else:
                    break
            
            throw_move()
            
            #always checks win first
            if win == True:
                break
            if caves[player_cave] == 'wumpus':
                print('The wumpus ate you. You lose!')
                break
            if caves[player_cave] == 'pit':
                if float_potion > 0:
                    #player can have up to two potions at once
                    float_potion = float_potion - 1
                    print('You walked into a pit but your floating potion saved you.')
                    print('You now have', float_potion, 'potion(s)')
                    #flow_control makes sure player acknowledges the loss of a potion
                    flow_control = input('(press enter to continue)')
                else:
                    print('You fell into a pit. You lose!')
                    break
            if grenades <= 0 and wumpus_alive == True:
                print('Out of grenades. You lose!')
                break
        restart = input('Play again?(Y or N) ')
        if restart.upper() == 'N':
            break




print('~~~Hunt the Wumpus~~~')
main()