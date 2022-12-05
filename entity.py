# Define the Entity class in a separate file named entity.py
class Entity:
  def __init__(self, name, hp, initiative):
    self.name = name
    self.hp = hp
    self.initiative = initiative
    
  def modify_hp(self, hp):
    self.hp += hp