

print("Welcome to Treasure Island!"
      "Your Mission is to find Treasure! " )
left_or_right =input('You have entered the room, where do you want to go, type "Left" to go left and type "Right" to go right')
left_or_right= left_or_right.lower()
if left_or_right =='left':
    swim_or_wait = input('You have arrived in a tunnel, your have two options, type "swim" to swim or "wait" to wait').lower()
    if swim_or_wait == 'wait':
        which_door = input("You now have three doors to enter one of them, Type'Red' for Red door, 'Yellow' for yellow door,'Blue' for blue door").lower()
        if which_door=='yellow':
            print("You win")
        elif which_door =='red':
            print("Game over")
        elif which_door =='blue':
            print("Game over")
    else:
        print("Game Over")

else:
    print("Game_over")





