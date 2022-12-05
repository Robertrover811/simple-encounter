# Import the Entity class from the entity.py file
from entity import Entity

# Define a function to create a new entity
def create_entity():
  name = input('Enter the name of the entity: ')
  hp = int(input('Enter the hit points of the entity: '))
  initiative = int(input('Enter the initiative of the entity: '))
  return Entity(name, hp, initiative)

# Define a function to start the initiative system
def start_initiative(entities):
  # Sort the entities in descending order of initiative
  entities.sort(key=lambda e: e.initiative, reverse=True)
  
  # Start the initiative system
  while True:

    if len(entities) == 0:
      print('There are no more entities in the initiative order.')
      print('The encounter has ended.')
      break

    # Print the entities in initiative order
    print('The entities in initiative order are:')
    for i, entity in enumerate(entities):
      print(f'{i + 1}. {entity.name}')

    # Start the turn of the entity with the highest initiative
    entity = entities[0]
    print(f'It is {entity.name}\'s turn.')
    
    # Ask the user if any new entities have joined the fight
    new_entities = input('Have any new entities joined the fight? (yes/no) ')
    if new_entities == 'yes':
      # Add the new entities to the initiative order
      while True:
        entity = create_entity()
        entities.append(entity)
        more_entities = input('Are there any more new entities? (yes/no) ')
        if more_entities == 'no':
          break
      
      # Sort the entities in descending order of initiative
      entities.sort(key=lambda e: e.initiative, reverse=True)
    
    # Ask the user if any entities have had their hit points modified
    hp_modified = input('Have any entities had their hit points modified? (yes/no) ')
    if hp_modified == 'yes':
      while True:
        # Ask the user to specify which entity and how their hit points were modified
        modification = input('Enter the name and hit point modification of the entity (e.g. "entity1 -2"): ')
        name, hp = modification.split()
        # Find the entity and modify their hit points
        for e in entities:
          if e.name == name:
            e.modify_hp(int(hp))
            break
        more_modifications = input('Are there any more hit point modifications? (yes/no) ')
        if more_modifications == 'no':
          break
    
    # Check if any entities have 0 or fewer hit points and remove them from the initiative order
    entities = [e for e in entities if e.hp > 0]
    
    # end = input('')
    # if end == 'end':
    #   break
