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

def in_forest():
    print("U entered to the darker forest u have ever been.... \nAnd tons of eyes look at u like their pray.")
    print("But u can ignore then, Because dog that barks, puppy that doesn't bite.")
    print("Wait a big wolf jumped in front of u")
    print(decorative_lines)
    print("What u wanna do?")
    print("1. Fight as a giga chad")
    print("2. Jump to the river at ur left")
    print("3. Climb the spined tree and lose 2 agility because of the injuries")
    choie = input()
    


def adventure_time():
    print(decorative_lines)
    print("It's adventure time!!")
    print("Ur mission as a brave adventurer is to rescue the life tree seed captured by the Ice King. \nFirst of all, u have to save his daughter from the Shadows Forest... Sooo let's go!")
    print(decorative_lines)
    print("U find ur self in front of the Shadows Forest. \nWhat u wanna do?")
    print("1. Enter the forest")
    print("2. Go back")
    choice = input()

    ##forest
    while choice not in ["1", "2"]:
        print("Invalid choice. Please try again.")
        choice = input()
        if choice == "1":
            in_forest()
        elif choice == "2": 
            print("U decided go to home and the whole life in the planet just fell down in pair of years.")
    




decorative_lines = "-"*60
character_selection()
adventure_time()

