from blockColors import *
import bedrock
import pygame

worldFolderPath = "C:\\Users\\Owner\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\"

print("\nVersion Info:\nGame version support 1.17\nEffeiency model v2\n")
print("Asking Some Basic Info")
#ask for inputs
print("Enter the name of the world folder you want to load:")
worldMapName = input()

print("Enter the x y size of how big you want to scan:")
scanSize = input()

worldFullName = worldFolderPath + worldMapName

scanSizeList = scanSize.split(',')

scanSizex = scanSizeList[0]
scanSizey = scanSizeList[1]
scanSizeX = int(scanSizex) - 1
scanSizeY = int(scanSizey) - 1

pointerX = 0
pointerY = 85
pointerZ = 0

pygame.init()
screen = pygame.display.set_mode((int(scanSizeX),int(scanSizeY)))
run = True

print("\nStarted!\n")
while pointerZ <= int(scanSizeY):
  with bedrock.World(worldFullName) as world:
    while str(world.getBlock(pointerX, pointerY, pointerZ, layer=0)) == "minecraft:air []":
      pointerY -= 1

    while str(world.getBlock(pointerX, pointerY, pointerZ, layer=0)) == "None":
      pointerY -= 1
      
    block = str(world.getBlock(pointerX, pointerY, pointerZ))
    blockSplit = block.split(' ')[0]
    blockName = blockSplit.split(':')[1]
    hex_code = blocks.get(blockName)
    #print(hex_code)
    screen.set_at((pointerX, pointerZ), str(hex_code))
    
    if pointerX + 1 > int(scanSizeX):
      pointerY = 85
      pointerZ += 1
      pointerX = 0
      pygame.display.update()
      print("Scanning new row.")
    else:
      pointerY = 85
      pointerX += 1
        
# Autosave on close.
pygame.display.update()
print("\nDone!\n")

while run: # so updates 
  pygame.display.update()
