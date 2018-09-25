import random
import time


DESC = 'desc'
DIRDESC = 'directiondesc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'
CANGO = "cango"
ISWEAPON = "itemisweapon"
DAMAGE = "itemdamage"
NPCHEALTH = "charhealth"
NPCDROPLOOT = "chardroploot"
NPCDAMAGE = "chardamage"
NPCFIGHTPROB = "charprob"
NPCSHOWPROB = "npcshowprobability"
NPCDESC = "npcdescription"
NPCISENEMY = "isenemy"
NPC = "roomnpcs"


class Rooms():

    def __init__(self):
        None

        self.worldRooms = {
            'Armory': {
                DESC: 'There are boxes of gear everywhere.',
                NPC: ["Soldier","Bounty Hunter"],
                CANGO: ["North", "East", "West"],
                NORTH: "Hallway",
                EAST: 'Docking Station',
                WEST: 'Storage Closet',
                DIRDESC: ['To the north is the hallway.',
                        'To the east is the docking station.',
                        '',
                        'To the west is the storage closet.'],
                GROUND: ['M451 Blaster', 'Ammo Pack']},

            'Hallway': {
                DESC: 'You are in a long hallway.',
                CANGO: ["North", "South", "West"],
                NORTH: "Living Quarters",
                SOUTH: 'Armory',
                WEST: "Deck",
                DIRDESC: ["To the north is the living quarters.",
                        "",
                        "To the south is the armory.",
                        "To the west is the deck."],
                GROUND: []},

            'Docking Station': {
                DESC: "You are in the ship's main docking center. There are spaceships everywhere.",
                NPC: ["Flight Captain"],
                CANGO: ["East", "West"],
                EAST: "Spaceship",
                WEST: "Armory",
                DIRDESC: ["",
                        "To the east one spaceship catches your eye.",
                        "",
                        "To the west is the armory."],
                GROUND: ["Flight Manuel", "Fuel", "Spaceship"]},

        }

        self.worldItems = {
            'M451 Blaster': {
                GROUNDDESC: 'A M451 Blaster lays on the ground.',
                SHORTDESC: 'a M451 Blaster',
                LONGDESC: 'A general blaster. Not anything special.',
                TAKEABLE: True,
                ISWEAPON: True,
                DAMAGE: 5,
                DESCWORDS: ['blaster', 'm451 blaster']},

            'Lightsaber': {
                GROUNDDESC: 'A lightsaber is sitting on the ground.',
                SHORTDESC: 'a lightsaber',
                LONGDESC: 'A blue blade lightsaber.',
                TAKEABLE: True,
                ISWEAPON: True,
                DAMAGE: 25,
                DESCWORDS: ['lightsaber']},

            'Ammo Pack': {
                GROUNDDESC: 'A pack of ammo lays on the floor.',
                SHORTDESC: 'a pack of ammo',
                LONGDESC: 'A pack of 50 ammo rounds',
                TAKEABLE: True,
                ISWEAPON: False,
                DESCWORDS: ['ammo', 'ammo pack']},

            'Shiny Object': {
                GROUNDDESC: 'A shiny object can be seen in the corner of the room.',
                SHORTDESC: 'a shiny object',
                LONGDESC: 'It appears to be some sort of crystal.',
                TAKEABLE: True,
                ISWEAPON: False,
                DESCWORDS: ['crystal', 'shiny']},

            'Flight Manual': {
                GROUNDDESC: 'A little booklet lays discareded on the ground in front of you.',
                SHORTDESC: 'a flight manual',
                LONGDESC: 'You read the manual.',
                TAKEABLE: True,
                ISWEAPON: False,
                DESCWORDS: ['manual', 'guide']},

            'Fuel': {
                GROUNDDESC: 'A container of fuel is on the ground.',
                SHORTDESC: 'a fuel container',
                LONGDESC: 'A large container of ship fuel.',
                TAKEABLE: True,
                ISWEAPON: False,
                DESCWORDS: ['fuel', 'gas']},

            'Spaceship': {
                GROUNDDESC: 'There is a very nice looking spaceship here.',
                SHORTDESC: 'a spaceship',
                LONGDESC: 'A shiny, silver spaceship with blue accents.',
                TAKEABLE: False,
                ISWEAPON: False,
                DESCWORDS: ['spaceship', 'ship']},

        }

        self.worldCharacters = {
            'Bounty Hunter': {
                NPCDESC: 'A Mandelorian bounty hunter appears out of nowhere and points his gun at you.',
                NPCISENEMY: True,
                NPCHEALTH: 20,
                NPCDROPLOOT: ["Mandelorian Helmet"],
                NPCDAMAGE: 5,
                NPCFIGHTPROB: 35,
                NPCSHOWPROB: 15},

            'Soldier': {
                NPCDESC: 'A soldier is loading his gun.',
                NPCISENEMY: False,
                NPCSHOWPROB: 100},

            'Flight Captain': {
                NPCDESC: 'The flight captain is surverying the area from a ledge above.',
                NPCISENEMY: False,
                NPCSHOWPROB: 100},

        }

        self.location = 'Armory'
        self.health = 100
        self.showFullExits = True
        self.taken = [""]
        self.inventory = ['Chest Guard', 'Leg Guards', 'Gloves', 'Communicator']
        self.ammo = 0
        self.abilities = [""]
        self.repeat = True
        self.enemyinroom = False
        self.currentenemy = [""]
        self.damage = 0
        self.readRoom(self.location)

    # def Armory(self):
    #     self.npc = ["Soldier"]
    #     self.npcDescription = ["A soldier stands next to you loading his weapon."]
    #     self.canfight = False
    #     self.isfighting = False
    #     self.cangoNorth = True
    #     self.cangoEast = True
    #     self.cangoSouth = False
    #     self.cangoWest = True
    #     self.fought = False
    #     self.randomAttack = random.randint(0,20)
    #     # when attack sequence is true
    #     if(self.randomAttack == 1):
    #         print(self.ammo)
    #         if(int(self.ammo) > 0) and ("Blaster" in self.taken):
    #             self.npc = ["Soldier"]
    #             self.enemy = ["Bounty Hunter"]
    #             self.randprobtotal = 25
    #             self.randprobsplit = 9
    #             self.enemypower = 5
    #             self.reward = "Helmet"
    #             self.rewardMessage = "You pick up the Mandelorian's Helmet and put it on."
    #             self.npcDescription = ["A soldier is on the ground, hit by blaster fire."]
    #             self.attackerdecription = "A bounty hunter looks straight at you. He raises his gun and points it straight at you."
    #             self.fightYouHitAttacker = "You fire your blaster, the bounty hunter is hit!"
    #             self.fightYouHitAttackerMiss = "You fire your blaster but the bounty hunter dodges your shot!"
    #             self.fightAttackerHitYou = "The bounty hunter fires and you are hit!"
    #             self.fightAttackerHitYouMiss = "The bounty hunter fires but but misses you!"
    #             self.fightAttackerDead = "As you fire your gun the bounty hunter breathes his last breath and falls to the ground."
    #             self.fightoutofammo = "You have ran out of ammo!"
    #             self.fightYouDead =  "You are hit and fall to the ground."
    #             self.enemyHealth = 20
    #             self.canfight = True
    #             self.isfighting = True
    #             self.cangoNorth = False
    #             self.cangoEast = False
    #             self.cangoSouth = False
    #             self.cangoWest = False
    #             self.fought = False
    #     else:
    #         self.npc = ["Soldier"]
    #         self.npcDescription = ["A soldier stands next to you loading his weapon."]
    #         self.canfight = False
    #         self.isfighting = False
    #         self.cangoNorth = True
    #         self.cangoEast = True
    #         self.cangoSouth = False
    #         self.cangoWest = True
    #         self.fought = False
    #     self.roomName = "Armory"
    #     self.roomDescription = "There are boxes of gear everywhere."
    #     self.roomItems = ['Blaster', 'Ammo']
    #     self.itemsDescription = ["An M451 Blaster is sitting on the ground.", "An ammo pack lays on the floor."]
    #     j = len(self.taken)
    #     try:
    #         while j > 0:
    #             alreadytakenItems = [i for i in self.taken if i in self.roomItems]
    #             alreadytakenIndex = self.roomItems.index(alreadytakenItems[0])
    #             self.roomItems.remove(alreadytakenItems[0])
    #             del self.itemsDescription[alreadytakenIndex]
    #             j = j - 1
    #     except TypeError:
    #         print(None)
    #
    #     self.exits = ['Hallway','Docking Bay','','Storage Closet']
    #     self.exitsDescriptions = ['To the north is a long hallway.','To the east is the docking bay.','','To the west is a storage closet.']
    #
    #     self.roomfunc()
    #
    # def Hallway(self):
    #     self.roomName = "Hallway"
    #     self.roomDescription = "You are in a long hallway."
    #     self.roomItems = None
    #     self.itemsDescription = None
    #     j = len(self.taken)
    #     try:
    #         while j > 0:
    #             alreadytakenItems = [i for i in self.taken if i in self.roomItems]
    #             alreadytakenIndex = self.roomItems.index(alreadytakenItems[0])
    #             self.roomItems.remove(alreadytakenItems[0])
    #             del self.itemsDescription[alreadytakenIndex]
    #             j = j - 1
    #     except TypeError:
    #         print(None)
    #     self.npc = None
    #     self.npcDescription = None
    #     self.exits = ['Living Quarters',None,'Armory','Deck']
    #     self.exitsDescriptions = ['To the north is the living quarters.','','To the south is the armory.',"To the west is the ship's main deck."]
    #     self.canfight = False
    #     self.isfighting = False
    #     self.cangoNorth = True
    #     self.cangoEast = False
    #     self.cangoSouth = True
    #     self.cangoWest = True
    #     self.roomfunc()
    #
    # def DockingBay(self):
    #     self.roomName = "Docking Bay"
    #     self.roomDescription = "There are ships everywhere."
    #     self.roomItems = ['Manual', 'Fuel']
    #     self.itemsDescription = ["In the corner of the bay, a ship control manuel sits.", ""]
    #     j = len(self.taken)
    #     try:
    #         while j > 0:
    #             alreadytakenItems = [i for i in self.taken if i in self.roomItems]
    #             alreadytakenIndex = self.roomItems.index(alreadytakenItems[0])
    #             self.roomItems.remove(alreadytakenItems[0])
    #             del self.itemsDescription[alreadytakenIndex]
    #             j = j - 1
    #     except TypeError:
    #         print(None)
    #     self.npc = ["Soldier"]
    #     self.npcDescription = ["A soldier stands next to you loading his weapon."]
    #     self.exits = ['Hallway','Docking Bay','','Storage Closet']
    #     self.exitsDescriptions = ['To the north is a long hallway.','To the east is the docking bay.','','To the west is a storage closet.']
    #     self.canfight = False
    #     self.isfighting = False
    #     self.cangoNorth = True
    #     self.cangoEast = True
    #     self.cangoSouth = False
    #     self.cangoWest = True
    #     self.roomfunc()


    def readRoom(self, loc):
        self.enemyinroom = False
        print(loc)
        print(self.worldRooms[loc][DESC], end='\n')
        for dir in self.worldRooms[loc][DIRDESC]:
            if dir != "":
                print(dir, end=' ')
        j = len(self.taken)
        try:
            while j > 0:
                alreadytakenItems = ([i for i in self.taken if i in self.worldItems])
                del self.worldItems[alreadytakenItems[0]]
                j = j - 1
        except IndexError:
            None
        print("")
        for npc in self.worldRooms[self.location][NPC]:
            try:
                if npc in self.worldCharacters:
                    if int(self.worldCharacters[npc][NPCSHOWPROB]) == 100:
                        print(self.worldCharacters[npc][NPCDESC],end=' ')
                        if self.enemyinroom == False:
                            if self.worldCharacters[npc][NPCISENEMY] == True:
                                self.enemyinroom = True;
                                self.currentenemy.append(str(npc))
                            else:
                                None
                        else:
                            None
                    else:
                        if self.enemyinroom == False:
                            if self.worldCharacters[npc][NPCISENEMY] == True:
                                self.enemyinroom = True;
                                self.currentenemy.append(str(npc))
                        None
            except KeyError:
                None


        print("")
        if len(self.worldRooms[loc][GROUND]) > 0:

            for item in self.worldRooms[loc][GROUND]:
                try:
                    if item not in self.taken:
                        print(self.worldItems[item][GROUNDDESC], end='\n')
                except KeyError:
                    None


        if self.enemyinroom == True:
            if "blaster" in self.inventory or "rifle" in self.inventory or "gun" in self.inventory and self.ammo > 0:
                randAttack = random.randint(0,100)
                if(randAttack >= 0 and randAttack <= int(self.worldCharacters[self.currentenemy][NPCSHOWPROB])):
                    print(self.worldCharacters[self.currentenemy][NPCDESC])
                    #self.fightsequence(self.location,self.currentenemy)
                else:
                    None
            else:
                None
        else:
            None

        self.inputLoop()


    def inputLoop(self):
        while self.repeat == True:
            self.input = input("\n> ")

            if(self.input.lower() == "north") or (self.input.lower() == "n"):
                if "North" in self.worldRooms[self.location][CANGO]:
                    self.readRoom(self.worldRooms[self.location]["north"])
                else:
                    print("You cannot go this way.")
                    self.inputloop()
            elif(self.input.lower() == "east") or (self.input.lower() == "e"):
                if "East" in self.worldRooms[self.location][CANGO]:
                    if self.worldRooms[self.location] != "Docking Bay":
                        self.readRoom(self.worldRooms[self.location]["east"])
                    else:
                        if "Flight" not in self.abilities:
                            print("Trying to fly a spaceship with no training would be suicide.")
                            self.inputLoop()
                        else:
                            self.readRoom(self.worldRooms[self.location]["east"])

                else:
                    print("You cannot go this way.")
                    self.inputloop()
            elif(self.input.lower() == "south") or (self.input.lower() == "s"):
                if "South" in self.worldRooms[self.location][CANGO]:
                    self.readRoom(self.worldRooms[self.location]["south"])
                else:
                    print("You cannot go this way.")
                    self.inputloop()
            elif(self.input.lower() == "west") or (self.input.lower() == "w"):
                if "West" in self.worldRooms[self.location][CANGO]:
                    self.readRoom(self.worldRooms[self.location]["west"])
                else:
                    print("You cannot go this way.")
                    self.inputloop()
            elif(self.input.lower() == "up") or (self.input.lower() == "u"):
                if "Up" in self.worldRooms[self.location][CANGO]:
                    self.readRoom(self.worldRooms[self.location]["up"])
                else:
                    print("You cannot go this way.")
                    self.inputloop()
            elif(self.input.lower() == "down") or (self.input.lower() == "d"):
                if "Down" in self.worldRooms[self.location][CANGO]:
                    self.readRoom(self.worldRooms[self.location]["down"])
                else:
                    print("You cannot go this way.")
                    self.inputloop()


            elif("take" in self.input.lower()):
                stripInput = self.input.title()
                strippedInput = stripInput[5:]
                item = self.getItemfromDesc(strippedInput.title(), self.worldRooms[self.location][GROUND])
                print(item)
                if self.worldItems[item][TAKEABLE] == False:
                    print('You cannot take "%s".' % (strippedInput))
                else:
                    print('You take %s.' % (self.worldItems[item.title()][SHORTDESC]))
                    self.worldRooms[self.location][GROUND].remove(item.title())
                    self.taken.append(item.title())
                    self.inventory.append(item.title())
                    if(item.title() == "Ammo Pack"):
                        self.ammo = self.ammo + 50
                    elif(self.worldItems[item.title()][ISWEAPON] == True):
                        self.damage = int(self.worldItems[item.title()][DAMAGE])
            elif("grab" in self.input.lower()):
                stripInput = self.input.title()
                strippedInput = stripInput[5:]
                item = self.getItemfromDesc(strippedInput.title(), self.worldRooms[self.location][GROUND])
                print(item)
                if self.worldItems[item][TAKEABLE] == False:
                    print('You cannot take "%s".' % (strippedInput))
                else:
                    print('You take %s.' % (self.worldItems[item.title()][SHORTDESC]))
                    self.worldRooms[self.location][GROUND].remove(item.title())
                    self.taken.append(item.title())
                    self.inventory.append(item.title())
                    if(item.title() == "Ammo Pack"):
                        self.ammo = self.ammo + 50
                    elif(self.worldItems[item.title()][ISWEAPON] == True):
                        self.damage = int(self.worldItems[item.title()][DAMAGE])
            elif("pick up" in self.input.lower()):
                stripInput = self.input.title()
                strippedInput = stripInput[8:]
                item = self.getItemfromDesc(strippedInput.title(), self.worldRooms[self.location][GROUND])
                print(item)
                if self.worldItems[item][TAKEABLE] == False:
                    print('You cannot take "%s".' % (strippedInput))
                else:
                    print('You take %s.' % (self.worldItems[item.title()][SHORTDESC]))
                    self.worldRooms[self.location][GROUND].remove(item.title())
                    self.taken.append(item.title())
                    self.inventory.append(item.title())
                    if(item.title() == "Ammo Pack"):
                        self.ammo = self.ammo + 50
                    elif(self.worldItems[item.title()][ISWEAPON] == True):
                        self.damage = int(self.worldItems[item.title()][DAMAGE])

            elif("drop" in self.input.lower()):
                stripInput = self.input.title()
                strippedInput = stripInput[5:]

                invDescWords = self.getAllDescWords(self.inventory)

                if strippedInput.lower() not in invDescWords:
                    print('You do not have "%s" in your inventory.' % (strippedInput))
                    self.inputLoop()

                item = self.getItemfromDesc(strippedInput.title(), self.inventory)
                if item != None:
                    print('You drop %s.' % (self.worldItems[item][SHORTDESC]))
                    self.inventory.remove(item)
                    self.taken.remove(item)
                    self.worldRooms[self.location][GROUND].append(item)


            # TODO: interact with npcs
            # TODO: weapons input show damage...
            # TODO: weight limit
            # TODO: learn flight = has book + in flight training = abilites + Fly

            elif(self.input.lower() == "read manual" or self.input.lower() == "read guide" or self.input.lower() == "read flight manual"):
                if(self.location == "Docking Bay"):
                    if("Flight" not in self.abilities):
                        if("Flight Manual" in self.inventory):
                            self.abilities.append("Flight")
                            print("You begin ")


            elif(self.input.lower() == "inventory") or (self.input.lower() == "i"):
                print("INVENTORY")
                print(*self.inventory, sep='\n')

            elif("examine" in self.input.lower()):
                stripInput = self.input.title()
                strippedInput = stripInput[8:]
                x = len(self.inventory)
                while x > 0:
                    try:
                        item = self.getItemfromDesc(strippedInput.lower(), self.inventory)
                        if item != None:
                            print(str(self.worldItems[item.title()][LONGDESC]))
                            break
                            # self.inputLoop()
                        else:
                            x = x -1
                    except KeyError:
                        None

                # for x in self.inventory:
                #     try:
                #
                #         # print(str(self.worldItems[strippedInput.title()][LONGDESC]))
                #     except KeyError:
                #         print("Error")

            elif(self.input.lower() == "ammo"):
                print("AMMO")
                print(self.ammo)

            elif(self.input.lower() == "abilities"):
                print("ABILITIES")
                print(*self.abilities, sep='\n')

            elif(self.input.lower() == "look") or (self.input.lower() == "l"):
                self.readRoom(self.location)
                break

            elif(self.input.lower() == "quit") or (self.input.lower() == "exit"):
                exit(0)


            elif("save" in self.input.lower()):
                stripSave = self.input.lower()
                strippedSave = stripSave[5:]
                yesorno = input("Do you want to save game as " + strippedSave + "? (Y/N) ")
                if(yesorno.lower() == "yes") or (yesorno.lower() == "y"):
                    open(strippedSave + ".txt", 'w').close()
                    savefileeditor = open(strippedSave + ".txt", mode='r+')
                    i = 0
                    try:
                        while i >= 0:
                            savefileeditor.write(self.inventory[i] + "\n")
                            i = i + 1
                    except IndexError:
                        print()
                    savefileeditor.write("TAKEN\n")
                    i = 0
                    try:
                        while i >= 0:
                            savefileeditor.write(self.taken[i] + "\n")
                            i = i + 1
                    except IndexError:
                        print()
                    savefileeditor.write("ROOM\n")
                    savefileeditor.write(self.location + "\n")
                    savefileeditor.write("HEALTH\n")
                    savefileeditor.write(str(self.health) + "\n")
                    savefileeditor.write("ABILITY\n")
                    savefileeditor.write(str(self.abilities) + "\n")
                    savefileeditor.write("AMMO\n")
                    savefileeditor.write(str(self.ammo) + "\n")
                    savefileeditor.write("DAMAGE\n")
                    savefileeditor.write(str(self.damage) + "\n")

                    savefileeditor.close()
                    print("Saved")


            elif("restore" in self.input.lower()):
                stripRestore = self.input.lower()
                strippedRestore = stripRestore[8:]
                yesorno = input("Do you want to restore " + strippedRestore + "? (Y/N) ")
                if(yesorno.lower() == "yes") or (yesorno.lower() == "y"):
                    restoreread = open(strippedRestore + '.txt', 'r')
                    spacerestorefullList = restoreread.readlines()
                    restorefulllist = []
                    for j in spacerestorefullList:
                        restorefulllist.append(j.strip())

                    breaktakenIndex = restorefulllist.index("TAKEN")
                    breakroomIndex = restorefulllist.index("ROOM")
                    breakhealthIndex = restorefulllist.index("HEALTH")
                    breakabilityIndex = restorefulllist.index("ABILITY")
                    breakammoIndex = restorefulllist.index("AMMO")
                    breakdamageIndex = restorefulllist.index("DAMAGE")
                    breakendIndex = len(restorefulllist)

                    restoredItems = restorefulllist[0:breaktakenIndex]
                    restoredTaken = restorefulllist[breaktakenIndex+1:breakroomIndex]
                    restoredRoom = restorefulllist[breakroomIndex+1:breakhealthIndex]
                    restoredHealth = restorefulllist[breakhealthIndex+1:breakabilityIndex]
                    restoredAbility = restorefulllist[breakabilityIndex+1:breakammoIndex]
                    restoredAmmo = restorefulllist[breakammoIndex+1:breakdamageIndex]
                    restoredDamage = restorefulllist[breakdamageIndex+1:breakendIndex]


                    self.inventory.clear
                    self.taken.clear
                    self.inventory = restoredItems
                    self.taken = restoredTaken
                    self.health = restoredHealth[0]
                    self.ammo = restoredAmmo[0]
                    self.abilities = restoredAbility
                    self.location = restoredRoom[0]
                    self.damage = restoredDamage

                    print("Restored")

                    self.readRoom(self.location)

                elif(yesorno.lower() == "no") or (yesorno.lower() == "n"):
                    print("Ok. I didn't restore it.")
                    self.roomfunc();
                else:
                    print("I'm sorry. I didn't understand that.")
                    self.roomfunc()




            # room specific actions


            # TODO: when at jedi temple + have lightsaber parts build lightsaber
            # TODO: stealth with mandalore helmet on Mandalore
            # TODO: attack enemies triggering batttle without having it activate itself



    def fightsequence(self,loc,enemy):
        self.isfighting = True
        enemyHealth = int(self.worldCharacters[enemy][NPCHEALTH])
        enemyDamage = int(self.worldCharacters[enemy][NPCDAMAGE])
        enemyProb = int(self.worldCharacters[enemy][NPCFIGHTPROB])

        while self.isfighting == True:
            while (self.isfighting == True):
               print("Health: " + str(self.health))
               print("Enemy Health: " + str(enemyHealth))
               print("Ammo: " + str(self.ammo))
               rand = random.randint(0,100)
               if(rand >= 1) and (rand <= enemyProb):
                   print("The " + enemy + " fires his gun...")
                   time.sleep(1)
                   print("You are hit!")
                   time.sleep(1)
                   self.health = int(self.health) - enemyDamage
               elif(rand >= enemyProb) and (rand <=enemyProb):
                   print("The attacker fires his gun...")
                   time.sleep(1)
                   print("Thankfully, you dodge the laser blast just in time.")
                   time.sleep(1)
               if (int(self.health) <= 0):
                   print("Unable to take it anymore, you collapse to the ground.")
                   time.sleep(2)
                   print("\n\n *** YOU HAVE DIED ***")
               elif (int(self.ammo) <= 0):
                   print("Oh no! You have ran out of ammo!")
                   time.sleep(1)
                   print("Realizing your mistake you turn to make a run for it, but you are to late.")
                   time.sleep(2)
                   print("\n\n *** YOU HAVE DIED ***")
               elif (int(enemyHealth) <= 0):
                   print("" + enemy + " breathes his last breath before falling to the ground.")
                   time.sleep(1.5)
                   print("Walking over, you pick up the " + enemy + "'s " + str(self.worldCharacters[enemy][NPCDROPLOOT]) + ".")
                   self.inventory.append(str(self.worldCharacters[enemy][NPCDROPLOOT]))
                   self.isfighting = False

               self.input = input("\n> ")

               if ("kill" in self.input.lower()) or ("shoot" in self.input.lower()) or ("fire" in self.input.lower()) or ("blast" in self.input.lower()) or ("attack" in self.input.lower()):
                   if(rand >= 1) and (rand <=40):
                       print("You fire your gun...")
                       time.sleep(1)
                       print("...but the " + enemy + " evaded your shot!")
                       self.ammo = int(self.ammo) - 1
                       time.sleep(1)
                   elif(rand >= (40 + 1)) and (rand <=100):
                       print("You fire your blaster at your target...")
                       time.sleep(1)
                       print("The enemy is hit!")
                       time.sleep(1)
                       enemyHealth = int(enemyHealth) - int(self.damage[0])
                       print(int(self.damage[0]))
                       self.ammo = int(self.ammo) - 1
                       time.sleep(1)
               else:
                   print("I don't know what you mean by that.")

               if (int(self.health) <= 0):
                   print("Unable to take it anymore, you collapse to the ground.")
                   time.sleep(2)
                   print("\n\n *** YOU HAVE DIED ***")
               elif (int(self.ammo) <= 0):
                   print("Oh no! You have ran out of ammo!")
                   time.sleep(1)
                   print("Realizing your mistake you turn to make a run for it, but you are to late.")
                   time.sleep(2)
                   print("\n\n *** YOU HAVE DIED ***")
               elif (int(enemyHealth) <= 0):
                  print("" + enemy + " breathes his last breath before falling to the ground.")
                  time.sleep(1.5)
                  print("Walking over, you pick up the " + enemy + "'s " + str(self.worldCharacters[enemy][NPCDROPLOOT][0]) + ".")
                  self.inventory.append(str(self.worldCharacters[enemy][NPCDROPLOOT][0]))
                  self.isfighting = False

        self.readRoom(self.location)




 # self.fought = False
#     self.randomAttack = random.randint(0,20)
#     # when attack sequence is true
#     if(self.randomAttack == 1):
#         print(self.ammo)
#         if(int(self.ammo) > 0) and ("Blaster" in self.taken):
#             self.npc = ["Soldier"]
#             self.enemy = ["Bounty Hunter"]
#             self.randprobtotal = 25
#             self.randprobsplit = 9
#             self.enemypower = 5
#             self.reward = "Helmet"
#             self.rewardMessage = "You pick up the Mandelorian's Helmet and put it on."
#             self.npcDescription = ["A soldier is on the ground, hit by blaster fire."]
#             self.attackerdecription = "A bounty hunter looks straight at you. He raises his gun and points it straight at you."
#             self.fightYouHitAttacker = "You fire your blaster, the bounty hunter is hit!"
#             self.fightYouHitAttackerMiss = "You fire your blaster but the bounty hunter dodges your shot!"
#             self.fightAttackerHitYou = "The bounty hunter fires and you are hit!"
#             self.fightAttackerHitYouMiss = "The bounty hunter fires but but misses you!"
#             self.fightAttackerDead = "As you fire your gun the bounty hunter breathes his last breath and falls to the ground."
#             self.fightoutofammo = "You have ran out of ammo!"
#             self.fightYouDead =  "You are hit and fall to the ground."
#             self.enemyHealth = 20
#             self.canfight = True
#             self.isfighting = True
#             self.cangoNorth = False
#             self.cangoEast = False
#             self.cangoSouth = False
#             self.cangoWest = False
#             self.fought = False


 # print(self.attackerdecription)
#             while (self.isfighting == True):
#                 print("Health: " + str(self.health))
#                 print("Enemy Health " + str(self.enemyHealth))
#                 print("Ammo " + str(self.ammo))
#                 rand = random.randint(0,self.randprobtotal)
#                 if(rand >= 1) and (rand <= self.randprobsplit):
#                     print(self.fightAttackerHitYou)
#                     self.health = int(self.health) - self.enemypower
#                 elif(rand >= self.randprobsplit) and (rand <=self.randprobtotal):
#                     print(self.fightAttackerHitYouMiss)
#                 if (int(self.health) <= 0):
#                     print(self.fightYouDead)
#                     print("\n\n *** YOU HAVE DIED ***")
#                 elif (int(self.ammo) <= 0):
#                     print(self.fightoutofammo)
#                 elif (int(self.enemyHealth) <= 0):
#                     print(self.fightAttackerDead)
#                     print(self.rewardMessage)
#                     self.inventory.append(self.reward)
#                     self.isfighting = False
#
#
#                 self.input = input("\n> ")
#
#                 if ("kill" in self.input.lower()) or ("shoot" in self.input.lower()) or ("fire" in self.input.lower()) or ("blast" in self.input.lower()) or ("attack" in self.input.lower()):
#                     if(rand >= 1) and (rand <=self.randprobsplit):
#                         print(self.fightYouHitAttackerMiss)
#                         self.ammo = int(self.ammo) - 1
#                     elif(rand >= (self.randprobsplit + 1)) and (rand <=self.randprobtotal):
#                         print(self.fightYouHitAttacker)
#                         self.enemyHealth = int(self.enemyHealth) - 5
#                         self.ammo = int(self.ammo) - 1
#                 else:
#                     print("I don't know what you mean by that.")
#
#                 if (int(self.health) <= 0):
#                     print(self.fightYouDead)
#                     print("\n\n *** YOU HAVE DIED ***")
#                 elif (int(self.ammo) <= 0):
#                     print(self.fightoutofammo)
#                 elif (int(self.enemyHealth) <= 0):
#                     print(self.fightAttackerDead)
#                     print(self.rewardMessage)
#                     self.inventory.append(self.reward)
#                     self.isfighting = False



    def getItemfromDesc(self,desc,itemList):
        itemList = list(set(itemList))
        for item in itemList:
            if desc.lower() in self.worldItems[item][DESCWORDS]:
                return item

    def getAllItemsMatchingDesc(self,desc,itemList):
        itemList = list(set(itemList))
        matchingItems = []
        for item in itemList:
            if desc in self.worldItems[item][DESCWORDS]:
                matchingItems.append(item)
        return matchingItems

    def getAllDescWords(self,itemList):
        itemList = list(set(itemList))
        descWords = []
        for item in itemList:
            descWords.extend(self.worldItems[item][DESCWORDS])
        return list(set(descWords))






    #
    #         elif(self.input.lower() == "read manual") or (self.input.lower() == "learn manual") or (self.input.lower() == "read book"):
    #             if("Manual" in self.taken):
    #                 if("Fly" not in self.abilities):
    #                     self.abilities.append("Flight Manual")
    #                     print("You have learned how to fly a spaceship!")
    #                 else:
    #                     print("You have already read this!")
    #             else:
    #                 print("You don't have a manual!")
    #
    #
    #         elif(self.input.lower() == "flytest"):
    #             print("You sit down and the controls and start the ships engine...")
    #             time.sleep(3.5)
    #             print("The ship slowly raises itself off the ground...")
    #             time.sleep(4)
    #             print("At the press of a button the ship blasts away into the deep darkness of space!")
    #             time.sleep(3)
    #             print(...)
    #             time.sleep(2)
    #             print("You have arrived at Testia!")
    #             time.sleep(1)
    #
    #
    #         elif(self.input.lower() == "take ship") or (self.input.lower() == "fly out") or (self.input.lower() == "get in ship" or (self.input.lower() == "fly")):
    #             if(self.roomName == "Docking Bay"):
    #                 if("Flight Training" in self.abilities):
    #                     if("Fuel" in self.taken):
    #                         repeatRoom = False
    #                         repeatInput = False
    #                         self.roomChanger(1)
    #                     else:
    #                         print("The ship's fuel is empty!")
    #                         repeatRoom = True
    #                 else:
    #                     print("You don't know how to fly a space ship!")
    #                     repeatRoom = True
    #             elif(self.roomName == "Coruscant"):
    #                 print("The ship's screen lights up: \"Destination?\" it asks.")
    #                 self.input2 = input("\n> ")
    #                 if self.input2 == "Mandalore":
    #                     self.Mandalore
    #                 elif self.input2 == "Endor":
    #                     self.Endor
    #                 elif self.input2 == "Tatooine":
    #                     self.Tatooine
    #                 elif self.input2 == "Hoth":
    #                     self.Hoth
    #                 elif self.input2 == "Tython":
    #                     self.Tython
    #                 elif self.input2 == "Mother Ship":
    #                     self.DockingBay()
    #                 else:
    #                     print("You can't fly there!")
    #
    #
    #             else:
    #                 print("You cannot go this way.")
    #                 repeatInput = True
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # def roomfunc(self):
    #     repeatRoom = True
    #     while repeatRoom == True:
    #         print(self.roomName)
    #         print(self.roomDescription, end=' ')
    #         if self.itemsDescription != None:
    #             print(*self.itemsDescription, sep=' ', end=' ')
    #         if self.npcDescription != None:
    #             print(*self.npcDescription, sep=' ', end=' ')
    #         print(*self.exitsDescriptions, sep=' ')
    #         # fighting sequence
    #         if self.isfighting == True:
    #             print(self.attackerdecription)
    #             while (self.isfighting == True):
    #                 print("Health: " + str(self.health))
    #                 print("Enemy Health " + str(self.enemyHealth))
    #                 print("Ammo " + str(self.ammo))
    #                 rand = random.randint(0,self.randprobtotal)
    #                 if(rand >= 1) and (rand <= self.randprobsplit):
    #                     print(self.fightAttackerHitYou)
    #                     self.health = int(self.health) - self.enemypower
    #                 elif(rand >= self.randprobsplit) and (rand <=self.randprobtotal):
    #                     print(self.fightAttackerHitYouMiss)
    #                 if (int(self.health) <= 0):
    #                     print(self.fightYouDead)
    #                     print("\n\n *** YOU HAVE DIED ***")
    #                 elif (int(self.ammo) <= 0):
    #                     print(self.fightoutofammo)
    #                 elif (int(self.enemyHealth) <= 0):
    #                     print(self.fightAttackerDead)
    #                     print(self.rewardMessage)
    #                     self.inventory.append(self.reward)
    #                     self.isfighting = False
    #
    #
    #                 self.input = input("\n> ")
    #
    #                 if ("kill" in self.input.lower()) or ("shoot" in self.input.lower()) or ("fire" in self.input.lower()) or ("blast" in self.input.lower()) or ("attack" in self.input.lower()):
    #                     if(rand >= 1) and (rand <=self.randprobsplit):
    #                         print(self.fightYouHitAttackerMiss)
    #                         self.ammo = int(self.ammo) - 1
    #                     elif(rand >= (self.randprobsplit + 1)) and (rand <=self.randprobtotal):
    #                         print(self.fightYouHitAttacker)
    #                         self.enemyHealth = int(self.enemyHealth) - 5
    #                         self.ammo = int(self.ammo) - 1
    #                 else:
    #                     print("I don't know what you mean by that.")
    #
    #                 if (int(self.health) <= 0):
    #                     print(self.fightYouDead)
    #                     print("\n\n *** YOU HAVE DIED ***")
    #                 elif (int(self.ammo) <= 0):
    #                     print(self.fightoutofammo)
    #                 elif (int(self.enemyHealth) <= 0):
    #                     print(self.fightAttackerDead)
    #                     print(self.rewardMessage)
    #                     self.inventory.append(self.reward)
    #                     self.isfighting = False
    #
    #         else:
    #             None
    #
    #         repeatInput = True
    #
    #         # input main loop options
    #         while repeatInput == True:
    #             self.input = input("\n> ")
    #
    #             if(self.input.lower() == "north") or (self.input.lower() == "n"):
    #                 if(self.cangoNorth == True):
    #                     repeatRoom = False
    #                     repeatInput = False
    #                     self.roomChanger(0)
    #                 else:
    #                     print("You cannot go this way.")
    #                     repeatInput = True
    #             elif(self.input.lower() == "east") or (self.input.lower() == "e"):
    #                 if(self.cangoEast == True):
    #                     repeatRoom = False
    #                     repeatInput = False
    #                     self.roomChanger(1)
    #                 else:
    #                     print("You cannot go this way.")
    #                     repeatInput = True
    #             elif(self.input.lower() == "south") or (self.input.lower() == "s"):
    #                 if(self.cangoSouth == True):
    #                     repeatRoom = False
    #                     repeatInput = False
    #                     self.roomChanger(2)
    #                 else:
    #                     print("You cannot go this way.")
    #                     repeatInput = True
    #             elif(self.input.lower() == "west") or (self.input.lower() == "w"):
    #                 if(self.cangoWest == True):
    #                     repeatRoom = False
    #                     repeatInput = False
    #                     self.roomChanger(3)
    #                 else:
    #                     print("You cannot go this way.")
    #                     repeatInput = True
    #
    #             elif("take" in self.input.lower()):
    #                 stripInput = self.input.title()
    #                 strippedInput = stripInput[5:]
    #                 if strippedInput in str(self.roomItems):
    #                     print("You picked up a " + strippedInput)
    #                     self.inventory.append(strippedInput)
    #                     self.taken.append(strippedInput)
    #                     if(strippedInput == "Ammo"):
    #                         self.ammo = self.ammo + 50
    #                 else:
    #                     print("You don't see a " + strippedInput + "!")
    #
    #             elif("grab" in self.input.lower()):
    #                 stripInput = self.input.title()
    #                 strippedInput = stripInput[5:]
    #                 if strippedInput in str(self.roomItems):
    #                     print("You picked up a " + strippedInput)
    #                     self.inventory.append(strippedInput)
    #                     self.taken.append(strippedInput)
    #                     if(strippedInput == "Ammo"):
    #                         self.ammo = self.ammo + 50
    #                 else:
    #                     print("You don't see a " + strippedInput + "!")
    #
    #             elif("pick up" in self.input.lower()):
    #                 stripInput = self.input.title()
    #                 strippedInput = stripInput[8:]
    #                 if strippedInput in str(self.roomItems):
    #                     print("You picked up a " + strippedInput)
    #                     self.inventory.append(strippedInput)
    #                     self.taken.append(strippedInput)
    #                     if(strippedInput == "Ammo"):
    #                         self.ammo = self.ammo + 50
    #                 else:
    #                     print("You don't see a " + strippedInput + "!")
    #
    #             # TODO: drop
    #
    #             # TODO: weight limit
    #
    #             # TODO: learn flight = has book + in flight training = abilites + Fly
    #
    #
    #             elif(self.input.lower() == "inventory") or (self.input.lower() == "i") or (self.input.lower() == "bag"):
    #                 print("INVENTORY")
    #                 print(*self.inventory, sep='\n')
    #                 repeatInput == True
    #
    #             elif(self.input.lower() == "ammo"):
    #                 print("AMMO")
    #                 print(self.ammo)
    #                 repeatInput == True
    #
    #             elif(self.input.lower() == "abilities"):
    #                 print("ABILITIES")
    #                 print(*self.abilities, sep='\n')
    #                 repeatInput == True
    #
    #             elif(self.input.lower() == "read manual") or (self.input.lower() == "learn manual") or (self.input.lower() == "read book"):
    #                 if("Manual" in self.taken):
    #                     if("Fly" not in self.abilities):
    #                         self.abilities.append("Flight Manual")
    #                         print("You have learned how to fly a spaceship!")
    #                     else:
    #                         print("You have already read this!")
    #                 else:
    #                     print("You don't have a manual!")
    #
    #
    #             elif(self.input.lower() == "flytest"):
    #                 print("You sit down and the controls and start the ships engine...")
    #                 time.sleep(3.5)
    #                 print("The ship slowly raises itself off the ground...")
    #                 time.sleep(4)
    #                 print("At the press of a button the ship blasts away into the deep darkness of space!")
    #                 time.sleep(3)
    #                 print(...)
    #                 time.sleep(2)
    #                 print("You have arrived at Testia!")
    #                 time.sleep(1)
    #
    #
    #             elif(self.input.lower() == "take ship") or (self.input.lower() == "fly out") or (self.input.lower() == "get in ship" or (self.input.lower() == "fly")):
    #                 if(self.roomName == "Docking Bay"):
    #                     if("Flight Training" in self.abilities):
    #                         if("Fuel" in self.taken):
    #                             repeatRoom = False
    #                             repeatInput = False
    #                             self.roomChanger(1)
    #                         else:
    #                             print("The ship's fuel is empty!")
    #                             repeatRoom = True
    #                     else:
    #                         print("You don't know how to fly a space ship!")
    #                         repeatRoom = True
    #                 elif(self.roomName == "Coruscant"):
    #                     print("The ship's screen lights up: \"Destination?\" it asks.")
    #                     self.input2 = input("\n> ")
    #                     if self.input2 == "Mandalore":
    #                         self.Mandalore
    #                     elif self.input2 == "Endor":
    #                         self.Endor
    #                     elif self.input2 == "Tatooine":
    #                         self.Tatooine
    #                     elif self.input2 == "Hoth":
    #                         self.Hoth
    #                     elif self.input2 == "Tython":
    #                         self.Tython
    #                     elif self.input2 == "Mother Ship":
    #                         self.DockingBay()
    #                     else:
    #                         print("You can't fly there!")
    #
    #
    #                 else:
    #                     print("You cannot go this way.")
    #                     repeatInput = True
    #
    #                 # TODO: rest of planets flight commands
    #
    #
    #
    #
    #             # TODO: learn flight
    #
    #
    #             # TODO: when at jedi temple + have lightsaber parts build lightsaber
    #
    #
    #             # TODO: interact with npcs
    #
    #
    #             # TODO: stealth with mandalore helmet on Mandalore
    #
    #
    #             # TODO: attack enemies triggering batttle without having it activate itself
    #
    #
    #
    #             elif("save" in self.input.lower()):
    #                 stripSave = self.input.lower()
    #                 strippedSave = stripSave[5:]
    #                 yesorno = input("Do you want to save game as " + strippedSave + "? (Y/N) ")
    #                 if(yesorno.lower() == "yes") or (yesorno.lower() == "y"):
    #                     open(strippedSave + ".txt", 'w').close()
    #                     savefileeditor = open(strippedSave + ".txt", mode='r+')
    #                     i = 0
    #                     try:
    #                         while i >= 0:
    #                             savefileeditor.write(self.inventory[i] + "\n")
    #                             i = i + 1
    #                     except IndexError:
    #                         print()
    #                     savefileeditor.write("TAKEN\n")
    #                     i = 0
    #                     try:
    #                         while i >= 0:
    #                             savefileeditor.write(self.taken[i] + "\n")
    #                             i = i + 1
    #                     except IndexError:
    #                         print()
    #                     savefileeditor.write("ROOM\n")
    #                     savefileeditor.write(self.roomName + "\n")
    #                     savefileeditor.write("HEALTH\n")
    #                     savefileeditor.write(str(self.health) + "\n")
    #                     savefileeditor.write("ABILITY\n")
    #                     savefileeditor.write(str(self.abilities) + "\n")
    #                     savefileeditor.write("AMMO\n")
    #                     savefileeditor.write(str(self.ammo) + "\n")
    #
    #                     savefileeditor.close()
    #                     print("Saved")
    #
    #
    #             elif("restore" in self.input.lower()):
    #                 stripRestore = self.input.lower()
    #                 strippedRestore = stripRestore[8:]
    #                 yesorno = input("Do you want to restore " + strippedRestore + "? (Y/N) ")
    #                 if(yesorno.lower() == "yes") or (yesorno.lower() == "y"):
    #                     restoreread = open(strippedRestore + '.txt', 'r')
    #                     spacerestorefullList = restoreread.readlines()
    #                     restorefulllist = []
    #                     for j in spacerestorefullList:
    #                         restorefulllist.append(j.strip())
    #
    #                     breaktakenIndex = restorefulllist.index("TAKEN")
    #                     breakroomIndex = restorefulllist.index("ROOM")
    #                     breakhealthIndex = restorefulllist.index("HEALTH")
    #                     breakabilityIndex = restorefulllist.index("ABILITY")
    #                     breakammoIndex = restorefulllist.index("AMMO")
    #                     breakendIndex = len(restorefulllist)
    #
    #                     restoredItems = restorefulllist[0:breaktakenIndex]
    #                     restoredTaken = restorefulllist[breaktakenIndex+1:breakroomIndex]
    #                     restoredRoom = restorefulllist[breakroomIndex+1:breakhealthIndex]
    #                     restoredHealth = restorefulllist[breakhealthIndex+1:breakabilityIndex]
    #                     restoredAbility = restorefulllist[breakabilityIndex+1:breakammoIndex]
    #                     restoredAmmo = restorefulllist[breakammoIndex+1:breakendIndex]
    #
    #
    #                     self.inventory.clear
    #                     self.taken.clear
    #                     self.inventory = restoredItems
    #                     self.taken = restoredTaken
    #                     self.health = restoredHealth[0]
    #                     self.ammo = restoredAmmo[0]
    #                     self.abilities = restoredAbility
    #
    #                     print("Restored")
    #                     if (restoredRoom[0] == "Armory"):
    #                         self.Armory()
    #                     elif (restoredRoom[0] == "Hallway"):
    #                         self.Hallway()
    #                     elif (restoredRoom[0] == "Docking Bay"):
    #                         self.DockingBay()
    #                     elif (restoredRoom[0] == "Space"):
    #                         self.Space
    #                     elif (restoredRoom[0] == "Living Quarters"):
    #                         self.LivingQuarters
    #                     elif (restoredRoom[0] == "Deck"):
    #                         self.Deck
    #                     elif (restoredRoom[0] == "Storage Closet"):
    #                         self.StorageCloset
    #                     elif (restoredRoom[0] == "Locked Room"):
    #                         self.LockedRoom
    #                     elif restoredRoom[0] == "Infirmary":
    #                         self.Infirmary
    #                     elif restoredRoom[0] == "Flight Training":
    #                         self.FlightTraining
    #                     elif restoredRoom[0] == "Coruscant":
    #                         self.Coruscant
    #                     elif restoredRoom[0] == "Hospital":
    #                         self.Hospital
    #                     elif restoredRoom[0] == "Mandalore":
    #                         self.Mandalore
    #                     elif restoredRoom[0] == "Endor":
    #                         self.Endor
    #                     elif restoredRoom[0] == "Tatooine":
    #                         self.Tatooine
    #                     elif restoredRoom[0] == "Hoth":
    #                         self.Hoth
    #                     elif restoredRoom[0] == "Cave":
    #                         self.Cave
    #                     elif restoredRoom[0] == "Rebel Base":
    #                         self.RebelBase
    #                     elif restoredRoom[0] == "Sand Dune":
    #                         self.SandDune
    #                     elif restoredRoom[0] == "Tython":
    #                         self.Tython
    #                     elif restoredRoom[0] == "Jedi Temple":
    #                         self.JediTemple
    #                     else:
    #                         print("Error Unkown Restore Room")
    #
    #
    #
    #                 elif(yesorno.lower() == "no") or (yesorno.lower() == "n"):
    #                     print("Ok. I didn't restore it.")
    #                     self.roomfunc();
    #                 else:
    #                     print("I'm sorry. I didn't understand that.")
    #                     self.roomfunc()
    #
    #                     # TODO: after fight restore remembers
    #
    #
    #             elif(self.input.lower() == "look") or (self.input.lower() == "l"):
    #                 repeatRoom = True;
    #                 break
    #
    #             elif(self.input.lower() == "quit") or (self.input.lower() == "exit"):
    #                 exit(0)
    #
    #
    #
    #
    # def roomChanger(self, dir):
    #     if self.exits[dir] == "Armory":
    #         self.Armory()
    #     elif self.exits[dir] == "Hallway":
    #         self.Hallway()
    #     elif self.exits[dir] == "Docking Bay":
    #         self.DockingBay()
    #     elif self.exits[dir] == "Space":
    #         self.Space
    #     elif self.exits[dir] == "Living Quarters":
    #         self.LivingQuarters
    #     elif self.exits[dir] == "Deck":
    #         self.Deck
    #     elif self.exits[dir] == "Storage Closet":
    #         self.StorageCloset
    #     elif self.exits[dir] == "Locked Room":
    #         self.LockedRoom
    #     elif self.exits[dir] == "Infirmary":
    #         self.Infirmary
    #     elif self.exits[dir] == "Flight Training":
    #         self.FlightTraining
    #     elif self.exits[dir] == "Coruscant":
    #         self.Coruscant
    #     elif self.exits[dir] == "Hospital":
    #         self.Hospital
    #     elif self.exits[dir] == "Mandalore":
    #         self.Mandalore
    #     elif self.exits[dir] == "Endor":
    #         self.Endor
    #     elif self.exits[dir] == "Tatooine":
    #         self.Tatooine
    #     elif self.exits[dir] == "Hoth":
    #         self.Hoth
    #     elif self.exits[dir] == "Cave":
    #         self.Cave
    #     elif self.exits[dir] == "Rebel Base":
    #         self.RebelBase
    #     elif self.exits[dir] == "Sand Dune":
    #         self.SandDune
    #     elif self.exits[dir] == "Tython":
    #         self.Tython
    #     elif self.exits[dir] == "Jedi Temple":
    #         self.JediTemple
    #     else:
    #         print("Room changer Error")
