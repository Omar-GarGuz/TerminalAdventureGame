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
    print("1. Go inside the village heal and then go to the Shadows Forest again")
    print("2. Go for information about the princess in the village")

    while True:
        choice = input()
        if choice == "1":
            in_forest2(False)
        elif choice == "2":
            daugther_info()
        else:
            print("Invalid choice. Please try again.")


def daugther_info():
    print(decorative_lines)
    print("U went to the village bar to ask about the ice king daugther")
    print("U asked to the bartender but he was so misterius")
    print("U decided to give him money for information")
    print("He tell u that people say that the icy daughter is living in the village but he stoped and extend him hand for more money")
    print("U say: that is all if u apreciate ur life u gonna tell me everything u know")
    print("He swallowed, and told u: ok ok, I know that she is living in the streets because her mom died and the house owner just put her in the street")
    print("What u wanna do?")
    print("1. Look for the girl that tryed to steel ur stuff to eat and see if she is the girl")
    print("2. Forfeig because there is not probability to find a girl in a big village and go to the forest again")


    while True:
        choice = input()
        if choice == "1":
            gave_food()
        elif choice == "2":
            in_forest2(False)
        else: 
            print("Invalid choice. Please try again.")
    

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
        if choice == "1" or choice == "2":
            in_forest2(True)
        else:
            print("Invalid choice. Please try again.")


def in_forest2(with_daughter):
    print(decorative_lines)

    if with_daughter:
        print("U returned to the Shadows Forest with ur new companion")
        print("And she knew the best way to the Ice King's castle")
    else:
        print("U returned to the Shadows Forest")
        reply = input("And see a kind of green portal, what could be it? do u wanna enter? Y/N")
        if reply == "Y":
            print("Its like a time portal...")    
            adventure_time()
        else: print("Ok")
        print("U can see the castle but is far and u could go through the trees avoiding monsters and things")
        print("U ran like a crazy and now u have lost 2 of strenght but u have earned 2 of agility")
        stats[1] -= 2
        stats[3] += 2
        print(f"Actual stats: {stats[1 : -1]}")

    print("So u now can enter to the castle")
    print("U enter to the castle but there is a warrior that blocks the way")
    print("What u wanna do?")
    print("1. Fight the warrior")
    print("2. Try to sneak around him")

    while True:
        choice = input()
        if choice == "1":
            if with_daughter: fight_warrior(True)
            else: fight_warrior(False)
        elif choice == "2":
            print("U decided to sneak around the warrior")
            print("Now u can continue ur way to the Ice King")
            if with_daughter: sneak_warrior(True)
            else: sneak_warrior(False)
        else: 
            print("Invalid choice. Please try again.")


def fight_warrior(with_daugther):
    print(decorative_lines)
    print("U decided to fight with that icy beast")

    if with_daugther:
        print("U asked her if she wants to fihgt")
        print("She said obviusly")
        print("What u wanna do?")
        print("1. Kill the monster while the girl distract it")
        print("2. Make a combined attack to kill this mother fucker")
    else:
        print("What u wanna do?")
        print("1. Throw something to distract the warrior and then kill it")
        print("2. Go and kill ahead of him like a bull")
        
    while True:
        choice = input()
        if choice == "1":
            if with_daugther:
                print("The girl was too load and the warrior smashed her")
                kill_girl()
            else:
                print("Ur distraction didn't work and the warrior killed u")
                print("GAME OVER")
                exit()
        elif choice == "2":
            if with_daugther: kill_warrior(True)
            else: kill_warrior(False)
        else:
            print("Invalid choice. Please try again.")


def kill_warrior(with_daughter):
    print(decorative_lines)
    print("U killed the warrior like a real Giga Chad because who needs strategy?")
    print("But he was too strong and u lost 3 strength")
    stats[1] -= 3
    print(f"Actual stats: {stats[1 : -1]}")
    print("Go ahed for the ice king head and the life tree seed")
    print("U entered to the Ice King Throne Room he was waiting for u")

    if with_daughter:
        print(decorative_lines)
        print("+ My daughter!! I have seen ur adventure with this trash but I have to say that I could send more minions to stop u")
        print("+ But I don't want to hurt u my princess")
        print("- Fuck u, u r killing the world, u r not my father u let my mom die and now Im alone")
        print("- Now u r gonna die for the world and its beatiful creatures")
        print("+ If that is what u want...")
        print("The Ice king had suicide him self for his daugther")
    else: print("U say: fuck u, u monster u r gonna die right now")


def castle():
    print(decorative_lines)
    print("You enter the Ice King's castle. The air is cold and the walls shimmer with frost.")
    print("You hear distant footsteps and see shadows moving.")
    print("What do you want to do?")
    print("1. Explore the main hall")
    print("2. Search for secret passages")
    print("3. Call out for the Ice King")

    while True:
        choice = input()
        if choice == "1":
            print("You bravely walk into the main hall and find the Ice King waiting for you.")
            ice_king_battle(False)
            break
        elif choice == "2":
            print("You find a hidden passage that leads directly to the throne room!")
            ice_king_battle(False)
            break
        elif choice == "3":
            print("Your voice echoes through the castle. The Ice King appears, ready for battle.")
            ice_king_battle(False)
            break
        else:
            print("Invalid choice. Please try again.")

def sneak_warrior(with_daughter):
    print(decorative_lines)
    print("You sneak past the warrior, using the shadows and your agility.")
    if with_daughter:
        print("Your companion helps distract the guard, making it easier for you both.")
    else:
        print("You move quietly and avoid detection.")
    print("You reach the throne room where the Ice King awaits.")
    ice_king_battle(with_daughter)

def ice_king_battle(with_daughter):
    print(decorative_lines)
    print("The Ice King stands before you, his power radiating through the room.")
    if with_daughter:
        print("Your companion stands by your side, ready to help.")
        print("What do you want to do?")
        print("1. Attack together")
        print("2. Let your companion distract while you attack")
    else:
        print("You face the Ice King alone.")
        print("What do you want to do?")
        print("1. Attack head-on")
        print("2. Try to outsmart him")

    while True:
        choice = input()
        if with_daughter:
            if choice == "1":
                print("You and your companion combine your powers and defeat the Ice King!")
                win_game()
                break
            elif choice == "2":
                print("Your companion distracts the Ice King, giving you an opening to strike. You win!")
                win_game()
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            if choice == "1":
                print("You attack with all your strength and narrowly defeat the Ice King!")
                win_game()
                break
            elif choice == "2":
                print("You use your intelligence to trick the Ice King and win the battle!")
                win_game()
                break
            else:
                print("Invalid choice. Please try again.")

def win_game():
    print(decorative_lines)
    print("Congratulations! You have defeated the Ice King and saved the world!")
    print("The life tree seed is safe, and peace returns to the land.")
    print("Thank you for playing 'The Legend of Kira'!")


def kill_girl():
    print("The girl is done but she was the Ice King's daughter before she died, she confessed:")
    print("'My father spelled me that if I ever got killed, the whole world would explode'")
    print("'Sorry, but I don't have election'")
    print("GAME OVER")
    exit()


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

