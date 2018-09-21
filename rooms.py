from settings import Settings

class Rooms():

    def roomChange(self, direction):
        if(direction == "North"):
            if(self.roomName == "Armory"):
                self.Halway()
            elif(self.roomName == "Halway"):
                self.something()
            else:
                print("Error Unkown Room Change")
        elif(direction == "East"):
            if(self.roomName == "Armory"):
                self.DockingBay()
            else:
                print("Error Unkown Room Change")
        elif(direction == "South"):
            if(self.roomName == "Halway"):
                self.Armory()
            else:
                print("Error Unkown Room Change")
        elif(direction == "West"):
            if(self.roomName == "YYY"):
                self.Armory()
            else:
                print("Error Unkown Room Change")
        else:
            print("Error: Unkown Room Change Direction")



    def Armory(self):
        self.roomName = "Armory"
        self.roomDescription = "There are boxes of gear everywhere."
        self.roomItems = ['M451 Blaster', 'Ammo Pack']
        self.itemsDescription = ["An M451 Blaster is sitting on the ground.", "An ammo pack lays on the floor."]
        self.npc = ["Soldier"]
        self.npcDescription = ["A soldier stands next to you loading his weapon."]
        self.exits = ['Halway','Docking Bay','','Storage Closet']
        self.exitsDescriptions = ['To the north is a long halway.','To the east is the docking bay.','','To the west is a storage closet.']
        self.canfight = False
        self.isfighting = False
        self.cangoNorth = True
        self.roomNorth = "Long Halway"
        self.cangoEast = True
        self.roomEast = "Docking Bay"
        self.cangoSouth = False
        self.roomSouth = None
        self.cangoWest = True
        self.roomWest = None
        self.roomfunc()

    def Halway(self):
        self.roomName = "Halway"
        self.roomDescription = "You are in a long halway."
        self.roomItems = None
        self.itemsDescription = None
        self.npc = None
        self.npcDescription = None
        self.exits = ['Living Quarters',None,'Armory',None]
        self.exitsDescriptions = ['To the north is the living quarters.','','To the south is the armory.','']
        self.canfight = False
        self.isfighting = False
        self.cangoNorth = True
        self.roomNorth = "Living Quarters"
        self.cangoEast = False
        self.roomEast = "Armory"
        self.cangoSouth = True
        self.roomSouth = "Armory"
        self.cangoWest = False
        self.roomWest = None

        self.roomfunc()


    def roomfunc(self):
        settings = Settings()
        repeatRoom = True
        while repeatRoom == True:
            print(self.roomName)
            print(self.roomDescription, end=' ')
            if self.itemsDescription != None:
                print(*self.itemsDescription, sep=' ', end=' ')
            if self.npcDescription != None:
                print(*self.npcDescription, sep=' ', end=' ')
            print(*self.exitsDescriptions, sep=' ')

            repeatInput = True
            while repeatInput == True:
                self.input = input("\n> ")
                if(self.input.lower() == "up"):
                    if self.roomUp == "Halway":
                        self.Halway()
                    elif self.roomUp == 'Armory':
                        self.Armory()

                elif(self.input.lower() == "north") or (self.input.lower() == "n"):
                    if(self.cangoNorth == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChange("North")
                    else:
                        print("You cannot go this way.")
                        repeatInput = True
                elif(self.input.lower() == "east") or (self.input.lower() == "e"):
                    if(self.cangoEast == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChange("East")
                    else:
                        print("You cannot go this way.")
                        repeatInput = True
                elif(self.input.lower() == "south") or (self.input.lower() == "s"):
                    if(self.cangoSouth == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChange("South")
                    else:
                        print("You cannot go this way.")
                        repeatInput = True
                elif(self.input.lower() == "west") or (self.input.lower() == "w"):
                    if(self.cangoWest == True):
                        repeatRoom = False
                        repeatInput = False
                        self.roomChange("West")
                    else:
                        print("You cannot go this way.")
                        repeatInput = True
                elif(self.input.lower() == "inventory") or (self.input.lower() == "i") or (self.input.lower() == "bag"):
                    print("Inventory")
                    print(*settings.inventory, sep='\n')
                    repeatInput == True


                elif(self.input.lower() == "quit"):
                    exit(0)
