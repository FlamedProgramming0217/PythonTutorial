# Collect input
name = input("What is the name of the main character of this story?\n")
friend = input("What is the name of the main character's friend?\n")
weapon = input("What weapon will you wield on your quest?\n")

# Start Story
print("\nYou awaken in a dark cave. Your friend " + friend +
      " sits beside you.")
print(friend +
      ": You're finally awake! We have to find a way out of this cave!")
print("You grab your " + weapon + " and find a way to exit the cave.")

# Decisions
print(
    "There are two paths in front of you that lead into the cave. There is a low rumbling noise that seems to be coming from the room to the left. The room on the right has thousands of bats hanging above."
)

path = input("Do you go left or right? ")

# Left Path
if path == "left":
    print(
        "As you slowly make your way down the left path, the rumbling grows louder."
    )
    print(
        "Slightly off the path you see a shimmer as the light from the flame of the torches lining the cave walls reflects off of something metal."
    )
    print(
        "You can stay on the path and head toward the source of the noise, or go investigate the objects off the path."
    )
    choice = input("Stay on path or investigate? ")

    # Only happens if player decides to investigate
    if choice == "investigate":
        print(
            "You approach the shiny object and see that it is a legendary sword, much more powerful than your "
            + weapon + ". You decide to take it with you.")
        weapon = "legendary sword"
    # Happens whether or not player investigates
    print(
        "You continue on the path and soon recognize the sound as the snoring of an enormous sleeping dragon!"
    )
    print(
        "The dragon wakes up and blocks your way back to safety with his massive tail. Looks like he wants to fight!"
    )

    # Boss Fight
    dragon_health = 50

    if weapon == "legendary sword":
        damage = 50
    else:
        damage = 30

    print("You attack the dragon with your " + weapon + ".")
    dragon_health = dragon_health - damage

    if dragon_health > 0:
        print("You were defeated by the dragon in an epic battle.\nYOU LOSE")
    else:
        print(
            "You defeat the dragon and claim all the treasure he was guarding!\nYOU WIN"
        )

elif path == "right":
    print(
        "As you walk down the cavern the bats begin to shake their wings. A few steps later they all take off in unison, flying away. You follow them and find yourself at the exit of the cave.\n"
    )

    #Add the rest of the story here
    print(
        "You see a waterfall to your right with something shiny behind the watery curtain.\n"
    )
    print(
        "You see a hole in the ground to your left with sinister laughing sounds in it.\n"
    )
    secondlastpath = input("Do you want to go left or right?\n")
    if secondlastpath == "right":
        print(
            "Running through the waterfall and getting miserably wet, a stone covers the exit and you have no choice but go on.\n"
        )
        print(
            "You see the shiny thing in a tunnel to your right, you hear slicing to your left, you see macoroni and CHEZ in front of you, and you see Steven He in a suit behind you looking at you like you are a failure.\n"
        )
        lastpath = input("right, left, in front, or behind?\n")
        if lastpath == "right":
            print(
                "The shiny thing was actually the forehead of a huge monster! The room is empty except you and the monster. Trying desperately to kill him with your "
                + weapon + ", the monster kills you anyways\nYOU LOSE!")
        elif lastpath == "left":
            print(
                "Stupidly following the slicing sound, you walk in the tunnel to your left and get sliced by something.\nYOU LOSE"
            )
        elif lastpath == "behind":
            print("As you approach Steven He, he asks what college you go to.")
            college = input(
                "Are you in a college? If you are not in a college, just type no college. If you are in a college, type your college.\n"
            )
            if college == "no college":
                print("Steven He: Wut is you age?\n")
                yourage = input("What is your age?\n")
                print(
                    "Steven He: YOU ALREADY " + yourage +
                    " AND NOT IN COLLEGE!! FAILURE.\n YOU DIE OF EXTREME EMOTIONAL DAMAGE THAT WAS A BIT TOO EFFECTIVE\n YOU DIE AN EXCRUCIATING DEATH"
                )
            else:
                print("Steven He: When did u go to college. Say truth.\n")
                joincollege = input("Enter the age that you joined college:\n")
                print(
                    "U FAILURE! MY SON GOT FULL SCHOLARSHIP TO HARVARD, MIT, AND GEORGIA TECH BEFORE HE BORN. U GO TO COLLEGE AT "
                    + joincollege +
                    ". FAILURE.\n YOU DIE OF EXTREME EMOTIONAL DAMAGE THAT WAS A BIT TOO EFFECTIVE\n YOU DIE AN EXCRUCIATING DEATH"
                )

        else:
            print(
                "You eat the macoroni and CHEZ, and the Gods speak to you: If you get this math problem right, we will reward you. If wrong, you will experience torture like no other..."
            )
            mathproblem = int(
                input(
                    "A bat and ball cost one dollar and ten cents combined. Now if the bat costs a full dollar more than the ball, what is the cost of the ball in cents(Do not put the word cents, just put the number of cents!!!)"
                ))
            if mathproblem == 5:
                print(
                    "You have recieved infinite dogecoin and 1000 more IQ.\n THE MOST ULTIMATE WIN IN THE GAME!!!!!!!!!!!!!!!!!!!"
                )
            else:
                print(
                    "The gods curse you for your stupidity and now you are a frog.\nYOU LOSE DUM DUM"
                )
    if secondlastpath == "left":
        print(
            "The sinister laughing sounds were actually just a prank. The sound came from a karoake machine, which was made from a 2 year old playing with the voice changing effects.\n"
        )
        print(
            "To your left, you see a suspicious-looking person in a hood. To your right, you see Spongebob with a taser.\n"
        )
        lastpath2 = input("left or right?\n")
        if lastpath2 == "left":
            print(
                "To your surprise, Mr. Beast lowers his hood and gives you 5829347627324686727486786282374862346876287364862736846728346290899013824719823789479187238749719872398749 grand!!!\nULTIMATE WIN!!!!!!!! But you could have done better....."
            )
        #Not working code
        if lastpath2 == "right":
            print("Spongebob asks you to pick a number.")

            numberchoice = int(input("Pick a number:\n"))
            if numberchoice > 50 < 100:
                print(
                    "Spongebob gives you 234673267486873268273489723748927974897237487892739874987e + 67688776786786 bitcoin!!\nULTIMATE WIN!!!!! But you could have done better....."
                )
            else:
                print(
                    "Spongebob tases you, and puts you into jail because he feels like it.\nYOU LOSE"
                )
