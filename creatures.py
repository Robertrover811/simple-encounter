import os
import sys
import math

class Player:
  def __init__(self, name, health, initiative):
    self.name = name
    self.health = health
    self.initiative = initiative

class Monster:
  def __init__(self, name, health, initiative):
    self.name = name
    self.health = health
    self.initiative = initiative