print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input('You\'re at crossroad, where do want to go?'
                 'Type "left" or "right".\n').lower()
if choice_1 == "left" :
    choice_2 = input ('You\'re at Lake'
                      'please type "swim" to swim across, '
                      'please type "wait" to wait for boat.\n').lower()
    if choice_2 == "swim" :
        print("You're attacked by the trout.Game Over")
    elif choice_2 == "wait" :    
        choice_3 = input("Please select the door, which are 'Red, 'Yellow, 'Blue'.\n").lower()
        
        if choice_3 == "red" :
            print("Burn by fire. Game Over")
        elif choice_3 == "blue" :
            print("Eaten by Beasts. Game Over")
        elif choice_3 == "yellow" :
            print("You won the treasure, you win")
        else :
            print("You've chosen the door doesn't exist. Game Over.")                 
    else:
        print("You're chosen incorrect color, Game Over")

else:
    print("Fall in a hole.Game over")        

