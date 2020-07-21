import tkinter as tk

#----------VARIABLE DECLARATIONS----------

root = tk.Tk()
root.title('Disco Zoo Layouts')

# 2D array for the 5x5 tile layout
tiles = []
for i in range(5):
    tiles.append([0, 0, 0, 0, 0])

selectedAnimals = []

totalLayouts = 0

numOfAnimals = 0
locationName = 'filler'
animalOptions = []

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

class buttons:
    class animalNums:
        def button_1():
            global numOfAnimals
            numOfAnimals = 1
        def button_2():
            global numOfAnimals
            numOfAnimals = 2
        def button_3():
            global numOfAnimals
            numOfAnimals = 3
    
    class locations:
        def farm():
            global locationName
            locationName = 'farm'
        def outback():
            global locationName
            locationName = 'outback'
        def savanna():
            global locationName
            locationName = 'savanna'
        def northern():
            global locationName
            locationName = 'northern'
        def polar():
            global locationName
            locationName = 'polar'
        def jungle():
            global locationName
            locationName = 'jungle'
        def jurassic():
            global locationName
            locationName = 'jurassic'
        def ice_age():
            global locationName
            locationName = 'ice_age'
        def city():
            global locationName
            locationName = 'city'
        def moon():
            global locationName
            locationName = 'moon'
        def mountain():
            global locationName
            locationName = 'mountain'
        def mars():
            global locationName
            locationName = 'mars'

    class animalOptionsClass:
        def animal_0():
            global selectedAnimals, animalOptions
            selectedAnimals.append(animalOptions[0])
            del animalOptions[0]
        def animal_1():
            global selectedAnimals, animalOptions
            selectedAnimals.append(animalOptions[1])
            del animalOptions[1]
        def animal_2():
            global selectedAnimals, animalOptions
            selectedAnimals.append(animalOptions[2])
            del animalOptions[2]
        def animal_3():
            global selectedAnimals, animalOptions
            selectedAnimals.append(animalOptions[3])
            del animalOptions[3]
        def animal_4():
            global selectedAnimals, animalOptions
            selectedAnimals.append(animalOptions[4])
            del animalOptions[4]
        def animal_5():
            global selectedAnimals, animalOptions
            selectedAnimals.append(animalOptions[5])
            del animalOptions[5]

    class phases:
        # ask how many animals will be chosen
        def phase1():
            clearScreen()

            label_askNumOfAnimals = tk.Label(root, text = 'How many animals are you going to chose?')
            label_askNumOfAnimals.grid(row=0, column=0)

            numButtons = [
                tk.Button(root, text='1', command = lambda:[buttons.animalNums.button_1(), buttons.phases.phase2()]),
                tk.Button(root, text='2', command = lambda:[buttons.animalNums.button_2(), buttons.phases.phase2()]),
                tk.Button(root, text='3', command = lambda:[buttons.animalNums.button_3(), buttons.phases.phase2()])
            ]

            for i in range(len(numButtons)):
                numButtons[i].grid(row = i+1, column = 0)

        # ask for the location
        def phase2():
            clearScreen()

            label_askLocation = tk.Label(root, text = 'What location do you want to choose animals from?')
            label_askLocation.grid(row=0, column=0)

            locationButtons = [
                tk.Button(root, text = 'Farm', command = lambda:[buttons.locations.farm(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Outback', command = lambda:[buttons.locations.outback(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Savanna', command = lambda:[buttons.locations.savanna(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Northern', command = lambda:[buttons.locations.northern(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Polar', command = lambda:[buttons.locations.polar(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Jungle', command = lambda:[buttons.locations.jungle(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Jurassic', command = lambda:[buttons.locations.jurassic(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Ice Age', command = lambda:[buttons.locations.ice_age(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'City', command = lambda:[buttons.locations.city(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Moon', command = lambda:[buttons.locations.moon(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Mountain', command = lambda:[buttons.locations.mountain(), buttons.phases.phase3a()]),
                tk.Button(root, text = 'Mars', command = lambda:[buttons.locations.mars(), buttons.phases.phase3a()])
            ]

            for i in range(len(locationButtons)):
                locationButtons[i].grid(row = i+1, column = 0)
        
        # ask for chosen animal 1
        def phase3a():
            global animalOptions

            clearScreen()

            animalOptions = calcAnimalOptions(locationName)

            label_askLocation = tk.Label(root, text = 'What is animal #1')
            label_askLocation.grid(row=0, column=0)

            animalButtons = []
            for i in range(len(animalOptions)):
                animalButtons.append(tk.Button(root, text = animalOptions[i], command = lambda:[eval('buttons.animalOptionsClass.animal_' + str(i)), buttons.phases.phase3b()]))
            
            for i in range(len(animalButtons)):
                animalButtons[i].grid(row = i+1, column = 0)
        
        # ask for chosen animal 2, if there is one
        def phase3b():
            global animalOptions
            
            if numOfAnimals >= 2:
                clearScreen()

                label_askLocation = tk.Label(root, text = 'What is animal #2')
                label_askLocation.grid(row=0, column=0)

                animalButtons = []
                for i in range(len(animalOptions)):
                    animalButtons.append(tk.Button(root, text = animalOptions[i], command = lambda:[eval('buttons.animalOptionsClass.animal_' + str(i)), buttons.phases.phase3c()]))
                
                for i in range(len(animalButtons)):
                    animalButtons[i].grid(row = i+1, column = 0)
            else:
                buttons.phases.phase3c()
        
        # ask for chosen animal 3, if there is one
        def phase3c():
            global animalOptions
            
            if numOfAnimals >= 3:
                clearScreen()

                label_askLocation = tk.Label(root, text = 'What is animal #3')
                label_askLocation.grid(row=0, column=0)

                animalButtons = []
                for i in range(len(animalOptions)):
                    animalButtons.append(tk.Button(root, text = animalOptions[i], command = lambda:[eval('buttons.animalOptionsClass.animal_' + str(i)), buttons.phases.phase4()]))
                
                for i in range(len(animalButtons)):
                    animalButtons[i].grid(row = i+1, column = 0)
            else:
                buttons.phases.phase4()
        
        def phase4():
            clearScreen()

            print('phase 4 activated')


def clearScreen():
    widget_list = root.winfo_children()

    for item in widget_list :
        if item.winfo_children() :
            widget_list.extend(item.winfo_children())
    
    for item in widget_list:
        item.grid_remove()


def combineArrays(baseArray, arrayToAdd, offset=(0, 0)):
    array1 = baseArray.copy()
    array2 = arrayToAdd.copy()
    
    offX = offset[1]
    offY = offset[0]
    
    newArray = []
    for i in range(len(array1)):
        newArray.append(array1[i].copy())

    for i in range(len(array2)):
        for j in range(len(array2[0])):
            newArray[i+offX][j+offY] = array1[i+offX][j+offY] + array2[i][j]
    
    return newArray


def calcAnimalOptions(location):
    if location == 'farm':
        animals = ['sheep', 'pig', 'rabbit', 'horse', 'cow', 'unicorn']
    elif location == 'outback':
        animals = ['kangaroo', 'platypus', 'crocodile', 'koala', 'cockatoo', 'tiddalik']
    elif location == 'savanna':
        animals = ['zebra', 'hippo', 'giraffe', 'lion', 'elephant', 'gryphon']
    elif location == 'northern':
        animals = ['bear', 'skunk', 'beaver', 'moose', 'fox', 'sasquatch']
    elif location == 'polar':
        animals = ['penguin', 'seal', 'muskox', 'polar bear', 'walrus', 'yeti']
    elif location == 'jungle':
        animals = ['monkey', 'toucan', 'gorilla', 'panda', 'tiger', 'phoenix']
    elif location == 'jurassic':
        animals = ['diplodocus', 'stegosaurus', 'raptor', 't-rex', 'triceraptops', 'dragon']
    elif location == 'ice_age':
        animals = ['wooly rhino', 'giant sloth', 'dire wolf', 'saber tooth', 'mammoth', 'akhlut']
    elif location == 'city':
        animals = ['raccoon', 'pigeon', 'rat', 'squirrel', 'opossum', 'sewer turtle']
    elif location == 'moon':
        animals = ['lunar tick', 'moonkey', 'tribble', 'luna moth', 'moonicorn', 'jade rabbit']
    elif location == 'mountain':
        animals = ['goat', 'cougar', 'elk', 'eagle', 'coyote', 'aatxe']
    elif location == 'mars':
        animals = ['rock', 'marsmot', 'marsmoset', 'rover', 'martian', 'marsmallow']
    
    return animals


def identifyAnimals():
    global selectedAnimals

    #locationName = input('Locations are farm, outback, savanna, northern, polar, jungle, jurassic, ice age, city, moon, mountain, and mars. What location do you want to choose animals from?: ').lower()
    #locationName = locationName.replace(' ', '_')
    #numOfAnimals = int(input('How many animals are you going to choose? Options are 1-3: '))

    for i in range(numOfAnimals):
        animalOptions = calcAnimalOptions(locationName)
        
        inputMSG = '{} animals are {}. What is animal number {}?: '.format(locationName.capitalize(), animalOptions, i+1)
        animal = input(inputMSG).lower().replace(' ', '_').replace('-', '_')
        
        selectedAnimals.append([animal, getattr(eval('pattern.'+locationName), animal)])


def checkForValidLayout(layout):
    possibleLayout = True

    for i in range(5):
        for j in range(5):
            if layout[i][j] > 1:
                possibleLayout = False

    if possibleLayout:
        return True
    else:
        return False


def findAllLayouts():
    global totalLayouts

    # how many times to go across x
    for x1 in range(6 - len(selectedAnimals[0][1][0])):
        # how many times to go across y
        for y1 in range(6 - len(selectedAnimals[0][1])):
            tiles1 = combineArrays(tiles, selectedAnimals[0][1], (x1, y1))

            # runs if theres more than 1 animal
            if len(selectedAnimals) > 1:
                # how many times to go across x
                for x2 in range(6 - len(selectedAnimals[1][1][0])):
                    # how many times to go across y
                    for y2 in range(6 - len(selectedAnimals[1][1])):
                        tiles2 = combineArrays(tiles1, selectedAnimals[1][1], (x2, y2))

                        # runs if the layout works for the first 2 animals
                        if checkForValidLayout(tiles2):
                            # runs if theres more than 2 animals
                            if len(selectedAnimals) > 2:
                                # how many times to go across x
                                for x3 in range(6 - len(selectedAnimals[2][1][0])):
                                    # how many times to go across y
                                    for y3 in range(6 - len(selectedAnimals[2][1])):
                                        tiles3 = combineArrays(tiles2, selectedAnimals[2][1], (x3, y3))
                                        
                                        if checkForValidLayout(tiles3):
                                            totalLayouts += 1
                            else:
                                totalLayouts += 1
            else:
                totalLayouts += 1
                                

def printTotalLayouts():
    if len(selectedAnimals) == 1:
        print('There are', str(totalLayouts), 'total layouts for the animal', selectedAnimals[0][0])
    elif len(selectedAnimals) == 2:
        print('There are', str(totalLayouts), 'total layouts for the animals', selectedAnimals[0][0], 'and', selectedAnimals[1][0])
    else:
        print('There are', str(totalLayouts), 'total layouts for the animals', selectedAnimals[0][0] + ',', selectedAnimals[1][0] + ',', 'and a', selectedAnimals[2][0])


#----------THE MAIN STUFF----------

button_start = tk.Button(root, text = 'start', command = buttons.phases.phase1)
button_start.grid(row=0, column=0)

root.mainloop()
'''
identifyAnimals()
findAllLayouts()
printTotalLayouts()
'''