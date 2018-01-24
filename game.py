# imports the sys and time modules
import sys,time

def print_slow(str):
    """every character in a string displays every 40 milliseconds"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

def scenario1():
    """introduction to game and first choice"""
    if response == 'yes':
        print_slow("\nAlright, you have made your first choice. Let's begin.\n")
# program pauses for 2 seconds
        time.sleep(2)
        print_slow("\nThe year is 2038. You have led a very successful life, resulting in lots of wealth. You own a mansion in Los Angeles, a private jet, and a chain of successful Italian restaurants. Nothing can possibly happen that can make life any worse.\n")
# program pauses for 1 second
        time.sleep(1)
        print_slow("\nYou are trying to expand your restaurant chain, Magnet Ristorante, overseas to Asia. The place you would like to start at is Cambodia, since you enjoy cultural Cambodian cuisine, especially balut. You have a meeting there tomorrow. You take your private jet, and take off.\n")
        time.sleep(1)
        print_slow("\nYou are well into your flight, and you have dozed off. Suddenly, you are jerked awake by turbulence. You shake it off and go back to sleep. A few minutes later, it happens again. The pilot runs to the back, and tells you that the plane has been hit! The plane will soon crash on the island of Koror, in the country of Palau. He gives you two options: (1) Grab the parachute and jump off, or (2) wait until the plane hits the ground and comes to a complete stop. What will you do? (Type in the number that corresponds to your decision, then press enter)\n\n")
        scenario2()
    elif response == 'no':
        print_slow("\nI took all the time to make this game and you don't want to play? Shame on you.")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type 'Yes' or 'No'! You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario2():
    """choice whether to wait in plane or jump out is decided"""
    response2 = input()
    if response2 == '1':
        print_slow("\nCongratulations! You have made the right choice. If you had waited in the plane, you would have died for sure. What idiot would do that? Anyway, you have landed safely on a beach. The pilot is nowhere to be seen. You have found a few things in the backpack that contained the parachute. You find a machete, a compass, some water bottles, and a lighter. I guess your pilot knew that one day you would be abandoned on a tropical island in the middle of the Pacific Ocean. Smart man. Alas, you have come to another decision. What do you do next? Do you (1) stay put on this beach and start working on an SOS signal? Or do you (2) walk along the beach in hopes of passing a nearby village, with food, extra water, and a way to get back home? (Type in the number that corresponds to your decision, then press enter)\n\n")
        scenario3()
    elif response2 == '2':
        print_slow("\nYou fool! You stayed in the plane, only to spiral down to a painful death. Had you jumped out, you would have had a much better chance of surviving. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")


def scenario3():
    """choice whether to stay on the beach or walk along the beach is decided. Rest of game's scenarios stem from this decision"""
    response3 = input()
    if response3 == '1':
        print_slow("\nYou have decided to stay on the beach. A fire is now your best bet, since it can act as an SOS and you can cook any food that you find. Hopefully a plane will fly by soon and extra food won't be necessary, but risking that is not in your best interest right now. You gather some wood, and use your lighter to make a fire. You scour the beach for anything remotely edible. There are mainly oysters and clams, which aren't of much interest to you. Many hours pass by, the sun sets, and you finally give up on being rescued today. You could be out there for days, or even weeks, and you need to get some sleep. A shelter is necessary. For now, you grab some bamboo stalks, lay them on the sand, tie them together with some vines. It's next to nothing, but at least it will keep the bugs out.\n")
        time.sleep(1)
        print_slow("\nAfter sleeping maybe 1 or 2 hours all night, morning finally comes. The first thing on your mind––food. Out in the clear, blue ocean, about 20-30 yards out, you see a fin zig-zagging back and forth. A SHARK! After starving all day, this could be the big boost of protein that you have needed. However, a shark can also potentially be very dangerous. Do you (1) try to catch the shark, or (2) stick to eating oysters and clam?\n\n")
        scenario4()
    elif response3 == '2':
        print_slow("\nWalking along the beach is a good option. There could be a town or village that you could possibly use to get off of this island and to Cambodia. You walk for an hour, and you are already fatiguing. The backpack seems to get heavier with every step, and you have little confidence. Will you ever get off of the island? I guess we'll find out. All you can do now is just continue walking and hope for the best.\n")
        time.sleep(1)
        print_slow("\nAnother hour passes, and you start to hear a faint yelling noise. You consider yourself crazy and continue walking. You hear it again, only louder. This is hope. You start to sprint towards the sound, and it only grows louder and louder. You make a sharp left into the jungle. You come across a clearing and are immediately stunned. In the opening, there are at least 100 people, dancing and singing: men wearing strands of a skirt with a headdress, and women wearing long, colorful dresses with nothing covering their top. This is a Palauan tribe. Hundreds of eyes are glaring right at you, and you have no idea what will happen. Should you (1) run away in case they attack you, or (2) walk in and greet them?\n\n")
        scenario8()
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")


def scenario4():
    """choice whether to kill shark or eat oysters and shells is decided"""
    response4 = input()
    if response4 == '1':
        print_slow("\nI had a feeling you would pick this option. Very smart choice as well, because if you passed up on the shark, your death would have been imminent. Now you need an approach to killing this shark. You have your machete, but it serves no purpose if you can't get to the shark. As you ponder possible solutions, a snake slithers over your shoe. You kick it away, but it gives you an idea. You follow the snake, and use your machete to cut it in half, killing it instantly. You take the dead snake and throw it into a shallow part of the ocean. As the blood of the snake seeps into the crystal clear water, the shark starts approaching. The shark gets closer and closer. In what seemed like an millisecond, the shark is at your feet. You grab your machete, and CHOP!\n")
# program pauses for 2 seconds
        time.sleep(2)
        print_slow("\nThe shark is dead. You, the wealthy restaurant owner, have just killed a shark for your survival. If there was TV show about people surviving on an island similar to you, this would be a pretty defining moment. You drag the shark to shore, and relight the fire. As you cook and eat the shark, you realize that you can take on this struggle to survive. However, while living on a beach is nice, getting home is so much better. There are two clear options for what to do next: (1) prepare yourself for an unexpected, longer stay on the beach by building a solid shelter, or (2) create a large SOS signal that can possibly catch the attention of overhead planes?\n\n")
        scenario7()
    elif response4 == '2':
        print_slow("\nYou just passed up a large chunk of meat and your best shot at surviving. As it sadly turns out, that shark would have been the best meal you could have possibly gotten on this beach. Since you didn't catch it, you're living on only clams and oysters, which provide very little energy. With a lack of energy, you wonder if you will ever leave this island. Finally, with no energy or will to live anymore, you expire on the beach. You can try the adventure again if you wish. Try not to make the same mistake twice.")
        time.sleep(1)
        print_slow("\nSometimes the more fun option is also the better option. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")


def scenario5():
    """intro to Survivor questions"""
    print_slow("\nNice choice. Better safe than sorry. Energy needs to be expended wisely, and building a shelter for a potentially longer-than-expected stay is worth it. Would digging a shelter in the sand work? Definitely not, that would easily flood if high tide came in. A makeshift shelter on the sand will have to do. You grab some bamboo from the jungle, and some vine. You assemble the bottom of the shelter so that it is about 6 inches from the ground. This will definitely keep the bugs out, resulting in a much better night's sleep. The structure of the roof is also made up of bamboo, and completely covered with layers and layers of palm fronds, which will hopefully keep rain from getting in. You take a step back, and admire the work that you have done.\n")
    time.sleep(1)
    print_slow("\nAnother night goes by, and there are still no planes flying overhead. Food has become more and more scarce, and the water bottles that you have been living off of are going to soon run out. The day has come and gone, and you make your fire for the night, lay on your bamboo bed, and try to sleep. As you lay down, you start to wonder if getting off of this island is ever going to happen. Does your family even know what's happening? Do the Cambodians hate you now because you never showed up to the meeting? Thoughts scramble in your head, but soon diminish as you slowly fall asleep.\n")
    time.sleep(2)
    print_slow("\nSuddenly, you hear a faint chopping sound. Are you dreaming about the time you killed that shark? No, the sound isn't from a dream. It's getting louder and louder, almost like its coming towards you. You open your eyes, and peer outside your shelter. It's still night, so you can barely see anything. You climb out of the shelter and see a single light coming from the sky, right at you. A helicopter!\n")
    time.sleep(1)
    print_slow("\nThe helicopter lands on the edge of the beach. You sprint towards it, nearly tripping with every step. The pilot emerges, and out comes...Jeff Probst , host of the TV show Survivor?\n")
    time.sleep(2)
    print_slow('\nThis is what he says: "I will ask you 10 questions about the TV show Survivor. If you get all ten right, then I will fly you to Cambodia so you can attend your meeting. If you do not succeed, then you will stay on this beach, possibly forever. I will give you this iPhone 20 to assist you, which means you may use the internet. Good luck. \n')
    time.sleep(1)
    print_slow("\nQuestion 1: \n")
    survivor_questions()

# list of 10 Survivor questions that player has to answer
# Each tuple has the question, answer choices, and answer
survivor_questions_list = [

    ('Who was the first winner of Survivor?',
    ['(A) Richard Hatch ' , '(B) Tyson Apostol  ' , '(C) Ben Driebergen  ' , '(D) Earl Cole'],
    ['a' , 'A']),

    ('What was the name of the 16th season of Survivor?',
    ['(A) Survivor: Gabon  ' , '(B) Survivor: China  ' , '(C) Survivor: Micronesia  ' , '(D) Survivor: Tocantins'],
    ['c' , 'C']),

    ('What was the brand new twist featured in Survivor: Panama?',
    ['(A) Exile Island  ' , '(B) Legacy Advantage  ' , '(C) Tribe Swap  ' , '(D) Returning Players'],
    ['a' , 'A']),

    ('Who was the 2nd member of the Jury in Survivor: China?',
    ['(A) Jaime Dugan  ' , '(B) Frosti Zernow  ' , '(C) James Clement  ' , '(D) Jean-Robert Bellande'],
    ['d' , 'D']),

    ('In which season was the Hidden Immunity Idol first revealed?',
    ['(A) Survivor: Fiji  ' , '(B) Survivor: Guatemala  ' , '(C) Survivor: Borneo  ' , '(D) Survivor: Panama'],
    ['b' , 'B']),

    ('What is the name of the main theme song of Survivor?',
    ['(A) Ancient Voices  ' , '(B) Survivant  ' , "(C) 'Survivor' Theme Song  " , '(D) Tribal Dance'],
    ['a' , 'A']),

    ("Who made the infamous 'Snakes and Rats' speech?",
    ['(A) Jan Gentry  ' , '(B) Sue Hawk  ' , "(C) Kathy Vavrick-O'Brien  " , '(D) Heidi Strobel'],
    ['b' , 'B']),

    ('How many contestants from Survivor: Kaôh Rōng have returned?',
    ['(A) 1  ' , '(B) 2  ' , '(C) 3  ' , '(D) 4'],
    ['d' , 'D']),

    ('In Survivor: Palau, which tribe had the most members become a part of the jury?',
    ['(A) Ulong  ' , '(B) Malakal  ' , '(C) Koror  ' , '(D) Airai'],
    ['c' , 'C']),

    ('How many times has a season of Survivor been located in Brazil?',
    ['(A) 1  ' , '(B) 2  ' , '(C) 3  ' , '(D) 4'],
    ['b' , 'B']),

    ]

class Player(object):

    def __init__(self, name):
        self.name = name

def survivor_questions():
    """enables player to answer questions about Survivor"""

# x is used as the question number that is up next
    x = 2

# loop iterates through each question
    for question, answer, correct_answer in survivor_questions_list:
        print_slow(question + '\n' + ' '.join(answer))
        print()
        print()
        their_answer = input()

# if player answers all 10 questions correctly, x=11, and they win
        if x == 11:
            print_slow('\nCONGRATULATIONS! You have completed your final challenge, and you will now be able to leave the island. What is your name, young traveler?\n')
            player = Player(input().title())
            print_slow(f"\nIt has been a long journey, {player.name}. It is time for you to go.\n")
            time.sleep(1)
            print_slow("\nAs the helicopter flies overhead, you peek down at the beach that you have called your home for the past several days. You can see the makeshift shelter that kept you from the bugs and rain. You can also spot the waters where you killed the shark that kept you alive. This has been a once-in-a-lifetime experience, but you're just glad it's over. You may try the adventure again, and choose a different path.")
            break
# provides a different response to each answer the player gets correct
        elif their_answer in correct_answer:
            if x == 2:
                print_slow('\nThat one was easy. Question 2: \n')
            elif x == 3:
                print_slow('\nAnother easy one. Question 3: \n')
            elif x == 4:
                print_slow("\nIf you hadn't noticed yet, these are getting slightly harder. Question 4: \n")
            elif x == 5:
                print_slow('\nCorrect, again. Question 5: \n')
            elif x == 6:
                print_slow('\nHalfway to survival! Question 6: \n')
            elif x == 7:
                print_slow('\nAncient Voices is right! Question 7: \n')
            elif x == 8:
                print_slow("\nCorrect! You won't be able to get the next three correct by just Googling it. Good luck. Question 8: \n")
            elif x == 9:
                print_slow("\nGood job. 2 more questions, and you'll survive. Question 9: \n")
            elif x == 10:
                print_slow('\nOne more question! Question 10: \n')
# player gets question wrong, this prompt comes up, they lose the game
        else:
            print_slow("\nWRONG!!!! Jeff Probst left, you were stuck on the island for one more day, and you died. You can try the adventure again if you wish. Try not to make the same mistake twice.")
            break
# x increases by 1 after every question the player gets correct
        x += 1

def scenario6():
    """choice whether to die or try again is decided"""
    response6 = input()
    if response6 == '1':
        print_slow("\nUnsurprisingly, the better choice. You were going to die anyway by falling into one of the fires that you made. This way, you don't have to die a painful death. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    elif response6 == '2':
        print_slow("\nYesterday really took a toll on your body. After working all day gathering wood, and then getting barely any sleep again, you have almost no energy. Going out and retrieving food is too much work. Maybe if you build a fire, you will be rejuvenated and you can find the strength to survive. You assemble a fire using the excess wood from yesterday, and use your lighter to light it. The fire quickly ignites, and a burst of smoke quickly rises. Having very little energy, you do not react in time, and you breathe in the smoke, causing you to pass out...right on top of the fire. Your body is burning, and the pain just keeps intensifying, but you don't have the strength to move, or even scream. You lay there, in the fire, as you are burned to death. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")


def scenario7():
    """choice whether to build shelter or create large SOS signal is decided"""
    response5 = input()
    if response5 == '1':
        scenario5()
    elif response5 =='2':
        print_slow("\nYou just can't take it any longer...you need to get off of this beach. You decide to build three large fires, and a very large S-O-S written with branches. You go out into the trees that line the edge of the sand, and search for branches and firewood. There is not much wood on the ground, meaning you have to climb into trees to get most of it. You get a sufficient amount, but you just wasted lots of time and energy. There's enough wood for the fires, but not nearly enough to spell out S-O-S. You build the fires, light them, and wait. You wait...and wait...but no planes come. It is already dark, and you have no shelter. Do you (1) end it all, or (2) sleep on the bamboo you constructed earlier and try again tomorrow?\n\n")
        scenario6()
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")


def scenario8():
    """choice whether to run away from Palauan tribe or greet them is decided"""
    response8 = input()
    if response8 == '1':
        print_slow("\nYou bolt out of there as quickly as you can. Messing with uncivilized people like that is a good way to get killed. Anyway, you are trying to find a town or village, not a tribe camp. So, you continue to walk along the beach in hopes of finding rescue. However, there is no rescue. You walk all day, and when night comes, you are spent. Maybe settling down and starting a fire is your best bet. Do you (1) risk not finding a village and try to survive on your own? Or (2) risk dying from exhaustion and keep walking?\n\n")
        scenario9()
    elif response8 == '2':
        print_slow("\nWell...here goes nothing. You start walking towards the tribe, and none of them move. It's as if you have froze time. Suddenly, everyone start shrieking and stomping at once. Two men come out from the crowd of them, right at you. You close your eyes, and hope they don't torture you to your death. Instead, they put a necklace around your head. It has long orange spiral shells on it, and wooden pieces with faces carved into them. It must be very important, as everybody starts chanting once it falls on your shoulders. The Palauan men lift you off of your feet, and put you on what seems to be a throne. 'Is this for real? Am I their king?' Thoughts scramble through your head, and they bring you into a hut.\n")
        time.sleep(1)
        print_slow("\nAs they bring you into the hut, the necklace's shells start to dig into your chest, making it very uncomfortable. Should you (1) take it off or (2) just leave it on, because it seems pretty important?\n\n")
        scenario10()
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario9():
    """choice whether to survive on own or keep looking for another village is decided"""
    response9 = input()
    if response9 == '1':
        print_slow("\nYou're going to die either way. You are already so tired, that you do not have the strength to build a shelter, or even find food. You lay on the sand, and with no food, and very little water remaining, you die on the beach. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    elif response9 == '2':
        print_slow("\nYou're going to die either way. There is no village for another 200 miles, so you end up walking until you physically cannot. You lay on the sand, and with no food, and very little water remaining, you die on the beach. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario10():
    """choice whether to keep necklace on or not is decided"""
    response10 = input()
    if response10 == '1':
        print_slow("\nYou fool! That necklace kept you immune from being overthrown as leader and killed. So, once the burly men realized that it was off of you, they executed you immediately. You can try the adventure again if you wish. Try not to make the same mistake twice.")
    elif response10 == '2':
        print_slow("\nSmart decision. That necklace keeps you immune from being overthrown as leader and killed. The men carry you into the hut, and set your throne down. Another man comes in the hut, dressed in much more elegant clothing than all the others. He kneels down in front of you, and pulls out what seems to be just a stick. He mumbles a prayer, kisses it, and hands it to you. You inspect it, and it really seems to be just a stick.")
# program pauses for 2 seconds
        time.sleep(2)
        print_slow(' Hm. ')
        time.sleep(2)
        print_slow("You are risen once again by the men, and carried out of the hut to the center of the tribe's camp. In the center is a large circle filled with water. Above the water is a torch, hanging by a string. As you approach the water, the entire tribe circles it, and starts cheering. 'Are they about to drown me??'\n")
        time.sleep(1)
        print_slow("\nJust when you think you are about to die (again), the men set you down. The cheering dies down, but everyone is still staring at you. 'What am I supposed to do?' The man on your right points to your hand. The stick? Really? You really want me to throw the stick in the water? Or just hand it to you? Do you (1) throw the stick into the water, or (2) give it to the man?\n\n")
        scenario11()
    else:
        print_slow("\nIs it really that hard to follow directions? I said to type '1' or '2'! You can try the adventure again if you wish. Try not to make the same mistake twice.")

def scenario11():
    """choice whether to throw stick in water or give it to man is decided"""
    response11 = input()
    if response11 == '1':
        print_slow("\nYou reel your hand back, and launch the stick into the water. You kinda expect there to be a riot, but there is none. I guess it really was just a stick.\n")
        scenario12()
    if response11== '2':
        print_slow("\nYou turn to your right, and give the man the stick. He looks at it for a moment, and then throws it into the jungle. You kinda expect there to be a riot, but there is none. I guess it really was just a stick.\n")
        scenario12()

def scenario12():
    """introduction to Palau questions"""
    print_slow("\nThe man on your left gives you a cube. Four sides say 'A', 'B', 'C', and 'D', and the other two sides say 'True' and 'False'. Wait a minute. Do these people know English? As you ponder that thought, the man who had kissed the stick earlier emerges from the crowd.\n")
    time.sleep(1)
    print_slow("\n'Hello, young traveler. I see that you are lost, and are trying to find your way home. I can help you with that, but you will have to answer these 6 questions about Palau. Each time you get a question wrong, the torch that is hanging above the water will drop. Get three questions wrong, the torch will fall into the water, and you lose. If you succeed, I will lead you home. Ready to play?'\n")
    time.sleep(2)
    print_slow("\n'Wait, WHAT?!? You could speak English this whole time? Oh well, I guess I'll play.'\n")
    time.sleep(1)
    print_slow("\n'Question 1: '\n")
    palau_questions()

# list of Palau questions that player has to answer
# each tuple has the question, answer choices, and answer
palau_questions_list = [
    ('Palau is famous for its green, mushroom-shaped islands, known as...',
    ['(A) Stone Islands  ' , '(B) Rock Islands  ' , '(C) Mushroom Islands'],
    ['b', 'B']),

    ('In the early days of Palau, stone was used as a form of money. The largest stone weighed up to...',
    ['(A) 5 pounds  ' , '(B) 10 pounds  ' , '(C) 100 pounds  ' , '(D) 10,000 pounds'],
    ['d' , 'D']),

    ('The islands of Palau are encompassed in the North Pacific Ocean, and which other body of water?',
    ['(A) The Indonesian Delta  ' , '(B) The Bay of Guam  ' , '(C) The Philippine Sea'],
    ['c' , 'C']),

    ('Palau lies in which direction relative to the equator?',
    ['(A) North  ' , '(B) South  ' , '(C) East  ' , '(D) West'],
    ['a' , 'A']),

    ('True or False: Palau was the first nation in the world to issue the Elvis Presley postage stamp.',
    [''],
    ['true' , 'True' , 't' , 'T']),


    ('The Coconut Crabs which inhabit the islands of Palau have the special ability to do what after they eat?',
    ['(A) change color  ' , '(B) leap up to 3 feet  ' , '(C) replicate themselves?'],
    ['a' , 'A']),

    ]

def palau_questions():
    """enables player to answer questions about Palau"""

# wrong variable starts at 0
    wrong = 0
# x is used as the question number that is up next
    x = 2

# loop iterates through each question
    for question, answer, correct_answer in palau_questions_list:
        print_slow(question + '\n' + ' '.join(answer))
        print()
        print()
        their_answer = input()

# player answers all 6 questions with 2 mistakes or less, then x=7, and they win
        if x == 7:
            print_slow("\n'Congratulations! You have successfully avoided letting your torch hit the water. Come with me, I will lead you home.'\n")
            time.sleep(1)
            print_slow("\nYou're having a really tough time believing this guy, but he's your only way to get to Cambodia. You follow him out of the tribe camp and into another clearing. Inside the clearing...a private jet?!\n")
            time.sleep(1)
            print_slow("\n'So you can speak English and you own a private jet, but you wouldn't let me leave unless I answered your trivia questions?'\n")
# pauses program for 3 seconds
            time.sleep(3)
            print_slow("\n'Yeah, basically.'\n")
            time.sleep(3)
            print_slow("\nAs I got on the plane and took off, the man screamed, 'FORGET YOU, GO HOME, GOODBYE!'\n")
# program pauses for 2 seconds
            time.sleep(2)
            print_slow("\nThat was very odd.\n")
            time.sleep(2)
            print_slow("\nI looked down, and saw the entire tribe camp from a bird's eye view, as well as the beach that I had walked along for hours. The Rock Islands look beautiful from above, and you can just make out a lake full of jellyfish in one of them. All of this causes you to realize that this has been a once-in-a-lifetime experience. However, you're just glad it's over. You may try the adventure again, and choose a different path.")
            break
# if player's answer is correct, then next question is displayed with its question number
        elif their_answer in correct_answer:
            print_slow(f'\nCorrect. Question {x}: \n')
# if player gets three wrong answers, then wrong=2, and they lose the game
        elif wrong == 2:
            print_slow('\nYou have failed. You will not return home. You will die to the hands of the beastly men to your left and right. You can try the adventure again if you wish. Try not to make the same mistake twice.')
            break
# if player gets the question wrong, then the wrong variable increases by 1, and text is displayed with next question and its number
        else:
            wrong += 1
# used for first wrong question
            if wrong == 1:
                print_slow(f'\nThat is wrong. You have gotten 1 question incorrect. Question {x}: \n')
# used for multiple wrong questions
            else:
                print_slow(f'\nThat is wrong. You have gotten {wrong} questions incorrect. Question {x}: \n')
# x increases by 1 after each question
        x += 1



# asks the player a question and their answer is assigned to the variable 'response'
response = input("Hello, traveler. You are about to embark on a journey unlike any other. Would you like to begin? \n(Answer 'yes' or 'no' and then press enter)\n\n").lower()

# scenario1 begins, other scenarios run because they are inside other scenarios, which all stem back to scenario1
scenario1()







