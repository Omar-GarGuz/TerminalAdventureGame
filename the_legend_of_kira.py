# The first comment of the game the legend of Kira
# Kira has to choose options to progress through the story and overcome challenges.

# print the character brothers
def skiraton():
    print("         .7")
    print("       .'/'")
    print("      / /")
    print("     / / ")
    print("   __|/")
    print(" ,-\__\\")
    print(" |f-\"Y\\|")
    print(" \\()7L/")
    print("  cgD                            __ _")
    print("  |\\(                          .'  Y '>,")
    print("   \\ \\                        / _   _   \\")
    print("    \\\\\\                       )(_) (_)(|})")
    print("     \\\\\\                      {  4A   } /")
    print("      \\\\\\                      \\uLuJJ/\\l")
    print("       \\\\\\                     |3    p)/")
    print("        \\\\___ __________      /nnm_n//")
    print("        c7___-__,__-)\\,__)('.  \\_>-<_/D")
    print("                   //V     \\_\"-._.__G G_c__.-__<\"/ ")
    print("                          <\"-._>__-,G_.___)\\   \\7\\")
    print("                         (\"-.__.| \\\"<.__.-\" )   \\ \\")
    print("                         |\"-.__\"\\  |\"-.__.-\".\\   \\ \\")
    print("                         (\"-.__\"\". \\\"-.__.-\".|    \\_\\")
    print("                         \\\"-.__\"\"|!|\"-.__.-\".)     \\ \\")
def lila():
    print("                    ,_  .--.")
    print("              , ,   _)\\/    ;--.")
    print("      . ' .    \\_\\-'   |  .'    \\")
    print("     -= * =-   (.-,   /  /       |")
    print("      ' .\\'    ).  ))/ .'   _/\\ /")
    print("          \\_   \\_  /( /     \\ /(")
    print("          /_\\ .--'   `-.    //  \\")
    print("          ||\\/        , '._//    |")
    print("          ||/ /`(_ (_,;`-._/     /")
    print("          \\_.'   )   /`\\       .'")
    print("               .' .  |  ;.   /`")
    print("              /      |\\(  `.( ")
    print("             |   |/  | `    `")
    print("             |   |  /")
    print("             |   |.'")
    print("          __/   /")
    print("      _ .'  _.-`")
    print("   _.` `.-;`")
    print("  /_.-'`")
def thorne():
    print("           .  .")
    print("           |\\_|\\")
    print("           | a_a\\")
    print("           | | \"]")
    print("       ____| '-\\___")
    print("      /.----.___.-'\\")
    print("     //        _    \\")
    print("    //   .-. (~v~) /|")
    print("   |'|  /\\:  .--  / \\")
    print("  // |-/  \\_/____/\\/~|")
    print("|/  \\ |  []_|_|_] \\ |")
    print("| \\  | \\ |___   _\\ ]_}")
    print("| |  '-' /   '.'  |")
    print("| |     /    /|:  | ")
    print("| |     |   / |:  /\\")
    print("| |     /  /  |  /  \\")
    print("| |    |  /  /  |    \\")
    print("\\ |    |/\\/  |/|/\\    \\")
    print(" \\|\\ |\\|  |  | / /\\/\\__\\")
    print("   \\ \\| | /   | |__")
    print("        / |   |____)")
    print("        |_/")
def zephyr():
    print("              .=.,")
    print("             ;c =\\")
    print("           __|  _/")
    print("         .'-'-._/-'-._")
    print("        /..   ____    \\")
    print("       /' _  [<_->] )  \\")
    print("      (  / \\--\\_>/-/'._ )")
    print("       \\-;/\\__;__/ _/ _/")
    print("        '._}|==o==\\{_\\/")
    print("         /  /-._.--\\  \\_")
    print("        // /   /|   \\ \\ \\")
    print("       / | |   | \\;  |  \\ \\")
    print("      / /  | :/   \\: \\   \\_\\")
    print("     /  |  /.'|   /: |    \\ \\")
    print("     |  |  |--| . |--|     \\_\\")
    print("     / _/   \\ | : | /___--._) \\")
    print("    |_(---'-| >-'-| |       '-'")
    print("           /_/     \\_\\")    
# character stats
def stats(x):
    stats = []  ##Stats = [Strength, Agility, Intelligence] 
    if x == '1':
        stats = ["Skiraton", 8, 6, 2] #skiraton
    elif x == '2':
        stats = ["Lila", 4, 7, 9] #lila
    elif x == '3':
        stats = ["Thorne", 5, 9, 6] #thorne
    elif x == '4':
        stats = ["Zephyr", 9, 5, 5] #zephyr
    return stats
# print the character stats
def print_stats(stats):
    print(decorative_lines)
    print("U made a good selection: ")
    if stats[0] == "Skiraton":
        skiraton()
    elif stats[0] == "Lila":
        lila()
    elif stats[0] == "Thorne":
        thorne()
    elif stats[0] == "Zephyr":
        zephyr()
    print(f"Character: {stats[0]}")
    print(f"Strength: {stats[1]}")
    print(f"Agility: {stats[2]}")
    print(f"Intelligence: {stats[3]}")
# character selection
def character_selection():
    print("Welcome to 'The Legend of Kira'!")
    print(decorative_lines)
    print("Select your character:")
    print("1. Skiraton - The Brave and Fearless Warrior")
    skiraton()
    print(decorative_lines)
    print("2. Lila - The Wise Fairy")
    lila()
    print(decorative_lines)
    print("3. Thorne - The Stealthy Rogue")
    thorne()
    print(decorative_lines) 
    print("4. Zephyr - The Swift Alien")
    zephyr()
    print(decorative_lines)
    choice = input("Enter the number of your choice: ")
    print_stats(stats(choice))

# forest options
def in_forest():
    print("U entered to the darker forest u have ever been.... \nAnd tons of eyes look at u like their pray.")
    print("But u can ignore then, Because dog that barks, puppy that doesn't bite.")
    print("Wait a big wolf jumped in front of u")
    print(decorative_lines)
    print("What u wanna do?")
    print("1. Fight as a giga chad")
    print("2. Jump to the river at ur left")
    print("3. Climb the spined tree and lose 2 agility because of the injuries")

    while True:
        choice = input()
        if choice == "1":
            fight_wolf()
        elif choice == "2":
            river()
        elif choice == "3":
            tree()
        else:
            print("Invalid choice. Please try again.")
            
# fight with the wolf in the forest
def fight_wolf():
    print("U decided to fight the wolf")
    print("The wolf is strong and fast, but u are determined to win.")
    print("After a fierce battle moving around the Shadows Forest, u emerge victorious.")
    print("U have defeated the wolf and can now continue ur journey through the forest.")
    print("U have won 2 strength and lost 1 agility in the fight.")
    stats[2] += 2
    stats[3] -= 1
    print(f"Actual stats: {stats[1 : -1]}")
    print(decorative_lines)
    print("U continue with ur journey and find the Ice King's castle in the middle of the forest.")
    print("What u wanna do?")
    print("1. Enter the castle")
    print("2. Look for princess information in nearby village u saw while the fight")
    

    while True:
        choice = input()
        if choice == "1":
            castle()
        elif choice == "2":
            village()
        else: 
            print("Invalid choice. Please try again.")

def river():
    print("U jumped to the river and the wolf couldn't follow u")
    print("But the river is full of crocosharks and u were eated by them and...")
    print("GAME OVER")
    exit()
    
def village():
    print("In the walking to the village u found a girl that tryed to rob ur gold")
    print("But she was not good doing it and u catched her")
    print("She said that she is poor and need the money to survive")
    print("What u wanna do?")
    print("1. Give her the money and let her go")
    print("2. Take her to the village and give her food")
    print("3. Kill her and take her stuff")
    

    while True:
        choice = input()
        if choice == "1":
            gave_money()
        elif choice == "2":
            gave_food()
        elif choice == "3":
            kill_girl()
        else: 
            print("Invalid choice. Please try again.")


## village options
def gave_money():
    print(decorative_lines)
    print("U gave her the money and let her go")
    print("She said that she will never forget ur kidness")
    print("Then she run to the village")
    print("What u wanna do?")
    print("1. Go sleep in the village and continue tomorrow")
    print("2. Go inside the village heal and then go to the Shadows Forest again")
    print("3. Go for information about the princess in the village")

    while True:
        choice = input()
        if choice == "1":
            sleep()
        elif choice == "2":
            in_forest2()
        elif choice == "3":
            daugther_info()
        else:
            print("Invalid choice. Please try again.")


def daugther_info():
    print(decorative_lines)
    

def gave_food():
    print(decorative_lines)
    print("U gave her food and she is very grateful")
    print("She asked u about ur plans")
    print("U told her ur plan to save the world")
    print("She said that she will help u")
    print("She is now ur companion")
    print("U have won 1 intelligence and 2 agility")
    stats[2] += 1
    stats[3] += 2
    print(f"Actual stats: {stats[1 : -1]}")
    print("U both gonna go to the Ice King's castle")
    print("What u wanna do?")
    print("1. Go inside the shadow forest again")
    print("2. Go to sleep in the village and continue tomorrow")

    while True:
        choice = input()
        if choice == "1":
            in_forest2()
        elif choice == "2":
            sleep()
        else: 
            print("Invalid choice. Please try again.")


def in_forest2():
    print(decorative_lines)
    print("U returned to the Shadows Forest with ur new companion")
    print("And she knew the best way to the Ice King's castle")
    print("So u now can enter to the castle")
    print("U enter to the castle but there is a warrior that blocks the way")
    print("What u wanna do?")
    print("1. Fight the warrior")
    print("2. Try to sneak around him")

    while True:
        choice = input()
        if choice == "1":
            fight_warrior()
        elif choice == "2":
            sneak_warrior()
        else: 
            print("Invalid choice. Please try again.")


def sleep():
    print(decorative_lines)

def kill_girl():
    print("U killed the girl but she was the Ice King's daughter before she died, she confessed:")
    print("'My father spelled me that if I ever got killed, the whole world would explode'")
    print("'Sorry, but I don't have election'")
    print("GAME OVER")
    exit()


def castle():
    print("hi")


def tree():
    print("U climbed the spined tree and lost 2 agility because of the injuries")
    stats[3] -= 2
    print(f"Actual stats: {stats[1 : -1]}")
    print("U reached the top of the tree and saw a village in the distance")
    print("U also find the Ice King's castle in the middle of the forest")
    print("What u wanna do?")
    print("1. Go to the village")
    print("2. Go to the castle")
    

    while True:
        choice = input()
        if choice == "1":
            village()
        elif choice == "2":
            castle()
        else: 
            print("Invalid choice. Please try again.")


def adventure_time():
    print(decorative_lines)
    print("It's adventure time!!")
    print("Ur mission as a brave adventurer is to rescue the life tree seed captured by the Ice King. \nFirst of all, u have to save his daughter from the Shadows Forest... Sooo let's go!")
    print(decorative_lines)
    print("U find ur self in front of the Shadows Forest. \nWhat u wanna do?")
    print("1. Enter the forest")
    print("2. Go back")
    

    ##forest
    while True:
        choice = input()
        if choice == "1":
            in_forest()
        elif choice == "2":
            print("U decided go to home and the whole life in the planet just fell down in pair of years.")
            break
        else: 
            print("Invalid choice. Please try again.")



    





decorative_lines = "-"*60
character_selection()
adventure_time()