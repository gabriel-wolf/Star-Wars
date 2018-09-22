import math
import random

class Rooms():

    def __init__(self):
        self.taken = []
        self.inventory = ['Chest Guard', 'Leg Guards', 'Gloves', 'Communicator']
        self.health = 100
        self.ammo = 0
        self.abilities = []

    def Armory(self):
        self.npc = ["Soldier"]
        self.npcDescription = ["A soldier stands next to you loading his weapon."]
        self.canfight = False
        self.isfighting = False
        self.cangoNorth = True
        self.cangoEast = True
        self.cangoSouth = False
        self.cangoWest = True
        self.fought = False
        self.randomAttack = random.randint(0,1)
        print(self.ammo)
        if(self.randomAttack == 1):
            print(self.ammo)
            if(int(self.ammo) > 0) and ("Blaster" in self.taken):
                self.npc = ["Soldier"]
                self.enemy = ["Bounty Hunter"]
                self.npcDescription = ["A soldier is on the ground, hit by blaster fire."]
                self.attackerdecription = "A bounty hunter looks straight at you. He raises his gun and points it straight at you."
                self.fightYouHitAttacker = "You fire your blaster, the bounty hunter is hit!"
                self.fightYouHitAttackerMiss = "You fire your blaster but the bounty hunter dodges your shot!"
                self.fightAttackerHitYou = "The bounty hunter fires and you are hit!"
                self.fightAttackerHitYouMiss = "The bounty hunter fires but but misses you!"
                self.fightAttackerDead = "As you fire your gun the bounty hunter breathes his last breath and falls to the ground."
                self.fightoutofammo = "You have ran out of ammo!"
                self.fightYouDead =  "You are hit and fall to the ground."
                self.enemyHealth = 20
                self.canfight = True
                self.isfighting = True
                self.cangoNorth = False
                self.cangoEast = False
                self.cangoSouth = False
                self.cangoWest = False
                self.fought = False
        else:
            self.npc = ["Soldier"]
            self.npcDescription = ["A soldier stands next to you loading his weapon."]
            self.canfight = False
            self.isfighting = False
            self.cangoNorth = True
            self.cangoEast = True
            self.cangoSouth = False
            self.cangoWest = True
            self.fought = False
        self.roomName = "Armory"
        self.roomDescription = "There are boxes of gear everywhere."
        self.roomItems = ['Blaster', 'Ammo']
        self.itemsDescription = ["An M451 Blaster is sitting on the ground.", "An ammo pack lays on the floor."]
        j = len(self.taken)
        try:
            while j > 0:
                alreadytakenItems = [i for i in self.taken if i in self.roomItems]
                alreadytakenIndex = self.roomItems.index(alreadytakenItems[0])
                self.roomItems.remove(alreadytakenItems[0])
                del self.itemsDescription[alreadytakenIndex]
                j = j - 1
        except TypeError:
            print(None)

        self.exits = ['Hallway','Docking Bay','','Storage Closet']
        self.exitsDescriptions = ['To the north is a long hallway.','To the east is the docking bay.','','To the west is a storage closet.']

        self.roomfunc()

    def Hallway(self):
        self.roomName = "Hallway"
        self.roomDescription = "You are in a long hallway."
        self.roomItems = None
        self.itemsDescription = None
        j = len(self.taken)
        try:
            while j > 0:
                alreadytakenItems = [i for i in self.taken if i in self.roomItems]
                alreadytakenIndex = self.roomItems.index(alreadytakenItems[0])
                self.roomItems.remove(alreadytakenItems[0])
                del self.itemsDescription[alreadytakenIndex]
                j = j - 1
        except TypeError:
            print(None)
        self.npc = None
        self.npcDescription = None
        self.exits = ['Living Quarters',None,'Armory','Deck']
        self.exitsDescriptions = ['To the north is the living quarters.','','To the south is the armory.',"To the west is the ship's main deck."]
        self.canfight = False
        self.isfighting = False
        self.cangoNorth = True
        self.cangoEast = False
        self.cangoSouth = True
        self.cangoWest = True
        self.roomfunc()


        def DockingBay(self):
            self.roomName = "Docking Bay"
            self.roomDescription = "There are ships everywhere."
            self.roomItems = ['Manual', 'Fuel']
            self.itemsDescription = ["In the corner of the bay, a ship control manuel sits.", ""]
            j = len(self.taken)
            try:
                while j > 0:
                    alreadytakenItems = [i for i in self.taken if i in self.roomItems]
                    alreadytakenIndex = self.roomItems.index(alreadytakenItems[0])
                    self.roomItems.remove(alreadytakenItems[0])
                    del self.itemsDescription[alreadytakenIndex]
                    j = j - 1
            except TypeError:
                print(None)
            self.npc = ["Soldier"]
            self.npcDescription = ["A soldier stands next to you loading his weapon."]
            self.exits = ['Hallway','Docking Bay','','Storage Closet']
            self.exitsDescriptions = ['To the north is a long hallway.','To the east is the docking bay.','','To the west is a storage closet.']
            self.canfight = False
            self.isfighting = False
            self.cangoNorth = True
            self.cangoEast = True
            self.cangoSouth = False
            self.cangoWest = True
            self.roomfunc()



    def roomfunc(self):
        repeatRoom = True
        while repeatRoom == True:
            print(self.roomName)
            print(self.roomDescription, end=' ')
            if self.itemsDescription != None:
                print(*self.itemsDescription, sep=' ', end=' ')
            if self.npcDescription != None:
                print(*self.npcDescription, sep=' ', end=' ')
            print(*self.exitsDescriptions, sep=' ')
            if self.isfighting == True:
                print(self.attackerdecription)
                while (self.isfighting == True):
                    print("Health: " + str(self.health))
                    print("Enemy Health " + str(self.enemyHealth))
                    print("Ammo " + str(self.ammo))
                    rand = random.randint(0,25)
                    if(rand >= 1) and (rand <= 8):
                        print(self.fightAttackerHitYou)
                        self.health = int(self.health) - 5
                    elif(rand >= 8) and (rand <=25):
                        print(self.fightAttackerHitYouMiss)
                    if (int(self.health) <= 0):
                        print(self.fightYouDead)
                        print("\n\n *** YOU HAVE DIED ***")
                    elif (int(self.ammo) <= 0):
                        print(self.fightoutofammo)
                    elif (int(self.enemyHealth) <= 0):
                        print(self.fightAttackerDead)
                        self.isfighting = False

                    self.input = input("\n> ")

                    if ("kill" in self.input.lower()) or ("shoot" in self.input.lower()) or ("fire" in self.input.lower()) or ("blast" in self.input.lower()) or ("attack" in self.input.lower()):
                        if(rand >= 1) and (rand <=8):
                            print(self.fightYouHitAttackerMiss)
                        elif(rand >= 9) and (rand <=25):
                            print(self.fightYouHitAttacker)
                            self.enemyHealth = int(self.enemyHealth) - 5
                    else:
                        print("I don't know what you mean by that.")

                    if (int(self.health) <= 0):
                        print(self.fightYouDead)
                        print("\n\n *** YOU HAVE DIED ***")
                    elif (int(self.ammo) <= 0):
                        print(self.fightoutofammo)
                    elif (int(self.enemyHealth) <= 0):
                        print(self.fightAttackerDead)
                        self.isfighting = False

            else:
                None

            repeatInput = True
            while repeatInput == True:
                self.input = input("\n> ")

                if(self.input.lower() == "north") or (self.input.lower() == "n"):
                    if(self.cangoNorth == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChanger(0)
                    else:
                        print("You cannot go this way.")
                        repeatInput = True
                elif(self.input.lower() == "east") or (self.input.lower() == "e"):
                    if(self.cangoEast == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChanger(1)
                    else:
                        print("You cannot go this way.")
                        repeatInput = True
                elif(self.input.lower() == "south") or (self.input.lower() == "s"):
                    if(self.cangoSouth == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChanger(2)
                    else:
                        print("You cannot go this way.")
                        repeatInput = True
                elif(self.input.lower() == "west") or (self.input.lower() == "w"):
                    if(self.cangoWest == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChanger(3)
                    else:
                        print("You cannot go this way.")
                        repeatInput = True

                elif("take" in self.input.lower()):
                    stripInput = self.input.title()
                    strippedInput = stripInput[5:]
                    if strippedInput in str(self.roomItems):
                        print("You picked up a " + strippedInput)
                        self.inventory.append(strippedInput)
                        self.taken.append(strippedInput)
                        if(strippedInput == "Ammo"):
                            self.ammo = self.ammo + 50
                    else:
                        print("You don't see a " + strippedInput + "!")

                elif("grab" in self.input.lower()):
                    stripInput = self.input.title()
                    strippedInput = stripInput[5:]
                    if strippedInput in str(self.roomItems):
                        print("You picked up a " + strippedInput)
                        self.inventory.append(strippedInput)
                        self.taken.append(strippedInput)
                        if(strippedInput == "Ammo"):
                            self.ammo = self.ammo + 50
                    else:
                        print("You don't see a " + strippedInput + "!")

                elif("pick up" in self.input.lower()):
                    stripInput = self.input.title()
                    strippedInput = stripInput[8:]
                    if strippedInput in str(self.roomItems):
                        print("You picked up a " + strippedInput)
                        self.inventory.append(strippedInput)
                        self.taken.append(strippedInput)
                        if(strippedInput == "Ammo"):
                            self.ammo = self.ammo + 50
                    else:
                        print("You don't see a " + strippedInput + "!")

                elif(self.input.lower() == "inventory") or (self.input.lower() == "i") or (self.input.lower() == "bag"):
                    print("INVENTORY")
                    print(*self.inventory, sep='\n')
                    repeatInput == True

                elif(self.input.lower() == "ammo"):
                    print("AMMO")
                    print(self.ammo)
                    repeatInput == True

                elif(self.input.lower() == "abilities"):
                    print("ABILITIES")
                    print(*self.abilities, sep='\n')
                    repeatInput == True

                elif(self.input.lower() == "read manual") or (self.input.lower() == "learn manual") or (self.input.lower() == "read book"):
                    if("Manual" in self.taken):
                        if("Fly" not in self.abilities):
                            self.abilities.append("Fly")
                            print("You have learned how to fly a spaceship!")
                        else:
                            print("You have already read this!")
                    else:
                        print("You don't have a manual!")



                elif(self.input.lower() == "take ship") or (self.input.lower() == "fly out") or (self.input.lower() == "get in ship" or (self.input.lower() == "fly")):
                    if(self.roomName == "Docking Bay"):
                        if("Fly" in self.abilities):
                            if("Fuel" in self.taken):
                                repeatRoom = False
                                repeatInput = False
                                self.roomChanger(1)
                            else:
                                print("The ship's fuel is empty!")
                                repeatRoom = True
                        else:
                            print("You don't know how to fly a space ship!")
                            repeatRoom = True
                    else:
                        print("You cannot go this way.")
                        repeatInput = True


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
                        savefileeditor.write(self.roomName + "\n")
                        savefileeditor.write("HEALTH\n")
                        savefileeditor.write(str(self.health) + "\n")
                        savefileeditor.write("ABILITY\n")
                        savefileeditor.write(str(self.abilities) + "\n")
                        savefileeditor.write("AMMO\n")
                        savefileeditor.write(str(self.ammo) + "\n")

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
                        breakendIndex = len(restorefulllist)

                        restoredItems = restorefulllist[0:breaktakenIndex]
                        restoredTaken = restorefulllist[breaktakenIndex+1:breakroomIndex]
                        restoredRoom = restorefulllist[breakroomIndex+1:breakhealthIndex]
                        restoredHealth = restorefulllist[breakhealthIndex+1:breakabilityIndex]
                        restoredAbility = restorefulllist[breakabilityIndex+1:breakammoIndex]
                        restoredAmmo = restorefulllist[breakammoIndex+1:breakendIndex]


                        self.inventory.clear
                        self.taken.clear
                        self.inventory = restoredItems
                        self.taken = restoredTaken
                        self.health = restoredHealth[0]
                        self.ammo = restoredAmmo[0]
                        self.abilities = restoredAbility

                        print("Restored")
                        if (restoredRoom[0] == "Armory"):
                            self.Armory()
                        elif (restoredRoom[0] == "Hallway"):
                            self.Hallway()
                        elif (restoredRoom[0] == "Docking Bay"):
                            self.DockingBay()
                        elif (restoredRoom[0] == "Space"):
                            self.Space
                        elif (restoredRoom[0] == "Living Quarters"):
                            self.LivingQuarters
                        elif (restoredRoom[0] == "Deck"):
                            self.Deck
                        elif (restoredRoom[0] == "Storage Closet"):
                            self.StorageCloset
                        elif (restoredRoom[0] == "Locked Room"):
                            self.LockedRoom
                        else:
                            print("Error Unkown Restore Room")



                    elif(yesorno.lower() == "no") or (yesorno.lower() == "n"):
                        print("Ok. I didn't restore it.")
                        self.roomfunc();
                    else:
                        print("I'm sorry. I didn't understand that.")
                        self.roomfunc()


                elif(self.input.lower() == "look") or (self.input.lower() == "l"):
                    repeatRoom = True;
                    break

                elif(self.input.lower() == "quit") or (self.input.lower() == "exit"):
                    exit(0)




    def roomChanger(self, dir):
        if self.exits[dir] == "Armory":
            self.Armory()
        elif self.exits[dir] == "Hallway":
            self.Hallway()
        elif self.exits[dir] == "Docking Bay":
            self.DockingBay()
        elif self.exits[dir] == "Space":
            self.Space
        elif self.exits[dir] == "Living Quarters":
            self.LivingQuarters
        elif self.exits[dir] == "Deck":
            self.Deck
        elif self.exits[dir] == "Storage Closet":
            self.StorageCloset
        elif self.exits[dir] == "Locked Room":
            self.LockedRoom
        else:
            print("Room changer Error")
