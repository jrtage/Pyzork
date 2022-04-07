#MAP CREATOR

import random
import os




#Loads all available items in the game into memory
infile = open('Items.txt', 'r')
itemList = {}

for line in infile:
    strLine = str(line)
    space = strLine.find(" ")
    word = strLine[:space]
    define = strLine[space:]
    itemList.update({word: define})


# Start Room
def roomGenerator(filename, startItems):

    itemGenList = dict(startItems)
    newItems = random.sample(itemList.items(),2)


    with open("Maps/" + filename,"w") as startRoom:

        for i in range(2):
            compressedItems = newItems[i]
            obj,func = compressedItems
            spliceLoc = func.find("\n")
            obj = str(obj)
            func = func[:spliceLoc]
            if obj != "NONE":
                itemGenList.update({obj:func})



        for key,value in itemGenList.items():
            item = str(key) + " " + str(value)
            startRoom.write(item)
            startRoom.write("\n")



startRoomList = {"RIFLE":"Can be used to kill enemies and defend yourself (Requires AMMO)", "FOOD":"Restores 5 healh points","MATCHES":"Used to light a torch", "KNIFE":"Can be used for defense" }
key = {"KEY":"used to open locked doors"}
pickaxe = {"PICKAXE":"used to dig"}
rand = {}
def create():
    roomGenerator("StartRoom.txt",startRoomList)
    roomGenerator("Shop.txt",key)
    roomGenerator("Mountain.txt",rand)
    roomGenerator("LogCabin.txt",rand)
    roomGenerator("Diner.txt",rand)
    roomGenerator("Crypt.txt",pickaxe)
    roomGenerator("AbandonedVillage.txt",rand)

create()
















