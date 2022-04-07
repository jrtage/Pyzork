#CMD Definining file

import os
os.system('python MapCreator.py')

import random

inventoryItems = {}
mapItems = {}

currentRow = 1
currentCol = 3

# Loads all the items in the game into memory
itemList = {}
infile = open('Items.txt', 'r')
for line in infile:
    strLine = str(line)
    space = strLine.find(" ")
    word = strLine[:space]
    define = strLine[space:]
    itemList.update({word: define})

# Prints all the items in the players inventory
def inventory():
    if inventoryItems:
        for key,value in inventoryItems.items():
            item = str(key) + ": " + str(value)
            print(item)

    else:
        print("Your Inventory Is Empty")

def loadMap(room):
    mapItems.clear()
    with open(room,"r") as theRoom:
        for line in theRoom:
            strLine = str(line)
            space = strLine.find(" ")
            word = strLine[:space]
            define = strLine[space:]
            mapItems.update({word: define})


# Allows player to pick up and add an item to the player's inventory
def pickUp(item):
    item = item.upper()
    flag = False
    if len(mapItems) > 0:
        for key,value in inventoryItems.items():
            if key == item:
                flag = True
                break
        if flag == True:
            print("You already have this item in your inventory")
        else:
            for key,value in mapItems.items():
                if key == item:
                    inventoryItems.update({key:value})
                    print("This item is now in your inventory")
                    del mapItems[item]
                    break
    else:
        print("The item ","'", item,"'", " is not in this room")


# Displays a map if player has a map in their inventory
def displayMap():
    for key,value in inventoryItems.items():
        if key == "MAP":
            with open("map.txt","r") as mapFile:
                for line in mapFile:
                    print(line, end="")
            return
    print("You do not have a map in your inventory")


def destroyItem(item):
    item = item.upper()
    flag = False
    for key,value in inventoryItems.items():
        if key == item:
            flag = True
            break
    if flag == False:
        print("You do not have this item in your inventory")
    else:
        for key,value in itemList.items():
            if key == item:
                del inventoryItems[item]


def use(item):
    item = item.upper()
    for key in inventoryItems:
        if key == item:
            if item == "CELLPHONE":
                rand = random.randrange(100)
                if rand <= 20:
                    print("Your call went through and you have been rescued")
                    return
                else:
                    print("Your phone caught fire and was destroyed.")
                    del inventoryItems[item]
                    return
    print("You do not have an item that you can interact with")

def search():
    allItems = ""
    for key in mapItems:
        allItems = allItems + key + ", "
    if len(allItems)<2:
        print("There is nothing here")
    else:
        print("You have found: ",allItems)

def moveRoom(mapIndexDict, direction):
    global currentRow
    global currentCol
    direction = direction.upper()
    direction = direction[:1]
    availableDirections = []
    directs = mapIndexDict["EXITS"]
    for x in range(len(mapIndexDict["EXITS"])):
        availableDirections.extend(directs[x])

    for i in range(len(availableDirections)):
        if direction == availableDirections[i]:
            if direction == "N":
                currentRow += 1
            if direction == "S":
                currentRow -= 1
            if direction == "E":
                currentCol += 1
            if direction == "W":
                currentCol -= 1
            return False

    print("You cannot travel that way")


def help():
    with open("CMD.txt", "r") as helpFile:
        for line in helpFile:
            print(line)


def main():
    mapIndexDict = {}
    x = 1
    finalRoom = False

    print("Type 'Help' for help")

    while not finalRoom:
        #get room data
        mapIndex = "M" + str(currentCol) + str(currentRow) + ".txt"
        with open("Maps/MapIndex/"+mapIndex,"r") as currentRoom:

            for line in currentRoom:
                strLine = str(line)
                eol = strLine.find("\n")
                space = strLine.find(" ")
                key = strLine[:space]
                value = strLine[space:eol].strip()
                mapIndexDict.update({key: value})
        #get room content
        print("You are currently in room: ", mapIndexDict["ROOMNAME"])
        if mapIndexDict["ROOMNAME"] == "Crypt":
            print("Congrats, you have escaped the wilderness!")
            finalRoom = True
            break
        loadMap("Maps/"+mapIndexDict["MAPNAME"])
        roomFlag = True
        #while in room
        while roomFlag == True:
            #user action
            cmd = str(input("Awaiting Command...:"))
            cmd = cmd.upper()
            cmd = cmd + " "
            #if move: leave room
            space = cmd.find(" ")
            cmd1 = cmd[:space]
            cmd2 = cmd[space:].strip()


            if cmd1 == "PICKUP":
                pickUp(cmd2)
            elif cmd1 == "GO":
                roomFlag = moveRoom(mapIndexDict, cmd2)
            elif cmd1 == "DESTROY":
                destroyItem(cmd2)
            elif cmd1 == "SHOW":
                if cmd2 == "MAP":
                    displayMap()
                elif cmd2 == "INVENTORY":
                    inventory()
                else:
                    print("You cannot look at this item")
            elif cmd1 == "USE":
                if cmd2 == "CELLPHONE":
                    use(cmd2)
                else:
                    print("This is not an item you can interact with")
            elif cmd1 == "SEARCH":
                search()
            elif cmd1 == "HELP":
                help()





main()







