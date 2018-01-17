# imports the sys and time modules
import sys,time

# makes the string display each character individually at a certain speed, to replicate someone typing it
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)

def scenario1():
    if response == 'yes':
        print("\nAlright, you have made your first choice. Let's begin.\n")
        print("\nThe year is 2038. You have led a very successful life, resulting in lots of wealth. You own a mansion in Los Angeles, a private jet, and a chain of successful Italian restaurants. Nothing can possibly happen that can make life any worse.\n")
        print("\nYou are trying to expand your restaurant chain, Magnet Ristorante, overseas to Asia. The place you would like to start at is Cambodia, since you like Cambodian people. You have a meeting there tomorrow. You take your private jet, and take off.\n")
        print("\nYou are well into your flight, and you have dozed off. Suddenly, you are jerked awake by turbulence. You shake it off and go back to sleep. A few minutes later, it happens again. The pilot runs to the back, and tells you that the plane has been hit! The plane will soon crash on the island of Koror, in the country of Palau. He gives you two options: (1)Grab the parachute and jump off, or (2)wait until the plane hits the ground and comes to a complete stop. What will you do? (Type in the number that corresponds to your decision, then press enter)\n\n")
    elif response == 'no':
        print_slow("\nI took all the time to make this game and you don't want to play? Shame on you.")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type 'Yes' or 'No'! You can try the adventure again if you wish. Try not to make the same mistake twice. Do you want to play again? (Answer 'yes' or 'no')")

def scenario2():
    response2 = input()
    if response2 == '1':
        print("\nCongratulations! You have made the right choice. If you had waited in the plane, you would have died for sure. What idiot would do that? Anyway, you have landed safely on a beach. The pilot is nowhere to be seen. You have found a few things in the backpack that contained the parachute. You find a machete, a compass, some water bottles, and a lighter. I guess your pilot knew that one day you would be abandoned on a tropical island in the middle of the Pacific Ocean. Smart man. Alas, you have come to another decision. What do you do next? Do you (1)stay put on this beach and start working on an SOS signal? Or do you (2)walk along the beach in hopes of passing a nearby village, with food, extra water, and a way to get back home? (Type in the number that corresponds to your decision, then press enter)\n\n")
    elif response2 == '2':
        print_slow("\nYou fool! You stayed in the plane, only to spiral down to a painful death. Had you jumped out, you would have had a much better chance of surviving. You can try the adventure again if you wish. Try not to make the same mistake twice. Do you want to play again? (Answer 'yes' or 'no')")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice. Do you want to play again? (Answer 'yes' or 'no')")

def scenario3():
    response3 = input()
    if response3 == '1':
        print("\nYou have decided to stay on the beach. A fire is now your best bet, since it can act as an SOS and you can cook any food that you find. Hopefully a plane will fly by soon and extra food won't be necessary, but risking that is not in your best interest right now. You gather some wood, and use your lighter to make a fire. You scour the beach for anything remotely edible. There are mainly oysters and clams, which aren't of much interest to you. Many hours pass by, the sun sets, and you finally give up on being rescued today. You could be out there for days, or even weeks, and you need to get some sleep. A shelter is necessary. For now, you grab some bamboo stalks, lay them on the sand, tie them together with some vines. It's next to nothing, but at least it will keep the bugs out.\n")
        print("\nAfter sleeping maybe 1 or 2 hours all night, morning finally comes. The first thing on your mind––food. Out in the clear, blue ocean, about 20-30 yards out, you see a fin zig-zagging back and forth. A SHARK! After starving all day, this could be the big boost of protein that you have needed. However, a shark can also potentially be very dangerous. Do you (1)try to catch the shark, or (2)stick to eating oysters and clam?\n\n")
    elif response3 == '2':
        print_slow("\n")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario4():
    response4 = input()
    if response4 == '1':
        print("\nI had a feeling you would pick this option. Very smart choice as well, because if you passed up on the shark, your death would have been imminent. Now you need an approach to killing this shark. You have your machete, but it serves no purpose if you can't get to the shark. As you ponder possible solutions, a snake slithers over your shoe. You kick it away, but it gives you an idea. You follow the snake, and use your machete to cut it in half, killing it instantly. You take the dead snake and throw it into a shallow part of the ocean. As the blood of the snake seeps into the crystal clear water, the shark starts approaching. The shark gets closer and closer. In what seemed like an millisecond, the shark is at your feet. You grab your machete, and CHOP!\n")
        print("\nThe shark is dead. You, the wealthy restaurant owner, have just killed a shark for your survival. If there was TV show about people surviving on an island similar to you, this would be a pretty defining moment. You drag the shark to shore, and relight the fire. As you cook and eat the shark, you realize that you can take on this struggle to survive. However, while living on a beach is nice, getting home is so much better. There are two clear options for what to do next: (1)prepare yourself for an unexpected, longer stay on the beach by building a solid shelter, or (2)create a large SOS signal that can possibly catch the attention of overhead planes?\n\n")
    elif response4 == '2':
        print("\nYou just passed up a large chunk of meat and your best shot at surviving. As it sadly turns out, that shark would have been the best meal you could have possibly gotten on this beach. Since you didn't catch it, you're living on only clams and oysters, which provide very little energy. With a lack of energy, you wonder if you will ever leave this island. Finally, with no energy or will to live anymore, you expire on the beach. You can try the adventure again if you wish. Try not to make the same mistake twice.")
        print("\nSometimes the more fun option is also the better option. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario5():
    response5 = input()
    if response5 == '1':
        print("\nNice choice. Better safe than sorry. Energy needs to be expended wisely, and building a shelter for a potentially longer-than-expected stay is worth it. Would digging a shelter in the sand work? Definitely not, that would easily flood if high tide came in. A makeshift shelter on the sand will have to do. You grab some bamboo from the jungle, and some vine. You assemble the bottom of the shelter so that it is about 6 inches from the ground. This will definitely keep the bugs out, resulting in a much better night's sleep. The structure of the roof is also made up of bamboo, and completely covered with layers and layers of palm fronds, which will hopefully keep rain from getting in. You take a step back, and admire the work that you have done.\n")
        print("\nAnother night goes by, and there are still no planes flying overhead. Food has become more and more scarce, and the water bottles that you have been living off of are going to soon run out. The day has come and gone, and you make your fire for the night, lay on your bamboo bed, and try to sleep. As you lay down, you start to wonder if getting off of this island is ever going to happen. Does your family even know what's happening? Do the Cambodians hate you now because you never showed up to the meeting? Thoughts scramble in your head, but soon diminish as you slowly fall asleep.\n")
        print("\nSuddenly, you hear a faint chopping sound. Are you dreaming about the time you killed that shark? No, the sound isn't from a dream. It's getting louder and louder, almost like its coming towards you. You open your eyes, and peer outside your shelter. It's still night, so you can barely see anything. You climb out of the shelter and see a single light coming from the sky, right at you. A helicopter!\n")
        print("\nThe helicopter lands on the edge of the beach. You sprint towards it, nearly tripping with every step. The pilot emerges, and out comes...Jeff Probst?\n")
        print('\nThis is what he says: "I will ask you 10 questions about the TV show Survivor. If you get all ten right, then I will fly you to Cambodia so you can attend your meeting. If you do not succeed, then you will stay on this beach, possibly forever.\n')
        print("\nQuestion 1: Who was the first winner of Survivor? (A) Richard     (B) Tyson     (C) Ben     (D) Earl\n")
    elif response5 =='2':
        print("\nYou just can't take it any longer...you need to get off of this beach. You decide to build three large fires, and a very large S-O-S written with branches. You go out into the trees that line the edge of the sand, and search for branches and firewood. There is not much wood on the ground, meaning you have to climb into trees to get most of it. You get a sufficient amount, but you just wasted lots of time and energy. There's enough wood for the fires, but not nearly enough to spell out S-O-S. You build the fires, light them, and wait. You wait...and wait...but no planes come. It is already dark, and you have no shelter. Do you (1)end it all, or (2)sleep on the bamboo you constructed earlier and try again tomorrow?\n\n")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario6():
    response6 = input()
    if response6 == '1':
        print("\nUnsurprisingly, the better choice. You were going to die anyway by falling into one of the fires that you made. This way, you don't have to die a painful death. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    elif response6 == '2':
        print("\nYesterday really took a toll on your body. After working all day gathering wood, and then getting barely any sleep again, you have almost no energy. Going out and retrieving food is too much work. Maybe if you build a fire, you will be rejuvenated and you can find the strength to survive. You assemble a fire using the excess wood from yesterday, and use your lighter to light it. The fire quickly ignites, and a burst of smoke quickly rises. Having very little energy, you do not react in time, and you breathe in the smoke, causing you to pass out...right on top of the fire. Your body is burning, and the pain just keeps intensifying, but you don't have the strength to move, or even scream. You lay there, in the fire, as you are burned to death. You can try the adventure again if you wish. Try not to make the same mistake twice.")


def scenario7():
    response7 = input().lower
    if response7 == 'A':
        print("\nThat one was easy. Question 2: What was the name of the 24th season of Survivor? (A) Survivor: Philippines      (B) Survivor: South Pacific      (C) Survivor: One World      (D) Survivor: Redemption Island\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario8():
    response8 = input().lower
    if response8 == 'C':
        print("\nAnother easy one. Question 3: What was the brand new twist featured in Survivor: Panama? (A) Exile Island      (B) Legacy Advantage      (C) Tribe Swap      (D) Returning Players\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")


def scenario9():
    response9 = input().lower
    if response9 == 'A':
        print("\nIf you hadn't noticed yet, these are getting slightly harder. Question 4: Who was the 2nd member of the Jury in Survivor: China?  (A) Jaime Dugan     (B) Frosti Zernow      (C) James Clement      (D) Jean-Robert Bellande\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario10():
    response10 = input().lower
    if response10 == 'D':
        print("\nCorrect, again. Question 5: In which season was the Hidden Immunity Idol first revealed? (A) Survivor: Fiji     (B) Survivor: Guatemala     (C) Survivor: Borneo     (D) Survivor: Panama\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario11():
    response11 = input().lower
    if response11 == 'B':
        print("\nHalfway to survival! Question 6: What is the name of the main theme song of Survivor? (A) Ancient Voices      (B) Survivant      (C) 'Survivor' Theme Song      (D) Tribal Dance\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario12():
    response12 = input().lower
    if response12 == 'A':
        print("\nAncient Voices is right! Question 7: Who made the infamous 'Snakes and Rats' speech? (A) Jan Gentry      (B) Sue Hawk       (C) Kathy Vavrick-O'Brien      (D) Heidi Strobel\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario13():
    response13 = input().lower
    if response13 == 'B':
        print("\nCorrect! You won't be able to get the next three correct by just Googling it. Good luck. Question 8: How many contestants from Survivor: Kaôh Rōng have returned? (A) 1       (B) 2      (C) 3      (D) 4\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario14():
    response14 = input().lower
    if response14 == 'D':
        print("\nGood job. 2 more questions, and you'll survive. Question 9:\n")
    else:
        print("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario15():
    response15 = input().lower
    if response15 == 'B':
        print("\nOne more question! Question 10: How many times has a season of Survivor been located in Brazil? (A) 1      (B) 2      (C) 3    (D) 4\n")


# asks the player a question and their answer is assigned to the variable 'response'
response = input("Hello, traveler. You are about to embark on a journey unlike any other. Would you like to begin? (Answer 'yes' or 'no' and then press enter)\n\n").lower()

scenario1()
scenario2()
scenario3()
scenario4()
scenario5()
scenario6()







