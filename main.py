import os
import sys
import time
import random
import sqlite3
import colorama

global username

eql = sqlite3.connect('data.db')
eq = eql.cursor()

eq.execute('''CREATE TABLE IF NOT EXISTS users (
    user text,
    hp int,
    cash int,
    level int, 
    xp int,
    arc int,
    gunI text,
    gunII text,
    gunIII text,
    ammoI int,
    ammoII int,
    ammoIII int,
    ammoIV int,
    ammoV int,
    potionI text,
    potionII text,
    potionIII text,
    keyI int,
    keyII int,
    keyIII int,
    keyIV int
)''')

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

# [[Common], [Uncommon], [Rare], [Legendary], [Mythic]]
starterWeapons = [["Rusty Nail Gun"], ["Soap Bar Spitter"], ["Tactical Spork"]]

weaponsI = [["BB Doomstick"], ["Caffeine Sprayer"], ["Toaster Blaster"], ["Sneeze Cannon"], ["Hot Glue Rifle"], ["Hairdryer of Justice"], ["Garden Hose Sniper"]]
weaponsII = [["The Stapler 5000"], ["Angry Toaster"], ["Bubble Wrap Reaper"], ["Emotional Damage Dealer"], ["Laser Pointer of Doom"], ["Office Warfare Specialist"], ["Slapstick Carbine"]]
weaponsIII = [["WIFI Disruptor"], ["Karens Complaint Launcher"], ["Cheese Grater Gatling"], ["Leaf Blower 9000"], ["Breadstick Repeater"], ["Banana Splitter"], ["Microwave Ray"]]
weaponsIV = [["Boomstick of Mild Inconvenience"], ["Yeet Cannon XL"], ["Doom Roomba"], ["Freedom Flute"], ["The Negotiator"], ["Quantum Pea Rifle"], ["Thunder Peashooter"]]
weaponsV = [["The Peacemaker"], ["Street Sweeper"], ["The Final Form of Karen"], ["Existential Dread Blaster"], ["The Atomic Fart Cannon"], ["Reality Eraser 3000"], ["The Almighty Pew"]]

def main():

    def explore():

        global username

        eq.execute(""" SELECT gunI, gunII, gunIII FROM users WHERE user = ?; """, (username,))
        result = eq.fetchall()
        x = 0

        for i in result:
            x = x + 1

        if x == 0:
            input("You have no guns!")
            menu()
        else:
            print(result)
            while True:
                try:
                    choice = int(input("Choose gun\n\nChoice: "))
                except:
                    clear()
                    continue
                else:
                    weapon = result[0][choice-1]

                    if weapon != 'N/A':

                        hasAmmo, ammoAmount, tier = ammoChecker(weapon)
                        
                        if hasAmmo == True:
                            pass

                            if ammoAmount >= 50:
                                pass
                            else:
                                input("You need at least 50 bullets in your gun to enter!")
                                clear()
                                menu()
                            
                            timex = random.randrange(5, 15)

                            for i in range(timex):
                                time.sleep(1)
                                clear()
                                print(f"Currently Exploring\n\nTime elapsed: {i}")

                            cash, xp = rewards(1)

                            eq.execute("SELECT cash FROM users WHERE user = ?;", (username,))
                            resultCash = eq.fetchone()

                            eq.execute("SELECT xp FROM users WHERE user = ?;", (username,))
                            resultXP = eq.fetchone()

                            eq.execute(f"SELECT ammo{tier} FROM users WHERE user = ?;", (username,))
                            resultTier = eq.fetchone()

                            
                            cashReward = resultCash[0] + cash 
                            xpReward = resultXP[0] + xp
                            bulletsLost = resultTier[0] - random.randint(10, 50)

                            eq.execute(f"UPDATE users SET cash = ?, xp = ?, ammo{tier} = ? WHERE user = ?;", (cashReward, xpReward, bulletsLost, username,))
                            eql.commit()

                            input(f"You have gained {cash} cash and {xp} xp\n\nYou have {bulletsLost} {tier} bullets left")

                            menu()

                        else:
                            print("No ammo")
                            time.sleep(2)
                            menu()


    def dungeon():
        print("Explore")


    def bag():
        print("Explore")

    
    def crates():
        eq.execute(""" SELECT gunI, gunII, gunIII FROM users WHERE user = ?; """, (username,))
        result = eq.fetchall()


    def casino():
        print("Explore")


    def afk():
        print("Explore")


    def menu():
        eq.execute(""" SELECT hp, xp, cash FROM users WHERE user = ?;""", (username,))
        hp = eq.fetchone()
        clear()
        while True:
            try:
                choice = int(input(f"Character Info | Username: {username} | HP: {hp[0]} | XP: {hp[1]} | Cash: {hp[2]}\n\n(1) Explore | (2) Enter Dungeon | (3) Casino | (4) View Bag | (5) Loot Crates | (6) AFK Farm | (7) Leave\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if choice == 1:
                    clear()
                    explore()
                    break
                elif choice == 2:
                    dungeon()
                elif choice == 3:
                    casino()
                elif choice == 4:
                    bag()
                elif choice == 5:
                    crates()
                elif choice == 6:
                    afk()
                elif choice == 7:
                    sys.exit()
                else:
                    clear()
                    continue

    def bag():
        eq.execute(""" SELECT hp, xp, cash, gunI, gunII, gunIII, ammoI, ammoII, ammoIII, ammoIV, ammoV, potionI, potionII, potionIII FROM users WHERE user = ?;""", (username,))
        result = eq.fetchone()
        clear()
        input(f"Bag\n\n[WEAPONARY]\nWeapon 1: {result[3]} | Weapon 2: {result[4]} | Weapon 3: {result[5]}    |    Common Ammo: {result[6]} | Uncommon Ammo: {result[7]} | Rare Ammo: {result[8]} | Legendary Ammo: {result[9]} | Mythic Ammo: {result[10]}\n\n[MISC]\nHealing Potions | Hangover Helper: {result[11]} | Feel Fine Flask: {result[12]} | Potion of Too Much Healing: {result[13]}")
        clear()

    def rewards(x):
        if x == 1:
            cash = random.randrange(50, 80)
            xp = random.randrange(10, 20)

        return cash, xp

    def levelChecker():
        eq.execute(" SELECT xp FROM users WHERE user = ?;", (username,))
        xp = eq.fetchone()

        for i in range(xp[0]):
            if xp[0] < 99:
                continue
            else:
                print(i)

    def ammoChecker(x):
            eq.execute(" SELECT ammoI, ammoII, ammoIII, ammoIV, ammoV FROM users WHERE user = ?;""", (username,))
            result = eq.fetchone()

            flat_starters = [w[0] for w in starterWeapons]
            flat_weaponsI = [w[0] for w in weaponsI]
            flat_weaponsII = [w[0] for w in weaponsII]
            flat_weaponsIII = [w[0] for w in weaponsIII]
            flat_weaponsIV = [w[0] for w in weaponsIV]
            flat_weaponsV = [w[0] for w in weaponsV]

            ammo = 0
            tier = None

            if x in flat_starters or x in flat_weaponsI:
                ammo = result[0]
                tier = "I"
            elif x in flat_weaponsII:
                ammo = result[1]
                tier = "II"
            elif x in flat_weaponsIII:
                ammo = result[2]
                tier = "III"
            elif x in flat_weaponsIV:
                ammo = result[3]
                tier = "IV"
            elif x in flat_weaponsV:
                ammo = result[4]
                tier = "V"
            else:
                print(f"Unknown weapon: {x}")
                return False, 0, tier
            
            hasAmmo = ammo > 0

            if ammo > 0:
                input(f"✅ {x} (Tier {tier}) has {ammo} ammo left.")
            else:
                input(f"❌ {x} (Tier {tier}) is out of ammo!")
            
            return hasAmmo, ammo, tier
    
    def openCrateI():
        eq.execute(""" SELECT key1, gun1, gun2, gun3, gun4 FROM users WHERE user = ?;""", (username,))
        result = eq.fetchone()

        if result[0] > 0:
            clear()

            i = 0
            while i < 2:
                i = i + 1
                print("Opening crate.")
                time.sleep(0.5)
                clear()
                print("Opening crate..")
                time.sleep(0.5)
                clear()
                print("Opening crate...")
                time.sleep(0.5)
                clear()

            crate_items = ["M16", "UZI", "G-17", "MP40"]
            item = random.choice(crate_items)


    menu()

def starterWeaponChoice():
    while True:
        try:
            starterWeapon = int(input(f"Choose your starter weapon\n\n(1) {starterWeapons[0]} | (2) {starterWeapons[1]} | (3) {starterWeapons[2]}\n\nChoice: "))
        except:
            input("broken")
            continue
        else:
            if starterWeapon > 0 and starterWeapon < 4:
                eq.execute(f"UPDATE users SET gunI = '{starterWeapons[starterWeapon-1][0]}' WHERE user = ?;", (username,))
                eql.commit()
                break
            else:
                clear()
                continue

    while True:
        try:
            confirmWeapon = int(input(f"Is this the weapon you want? {starterWeapon}\n\n (1) Yes | (2) No\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if confirmWeapon == 1:
                clear()
                intro()
                break
            elif confirmWeapon == 2:
                clear()
                starterWeaponChoice()
            else:
                clear()
                continue

def intro():
    global username
    eq.execute(""" SELECT gunI FROM users WHERE user = ?;""", (username,))
    result = eq.fetchone()

    if result[0] == 'N/A':
        input("Universal Studios Production")
        input("Made by WolvTMG\n\n[Enter] to continue")

        input(f"Welcome to Rainfare, {username}, choose your starter weapon")
        clear()
        starterWeaponChoice()
    else:
        eq.execute(""" SELECT hp FROM users WHERE user = ?;""", (username,))
        hp = eq.fetchone()

        clear()
        main()

def newSave():
    global username
    eq.execute(""" SELECT user from users; """)
    result = eq.fetchall()
    x = 0
    for i in result:
        x = x + 1

    if x == 3:
        input("Too many saves!")
        startUp()
    while True:
        try:
            username = str(input("Username: "))
            break
        except:
            clear()
            continue

    input(f"Welcome, {username}")

    while True:
        try:
            confirmUsername = int(input(f"Would you like to keep this name?\n\n (1) Yes | (2) No\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if confirmUsername == 1:
                eq.execute(""" INSERT INTO users (user, hp, cash, level, xp, arc, gunI, gunII, gunIII, ammoI, ammoII, ammoIII, ammoIV, ammoV, potionI, potionII, potionIII, keyI, keyII, keyIII, keyIV) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """, (username, 100, 0, 0, 0, 1, "N/A", "N/A", "N/A", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
                eql.commit()
                clear()
                intro()
                break
            elif confirmUsername == 2:
                clear()
                newSave()
                break
            else:
                clear()
                continue

def loadSave():
    global username
    eq.execute(""" SELECT user from users; """)
    result = eq.fetchall()

    x = 0

    for i in result:
        x = x + 1

    if x == 0:
        clear()
        input("There are no saves!")
        startUp()
    else:
        while True:
            try:
                choice = int(input(f"{result}\n\n(1) Load Save 1 | (2) Load Save 2 | (3) Load Save 3 | (4) Go Back\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if choice == 1:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 2 and x > 1:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 2 and x < 2:
                    clear()
                    input("No data found")
                    clear()
                    continue
                elif choice == 3 and x > 2:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 3 and x < 3:
                    clear()
                    input("No data found")
                else:
                    clear()
                    startUp()

        while True:
            try: 
                confirmChoice = int(input(f"Confirm choice: {username[0]} (1) Yes | (2) No\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if confirmChoice == 1:
                    username = username[0]
                    clear()
                    intro()
                    break
                elif confirmChoice == 2:
                    clear()
                    loadSave()
                    break
                else:
                    clear()
                    continue

def deleteSave():
    input("| WARNING !!! | Entering dangeroust territory !!! | Proceed with caution |")

    eq.execute(""" SELECT user from users; """)
    result = eq.fetchall()

    x = 0

    for i in result:
        x = x + 1

    if x == 0:
        clear()
        input("There are no saves!")
        startUp()
    else:
        while True:
            try:
                choice = int(input(f"{result}\n\n(1) Delete Save 1 | (2) Delete Save 2 | (3) Delete Save 3 | (4) Go Back\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if choice == 1:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 2 and x > 1:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 2 and x < 2:
                    clear()
                    input("No data found")
                    continue
                elif choice == 3 and x > 2:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 3 and x < 3:
                    clear()
                    input("No data found")
                else:
                    clear()
                    startUp()

        while True:
            try: 
                confirmChoice = int(input(f"Confirm choice: {username[0]} (1) Yes | (2) No\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if confirmChoice == 1:
                    clear()
                    eq.execute("DELETE FROM users WHERE user = ?;", (username,))
                    eql.commit()
                    startUp()
                    break
                elif confirmChoice == 2:
                    clear()
                    deleteSave()
                    break
                else:
                    clear()
                    continue


def startUp():
    while True:
        try:
            choice = int(input("(1) New Save | (2) Load Save | (3) Delete Save | (4) Exit\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if choice == 1:
                clear()
                newSave()
                break
            elif choice == 2:
                clear()
                loadSave()
                break
            elif choice == 3:
                clear()
                deleteSave()
                break
            elif choice == 4:
                sys.exit()
            else:
                clear()
                continue

startUp()
