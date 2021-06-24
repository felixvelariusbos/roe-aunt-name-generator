import random

def get_places():
    """
    returns the full list of places at our disposal
    """
    with open('data/places.txt', 'r') as fi:
        data = fi.read()
        places = data.split('\n')[:-1]
        
    return places

def get_place():
    """returns a random place"""
    
    # get all our places
    places = get_places()
    
    # grab a rando one. I think it's a uniform distro, althou honestly
    # i've forgotten and am too lazy to look it up right now
    length = len(places)

    idx = random.randint(0,length-1)
    return places[idx]
    
    
    
def get_animals():
    with open('data/animals.txt', 'r') as fi:
        data = fi.read()
        animals = data.split('\n')[:-1]
        
    return animals
    
    
def get_animal(start_letter = None):
    """
    returns a random animal.
    if start_letter is not set, it's truly random.
    
    setting start letter will restrict the generator to just
    animals with that start letter
    """
    
    # get all our places
    animals = get_animals()
    
    # if start_letter was set...parse it down a smidge
    
    # grab a rando one.
    length = len(animals)
    idx = random.randint(0,length-1)
    return animals[idx]
    

place = get_place()
animal = get_animal()
name = "%s %s-Eye" % (place, animal)
print("Congrats, new roe aunt! Your name is %s" % name)
    
   