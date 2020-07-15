#----------VARIABLE DECLARATIONS----------

# 2D array for the 5x5 tile layout
tiles = []
for i in range(5):
    tiles.append([0, 0, 0, 0, 0])

selectedAnimals = []

totalLayouts = 0

#----------CLASS DECLARATIONS----------

class pattern:
    def __init__(self):
        pass
    def __getitem__(self, i):
        options = {
            0 : self.farm,
            'farm':self.farm,
            1 : self.outback,
            'outback' : self.outback,
            2 : self.savanna,
            'savanna' : self.savanna,
            3 : self.northern,
            'northern' : self.northern,
            4 : self.polar,
            'polar' : self.polar,
            5 : self.jungle,
            'jungle' : self.jungle,
            6 : self.jurassic,
            'jurassic' : self.jurassic,
            7 : self.ice_age,
            'ice_age' : self.ice_age,
        }
        return options[i]

    class farm:
        def __getitem__(self, i):
            options = {
                0 : self.sheep,
                'sheep':self.sheep,
                1 : self.pig,
                'pig':self.pig,
                2 : self.rabbit,
                'rabbit':self.rabbit,
                3 : self.horse,
                'horse':self.horse,
                4 : self.cow,
                'cow':self.cow,
                5 : self.unicorn,
                'unicorn':self.unicorn,
            }
            return options[i]
        sheep = [[1, 1, 1, 1]]
        pig = [[1, 1], [1, 1]]
        rabbit = [[1], [1], [1], [1]]
        horse = [[1], [1], [1]]
        cow = [[1, 1, 1]]
        unicorn = [[1, 0, 0], [0, 1, 1]]
    class outback:
        def __getitem__(self, i):
            options = {
                0 : self.kangaroo,
                'kangaroo':self.kangaroo,
                1 : self.platypus,
                'platypus':self.platypus,
                2 : self.crocodile,
                'crocodile':self.crocodile,
                3 : self.koala,
                'koala':self.koala,
                4 : self.cockatoo,
                'cockatoo':self.cockatoo,
                5 : self.tiddalik,
                'tiddalik':self.tiddalik,
            }
            return options[i]

        kangaroo = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        platypus = [[1, 1, 0], [0, 1, 1]]
        crocodile = [[1, 1, 1, 1]]
        koala = [[1, 1], [0, 1]]
        cockatoo = [[1, 0], [0, 1], [0, 1]]
        tiddalik = [[0, 1, 0], [1, 0, 1]]

    class savanna:
        def __getitem__(self, i):
            options = {
                0 : self.zebra,
                'zebra':self.zebra,
                1 : self.hippo,
                'hippo':self.hippo,
                2 : self.giraffe,
                'giraffe':self.giraffe,
                3 : self.lion,
                'lion':self.lion,
                4 : self.elephant,
                'elephant':self.elephant,
                5 : self.gryphon,
                'gryphon':self.gryphon,
            }
            return options[i]

        zebra = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        hippo = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        giraffe = [[1], [1], [1], [1]]
        lion = [[1, 1, 1]]
        elephant = [[1, 1], [1, 0]]
        gryphon = [[1, 0, 1], [0, 1, 0]]

    class northern:
        def __getitem__(self, i):
            options = {
                0 : self.bear,
                'bear':self.bear,
                1 : self.skunk,
                'skunk':self.skunk,
                2 : self.beaver,
                'beaver':self.beaver,
                3 : self.moose,
                'moose':self.moose,
                4 : self.fox,
                'fox':self.fox,
                5 : self.sasquatch,
                'sasquatch':self.sasquatch,
            }
            return options[i]

        bear = [[1, 1], [0, 1], [0, 1]]
        skunk = [[0, 1, 1], [1, 1, 0]]
        beaver = [[0, 0, 1], [1, 1, 0], [0, 0, 1]]
        moose = [[1, 0, 1], [0, 1, 0]]
        fox = [[1, 1, 0], [0, 0, 1]]
        sasquatch = [[1], [1]]

    class polar:
        def __getitem__(self, i):
            options = {
                0 : self.penguin,
                'penguin':self.penguin,
                1 : self.seal,
                'seal':self.seal,
                2 : self.muskox,
                'muskox':self.muskox,
                3 : self.polar_bear,
                'polar_bear':self.polar_bear,
                4 : self.walrus,
                'walrus':self.walrus,
                5 : self.yeti,
                'yeti':self.yeti,
            }
            return options[i]

        penguin = [[0, 1, 0], [0, 1, 0], [1, 0, 1]]
        seal = [[1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
        muskox = [[1, 1, 0], [1, 0, 1]]
        polar_bear = [[1, 0, 1], [0, 0, 1]]
        walrus = [[1, 0, 0], [0, 1, 1]]
        yeti = [[1], [0], [1]]

    class jungle:
        def __getitem__(self, i):
            options = {
                0 : self.monkey,
                'monkey':self.monkey,
                1 : self.toucan,
                'toucan':self.toucan,
                2 : self.gorilla,
                'gorilla':self.gorilla,
                3 : self.panda,
                'panda':self.panda,
                4 : self.tiger,
                'tiger':self.tiger,
                5 : self.phoenix,
                'phoenix':self.phoenix,
            }
            return options[i]

        monkey = [[1, 0, 1, 0], [0, 1, 0, 1]]
        toucan = [[0, 1], [1, 0], [0, 1], [0, 1]]
        gorilla = [[1, 0, 1], [1, 0, 1]]
        panda = [[0, 0, 1], [1, 0, 0], [0, 0, 1]]
        tiger = [[1, 0, 1, 1]]
        phoenix = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]

    class jurassic:
        def __getitem__(self, i):
            options = {
                0 : self.diplodocus,
                'diplodocus':self.diplodocus,
                1 : self.stegosaurus,
                'stegosaurus':self.stegosaurus,
                2 : self.raptor,
                'raptor':self.raptor,
                3 : self.t_rex,
                't_rex':self.t_rex,
                4 : self.triceraptops,
                'triceraptops':self.triceraptops,
                5 : self.dragon,
                'dragon':self.dragon,
            }
            return options[i]

        diplodocus = [[1, 0, 0], [0, 1, 1], [0, 1, 0]]
        stegosaurus = [[0, 1, 1, 0], [1, 0, 0, 1]]
        raptor = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
        t_rex = [[1, 0], [0, 0], [1, 1]]
        triceraptops = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
        dragon = [[1, 0, 0], [0, 0, 1]]

    class ice_age:
        def __getitem__(self, i):
            options = {
                0 : self.wooly_rhino,
                'wooly_rhino':self.wooly_rhino,
                1 : self.giant_sloth,
                'giant_sloth':self.giant_sloth,
                2 : self.dire_wolf,
                'dire_wolf':self.dire_wolf,
                3 : self.saber_tooth,
                'saber_tooth':self.saber_tooth,
                4 : self.mammoth,
                'mammoth':self.mammoth,
                5 : self.akhlut,
                'akhlut':self.akhlut,
            }
            return options[i]

        wooly_rhino = [[0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0]]
        giant_sloth = [[1, 0, 0], [0, 0, 1], [1, 0, 1]]
        dire_wolf = [[0, 1, 0, 0], [1, 0, 0, 1], [0, 1, 0, 0]]
        saber_tooth = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        mammoth = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
        akhlut = [[0, 0, 1], [1, 0, 0], [0, 0, 1]]

    class city:
        def __getitem__(self, i):
            options = {
                0 : self.raccoon,
                'raccoon':self.raccoon,
                1 : self.pigeon,
                'pigeon':self.pigeon,
                2 : self.rat,
                'rat':self.rat,
                3 : self.squirrel,
                'squirrel':self.squirrel,
                4 : self.opossum,
                'opossum':self.opossum,
                5 : self.sewer_turtle,
                'sewer_turtle':self.sewer_turtle,
            }
            return options[i]

        raccoon = [[1, 0, 1, 0], [1, 0, 0, 1]]
        pigeon = [[1, 0, 0], [0, 1, 0], [0, 1, 1]]
        rat = [[1, 1, 0, 0], [0, 1, 0, 1]]
        squirrel = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
        opossum = [[1, 0, 0], [1, 0, 1]]
        sewer_turtle = [[1, 1]]

    class moon:
        def __getitem__(self, i):
            options = {
                0 : self.moonkey,
                'moonkey':self.moonkey,
                1 : self.lunar_tick,
                'lunar_tick':self.lunar_tick,
                2 : self.tribble,
                'tribble':self.tribble,
                3 : self.moonicorn,
                'moonicorn':self.moonicorn,
                4 : self.luna_moth,
                'luna_moth':self.luna_moth,
                5 : self.jade_rabbit,
                'jade_rabbit':self.jade_rabbit,
            }
            return options[i]

        moonkey = [[1, 0, 0], [1, 0, 1], [0, 0, 1]]
        lunar_tick = [[0, 1, 0], [0, 0, 0], [0, 1, 0], [1, 0, 1]]
        tribble = [[0, 1, 0], [1, 1, 1]]
        moonicorn = [[1, 0], [1, 1]]
        luna_moth = [[1, 0, 1], [0, 0, 0], [0, 1, 0]]
        jade_rabbit = [[1, 0], [0, 0], [0, 1]]

    class mountain:
        def __getitem__(self, i):
            options = {
                0 : self.goat,
                'goat':self.goat,
                1 : self.cougar,
                'cougar':self.cougar,
                2 : self.elk,
                'elk':self.elk,
                3 : self.eagle,
                'eagle':self.eagle,
                4 : self.coyote,
                'coyote':self.coyote,
                5 : self.aatxe,
                'aatxe':self.aatxe,
            }
            return options[i]

        goat = [[1, 0, 0], [1, 1, 1]]
        cougar = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]
        elk = [[1, 0, 1], [0, 1, 1]]
        eagle = [[1, 0], [1, 0], [0, 1]]
        coyote = [[1, 1, 0], [0, 0, 1]]
        aatxe = [[0, 0, 1], [1, 0, 0]]

    class mars:
        def __getitem__(self, i):
            options = {
                0 : self.rock,
                'rock':self.rock,
                1 : self.marsmot,
                'marsmot':self.marsmot,
                2 : self.marsmoset,
                'marsmoset':self.marsmoset,
                3 : self.rover,
                'rover':self.rover,
                4 : self.martian,
                'martian':self.martian,
                5 : self.marsmallow,
                'marsmallow':self.marsmallow,
            }
            return options[i]

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
        #p = pattern()
        #location = p[locationName]
        #selectedAnimals.append([animal, p[locationName][animal]])


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