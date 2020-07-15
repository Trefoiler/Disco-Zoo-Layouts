#----------VARIABLE DECLARATIONS----------

# 2D array for the 5x5 tile layout
tiles = []
for i in range(5):
    tiles.append([0, 0, 0, 0, 0])

selectedAnimals = []

totalLayouts = 0

#----------CLASS DECLARATIONS-----------

class pattern:
    class farm:
        sheep = [[1, 1, 1, 1]]
        pig = [[1, 1], [1, 1]]
        rabbit = [[1], [1], [1], [1]]
        horse = [[1], [1], [1]]
        cow = [[1, 1, 1]]
        unicorn = [[1, 0, 0], [0, 1, 1]]
    class outback:
        kangaroo = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        platypus = [[1, 1, 0], [0, 1, 1]]
        crocodile = [[1, 1, 1, 1]]
        koala = [[1, 1], [0, 1]]
        cockatoo = [[1, 0], [0, 1], [0, 1]]
        tiddalik = [[0, 1, 0], [1, 0, 1]]
    class savanna:
        zebra = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        hippo = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        giraffe = [[1], [1], [1], [1]]
        lion = [[1, 1, 1]]
        elephant = [[1, 1], [1, 0]]
        gryphon = [[1, 0, 1], [0, 1, 0]]
    class northern:
        bear = [[1, 1], [0, 1], [0, 1]]
        skunk = [[0, 1, 1], [1, 1, 0]]
        beaver = [[0, 0, 1], [1, 1, 0], [0, 0, 1]]
        moose = [[1, 0, 1], [0, 1, 0]]
        fox = [[1, 1, 0], [0, 0, 1]]
        sasquatch = [[1], [1]]
    class polar:
        penguin = [[0, 1, 0], [0, 1, 0], [1, 0, 1]]
        seal = [[1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
        muskox = [[1, 1, 0], [1, 0, 1]]
        polar_bear = [[1, 0, 1], [0, 0, 1]]
        walrus = [[1, 0, 0], [0, 1, 1]]
        yeti = [[1], [0], [1]]
    class jungle:
        monkey = [[1, 0, 1, 0], [0, 1, 0, 1]]
        toucan = [[0, 1], [1, 0], [0, 1], [0, 1]]
        gorilla = [[1, 0, 1], [1, 0, 1]]
        panda = [[0, 0, 1], [1, 0, 0], [0, 0, 1]]
        tiger = [[1, 0, 1, 1]]
        phoenix = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    class jurassic:
        diplodocus = [[1, 0, 0], [0, 1, 1], [0, 1, 0]]
        stegosaurus = [[0, 1, 1, 0], [1, 0, 0, 1]]
        raptor = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
        t_rex = [[1, 0], [0, 0], [1, 1]]
        triceraptops = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
        dragon = [[1, 0, 0], [0, 0, 1]]
    class ice_age:
        wooly_rhino = [[0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0]]
        giant_sloth = [[1, 0, 0], [0, 0, 1], [1, 0, 1]]
        dire_wolf = [[0, 1, 0, 0], [1, 0, 0, 1], [0, 1, 0, 0]]
        saber_tooth = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        mammoth = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
        akhlut = [[0, 0, 1], [1, 0, 0], [0, 0, 1]]
    class city:
        raccoon = [[1, 0, 1, 0], [1, 0, 0, 1]]
        pigeon = [[1, 0, 0], [0, 1, 0], [0, 1, 1]]
        rat = [[1, 1, 0, 0], [0, 1, 0, 1]]
        squirrel = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
        opossum = [[1, 0, 0], [1, 0, 1]]
        sewer_turtle = [[1, 1]]
    class moon:
        moonkey = [[1, 0, 0], [1, 0, 1], [0, 0, 1]]
        lunar_tick = [[0, 1, 0], [0, 0, 0], [0, 1, 0], [1, 0, 1]]
        tribble = [[0, 1, 0], [1, 1, 1]]
        moonicorn = [[1, 0], [1, 1]]
        luna_moth = [[1, 0, 1], [0, 0, 0], [0, 1, 0]]
        jade_rabbit = [[1, 0], [0, 0], [0, 1]]
    class mountain:
        goat = [[1, 0, 0], [1, 1, 1]]
        cougar = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]
        elk = [[1, 0, 1], [0, 1, 1]]
        eagle = [[1, 0], [1, 0], [0, 1]]
        coyote = [[1, 1, 0], [0, 0, 1]]
        aatxe = [[0, 0, 1], [1, 0, 0]]
    class mars:
        rock = [[1, 1], [1, 1]]
        marsmot = [[0, 1], [0, 1], [1, 1]]
        marsmoset = [[1, 0, 1], [0, 0, 1], [0, 1, 0]]
        rover = [[0, 1, 0], [1, 0, 1]]
        martian = [[1, 0, 1], [0, 1, 0]]
        marsmallow = [[1], [0], [1]]


#----------FUNCTIONS----------

def combineArrays(array1, array2, offset=(0, 0)):
    offX = offset[1]
    offY = offset[0]
    
    newArray = []
    for i in range(len(array1)):
        newArray.append([0]*len(array1[0]))

    for i in range(len(array2)):
        for j in range(len(array2[0])):
            newArray[i+offX][j+offY] = array1[i+offX][j+offY] + array2[i][j]
    
    return newArray


def calcAnimalOptions(location):
    if location == 'farm':
        animals = 'sheep, pig, rabbit, horse, cow, and unicorn'
    elif location == 'outback':
        animals = 'kangaroo, platypus, crocodile, koala, cockatoo, and tiddalik'
    elif location == 'savanna':
        animals = 'zebra, hippo, giraffe, lion, elephant, and gryphon'
    elif location == 'northern':
        animals = 'bear, skunk, beaver, moose, fox, and sasquatch'
    elif location == 'polar':
        animals = 'penguin, seal, muskox, polar bear, walrus, and yeti'
    elif location == 'jungle':
        animals = 'monkey, toucan, gorilla, panda, tiger, and phoenix'
    elif location == 'jurassic':
        animals = 'diplodocus, stegosaurus, raptor, t-rex, triceraptops, and dragon'
    elif location == 'ice age':
        animals = 'wooly rhino, giant sloth, dire wolf, saber tooth, mammoth, and akhlut'
    elif location == 'city':
        animals = 'raccoon, pigeon, rat, squirrel, opossum, and sewer turtle'
    elif location == 'moon':
        animals = 'lunar tick, moonkey, tribble, luna moth, moonicorn, and jade rabbit'
    elif location == 'mountain':
        animals = 'goat, cougar, elk, eagle, coyote, and aatxe'
    elif location == 'mars':
        animals = 'rock, marsmot, marsmoset, rover, martian, and marsmallow'
    
    return animals


def identifyAnimals():
    global selectedAnimals

    locationName = input('Locations are farm, outback, savanna, northern, polar, jungle, jurassic, ice age, city, moon, mountain, and mars. What location do you want to choose animals from?: ').lower()
    locationName = locationName.replace(' ', '_')
    numOfAnimals = int(input('How many animals are you going to choose? Options are 1-3: '))

    for i in range(numOfAnimals):
        animalOptions = calcAnimalOptions(locationName)
        
        inputMSG = '{} animals are {}. What is animal number {}?: '.format(locationName.capitalize(), animalOptions, i+1)
        animal = input(inputMSG).lower().replace(' ', '_').replace('-', '_')
        
        selectedAnimals.append([animal, getattr(eval('pattern.'+locationName), animal)])


def findAllLayouts():
    global totalLayouts

    # runs for every aninal in selectedAnimals
    for k in range(len(selectedAnimals)):
        # how many times to go across x
        for x in range(6 - len(selectedAnimals[k][1][0])):
            # how many times to go across y
            for y in range(6 - len(selectedAnimals[k][1])):
                newTiles = combineArrays(tiles, selectedAnimals[k][1], (x, y))

                possibleLayout = True
                
                for i in range(5):
                    for j in range(5):
                        if newTiles[i][j] > 1:
                            possibleLayout = False

                if possibleLayout:
                    totalLayouts += 1


#----------THE MAIN STUFF----------

identifyAnimals()
print(selectedAnimals)
findAllLayouts()
print(totalLayouts)