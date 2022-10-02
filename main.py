import os
import sys
import math

def startEncounter():
  print("Add your encounter! Enter 1 to add a monster, 2 to add a player, and 3 to start the encounter.")
  encounter = input()
  if (encounter == "1"):
    addMonster()
  elif (encounter == "2"):
    addPlayer()
  elif (encounter == "3"):
    startEncounter()
  else:
    print("Invalid input, try again.")
    startEncounter()

def addMonster():

def addPlayer():

# def encounter():
#   print("Welcome to the encounter tracker!")
#   startEncounter()



def endEncounter():
  if (party.health <= 0):
    print("End of Encounter")
    sys.exit()
  elif:
    monsters.health <= 0:
    print("End of Encounter")
    sys.exit()
