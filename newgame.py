#! python3

DESC = 'desc'
DIRDESC = 'directiondesc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
UDESC = 'updesc'
DOWN = 'down'
DDESC = 'downdesc'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'

SCREEN_WIDTH = 40


worldRooms = {
    'Town Square': {
        DESC: 'The town square is a large open space with a fountain in the center. Streets lead in all directions.',
        NORTH: 'North Y Street',
        EAST: 'East X Street',
        SOUTH: 'South Y Street',
        WEST: 'West X Street',
        DIRDESC: ['To the north, Y street is just in view.',
                'To the east, X street is just in view.',
                'To the south, Y street is just in view.',
                'To the west, X street is just in view.'],
        GROUND: ['Welcome Sign', 'Fountain']},

    'North Y Street': {
        DESC: 'The northern end of Y Street has really gone down hill. Pot holes are everywhere, as are stray cats, rats, and wombats.',
        SOUTH: 'Town Square',
        DIRDESC: ["NONE",
                "NONE",
                "Town square to south,",
                "NONE"],
        GROUND: []},

}

worldItems = {
    'Welcome Sign': {
        GROUNDDESC: 'A welcome sign stands here.',
        SHORTDESC: 'a welcome sign',
        LONGDESC: 'The welcome sign reads, "Welcome to this text adventure demo. You can type "help" for a list of commands to use. Be sure to check out Al\'s cool programming books at http://inventwithpython.com"',
        TAKEABLE: False,
        DESCWORDS: ['welcome', 'sign']},

    'Fountain': {
        GROUNDDESC: 'A bubbling fountain of green water.',
        SHORTDESC: 'a fountain',
        LONGDESC: 'The water in the fountain is a bright green color. Is that... gatorade?',
        TAKEABLE: False,
        DESCWORDS: ['fountain']},

}



location = 'Town Square'
inventory = ['README Note', 'Sword', 'Donut']
showFullExits = True

import cmd, sys, textwrap

def displayLocation(loc):
    # room name
    print(loc)

    # print room description
    print(worldRooms[loc][DESC], end='\n')

    # print exits
    exits = []
    if showFullExits:
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction in worldRooms[loc].keys():
                exits.append(direction.title())
        if len(worldRooms[loc][DIRDESC]) > 0:
            for dir in worldRooms[loc][DIRDESC]:
                if dir == "NONE":
                    print(None)
                else:
                    print(dir,end=' ')
                # print(' '.join(textwrap.wrap(dir, SCREEN_WIDTH)),end=' ')
        print("")


    # print room items
    if len(worldRooms[loc][GROUND]) > 0:
        for item in worldRooms[loc][GROUND]:
            print(worldItems[item][GROUNDDESC], end='\n')

    else:
        print('Exits: %s' % ' '.join(exits))


def moveDirection(direction):
    global location

    if direction in worldRooms[location] or direction in worldRooms:
        # print('You move to the %s.' % direction)
        # location = worldRooms[location][direction]
        # location = worldRooms[direction]
        displayLocation(direction)
    else:
        print('You cannot move in that direction')



# TEMPORARY CODE:
while True:
    displayLocation(location)
    response = input("\n> ")
    if response == 'quit':
        break
    if response.lower() in (NORTH, SOUTH, EAST, WEST, UP, DOWN) or response.lower() in (NORTH[:1], SOUTH[:1], EAST[:1], WEST[:1], UP[:1], DOWN[:1]):
        if(response.lower() in worldRooms[location]):
            moveDirection(worldRooms[location][response.lower()])

        # moveDirection(response)
    # if response.lower() in ("north", "east", West):
    #
    #     moveDirection(worldRooms[direction.upper())
