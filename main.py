#Treasure Quest Text Adventure Game 
import random
intro_art = '''
 _______ __   __ _______                                             
|       |  | |  |       |                                            
|_     _|  |_|  |    ___|                                            
  |   | |       |   |___                                             
  |   | |       |    ___|                                            
  |   | |   _   |   |___                                             
 _______|_______|________ _______ _______ __   __ ______   _______   
|       |    _ | |       |   _   |       |  | |  |    _ | |       |  
|_     _|   | || |    ___|  |_|  |  _____|  | |  |   | || |    ___|  
  |   | |   |_||_|   |___|       | |_____|  |_|  |   |_||_|   |___   
  |   | |    __  |    ___|       |_____  |       |    __  |    ___|  
  |   | |   |  | |   |___|   _   |_____| |       |   |  | |   |___   
 _______|___| ___________________________|_______|___|  |_|_______|  
|       |  | |  |       |       |       |                            
|   _   |  | |  |    ___|  _____|_     _|                            
|  | |  |  |_|  |   |___| |_____  |   |                              
|  |_|  |       |    ___|_____  | |   |                              
|      ||       |   |___ _____| | |   |                              
|____||_|_______|_______|_______| |___|                              '''


print(intro_art)


def intro():
    print(f"Welcome to the Treasure Quest {name}!")
    print("You are an adventurer seeking the hidden treasure in the Lost Forest.")
    print("Along the way, you will face choices and challenges. Choose wisely!")
    print("Let's begin your adventure!")

# Main menu function that loops until '1' is chosen
def main_menu():
    while True:
        print("Main Menu:")
        print("1. Start Game")
        print("2. Quit")
        choice = input("Enter your choice (1 to start, 2 to quit): ")
        
        if choice == '1':
            return  # Exit the loop and start the game
        elif choice == '2':
            print("Thanks for playing! Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.\n")

# Game starts here
name = input("What is your name?: ")
main_menu()
intro()

# First choice
first_choice = input("Do you choose the 'well-traveled' path or the 'overgrown' path? (well-traveled/overgrown) ")

if first_choice == 'well-traveled':
    print("\nYou take the well-traveled path. It's easier to walk, but you wonder if it might lead to traps.")
    # Second choice after taking the well-traveled path
    second_choice = input("You encounter a fork in the path. Do you go 'left' toward the sound of water or 'right' toward a faint light? (left/right) ")
    
    if second_choice == 'left':
        print("\nYou follow the sound of water and find a creek with animal tracks nearby.")
        # Third choice near the creek
        third_choice = input("Do you 'follow' the animal tracks or 'explore' around the creek? (follow/explore) ")
        
        if third_choice == 'follow':
            print("\nYou follow the tracks and find signs of an old camp. You sense you're getting closer to something important!")
        elif third_choice == 'explore':
            print("\nYou explore around the creek and find a carved stone with a strange map on it!")
        else:
            print("\nUnable to decide, you sit by the creek as the sun begins to set.")
        
    elif second_choice == 'right':
        print("\nYou head toward the faint light and discover an abandoned campsite with supplies and a map.")
        # Third choice at the campsite
        third_choice = input("Do you take the 'map' or 'search' the camp for other clues? (map/search) ")
        
        if third_choice == 'map':
            print("\nThe map shows a winding path deeper into the forest. You're one step closer to the treasure!")
        elif third_choice == 'search':
            print("\nYou search the camp and find a compass that might help you navigate through the forest.")
        else:
            print("\nUnable to decide, you find yourself resting by the campfire until night falls.")
        
    else:
        print("\nUnable to decide, you find yourself circling back to the start of the well-traveled path.")
        
elif first_choice == 'overgrown':
    print("\nYou push through the overgrown path and you feel it might lead to something hidden.")
    # Second choice after taking the overgrown path
    second_choice = input("You come across dense bushes and hear rustling nearby. Do you 'investigate' or 'avoid' it? (investigate/avoid) ")
    
    if second_choice == 'investigate':
        print("\nYou investigate the rustling and find an ancient stone marker with strange symbols.")
        # Third choice near the stone marker
        third_choice = input("Do you 'examine' the symbols or 'continue' on your path? (examine/continue) ")
        
        if third_choice == 'examine':
            print("\nThe symbols seem to point in a direction. You follow them, feeling you're on the right track!")
        elif third_choice == 'continue':
            print("\nYou continue on and stumble upon a clearing with an old stone archway. This could be a clue!")
        else:
            print("\nUnable to decide, you find yourself waiting by the stone marker as the day fades.")
        
    elif second_choice == 'avoid':
        print("\nYou avoid the bushes and carefully make your way along a faint path.")
        # Third choice along the faint path
        third_choice = input("Do you 'climb' a nearby tree to get a better view or 'keep walking' down the path? (climb/keep walking) ")
        
        if third_choice == 'climb':
            print("\nFrom the top of the tree, you see a glimmer in the distance. It could be the treasure's hiding place!")
        elif third_choice == 'keep walking':
            print("\nYou keep walking and soon find a moss-covered statue. It seems to be pointing somewhere.")
        else:
            print("\nUnable to decide, you end up resting by the path until evening.")
        
    else:
        print("\nFrozen with indecision, you stand there until night falls and you have to retreat.")

else:
    print("\nYou hesitate and can't decide. Suddenly, a gust of wind pushes you toward the overgrown path.")
    # Treating as if 'overgrown' was chosen
    second_choice = input("You come across dense bushes and hear rustling nearby. Do you 'investigate' or 'avoid' it? (investigate/avoid) ")
    
    if second_choice == 'investigate':
        print("\nYou investigate the rustling and find a stone marker with strange symbols.")
        # Third choice near the stone marker
        third_choice = input("Do you 'examine' the symbols or 'continue' on your path? (examine/continue) ")
        
        if third_choice == 'examine':
            print("\nThe symbols seem to point in a direction. You follow them, feeling you're on the right track!")
        elif third_choice == 'continue':
            print("\nYou continue on and stumble upon a clearing with an old stone archway. This could be a clue!")
        else:
            print("\nUnable to decide, you find yourself waiting by the stone marker as the day fades.")
    
    elif second_choice == 'avoid':
        print("\nYou avoid the bushes and carefully make your way along a faint path.")
        # Third choice along the faint path
        third_choice = input("Do you 'climb' a nearby tree to get a better view or 'keep walking' down the path? (climb/keep walking) ")
        
        if third_choice == 'climb':
            print("\nFrom the top of the tree, you see a  glimmer in the distance. It could be the treasure's hiding place!")
        elif third_choice == 'keep walking':
            print("\nYou keep walking and soon find a moss-covered statue. It seems to be pointing somewhere.")
        else:
            print("\nUnable to decide, you end up resting by the path until evening.")


