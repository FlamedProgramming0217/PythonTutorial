name = input("What is the name of the main character of this story?\n")
friend = input("What is the name of the main character's friend?\n")
weapon = input("What weapon will you wield on your quest?\n")
print("\nYou awaken in a dark cave. Your friend " + friend +
      " sits beside you.")
print(friend + ": You're finally awake! We have to find a way to get home!")
print("You grab your " + weapon + " and find a way to get home.")
print(
  "There are five paths in front of you that lead into the cave. There is a demonic laughing sound that seems to be coming from the room to the left. The room on the right has thousands of bats hanging above, the passage in front of you has some Tabasco sauce sitting in the middle of the floor, and the passage that goes deeper under the cave looks futuristic, as the walls are lined with robotic stuff, and a ladder that goes up the cave has comlete darkness..."
)
path = input("Do you go left, right, forward, down, or up?\n")
if path == "left":
  print(
    "You go to the left and see some cartoon cavemen drawings on the walls. Looks like someone lives here\n"
  )
  print(
    "You also see a table with some food on it. Grabbing the nearest bag of junk food, you start munching on some Takis. Then, a huge caveman with a obsidian club comes out and asks you why you are in his room and munching crunching on his Takis.\n"
  )
  run_fight_talk = input("Do you want to run, fight, or talk?\n")
  if run_fight_talk == "run":
    print(
      "You look behind you, and see three paths. The left path has some creepy smiles smiling at you, the forward path has some money in a pile, and the right path has some weird ant-like creatures on the ground.\n"
    )
    weirdpaths = input("Do you want to go left, forward, or right?\n")
    if weirdpaths == "left":
      print(
        "You go left, and the creepy smiles start laughing at you. The sound of their laughter seems to distort your vision and mind. You go insane and fall on the ground, dying extremely painfully.\nUltimate Lose"
      )
    if weirdpaths == 'right':
      print(
        "The ant-like creatures go near you ands just ignore you. You try to sneak past, but they don't let you. Pulling out your "
        + weapon +
        ", the ants let you go past. There are two paths in front of you, the left one has some nerd reading a book, and the right one has some football player flexing his muscles.\n"
      )
      bruhpaths = input("Do you want to go left or right?\n")
      if bruhpaths == "left":
        print("You go left, and the nerd asks you a question:\n")
        print(
          "Let $\triangle ABC$ be a scalene triangle. Point $P$ lies on $\overline{BC}$ so that $\overline{AP}$ bisects $\angle BAC.$ The line through $B$ perpendicular to $\overline{AP}$ intersects the line through $A$ parallel to $\overline{BC}$ at point $D.$ Suppose $BP=2$ and $PC=3.$\n"
        )
        mathanswer = input("What is $AD?$\n")
        if mathanswer == "10":
          print(
            "You are a genius, so you build the next Microsoft and make Apple, Samsung, Razer, HP, DELL, and Google get out of business. You win!!!"
          )
        else:
          print("You are so stupid, how did you get this problem wrong?")
      if bruhpaths == "right":
        print("The football player challenges you to a fitness test.\n")
        strength = int(
          input(
            "How strong are you? 1-10. 1 being a couch potato and 10 being a super body builder."
          ))
        if strength > 7:
          print(
            "You beat the football player so good, that he goes home crying, also flexing his muscles at the same time"
          )
        else:
          print("The football player beats you up, and you go home crying.")
    if weirdpaths == "forward":
      print(
        "The money comes out of the ground and strangles you.\nGreedy lose.")
  if run_fight_talk == "fight":
    print(
      "Pulling out your " + weapon +
      ", the big caveman bonks you over the head with his obsidian club and you get knocked unconcious.\nYou Lose"
    )
  if run_fight_talk == "talk":
    print(
      "You explain to him that you just want to go home, and the caveman understands. Touching your shoulder, you teleport home.\nYou Win!!!!!"
    )
elif path == "right":
  print(
    "As you walk down the cavern the bats begin to shake their wings. A few steps later they all take off in unison, flying away. You follow them and find yourself at the exit of the cave.\n"
  )
  print(
    "You see a waterfall to your right with something shiny behind the watery curtain.\n"
  )
  print(
    "You see a hole in the ground to your left with sinister laughing sounds in it.\n"
    + friend + " wants to go to the shiny thing.")
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
    if lastpath2 == "right":
      print("Spongebob asks you to pick a number.")

      numberchoice = int(input("Pick a number:\n"))
      if numberchoice > 50 < 100:
        print(
          "Spongebob gives you 234673267486873268273489723748927974897237487892739874987e + 67688776786786 bitcoin!!\nULTIMATE WIN!!!!! But you could have done better....."
        )
      else:
        print(
          "Spongebob tases you and puts you into his pineapple house and laughs at you for the rest of eternity.\nYOU LOSE"
        )
elif path == "forward":
  print(
    "The Tabasco sauce just sits there awkwardly, and you decide whether or not to take it with you:\n"
  )
  takeTabasco = input("Do you want to take the Tabasco sauce with you? Y/N\n")
  if takeTabasco == "Y":
    print(
      "You take the Tabasco sauce with you, and add it to your other weapon: "
      + weapon)
    weapon = "Tabasco sauce"
  elif takeTabasco == "N":
    print(
      "You don't take the Tabasco with you, and feel like you may have just something wrong.\n"
    )
  print(
    "You walk down the passage and see three paths in front of you. The left one has a cute cat, the right has a cute puppy, and in front of you is a hovering goldfish that looks as if it wants to beat you up.\n"
  )
  which_pet = input("Which animal do you want to go to?\n")
  if which_pet == "puppy":
    print("You go near the puppy, and the puppy turns into a wolf.\n")
    if weapon == "Tabasco sauce":
      print(
        "You remeber about that Tabasco sauce you brought with you, and you splash it in the wolf's open jaws, which were about to make you dinner, and it runs away, revealing two trapdoors that were underneath it\n"
      )
      trapdoor = input("Do you want to go to the left or right trapdoor?\n")
      if trapdoor == "left":
        print(
          "You go to the left trapdoor, and you find a demon there. You ran out of Tabasco sauce, so you get knocked out by the demon\nYOU LOSE!!!!"
        )
      if trapdoor == "right":
        print(
          "There in front of you, appears Jesus. He blesses you, and you are promised that you will go to heaven after you die, because you were smart enough to bring the Tabasco with you."
        )
    else:
      print("You desperately try to kill the wolf with your " + weapon +
            ", but you get killed anyways.\nNever doubt Tabasco sauce...")
  if which_pet == "cat":
    print("The cat turns into a bobcat.\n")
    if weapon == "Tabasco sauce":
      print(
        "You remember about that Tabasco sauce you brought with you, and you pour it in the bobcat's eyes.\n The cat runs away, and you see treasure underneath it.\nYOU WIN!!!"
      )
    else:
      print("You desperately try to kill the bobcat with your " + weapon +
            ", but you get killed anyways.\nNever doubt Tabasco sauce...")
  if which_pet == "goldfish":
    print("The goldfish hovers towards you.\n")
    if weapon == "Tabasco sauce":
      print(
        "The fish is about to laser eye you, but you take out your Tabasco sauce you saved for later and you splash Tabasco sauce towards it. The laser hits the Tabasco sauce, but the Tabasco sauce was too hot to penetrate. The sauce covers the fish, and it disenegrates. You collect the remaining scales, which seem like 24k gold. You decide whether or not to touch those scales that you departed from the goldfish\n"
      )
      takescales = input("Do you want to take the scales???")
      if takescales == "yes":
        print(
          "You touch the scales, and you also disenegrate, because you forgot that the Tabasco sauce was still on the scales\nGreedy Lose"
        )
      elif takescales == "no":
        print(
          "You don't take the scales, and you go down the path, finding the exit of the cave, which was conveniently right where the front door of your house is.\nYou WINNN!!!!"
        )

    else:
      print("You desperately try to kill the goldfish with your " + weapon +
            ", but you get killed anyways.\nNever doubt Tabasco sauce")
if path == "down":
    print("You walk down the futuristic path, thinking nothing bad is going to happen, when the robots suddenly come to life. On their chests, it says that they are not waterproof. Weird, why would anyone put a lable on a robot saying its not waterproof.\n")
    print("You pull out your" + weapon + " and try to hold them off(" + friend + ")also tries to help by bonking over the head, and nothing works. You look around you to see if there is anything else you can do, and you see a glass showing the outside, which is full of coral and sharks. You realize that you are actually underwater...\n")
    print("You look to your left, and you see a few really cool weapons that have the label: DO NOT TOUCH. DEATH IS INVETIBLE.\n")
    water_or_weapon = input("Do you want to take the weapon and get out of here, or break the glass and kill the robots?")
    if water_or_weapon == "break":
        print("You broke the glass and water rushes in, the robots panic and run away, and, of course, you also run away, because who wants to be eaten by sharks and drown?\n")
        print("Rushing down the path with" + friend + ", you see two paths in front of you, the one on the left is a path that is going up, while the one on the right is going even deeper into the cave, with a airtight waterproof door that can be closed with a red button.\n")
        down_up = input("Do you want to go down or up?")
        if down_up == "up":
          print("You go up the path, and you are cornered by those panicked robots you met earlier. This time, they don't hesitate.\nYOU LOSE")
        elif down_up == "down":
          print("You go down the path and ")