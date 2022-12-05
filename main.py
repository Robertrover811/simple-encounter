# Import the Entity class and the start_initiative function from the io.py file
from io_1 import Entity, start_initiative

# Define a function to create a new entity
def create_entity():
  name = input('Enter the name of the entity: ')
  
  # Keep asking the user to input the hit points until they provide a valid integer
  while True:
    try:
      hp = int(input('Enter the hit points of the entity: '))
      break
    except ValueError:
      print('Please enter an integer for the hit points.')
  
  # Keep asking the user to input the initiative until they provide a valid integer
  while True:
    try:
      initiative = int(input('Enter the initiative of the entity: '))
      break
    except ValueError:
      print('Please enter an integer for the initiative.')
  
  return Entity(name, hp, initiative)


# Define the main function that contains the main program logic
def main():
  print('Welcome to the simple encounter tracker CLI app for D&D 5e!')
  print('To get started, create a new entity.')
  print('This new entity can be a player character, an enemy, or an NPC.')
  print('To exit, run a keyboard interrupt.')

  # Create an empty list to store the entities in initiative order
  entities = []
  
  # Prompt the user to add new entities until they are ready to start
  while True:
    entity = create_entity()
    entities.append(entity)
    ready = input('Are you ready to start? To add another entity, enter no. (yes/no) ')
    if ready == 'yes':
      break
  
  # Start the initiative system
  start_initiative(entities)

# Call the main function to run the program
if __name__ == '__main__':
  main()
