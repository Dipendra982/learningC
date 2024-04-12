def game_intro():
    print("Welcome to the Adventure Game!")
    print("You wake up in a dark room with no memory of how you got there.")
    print("Your goal is to find a way out and escape.")

def get_player_choice():
    choice = input("Enter 1 to look around the room, or 2 to try to open the door: ")
    return choice

def look_around_room():
    print("You look around the room and see a small table with a lamp on it.")
    print("The lamp doesn't seem to be working.")
    print("Other than that, the room is empty.")

def try_open_door():
    print("You try to open the door, but it's locked from the outside.")
    print("You don't have a key, and there's no way to unlock it.")

def game_over():
    print("Unfortunately, you couldn't find a way out of the room.")
    print("Game over!")

def main():
    game_intro()

    while True:
        choice = get_player_choice()

        if choice == "1":
            look_around_room()
        elif choice == "2":
            try_open_door()
            game_over()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
