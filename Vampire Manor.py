import random


#detect player response
class Response:
    def __init__(self, playerResponse):
        self.playerResponse = playerResponse
        
myResponse = Response(playerResponse = "")

myResponse.playerResponse = input("Welcome brave adventurer, to get started enter 'start' but if you wish to familiarize yourself with your character, enter 'stats': ")

#player stats
class Player:
    def __init__(self, playerAC, playerMaxHealth, playerHealth, playerStrength, playerMagicka, playerCrit, playerPhysical, playerMagic):
        self.playerAC = playerAC
        self.playerMaxHealth = playerMaxHealth
        self.playerHealth = playerHealth
        self.playerStrength = playerStrength
        self.playerMagicka = playerMagicka
        self.playerCrit = playerCrit
        self.playerPhysical = playerPhysical
        self.playerMagic = playerMagic

myPlayer = Player(playerAC = 14, playerMaxHealth = 100, playerHealth = 100, playerStrength = 30, playerMagicka = 30, playerCrit = 15, playerPhysical = 20, playerMagic = 5)

#Ramsey Stats
class Ramsey:
    def __init__(self, ramseyAC, ramseyMaxHealth, ramseyHealth, ramseyStrength, ramseyMagicka, ramseyCrit, ramseyPhysical, ramseyMagic, ramseyClass, ramseyAbility, ramseyTick1, ramseyTick2, ramseyTick3, ramseySanguineTreat):
        self.ramseyAC = ramseyAC
        self.ramseyMaxHealth = ramseyMaxHealth
        self.ramseyHealth = ramseyHealth
        self.ramseyStrength = ramseyStrength
        self.ramseyMagicka = ramseyMagicka
        self.ramseyCrit = ramseyCrit
        self.ramseyPhysical = ramseyPhysical
        self.ramseyMagic = ramseyMagic
        self.ramseyClass = ramseyClass
        self.ramseyAbility = ramseyAbility
        self.ramseyTick1 = ramseyTick1
        self.ramseyTick2 = ramseyTick2
        self.ramseyTick3 = ramseyTick3
        self.ramseySanguineTreat = ramseySanguineTreat


myRamsey = Ramsey(ramseyAC= 12, ramseyMaxHealth= 90, ramseyHealth=90, ramseyStrength=10, ramseyMagicka=40, ramseyCrit=10, ramseyPhysical=5, ramseyMagic=15, ramseyClass="Mage - Cook", ramseyAbility="Special Ability: Sanguine Treat – Lady Ramsey throws one of her special treats at her enemy, it deals damage equal to 10% of the enemy's total health and Lady Ramsey heals that much.", ramseyTick1 = False, ramseyTick2 = False, ramseyTick3 = False, ramseySanguineTreat = False)

#rooms
class Room:
    def __init__(self, room1, room1pt2, room2, room3, room4, room4bite, room4resist, room5, room5eat, room5decline, room6, room7, room8, room9, room10):
        self.room1 = room1
        self.room1pt2 = room1pt2
        self.room2 = room2
        self.room3 = room3
        self.room4 = room4
        self.room4bite = room4bite
        self.room4resist = room4resist
        self.room5 = room5
        self.room5eat = room5eat
        self.room5decline = room5decline
        self.room6 = room6
        self.room7 = room7
        self.room8 = room8
        self.room9 = room9
        self.room10 = room10


myRoom = Room(room1 = False, room1pt2 = False, room2 = False, room3 = False, room4 = False, room4bite = False, room4resist = False, room5 = False, room5eat = False, room5decline = False, room6 = False, room7 = False, room8 = False, room9 = False, room10 = False)

class Interactions:
    def __init__(self, room4int, firstFight):
        self.room4int = room4int
        self.firstFight = firstFight

myInteraction = Interactions(room4int = False, firstFight = False)

#weapons
class Weapons:
    def __init__(self, punch):
        self.punch = punch

myWeapons = Weapons(punch = 1)

#weapon calculations
while myPlayer.playerHealth > 0:
    myWeapons.punch = myWeapons.punch * myPlayer.playerStrength / 2

class Mechanics:
    def __init__(self, playerDamageToDeal, playerDamageDone, enemyDamageToDeal, enemyDamageDone, playerCritHit, enemyCritHit, playerRollToHit, enemyRollToHit, gameStarted):
        self.playerDamageToDeal = playerDamageToDeal
        self.playerDamageDone = playerDamageDone
        self.enemyDamageToDeal = enemyDamageToDeal
        self.enemyDamageDone = enemyDamageDone
        self.playerCritHit = playerCritHit
        self.enemyCritHit = enemyCritHit
        self.playerRollToHit = playerRollToHit
        self.enemyRollToHit = enemyRollToHit
        self.gameStarted = gameStarted

myMechanics = Mechanics(playerDamageToDeal = 0, playerDamageDone = False, enemyDamageToDeal = 0, enemyDamageDone = False, playerCritHit = False, enemyCritHit = False, playerRollToHit = 0, enemyRollToHit = 0, gameStarted = False)

#display stats to player
def statsDisplay():
    print("")
    print("##YOUR STATS##")
    print("AC:", myPlayer.playerAC)
    print("Health:", myPlayer.playerHealth , "/" , myPlayer.playerMaxHealth)
    print("Strength:", myPlayer.playerStrength)
    print("magicka:", myPlayer.playerMagicka)
    print("Crit Chance:", myPlayer.playerCrit)
    print("Physical Resistance:", myPlayer.playerPhysical)
    print("Magical Resistance:", myPlayer.playerMagic)
    myResponse.playerResponse = input("What would you like to do next: ")
    print("")

#rooms and interactions
def firstFight():
    print("Welcome to your first fight in the Vampire Manor!")
    print("")
    print("##HOW FIGHTS WORK##")
    print("____________________")
    print("Fights are one time and are unescapable, meaning once a fight has started, you must survive, so be careful!")
    print("1. Your enemies stats will be shown so plan out your attack.")
    print("2. Enemies have the same stats as you. Class and Special Ability: The class can help determine what type of enemy you are fighting, the special ability gives you a warning on the enemy's strongest move. AC: AC or armour class is the number you have to get to be able to hit the enemy which will be determined by a random D20 roll. Health: Once the enemy's health is reduced to 0, you win! Strength and Magicka: Strength is the stat that determines how much physical damage they do, and vice versa for magicka, certain weapons use different damage stats, so it's adivsed to build your character around one of these stats. Physical Resistance and Magic Resistance: These are the stats that protect the enemy, or you, from certain attacks, typically one resistance will be much lower than the other, so abuse it! Critical Chance: The higher you or your enemy's crit chance is, the more likely they are to deal double damage in one turn.")
    print("3. Each round, you will have a choice of attacks to choose from, pick wisely, some have cooldowns.")
    print("Good Luck!")
    myInteraction.firstFight = True


def playRoom1():
    myRoom.room1 = True
    print("__________________________________________")
    print("")
    print("You awake from a coarse slumber, sat wreathed in your own blood. Your face feels cold and lifeless, your skin, a pale blue, and an intense hunger rages deep inside you. You lay inside an enclosed space, the walls are laid with soft pillow that feels quite comfortable, apart from the warm stickiness of your own blood, you’re locked in a coffin. Despite the stark appearance of your body, you feel unparalleled strength, hopefully enough to break yourself out.")
    print("")
    print("Enter: attack")
    print("")
    myResponse.playerResponse = input()

def playRoom1pt2():
    myRoom.room1pt2 = True
    print("__________________________________________")
    print("")
    print("As you look around, you see that the coffin you were in is placed in the centre of a small room. The building is cold and has an intricately designed gothic architecture, it’s dark, with small torches illuminating the surrounding area. There is only one exit, to your east.")
    print("")
    print("Exits: E")
    print("")
    print("Enter 'E' or 'east'")
    print("")
    myResponse.playerResponse = input()

def playRoom2():
    myRoom.room2 = True
    print("__________________________________________")
    print("")
    print("You enter into a large intersection, once again dimly lit with torches. To the south is an open archway that leads to another room. To the east is an open door and to the north is a large, locked gateway, adorned with silver and engraved with a symbol you don’t remember but it still feels familiar.")
    print("")
    print("Exits: E, S")
    print("")
    myResponse.playerResponse = input()
    

def playRoom4():
    myRoom.room4 = True
    if myInteraction.room4int == False:
        print("__________________________________________")
        print("")
        print("As you enter this room, a strong smell of flesh wafts over you, and as you look down, you see a lifeless human laying in a pool of their own blood. You feel an intense urge to fulfill your hunger, the body does seem fresh, however you know what you want to do is wrong.")
        print("")
        print("Enter: 'bite' or 'resist'")
        print("")
        myInteraction.room4int = True
        myResponse.playerResponse = input()
    elif myInteraction.room4int == True:
        print("__________________________________________")
        print("")
        print("You're back in this room, the lifeless body lies here, staring blankly into space")
        print("")
        print("Exits: E, W, N")
        print("")
        myResponse.playerResponse = input()

def playRoom4bite():
    myRoom.room4bite = True
    print("__________________________________________")
    print("")
    print("You dig your fangs into the corpse, and as you do, you start to feel stronger and happier.")
    print("")
    print("Your corruption increases by 20%, but your health increases by 15")
    print("")
    print("Exits: E, W, N")
    print("")
    myResponse.playerResponse = input()

def playRoom4resist():
    myRoom.room4resist = True
    print("__________________________________________")
    print("")
    print("You resist the urge, the hunger still rages, but you feel slightly more at ease")
    print("")
    print("Exits: E, W, N")
    print("")
    myResponse.playerResponse = input()
    
def playRoom5():
    myRoom.room5 = True
    print("__________________________________________")
    print("")
    print("As you enter this room a soft and sweet smell wafts over you. As you look closer, you see a table laid with sanguine cloth and a vase of roses sits in the middle. The table holds an assortment of deserts, some puddings, some cake, some pastries, but all of them seem to have a hint of red.")
    print("")
    print("You see a woman, dressed in chef’s clothes walk towards you.")
    print("")
    print("Lady Ramsey: 'Oh hello newborn, looking for a meal?' She peers closer, her eyes giving an uncanny valley feel. 'They're fresh.'")
    print("")
    print("Enter: 'eat' or 'decline'")
    print("")
    myResponse.playerResponse = input()

def playRoom5eat():
    myRoom.room5eat = True
    print("__________________________________________")
    print("")
    print("Lady Ramsey: 'Isn’t it tasty? Made fresh with human blood.'")
    print("")
    print("Your corruption increases by 15%, but your  max health increases by 10")
    print("")
    print("Exits: E")
    print("")
    myResponse.playerResponse = input()



def playerDamage():
    attack = input("What attack would you like to do?: ")
    if attack == "punch":
        myMechanics.playerDamageToDeal = myWeapons.punch

def ramseyDamage():
    ramseyCritChance = random.randint(1, 100)
    if myRamsey.ramseyTick1 == False and myRamsey.ramseyTick2 == False and myRamsey.ramseyTick3 == False:
        myRamsey.ramseySanguineTreat = False
        myRamsey.ramseyTick1 = True

        myMechanics.enemyDamageToDeal = myRamsey.ramseyMagicka
        if ramseyCritChance > myRamsey.ramseyCrit:
            myMechanics.enemyDamageToDeal / 2

    elif myRamsey.ramseyTick1 and myRamsey.ramseyTick2 == False and myRamsey.ramseyTick3 == False:
        myRamsey.ramseyTick2 = True

        myMechanics.enemyDamageToDeal = myRamsey.ramseyMagicka
        if ramseyCritChance > myRamsey.ramseyCrit:
            myMechanics.enemyDamageToDeal / 2

    elif myRamsey.ramseyTick1 and myRamsey.ramseyTick2 and myRamsey.ramseyTick3 == False:
        myRamsey.ramseyTick3 = True
        
        myMechanics.enemyDamageToDeal = myRamsey.ramseyMagicka
        if ramseyCritChance > myRamsey.ramseyCrit:
            myMechanics.enemyDamageToDeal / 2

    elif myRamsey.ramseyTick1 and myRamsey.ramseyTick2 and myRamsey.ramseyTick3:
        myRamsey.ramseySanguineTreat = True
        myRamsey.ramseyTick1 = False
        myRamsey.ramseyTick2 = False
        myRamsey.ramseyTick3 = False

def ramseyHealthCheck():
    if myRamsey.ramseyHealth > myRamsey.ramseyMaxHealth:
        myRamsey.ramseyHealth = myRamsey.ramseyMaxHealth
   


def ramseyFight():
    while myPlayer.playerHealth > 0 and myRamsey.ramseyHealth > 0:
        playerDamage()
        ramseyDamage()
        myMechanics.playerRollToHit = random.randint(1, 20)
        if myMechanics.playerRollToHit > myRamsey.ramseyAC:
            myRamsey.ramseyHealth = myRamsey.ramseyHealth - myMechanics.playerDamageToDeal
            print("You dealt Ramsey" , myMechanics.playerDamageToDeal, "damage!")
        elif myMechanics.playerRollToHit == 1:
            myPlayer.playerHealth = myPlayer.playerHealth - myMechanics.playerDamageToDeal / 2
            print("Critical miss! You dealt yourself", myMechanics.playerDamageToDeal / 2, "damage!")
        elif myMechanics.playerRollToHit == 20:
            myRamsey.ramseyHealth = myRamsey.ramseyHealth - myMechanics.playerDamageToDeal * 1.5
            print("Critical hit! You dealt Ramsey", myMechanics.playerDamageToDeal * 1.5 )
        print("")
        if myRamsey.ramseySanguineTreat == True:
            ramseyHeal = myPlayer.playerHealth * 0.2
            myPlayer.playerHealth = myPlayer.playerHealth - myPlayer.playerHealth * 0.2
            myRamsey.ramseyHealth = myRamsey.ramseyHealth + ramseyHeal
            ramseyHealthCheck()
        elif myRamsey.ramseySanguineTreat == False:
            myMechanics.enemyRollToHit = random.randint(1, 20)
            if myMechanics.enemyRollToHit > myPlayer.playerAC:
                myPlayer.playerHealth = myPlayer.playerHealth - myMechanics.enemyDamageToDeal
                print("Ramsey dealt you", myMechanics.enemyDamageToDeal, "damage!")
            elif myMechanics.enemyRollToHit == 1:
                myRamsey.ramseyHealth = myRamsey.ramseyHealth - myMechanics.enemyDamageToDeal / 2
                print("Critical miss! Ramsey dealt herself", myMechanics.enemyDamageToDeal / 2, "damage!")
            elif myMechanics.enemyRollToHit == 20:
                myPlayer.playerHealth = myPlayer.playerHealth - myMechanics.enemyDamageToDeal * 1.5
                print("Critical hit! Ramsey dealt you", myMechanics.enemyDamageToDeal * 1.5, "damage!")
    print("Well done! You have defeated Ramsey the Cook!")
        




    

    

def playRoom5decline():
    myRoom.room5decline = True
    print("__________________________________________")
    print("")
    print("Lady Ramsey: 'Wrong choice'")
    print("")
    if myInteraction.firstFight == False:
        firstFight()
        ramseyFight()
    elif myInteraction.firstFight == True:
        print("Good Luck!")
        ramseyFight()
    
    
        

while myPlayer.playerHealth > 0:
    if myResponse.playerResponse == "stats":
        myResponse.playerResponse = ""
        statsDisplay()
    elif myResponse.playerResponse == "start" and gameStarted == False:
        myResponse.playerResponse = ""
        gameStarted = True
        playRoom1()
    elif myResponse.playerResponse == "attack" and myRoom.room1 == True:
        myResponse.playerResponse = ""
        print("")
        myRoom.room1 = False
        playRoom1pt2()
    elif ((myResponse.playerResponse == "E" or myResponse.playerResponse == "east") and myRoom.room1pt2 == True) or ((myResponse.playerResponse == "N" or myResponse.playerResponse == "north") and myRoom.room4 == True):
        myResponse.playerResponse = ""
        print("")
        myRoom.room1pt2 = False
        myRoom.room4 = False
        playRoom2()
    elif ((myResponse.playerResponse == "S" or myResponse.playerResponse == "south") and myRoom.room2 == True) or ((myResponse.playerResponse == "E" or myResponse.playerResponse == "east") and myRoom.room5 == True or myRoom.room5eat == True or myRoom.room5decline == True):
        myResponse.playerResponse = ""
        print("")
        myRoom.room2 = False
        myRoom.room5 = False
        playRoom4()
    elif myResponse.playerResponse == "bite" and myRoom.room4 == True:
        myResponse.playerResponse = ""
        print("")
        myRoom.room4 = False
        playRoom4bite()
    elif myResponse.playerResponse == "resist" and myRoom.room4 == True:
        myResponse.playerResponse = ""
        print("")
        myRoom.room4 = False
        playRoom4resist()
    elif ((myResponse.playerResponse == "W" or myResponse.playerResponse == "west") and (myRoom.room4 == True or myRoom.room4bite == True or myRoom.room4resist == True)):
        myResponse.playerResponse = ""
        print("")
        myRoom.room4 = False
        myRoom.room4bite = False
        myRoom.room4resist = False
        playRoom5()
    elif myResponse.playerResponse == "eat" and myRoom.room5 == True:
        myResponse.playerResponse = ""
        print("")
        myRoom.room5 = False
        playRoom5eat()
    elif myResponse.playerResponse == "decline" and myRoom.room5 == True:
        myResponse.playerResponse = ""
        print("")
        myRoom.room5 = False
        playRoom5decline()
