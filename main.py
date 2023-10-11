import os  # The os module for making a user interface
import time  # Importing the time module... to add suspense!
from replit import db
from pyfiglet import Figlet
from colored import fore, style
import fkeycapture as fkey  # Better menus 😀
import sys
import termios
import tty
from gutils import printt
from gutils.auth import accountCheck
from gutils.dbtools import registerData, jread
# Test variables
storyLocation = 0
hasAccount = 0
# The main function for simulating typing
userStrDelay = 0.04
numDeaths = 0
bestFriend = ""
# I don't know which one of these next two is right, I'm leaving them both in - Firepup650
db.db_url = "https://Shrunk-Database.tg101.repl.co"  # type: ignore
os.environ["REPL_DB_URL"] = "https://Shrunk-Database.tg101.repl.co"
# Next line is so one user's data doesn't overwrite everyone else's
username = os.environ["REPL_OWNER"]

def sparrowEncounterTwo():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        , userStrDelay)
    time.sleep(0.5)
    printt(
        f"Could you do the opposite? Jump up and hoist yourself up the front steps? Probably...\n\nYou do not notice a mysterious shadow towering over you as you try to think.{fore(1)}{style(3)} Suddenly, you're knocked over by something! What was that?-- Like a flap of wind...\n\n{style(0)} Landing on both elbows and knees, you finally see that shadow's bigger. Wondering what's behind you, you wheel around and gasp!--\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"It's a sparrow 🐦, looking down with a blank stare.\n\n Frozen and motionless, you remember how you used to look at them outside the window, doing their usual business. {style(3)}How innocent they were!{style(0)}\n{fore(1)}\n\n The cute little bird appeared ENORMOUS now... \n\nThe sparrow's black eyes were as big as basketballs 🏀. And, its {fore(3)}yellow {fore(1)}beak, began to click open-and-shut, open-and-shut like a pair of scissors.\n\n {style(1)}{style(3)}{style(4)}The huge bird then dives it head!{style(0)}\n\n 'NOOOO!', you yell out in vain by the moment the bird's beak hits the pavement. The sparrow lets out a startled warble deep in its throat.\n\n It then tries to grab you again, but luckily you escape from the huge brown bird.\n\n With your heart racing, you stare at the towering front steps.... YOU HAVE TO GET UP THERE,{style(3)}FAST!\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"'PIIIKK!'\n\n The brown sparrow lets out a ear-splitting chirp.\n\n Covering your ears, you scramble to get yourself up onto the first step.\n\n But, as you proceed to run and leap onto the edge,{fore(1)} something sharp clasps around your waist.... It's the beak of the sparrow!{style(0)}The sharp beak holds you tightly as you struggle to let go. Carrying you like how a robin carries a worm, the sparrow proceeds to mess with you. 'HEY! LET ME DOWN!', you shout out. The huge bird walks around in circles, too busy to understand you, and resumes carrying you, happily.\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"Then, it starts to flutter its wings, open its jaws, and you tumble out.\n\n'Unnhhh!'\n\n Hitting the first step of the porch hard leaving your back sore, you get up and try to look for a shortcut to get up the porch (i.e: A ramp or some sort of an inclined plane). Now, the brown bird swoops down....\n\n... And grabs you AGAIN! You protest to be left alone, but nothing happens! The sparrow drops you once again, and lifts you up from the first step of the porch....\n\n Drops you. Lifted you. Dropped you. And, lifted you.\n\n Your entire body is extremely weak, just from hitting the cement. You try to shield yourself, but you're too weak against the big bird. 'Please--DON'T HURT ME!-'\n\n Too late, the sparrow grabs you for a third time.{style(3)} It thinks {style(4)} I'm a bug!{style(0)}, you immediately realize.\n\n{style(3)}It's playing with me--before it eats me alive!{style(0)}\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt("**THUD**\n\n You hit the pavement, face down, in extreme pain...\n\n Lying down on the first step, all battered and bruised, you see the huge head of the sparrow. The bird lowers its head....\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"Groaning in pain, you slowly roll over.{fore(2)} The sparrow's beak misses you!{style(0)}\n\n Getting up slowly, your eyes dart around, looking for someone to help you, to save you, of course!\n\n You see your next-door neighbor, mowing the lawn. Maybe you can get his attention?\n\n 'HEY!', you shout, hoarsely. 'I'M DOWN HERE! IT'S ME,{username}!'\n\n Waving your hands, you try to get your neighbor to hear you, but your voice comes out so tiny and faint. The sparrow comes closer...\n\n 'CAN YOU HEAR ME? A LITTLE HEL--EYAAAUUUGGHHH!'\n\n{fore(1)} You scream in absolute fright as the sparrow attempts to grab you again, and by escaping, you fall off the step!{style(0)}\n\n 'OWWWCH!'\n Your tiny body slams onto the pavement, and getting up,{fore(2)} you see your way out: A snow shovel, leaning on the first two steps.{style(0)} Even though you're in sooooo much pain right now... {fore(3)}This could be your LAST CHANCE of survival.{style(0)}\n Quickly running as if its the last day of your life, you get on the shovel, panting.\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"Turning around, the sparrow hovers over you, looking for its prey. Could you make it to the porch in just a few seconds?!\n\n {fore(3)}Time to find out!{style(0)}\n\n", userStrDelay)
    time.sleep(0.5)
    printt("1. Get to the front door", userStrDelay)
    printt("2. Hide in the grass", userStrDelay)
    printt("3. Fight the huge bird", userStrDelay)
    print(f"{fore(6)}>{style(0)}")
    escapeOption = int(fkey.getchars(chars=["1", "2", "3"]))
    if escapeOption == 1:
        os.system("clear")
    elif escapeOption == 2:
        pass
    elif escapeOption == 3:
        pass


def sparrowEncounterOne():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        f"As you turn to the front steps, a shudder rolls down your back....\n{fore(3)}{style(3)} HOW would you climb UP the steps? You know how to get down the steps, but up the steps?.... IMPOSSIBRU!\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt(
        f"Could you do the opposite? Jump up and hoist yourself up the front steps? Probably...\n\n You do not notice a mysterious shadow towering over you as you try to think.{fore(1)}{style(3)} Suddenly, you're knocked over by something!\n\n What was that?-- Like a flap of wind...\n\n{style(0)} Landing on both elbows and knees, you finally see that shadow's bigger. Wondering what's behind you, you wheel around and gasp!--\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"It's a sparrow 🐦, looking down with a blank stare.\n\n Frozen and motionless, you remember how you used to look at them outside the window, doing their usual business. {style(3)}How innocent they were!{style(0)}\n{fore(1)}\n\n The cute little bird appeared ENORMOUS now... \n\nThe sparrow's black eyes were as big as basketballs 🏀. And, its {fore(3)}yellow {fore(1)}beak, began to click open-and-shut, open-and-shut like a pair of scissors.\n\n {style(1)}{style(3)}{style(4)}The huge bird then dives it head!{style(0)}\n\n 'NOOOO!', you yell out in vain by the moment the bird's beak hits the pavement. The sparrow lets out a startled warble deep in its throat.\n\n It then tries to grab you again, but luckily you escape from the huge brown bird.\n\n With your heart racing, you stare at the towering front steps.... YOU HAVE TO GET UP THERE,{style(3)}FAST!\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"'PIIIKK!'\n\n The brown sparrow lets out a ear-splitting chirp.\n\n Covering your ears, you scramble to get yourself up onto the first step.\n\n But, as you proceed to run and leap onto the edge,{fore(1)} something sharp clasps around your waist....\n\n It's the beak of the sparrow!{style(0)}\n\n The sharp beak holds you tightly as you struggle to let go. Carrying you like how a robin carries a worm, the sparrow proceeds to mess with you. \n\n'HEY! LET ME DOWN!', you shout out. The huge bird walks around in circles, too busy to understand you, and resumes carrying you, happily.\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"Then, it starts to flutter its wings, open its jaws, and you tumble out.\n\n'Unnhhh!'\n\n Hitting the first step of the porch hard leaving your back sore, you get up and try to look for a shortcut to get up the porch (i.e: A ramp or some sort of an inclined plane). Now, the brown bird swoops down....\n\n...{fore(1)}{style(3)} And grabs you AGAIN!{style(0)} You protest to be left alone, but nothing happens! The sparrow drops you once again, and lifts you up from the first step of the porch....\n\n Drops you. Lifted you. Dropped you. And, lifted you.\n\n Your entire body is extremely weak, just from hitting the cement. You try to shield yourself, but you're too weak against the big bird. 'Please--DON'T HURT ME!-' Too late, the sparrow grabs you for a third time.{style(3)} It thinks {style(4)} I'm a bug!{style(0)}, you immediately realize.\n{style(3)}It's playing with me--before it eats me alive!{style(0)}\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt("**THUD**\n\n You hit the pavement, face down, in extreme pain...\n\n Lying down on the first step, all battered and bruised, you see the huge head of the sparrow.\n\n The bird lowers its head....\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"Groaning in pain, you slowly roll over.{fore(2)} The sparrow's beak misses you!{style(0)}\n\n Getting up slowly, your eyes dart around, looking for someone to help you, to save you, of course!\n\n You see your next-door neighbor, mowing the lawn. Maybe you can get his attention?\n\n 'HEY!', you shout, hoarsely.\n\n 'I'M DOWN HERE! IT'S ME,{username}!'\n\n Waving your hands, you try to get your neighbor to hear you, but your voice comes out so tiny and faint. The sparrow comes closer...\n\n 'CAN YOU HEAR ME? A LITTLE HEL--EYAAAUUUGGHHH!'\n\n{fore(1)} You scream in absolute fright as the sparrow attempts to grab you again, and by escaping, you fall off the step!{style(0)}\n\n 'OWWWCH!'\n\n Your tiny body slams onto the pavement, and getting up,{fore(2)} you see your way out: A snow shovel, leaning on the first three steps.{style(0)} Even though you're in sooooo much pain right now... {fore(3)}This could be your LAST CHANCE of survival.{style(0)}\n\n Quickly running as if its the last day of your life, you get on the shovel, panting. All of a sudden, you hear a familiar rubbing sound...\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"'NOT AGAAAAIIIINNN!'\n\n{fore(1)} It's the grasshopper, presumably back for revenge!\n\n{style(0)}", userStrDelay)
    grasshopper = (
        fore(2)
        + r"""
    //_____ __
   @ )====// .\___
   \#\_\__(_/_\\_/
     / /       \\
         """
        + style(0)
    )
    time.sleep(0.5)
    print(grasshopper)
    time.sleep(0.5)
    printt(
        f"It's still hovering in the air though. Maybe it was watching you like a hawk from a distance and didn't care about you..?\n\n Finding another rock, which is more jagged at the edges, you heave it to knock the huge insect off of its feet. {fore(2)}This time, the grasshopper drops to the pavement! Success, at last!--\n\n{fore(1)} OH-NO...\n\n The sparrow who enjoyed torturing you a lot lands centimetres in front of you!{style(0)}\n\n Let's face it, its like as if an airplane ✈️ came toward you. A great whoosh of air pushes you off the shovel and almost to the edge of the front walkway.\n\n 'Got to-- g-get out of h-here', you muse, attempting to escape from this painful ordeal. Crawling on all fours, you see the shovel within your reach. {style(3)} I can do this! I CAN DO THIS!!!{style(0)}\n\n Turning around, blinking in the bright sunlight,{fore(1)} you realize that you celebrated too early!-- The 🦗 and 🐦 corner you! The sparrow is high in the air, and the grasshopper is climbing up the shovel!\n\n You're TRAPPED (sort of....?)...\n\n No way to fight these two creatures. The giant bird then spreads its wings...\n\n...and dove.{style(0)}", userStrDelay)
    time.sleep(0.95)
    os.system("clear")
    printt(f"{fore(1)}'AAAAAAAAAAHHHHH!'\n\n You let out a shrill scream as the grasshopper lunges at you AGAIN! It then pulls you forward, and the legs have a pretty strong grip on your arms. You almost start to slide down the shovel, and you shut your eyes...Waiting.....\n...Waiting for the gruesome, gore-ish death....\n\n{style(0)}")
    time.sleep(0.5)
    printt(f"{fore(1)}You then feel the sparrow's wings envelope you... It's over, right?!\n{fore(2)} But, wait!--\n\n Opening your eyes, you're bewildered (and confused) that the sparrow had snatched the grasshopper! You see it flying away, away from you. Good riddance...\n\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt("However, your body's in extreme pain, and you're completely traumatized by your current situation. Gazing at the front door, you are determined to get back into the house. Even though you're weak and tired, you run up the shovel as fast as you can.\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(f"You then come to a stop as you reach the shovel's handle. Since the shovel was leaning on two steps of the porch, the third, last, and final step is out of its reach. NOW WHAT?!\n\n Thinking hard, you realize that you have to leap off the shovel-- and onto the step...\n\n Could you do it? Of course you can!👍🏽\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"Feeling groggy and weak, you still move to action, by doing a running start....\n\n...And you leap!\n\n{style(3)} I can do this! I CAN DO THI--{style(0)}\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"Your shoe gets caught on the handle's end...\n\nBoth of your hands grabbed air!--\n\nShooting out both arms, you're desperate to hold on, and then--\n\n**SMACK!**\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(f"You grab onto the edge of the step! But, your entire lower body smashes into the cement. No Pain...No Gain, they say--\n\n Instantly, your arms ached and throbbed within seconds! You can't handle this at all! You knew that you aren't strong enough, as your arms were more thinner than bird legs, but alas!--\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"{fore(2)}You successfully climb up the third step of your front porch! Give yourself a pat on the back for this one!\n\n{style(0)} Slowly getting up, you lie face-down on the concrete. Your skin feels hot, since the sun is shining down on your neighborhood.\n\n {fore(1)}You feel like you're about to be baked alive in the blistering heat!{style(0)}\n\n {style(3)} Maybe.... It's all just a dream, right?{style(0)}, you think to yourself...\n\n{style(3)} Maybe-- I didn't shrink.....{style(0)}\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"To verify this, you slap yourself twice, eyes shut.\n\n Nope-- Not a dream! Or, nightmare?\n\n You then punch yourself in the face HARD, only for you to collapse to the floor.\n\n Yep... so NOT a nightmare....\n\n... or even a dream!\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(f"You then sit down on the edge of the step that you climbed up earlier. You're so small, that your feet doesn't even touch the ground! Looking around, you see different birds of whatever species flying around out and about. Not only that, but seeing them sends a shudder down your back, as you're reminded of the sparrow you encountered earlier....\n\n 'No time to think', you muse to yourself....\n\n Turning to the front door, you run straight towards it. You don't even care how long it takes to get back in the house!\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"--About 5-10 Minutes Later--", userStrDelay)
    storyLocation = "2"
    saveGame()
    encounterTwo()


def grasshopperEncounter():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    time.sleep(0.5)
    printt(
        f"After lowering yourself off the stoop, even though it took a toll on your arm muscles, you then jump off the sidewalk, and hide in the tall grass until your dog and his girlfriend (The 🐩, bro...) leave the house. Since you were covered in dog saliva, you find a small leaf to use as a towel, wiping your dripping, sticky body.\n\n Okay, here you are, a real person, but less than 10 inches tall, likely {fore(1)}{style(4)}{style(3)}doomed to be small for the rest of your life.\n\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt(f"'I {style(4)}have{style(0)} to get back to normal size...', you murmur as you walk across the front yard, pushing the blades of grass, which came way above your waist.{fore(3)}{style(1)}{style(3)} You need to make a plan, you have to think-- DO SOMETHING!{style(0)}\n\n As your mind wanders about becoming bigger again,{fore(1)} something rustles in the grass up ahead!--{style(0)}\n\n", userStrDelay)
    time.sleep(0.5)
    printt("You stop moving forward. The rustling sound gets louder and closer...\n\n", userStrDelay)
    time.sleep(0.5)
    printt("Pushing the blades of grass again, and stepping forward once more, you see whatever made that sound!--\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    grasshopper = (
        fore(2)
        + r"""
    //_____ __
   @ )====// .\___
   \#\_\__(_/_\\_/
     / /       \\
         """
        + style(0)
    )
    time.sleep(0.5)
    print(grasshopper)
    time.sleep(0.5)
    printt(
        f"It's a {fore(149)}{style(1)}green, slender stick-like figure....\n\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt(f".... A grasshopper (or a cricket, perhaps?)\n\n Your heart skips a beat as you stare into its eyes...\n\n It then rises up on two hind legs, being taller than you! {fore(9)}The big insect then looks down at you, in complete silence....\n\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(f"That's when you hear a bubbling sound from the grasshopper. The insect spits out a {fore(0)}black, gooey paste{style(0)}(A defense mechanism, perhaps?) which splatters your shirt! 'Yeeeoooow!' You feel more startled than being hurt! \n\n{fore(1)} OK, hiding outside must've been a bad idea, right?!{style(0)} As you turn to run away from the grasshopper,{fore(1)} it catches up to you quickly!{style(0)} Raising your arms to protect yourself, the grasshopper comes forward. The head looms over you, clicking its jaws, ready for the kill...\n\n You then see it lifting up a slender leg, arching its long body...\n\n{fore(1)}... What's gonna happen next? 😬\n\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(f"{fore(1)}**SLAP!**\n The grasshopper slaps your cheek, HARD!\n\n That slap sends you toward the ground, face down in the dirt.{style(3)} No time to get away!-- It slaps you AGAIN!\n\n{style(0)} With your face stinging from the two slaps, you attempt to run towards the front porch. The grasshopper then again spits out the putrid black paste. Looking behind, you dodge-roll the ranged defense-attack, or in other words, you steer away from the paste.\n\n Not looking back, you continue to run like crazy. Unknowingly to you, the grasshopper plans its next move...\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(f"{fore(1)}{style(3)}'WHOOOAH!'\n\n The grasshopper LUNGES at you! Its slender legs felt like darts piercing your back, way more un-relaxing than acupuncture...\n\n{style(0)} Sprawled on the ground, you look at the huge insect, with a fearful look on your face.\n\n", userStrDelay)
    time.sleep(0.5)
    printt(f"{fore(1)}{style(1)}{style(3)}{style(4)}You're TRAPPED! No way to hide....No way to fight this monstrosity...\n\n{style(0)} {fore(3)}Or... maybe there's hope...\n\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt("1. Take down the grasshopper", userStrDelay)
    printt("2. Run", userStrDelay)
    printt("3. Tame it as a pet", userStrDelay)
    printt("4. Accept death", userStrDelay)
    print("Choose your fate...\n>")
    fate = int(fkey.getchars(chars=["1", "2", "3", "4"]))
    if fate == 1:
        os.system("clear")
        printt("With a fast reaction time, you grab one of the legs of the grasshopper. It felt warm and solid rock, like a lobster claw.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"Using both hands and all your strength, you try to burrow the grasshopper's head into the dirt. {fore(9)}Suddenly, you hear a rumbling beneath you-- Is it an earthquake?\n\n The wings of the grasshopper sprout up, and it sends you flying in the air!\n\n{style(0)} Aside from all the commotion happening down below, absolutely NO-ONE in your neighborhood sees you fight a grasshopper and even bother to help you, as per logic...(WHY did I write this?!)\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"Anyway, back to where we are NOW: You hit a bent grass blade, limp from the pain shooting down your miniscule body. Slowly getting up, you see the grasshopper hovering above you, rubbing its legs together. The audible rubbing sound it makes reminds you of celery cracking into two pieces.\n\n It tries to dive towards you, but you step out of the way,{fore(2)} as you realize that very blade of grass you're on is a one-way ticket to the pavement, and to the front porch!\n\n{style(0)}", userStrDelay)
        time.sleep(0.5)
        printt(
            f"In a rush, you jump onto the sidewalk, and sprint to the porch. The grasshopper is still airborne, looking for its prey...\n\n Grabbing a small rock, you huck it HARD at the flying insect. **WHACK!**\n\n {fore(9)}The grasshopper is injured, but you failed to stun it, however.{style(0)} Then it circles around you, still not going towards you...\n\n", userStrDelay)
        time.sleep(0.5)
        printt(f"{fore(3)}Your time is LIMITED-- you {style(1)}{style(3)}{style(4)}need{style(0)} to get back in the house!{style(0)} You then see the pet door being swung open--It's your dog and the neighbor's poodle! You run to the flower bed of your house and hide (from both the two dogs and the grasshopper) for a few minutes. You see that your pet dog and the poodle are trotting side by side, leaving the house...\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"{fore(3)}But... what about the grasshopper?! It's not finished with you yet!\n\n{style(0)}", userStrDelay)
        time.sleep(0.5)
        printt("1. Deal with the airborne grasshopper", userStrDelay)
        printt("2. Get up the front porch", userStrDelay)
        print("It's a DO or DIE situation...\n>")
        choice = int(fkey.getchars(chars=["1", "2"]))
        if choice == 1:
            os.system("clear")
            time.sleep(0.5)
            printt(f"{fore(2)}You take down the grasshopper with your bare hands! You did it! You're a hero!\n\n{style(0)}", userStrDelay)
            time.sleep(0.5)
            printt(f"{fore(1)}{style(3)}SIKE-- You're NOT!{style(0)}\n\n It just ignored you, anyway....\n\n Bro literally gave up.(Wow... What a dumb line...)\n\n You then move on to the next task...\n\n", userStrDelay)
            time.sleep(0.5)
            storyLocation = "35"
            saveGame()
            sparrowEncounterTwo()
        elif choice == 2:
            os.system("clear")
            storyLocation = "34"
            saveGame()
            sparrowEncounterOne()
    elif fate == 2:
        os.system("clear")
        printt("You turn around and run away from the grasshopper...\n\n Unfortunately, you're too slow!\n\n", userStrDelay)
        time.sleep(0.5)
        printt("The grasshopper swiftly kills you immediately. That insect is fast as Usain Bolt! DAMN!\n\n", userStrDelay)
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    elif fate == 3:
        pass
    elif fate == 4:
        os.system("clear")
        printt("You convince the 🦗 to murder you. Apparently, NOTHING HAPPENS. The insect just leaves you....\n\n... Perfect?--", userStrDelay)
        time.sleep(0.5)
        printt("Alright, now you gotta get back in the house!--You then see the pet door being swung open--It's your dog and the neighbor's poodle! You run to the flower bed of your house and hide. You see that your pet dog and the poodle are trotting side by side, leaving the house...", userStrDelay)
    else:
        pass


def encounterZero():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "You stand there thinking about on what could make you big again, when all of a sudden, you hear a bark behind you...\nYou spin around and see that...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(1)}... Your pet dog is staring at you 🐶.\n Does it think that you're food? Or a chew toy?{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Hey, nice boy... nice boy', you say to your dog...\n Unfortunately, your dog doesn't listen and opens its mouth wide open!\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'NOOO!', you scream, and try to shield yourself as your dog's jaw is in open-and-shut mode. 'Don't eat me!'\n But, your cries of not being dog food are helpless as your dog picks you up with his mouth and plays with you. You feel its sharp teeth cut into your skin...\n\n",
        userStrDelay,
    )
    printt(
        f"\n\n\n'PUT ME DOWN!', you yell in vain. Your voice comes out in a tiny yelp, which is why your dog doesn't give an F.\n\n 'PLEASE, PUT ME DOWN!', you yell again.\n\n And, your dog still doesn't listen, as he's too busy playing with you.\n\n{fore(3)} You have to escape your pet's grasp and prevent yourself from being eaten! But, you're extremely impatient...{style(0)}\n",
        userStrDelay,
    )
    printt("1. Wait until your dog drops you", userStrDelay)
    printt("2. Try to free yourself", userStrDelay)
    printt("3. Do nothing, just wait and see!", userStrDelay)
    print(
        f"{fore(3)}You really need to think fast now...\n{style(0)} Select an option: "
    )
    decision = int(fkey.getchars(chars=["1", "2", "3"]))
    if decision == 1:
        os.system("clear")
        printt(
            "Your dog drops you, and you fall free.\n Scrambling to your feet, you make a run for the front door. Running as fast as you can, the little furry beast then chases you! Was running all for nothing?\n\n Maybe, as you push open the pet door and swing it open.\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\nYou then continue running outside your front yard, but then you feel a familiar tightening sensation all over you...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1) + "Oh-No....\n YOU'RE STILL SHRINKING!" + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\nYou really couldn't believe your eyes. I mean, you're getting more smaller and smaller. Are you going to shrink down to"
            + fore(6)
            + " nothing?!\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "As you think about your future, something leaps at you, and sends you toward the grass! Just as your dog attempts to catch you.\n\n Hooray, you're saved! But from what?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\nComing to your senses, you see that you are now 1.27 cm tall (equivalent to the size of an ant), and you see that a huge grasshopper(🦗),towering over you, has saved your life.\n Strange, isn't it?\n",
            userStrDelay,
        )
        grasshopper = (
            fore(2)
            + r"""
    //_____ __
   @ )====// .\___
   \#\_\__(_/_\\_/
     / /       \\
         """
            + style(0)
        )
        time.sleep(0.5)
        print(grasshopper)
        time.sleep(0.5)
        printt(
            "\n\n However, it now wants YOU as food. Yikes!\n\n With a slender leg, the grasshopper slaps you, which sends you flying! You only have one option, and that option is:",
            userStrDelay,
        )
        time.sleep(0.5)
        print("   _____  _    _ _   _ ")
        print(r" |  __ \| |  | | \ | |")
        print(r" | |__) | |  | |  \| |")
        print(r" |  _  /| |  | | . ` |")
        print(r" | | \ \| |__| | |\  |")
        print(r" |_|  \_\\____/|_| \_|")
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n\n And you do so eventually, you run away from that grasshopper.\n As you run, everything around you is rising on both sides, slowly...and slowly...\n\n ... the ground is being more spread out than ever.\n\n\n You start to feel extremely cold 🥶, as you're getting more smaller (more small = more larger surface area, which means more loss of body heat... unless you eat something!) by every hour, minute, and second...\n\n You're astonished by how extremely tiny you are.\n\n\n A single blade of grass is equivalent to the size of an oak tree!\n\n You get dizzy from just seeing it and assume you might be dreaming...\n\n But you're not dreaming. You're about 1/7 of an inch tall now!\n\n 'Man, WHEN WILL IT END?!?', you ponder in fear...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\nYou stop running by the moment you reach the front walkway of your house, and lie down in the middle of the pavement. You can't take the pain anymore, as your whole body is tightening, physically contracting in size.\n Your teeth are constantly chattering as your body temperature drops faster and faster as you continue to shrink...\n Your heart's BPM is rising fast!\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\nThat's when you have to make a very difficult choice: Accept your inevitable fate or deny it....\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n You then deny the fact that you're going sub-atomic for a few minutes, but as you attempt to hug yourself tightly, to prevent from freezing to death, you realize that...\n It's too late...\n\n"
            + fore(11)
            + "You will never be back to your normal size EVER AGAIN..."
            + style(0),
            userStrDelay,
        )
        time.sleep(1)
        printt(
            "\nLooking up at the sky, you fear that nobody will find a single trace of you -- AT ALL! You're still shrinking....\n Going....\n\n...... Going.......\n.... going ....\n going.....\n\n\n\n ....going.....\n....going!....\n\n\n....What a world.... What a wonderful world..... What a wonderful world.....\n\n... what a wonderful world.....\n\n what a world....\n\n what a wonderful, beautiful world....",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n\nAfter several minutes, you see the sky has disappeared. You're now the size of an atom, and you are now close to death. Even though you know that you really don't exist in this world right now, you know one thing for sure...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'To God, I am no zero. But I still exist', you say out loud as you breathe your last breath.... or is it really your last breath?\n\n.....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(4) + "⚛️ THE END? ⚛️" + style(0), userStrDelay)
        quit(0)
    elif decision == 2:
        os.system("clear")
        printt(
            "You struggle to free yourself from the tightening of your's dog mouth, but you don't budge. Unexpectedly, you accidentally push yourself toward the front of its mouth!😨",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Picture this: Your legs are visible from the mouth of your dog, but your chest, waist, arms, and head aren't visible.\n\n You're seeing nothing but"
            + fore(0)
            + " darkness..."
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt("Then, your dog tilts its head--\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "\n -- And you fall.... Headfirst...\n"
            + fore(1)
            + "Inside the body of your dog...."
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "...After 5 minutes, you fall into your dog's stomach and die of acid corrosion and being digested. I guess you should've picked option 1 then.... Too bad...\n",
            userStrDelay,
        )
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    elif decision == 3:
        os.system("clear")
        printt(
            f"Your pet dog is still holding you in his mouth. When will he will drop you? You anxiously wait for that moment...\n'Put me down.... RIGHT NOW!', you scream.\n Nothing happens....\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"That's when your dog tosses you up in the air!\n\n Seems like he's still playing with you!\n\n Your back hits the floor on impact. 'OOMPH!'\n\n Sitting up, you shout: 'HEY! C-CAN'T YOU SMELL ME? DON'T YOU RECOGNIZE ME?! IT'S ME,{username.upper()}!'\n {fore(3)}You're bewildered by the fact your pet dog doesn't even recognize its owner, especially when you're 2 inches tall!{style(0)}\nYou then quickly try to crawl to safety--\n", userStrDelay)
        time.sleep(0.5)
        printt("But, your dog is not done with you...\nHe still keeps his eye on the prize (which is you, actually)!\n'Didn't you hear me? Down boy, down!', you protest, but your small voice doesn't do any justice to get your dog from grabbing your pint-sized waist.\n\n Hot, sticky saliva covers your face, arms, and legs....\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"Okay, so if your pet dog is currently playing with you now--\n\n{fore(1)}Then what is he going to do AFTER he's done playing?{style(0)}\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"{fore(1)}Leave you alone?\n\n {style(4)}Or chew you to bits?{style(0)}\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"Many years ago, you saw your pet dog stroll into the kitchen with a dead mouse between his teeth.'Whatcha got there, bud?', you ask, eyeing the dead creature in the dog's mouth.{style(3)} The last thing that you remember was the sickening, horrid crunch of the mouse's head being snapped and chewed--{style(0)}\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Now, with you in your current shrunken state, only a single thought races through your mind...\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"{style(3)}Great...,{style(0)} you think to yourself.{style(3)}Now, {style(4)}I'm{style(0)}{style(3)} the mouse...{style(0)}\n\n The saliva-covered mouth of your dog still has its strong grip on your tiny body. 'L-Let go of me--PLEASE!', you moan. BUT NO!\n\n", userStrDelay)
        time.sleep(0.5)
        printt(f"{fore(1)}You feel yourself tossed even more higher, along with a trail of saliva following your trajectory, and sure enough, you skid on the carpet floor. Your dog immediately picks you up again, doing the same thing. Again, you picture the dead mouse...And that not-so-satisfying crunch.{style(0)}\n\n{style(3)} The same pattern repeats: Your dog picks you up, tosses you,and you still are traumatized by facing the same fate that the mouse did--\n\n{style(0)}Yeah, we get it.😠\n\n", userStrDelay)
        os.system("clear")
        time.sleep(0.5)
        printt("Alright, enough with the exposition.\n\nBy the moment you hit the ground for a fifth time, although weak and tired--You quickly decide to duck for cover... underneath the 🛋️.\n\n", userStrDelay)
        time.sleep(0.5)
        printt("Your pet dog carefully eyes your movements, and tries to grab you again, but you dodge it! Then, you crawl on all fours to reach the bottom of the couch, then run. However, you keep tripping on the thick living room carpet.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"The enormous golden retriever then follows you as you try to escape.\n\n{fore(1)}{style(4)} THIS IS IT!{style(0)}\n\n Your dog attempts to nab you by diving his head for the kill....\n\n...Luckily, its a near miss, as you roll over slowly, then quickly scurry to safety....\n\n Thinking fast, you then do a long jump and land on your knees.... right under the couch!\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(
            f"Your pet dog sniffs the air, looking around for you, the tiny person he found. {fore(2)}The good news is, he DID NOT LOOK UNDER THE COUCH... Phew!\n\n{fore(1)} SIKE!!!-- IT WAS ONLY FOR 5 SECONDS!{style(0)}", userStrDelay)
        time.sleep(0.5)
        printt("As you continue to run, your dog's big, furry paw knocks you over. Scrambling to your feet, you quickly crawl again and hide behind a tennis ball...\n\nThat was close!😮‍💨\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"However, your dog SAW you hide, and could grab you at {style(3)}{style(4)}any{style(0)} moment...\n\n'WOOOOOFFFF!'\n\n You hear an angry bark from your dog, which came out as a menacing roar, banging your eardrums....\n\n{fore(1)}{style(3)} Okay... NOW WHAT?!{style(0)}\n\n Holding yourself still against the round 🥎, you pray that your dog will forget about you--\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"**SCRATCH**,**SCRATCH**,**SCRATCH**...\n\n {style(3)}Uhhhh....WHAT is THAT?--{style(0)}, you wonder as you hear a faint scratching sound in the distance, and also in {fore(0)}the darkness....{style(0)}\n\n Hmmm.... What could it be?--\n\n The scratching sound gets {style(3)}louder and louder by the second...{style(0)}\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"It's-- errrr-- something? That creature has FUR... a bear I'm guessing?--\n\n {fore(1)}{style(3)}Wait, THAT LOOKS TOO BIG TO BE A BEAR--{style(0)}\n\n The mysterious furry animal comes into view....\n\n", userStrDelay)
        time.sleep(0.5)
        printt(f".....A mouse....?\n\n {fore(1)}Yep! IT'S A GIANT MOUSE, ALRIGHT! {style(3)}Since you're literally smaller than a mouse...{style(0)}\n\n You still stay where you are, as the mouse wanders toward you.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"'HEY!', you shout, pointing a finger at the 🐁. 'GET AWAY FROM ME!'\n\n{fore(1)} Nothing happens.{style(0)}\n\n The mouse then twitches its whiskers, examining you. You then hear another loud bark from your pet dog.\n\n{style(3)} What would the enormous mouse DO to you, anyway?{style(0)}\n\nEh, probably will ignore yo--\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(f"{fore(1)}{style(4)}Suddenly, the mouse scratches you with one of its claws!{style(0)} You stagger back, shocked by what happened.{fore(1)} Maybe it considers you as food now?\n\n{style(3)} Then, it grabs you by your shirt!{style(0)}\n\n 'LET GO!', you protest.\n\n The white rodent doesn't even bother to listen as it tries to tear you to shreds, maybe?\n\n A painful scuffle ensues as you struggle to free yourself from the 🐁.\n\n Why do I say, 'painful', you ask?\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt("Because you get cuts and scrapes on your arms, legs,(some) portions of your face. Need I say more?\n\n At least they're nothing but minor injuries.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(f"Now the mouse stares down at you, on its hind legs.{fore(1)} You're seeing T-Rex vision now! The mouse towered over you like a dinosaur!\n\n {fore(3)}You are forced to make a choice-- a {style(3)}horrifying{style(0)}{fore(3)} choice: Stay here and fight the mouse? Or crawl back out and face your dog?\n\n{style(0)}", userStrDelay)
        time.sleep(0.5)
        printt("1. Fight the mouse", userStrDelay)
        printt("2. Run-- JUST RUN", userStrDelay)
        printt("3. Face your dog", userStrDelay)
        printt("4. Two 🐦s, one 🪨", userStrDelay)
        print("The choice is yours.\n\n Select an option:\n\n")
        decision = int(fkey.getchars(chars=["1", "2", "3"]))
        if decision == 1:
            os.system("clear")
            printt(f"You start to crab-crawl backwards, continuing to stare at the black beady eyes of the mouse. \n\n 🐁: 'Squeeee?'\n\n Without saying anything, you still continue to stagger backwards.\n\n That's when your hand feels something... What could it be?\n\n", userStrDelay)
            time.sleep(0.5)
            printt(f"You lower your gaze at what you just bumped into.{fore(2)} It's a toothpick!{style(0)}\n\n It seems as long as a spear from your perspective...\n\n You then stare back at the mouse and then back at the toothpick. Could you use it as a weapon? Stab the mouse? Pin it with the toothpick?{fore(150)} You have to try...{style(0)}\n\n 'SQUEEEE?', the mouse exclaims, maybe probably wondering what you're doing...\n\n Moving to action, you try to pick up the toothpick with one hand.{fore(1)} Nope, its too heavy for you! You have to use two hands instead of one!{style(0)}\n\n 'So-- h-heavy...', you grumble to yourself, lifting up the toothpick with both tiny hands.\n\n You then point it at the mouse, waiting for it to be scared and run away....\n\n", userStrDelay)
            time.sleep(0.5)
            printt("And nothing happens....\n\n You have no choice....\n\n You then make a sharp-stabbing move with the toothpick and charge towards the mouse....\n\n", userStrDelay)
            time.sleep(0.5)
            printt(f"'SQUEEEEEEEEEEEEECCCC!!!'\n\n{fore(2)} The mouse screeches in pure pain as you stab it in the chest (and likely through the heart as well)!{style(0)} You continue to stab it, until the unexpected happens...\n\n {fore(2)}The mouse bleeds to death!\n\n SUCCESS!{style(0)}", userStrDelay)
            time.sleep(0.5)
            os.system("clear")
            printt(
                f"Okay, if you have killed the mouse.... Now what?\n\n Your hands start to feel 🧊-cold all of a sudden. Your stomach loudly growls, but not enough for your dog (who's still outside) to hear.\n\n{fore(105)} Yeah, you should've ate something, otherwise this heck of a NIGHTMARE won't even happen in the first place!{style(0)}\n\n But, WHAT WOULD YOU EAT?!\n\n Unfortunately, you don't have time to think as you hear a loud, low growl....\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                f"{fore(1)}{style(3)}Uh-Oh....\n\n...Seems like your 🐕 has lost its patience!\n\n{style(0)}", userStrDelay)
            time.sleep(0.5)
            printt(
                f"Or... maybe NOT?\n\n{fore(2)} You look under the couch and see that your dog is gone!\n\n Coast's clear, right?\n\n{style(0)}", userStrDelay)
            time.sleep(0.5)
            printt(
                f"Slowly stepping out of your hiding place, with the toothpick in both hands, you decide to get something to eat, being cautious as you walk.\n\n {fore(1)}But, by the moment you turn around, you freeze in pure horror as you see your dog, far away from where you are, with his mouth open!--\n\n{style(0)} You completely forgot that dogs have great ears, what a dumbo you are!\n\n", userStrDelay)
            time.sleep(0.5)
            os.system("clear")
            time.sleep(0.5)
            printt(
                f"'Just-- Just LEAVE ME ALONE, please!', you exclaim. Your voice is so tiny, it cannot be heard beyond the rest of the living room in your house...\n\n However, even though your dog can actually hear you,{fore(1)} it still thinks you're something to play with.\n\n{style(0)}", userStrDelay)
            time.sleep(0.5)
            printt(f"The dog then walks toward you, with its mouth still open--\n\n{fore(1)}{style(3)}AND LEAPS!{style(0)}\n\n'NOOOOOOOOOOOO!'\n\n A blood-curling scream escapes your throat as two out of four enormous paws attempt to crush your tiny, fragile body. Trying to push the hulking golden retriever as you could, your weak muscles aren't enough to fight back! So, you do the other option--COMBAT!\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                f"Using your wooden 'spear' (AKA: The toothpick), you try to stab one of the front paws of your pet dog.{fore(1)} That eventually fails when your dog lifts you up with his teeth! NOT AGAIN!\n\n Upon being lifted, you drop the toothpick!\n\n{style(0)}", userStrDelay)
            time.sleep(0.5)
            printt("'LET ME DOWN!', you bellow. 'LET GO OF ME THIS INSTANT! DON'T YOU RECOGNIZE MY VOICE?!'\n\n Admit it, your dog doesn't care...\n\n He then pulls you HARD. Pulls like one of his long pull-rope toys. You continue to scream and shout to be put down, but that's when you hear the pet door being swung open...\n\n", userStrDelay)
            time.sleep(0.5)
            os.system("clear")
            time.sleep(0.5)
            printt("Turning to your right, you see that its your next-door neighbor's dog from across the street. Eh, probably your dog's girlfriend, who's a poodle. Your dog and the possible 'love of his life' exchange glances with each other, then the poodle sees you, and growls.\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                f"You shudder in terror as you realize what's about to happen--\n\n{fore(1)}They're fighting over you!{style(0)}\n\n The poodle approaches you, and dives its mouth, aiming for the feet. Your dog quickly turns away and growls.\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                f"This time, your dog caves in to let the innocent looking poodle have her share. {fore(1)}In several seconds, the poodle's sharp teeth digs into your ankles! And, your dog pulls back!\n\n {style(1)}{style(3)}{style(4)}OH MAN! IT'S A TUG OF WAR!{style(0)}\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                f"You let out a wail as a wave of pure extreme pain moves along your limp body.{style(3)}I- can't s-stand this anymore{style(0)}, you immediately thought.\n\n{fore(3)} You have to escape-- FAST!\n\n{style(0)}", userStrDelay)
            time.sleep(0.5)
            printt("1. Get out of this tug of war", userStrDelay)
            printt("2. Give up", userStrDelay)
            print("It's NOW or NEVER!\n\n>")
            escapeRoute = int(fkey.getchars(chars=["1", "2"]))
            if escapeRoute == 1:
                os.system("clear")
                printt(
                    f"Still in your dog's mouth, you reach for its snout and grasp it tightly with your last bit of strength. Your dog gets startled and drops you!{fore(2)}{style(3)} YESSS!{style(0)}\n\n Falling to the floor, your final decision is to get out of the house quickly, and to likely go back in to eat some food, before you die of starvation.\n\n{style(3)} Good thing that dogs have terrible attention spans{style(0)}, you thought. How lucky you are!\n\n", userStrDelay)
                time.sleep(0.5)
                os.system("clear")
                time.sleep(0.5)
                printt(
                    f"Lucky probably isn't the right word...\n\n This was so NOT your lucky day...\n\n", userStrDelay)
                time.sleep(0.5)
                printt("Pushing the pet door's latch, you successfully swing it open and drop onto the front stoop. Your butt gets sore on impact. Ouch...\n\n", userStrDelay)
                time.sleep(0.5)
                printt("Getting up to your feet, you face the front door, fearing that your dog might find you and likely eat you. You have to hide QUICK!\n\n You turn towards the front yard and start to walk, until you see the front porch.\n\n", userStrDelay)
                time.sleep(0.5)
                os.system("clear")
                printt("Looking down, your stomach starts to lurch. The front stairs crept up like a cavern! No way that you could step down the normal way. Your small feet wouldn't even reach.\n\n Maybe, you have to lower yourself down-- one step at a time...\n\n", userStrDelay)
                time.sleep(0.5)
                printt("'No problem,' you say out loud, trying to cheer yourself up.\n\n'Its like climbing down a ladder--What could go wrong?'\n\n Therefore, you move to action. Turning yourself around, you put one foot in the air, but it doesn't even go all the way down, as per your current height. That means you have to drop onto the next step!\n\n Here goes nothing...\n\n", userStrDelay)
                time.sleep(0.5)
                printt("You land on the next step, feet first. Your shoes pinch your toes as you hit the cement. 'Ow.'\n Only 3 steps left!\n\n You do the same procedure: Lower. Drop. Repeat.\n\n Lower. Drop. Repeat.\n\n", userStrDelay)
                time.sleep(0.5)
                storyLocation = "33"
                saveGame()
                grasshopperEncounter()
            elif escapeRoute == 2:
                os.system("clear")
                printt("Wow, I can't believe that you lack a TON of motivation to stay alive!\n\nAnyway, you are ripped apart in half by the two dogs who fought over you. A dog's favorite thing to do: Destroying whatever it finds...\n\n", userStrDelay)
                printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                numDeaths += 1
                saveGame()
                playAgain()
        elif decision == 2:
            os.system("clear")
            printt("You run....\n\n", userStrDelay)
            time.sleep(0.5)
            printt("But, in which direction do you run exactly?\n\n", userStrDelay)
            time.sleep(0.5)
            printt("1. Left 👈🏽", userStrDelay)
            printt("2. Right 👉🏽", userStrDelay)
            print(
                "{To the tune of Guns and Roses's 'Sweet Child of Mine'} Where do you go now?\n\n>")
            route = int(fkey.getchars(chars=["1", "2"]))
            if route == 1:
                os.system("clear")
                printt(
                    "You turn to the left, and crawl out of the couch...\n\n...The mouse follows you!", userStrDelay)
                time.sleep(0.5)
                printt(f"Suddenly, you trip and lose your balance! You're too tired to run anymore! The mouse comes closer...\n\n And closer....\n\n Now, its near you, drooling with its mouth wide open! You shut your eyes and wait for the mouse to rip you to shreds....\n\n", userStrDelay)
                time.sleep(0.5)
                printt(f"And, NOTHING happens. Opening your eyes, you're astonished that your pet dog has saved your life by eating the mouse! He then walks away from you and goes upstairs. Great, you're safe!\n\n Then, you start to worry that your dog may come for you again....\n... You gotta act quick! Therefore, you run to the living room, ready for the next part of your journey...\n\n ", userStrDelay)
                storyLocation = "2"
                saveGame()
                encounterOne()
            elif route == 2:
                os.system("clear")
                printt(
                    "You turn to the right, and all that you get is a DEAD END!\n\n The mouse follows you...\n\n", userStrDelay)
                time.sleep(0.5)
                printt(
                    f"{fore(1)}... And you're ripped apart to shreds...\n{style(0)}", userStrDelay)
                printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                numDeaths += 1
                saveGame()
                playAgain()
        elif decision == 3:
            os.system("clear")
        elif decision == 4:
            os.system("clear")
            printt(
                f"{style(3)}Two 🐦s, one 🪨{style(0)}, you think to yourself as you get an idea. And what is that idea?\n\n", userStrDelay)
            time.sleep(0.5)
        else:
            pass


def treatments():
    global userStrDelay, numDeaths
    os.system("clear")
    printt(
        "Your doctor then hangs up the 📞. 'Pym will be coming in about an hour or so.', he says.\n\n Ok, so you already know help's on the way... but it'll take forever!\n\n 'If you really don't want to wait several hours, I have some treatments.' You grin 😀 with happiness.\n\n"
        + fore(14)
        + "Great! You're at this point where you can choose your own method of curing yourself... but it has a specific catch!\n"
        + style(0),
        userStrDelay,
    )
    printt(
        "1."
        + fore(11)
        + "Magnetism 🧲 (Need a scientific explanation? I hope not.\n Just kidding: It changes your molecular structure, which is what exactly happened to you after you shrank.)"
        + style(0),
        userStrDelay,
    )
    printt("2." + fore(5) + "⚡Lasers⚡" + style(1) + style(0), userStrDelay)
    printt("3.Never mind, I'm gonna wait for Hank Pym", userStrDelay)
    print("Which cure do you want to select?")
    treatmentOption = int(fkey.getchars(
        chars=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]))
    if treatmentOption == 1:
        os.system("clear")
        printt("'I would like to try magnetism, sir', you answer. \n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "'That's great', your physician responds.'Please wait, I'll be back.'\n\n He leaves the office and comes back after 5 minutes, with a sliver tube-like machine.\n\n He then props you into the tube. 'Ok, stay still and don't move!'\n\n You stay where you were, lying down on your back....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("\n\n\n .... And then.....\n\n", userStrDelay)
        printt(
            fore(3) + ".... ⚡A beam of light blinds your eyes 👀....⚡" + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt("... And....." + fore(0) +
               " darkness 🕶️ ...." + style(0), userStrDelay)
        os.system("clear")
        printt("Did it work?\n Are you back to normal?", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            "You feel a bit cramped in the clear tube. The tube is smaller now!\n\n\n"
            + fore(2)
            + "HOORAY! YOU'RE BACK TO NORMAL!\n\n\n"
            + style(0)
            + "'I can't believe it... it worked!', your physician says in glee.\n 'But, at least I'm back! Everything's the right size again!', you shout out in excitement.\n\n That's when, a 🪙 gets attached to you!\n\n 'Wait, am I Magneto?!', you ask. 'Well, that's the drawback. Please be careful though.'\n You really don't care. You go out the doctor's office, feeling happy as ever.\n\n Hey, since you're a living, breathing magnet, what would you like to do now?",
            userStrDelay,
        )
        printt("1. Try to test out your ability", userStrDelay)
        printt("2. Eh, I don't care", userStrDelay)
        print("Choose your choice wisely...")
        decision = int(fkey.getchars(chars=["1", "2"]))
        if decision == 1:
            os.system("clear")
            printt(
                "You still continue walking, and come by a dumpster. Not taking a peep on what's in that 🚮, about 50🥤 aluminum cans attach to you (plus a 🗑️, a 🐈, and a 🦏), crushing you to death",
                userStrDelay,
            )
            printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
            numDeaths += 1
            saveGame()
            playAgain()
        elif decision == 2:
            os.system("clear")
            printt(
                "You continue walking on the way home, as happy as ever. You pass by the bank and $99.74 in change get stuck to your back, arms, and legs.\n\n"
                + fore(2)
                + "The good news is.... YOU'RE FILTHY RICH! 🤑"
                + style(0)
                + "\n\n But, I wonder what are you going to do with this 💰?\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(2) + "🎉 THE END 🎉" + style(0), userStrDelay)
            quit(0)
    elif treatmentOption == 2:
        os.system("clear")
        printt(
            "'I would like to try the laser gun, sir.', you respond.\n\n'Ok, lemme take that out.', your physician says.\n He then takes out a NERF: Super Soaker with a laser beam attached to it. He points the 🔫 towards you, and then presses the button....\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\nWithin a split second, you explode to bits, like these 🍎s in 'Honey, I Shrunk The Kids'. Turns out that laser was a faulty one...\n",
            userStrDelay,
        )
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    elif treatmentOption == 3:
        os.system("clear")
        printt("You decide to wait for Hank Pym.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"And, sure enough, he arrives, an hour later, with briefcase in hand 💼. 'What seems to be the problem?', he asks your physician. Your doctor points at you. 'Hank, you have the antidote, right?', you question. 'Well, yes I do, BTW', he responds as he opens the briefcase and pulls out another small bottle. Instead of the liquid being clear, it's {fore(4)}blue.{style(0)} \n\n Could it be the antidote? Looks like it...\n\n 'Why'd you send that package, Hank?', you ask again. No answer...\n\n Hank comes toward you, and gives you a spoon, which contained the blue liquid.\n\n{fore(3)} Seems like he wanted you to be back to your normal size desperately, since {style(3)}{style(4)}he's the one that screwed up.{style(0)}\n\n You drink it up like a person who just saw water for the first time, then sit back and wait....\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "... And then you feel your body aching. Is it working?...\n\n You look at your hands, and boy oh boy, they're inflating!\n\n"
            + fore(2)
            + "YOU'RE GROWING NOW!"
            + style(0)
            + "\n\n You feel your head shoot up, and everything's decreasing in size....\n\n You jump off the office table and give Hank a tight hug. 'Hey! Easy, easy...', Pym responds.",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "'Ok,' you say to Hank. 'Why did you send that package to my doorstep that contained THIS?'.\n\n You pick up the small bottle. 'I was sending samples door-to-door. It's my latest product.'\n\n'Wait a minute... You were always a guy who was afraid that someone would steal your secret... The secret to shrink yourself...\n\n Why are you so open minded nowadays?'. Hank looks at you with a glum face and then says...\n\n'I don't know how Pym Particles work, and people change. I stopped making suits and made remedies instead.'\n\n 'Yeah, who even cares. You need to change your business strategy.' you respond, as you exit the office.\n\n'Thank you for everything!', you yell to Pym. That's when Pym chucks something at you...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'Hey! What was that for?!', you complain. 'Oh well...'\n\n You pick the item up, and believe it or not...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "It's a collection of size-shifting discs. But what for? You then see a note pinned to it:\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{style(3)}FEEL FREE TO USE ANY OF THESE DISCS. HERE'S WHAT THEY DO:\n\n"
            + fore(1)
            + f"RED --> SHRINKS ANY OBJECT\n\n\n"
            + fore(6)
            + f"BLUE --> ENLARGES ANY OBJECT"
            + style(0)
            + f"{style(3)}\n\n USE IT AT YOUR OWN RISK! IF YOU MESS AROUND WITH IT... YOU'LL ENTER THE QUANTUM REALM.\n BEST WISHES -- HANK{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n\n You still hold these discs, and continue walking on the way home. In order to celebrate, you decide to make 🍰, order some 🍕, and some 🍦 when you get home. You also wonder if Hank is recruiting you for a very important mission...",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "What's next for you, anyway?\n\n Is it a new beginning? Or...\n\n",
            userStrDelay,
        )
        printt(fore(2) + "🎉 THE END 🎉" + style(0), userStrDelay)
        quit(0)
    else:
        printt(
            "That treatment doesn't even exist!\n\n Then you accidentally trip on a staple and fall....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Oh-No.... is it " + fore(1) + "GAME OVER" +
            style(0) + " for you?!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("You hit the floor with a hard BANG!--", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt("... And you wake up. Wait, what?", userStrDelay)
        time.sleep(0.5)
        printt(
            "\n\n Turns out it was all nothing but a bad dream, right? You didn't shrink to 2 inches at all!\n\n You forget about the dream and fall asleep....\n",
            userStrDelay,
        )
        printt(fore(2) + "🎉 THE END 🎉" + style(0), userStrDelay)
        quit(0)


def endGame():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "You and your family physician enter his office. The doctor then props you up on his office table. 'Alright,' he says.'Tell me from the beginning...'.\n\n You then start to tell about what happened, with you finding the mysterious package at your doorstep, the fat-burner/dieting remedy, and the eventual dangers you experienced along the way. 'I think you wouldn't want to go through the trauma I went', you conclude.\n\n 'Sir,what I fear...is that--', your voice then trails off. You're too stunned to speak. Something is bugging you... but what is it?\n'--I fear... that...'\n\n\n\n'I'm going to shrink down to NOTHING.'\n\n'No one would find me.... I'll be gone!', you exclaim to your doctor. 'So, please! I really, really, desperately need to get bigger again.'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Wait, so you said that you took a dieting type of medicine?', the doctor says. 'Yep.', you respond.\n\n'Well, I know that person, who created this fat burner drink.'\n'Tell me', you beg.'Please tell me. Who the heck made this?'\n Your physician pauses for a moment, and then says those words that you wanted to hear....",
        userStrDelay,
    )
    time.sleep(1)
    os.system("clear")
    printt(
        "'Hank Pym.'\n\n🤯\n\n'Wait, WHAT?!', you cried, bewildered. \n 'Yes, THAT HANK PYM. The one who created Pym Particles. He now sells products like these dieting remedies, just after he discovered that the technology in them can also be used for weight loss.'\n\n 'Then, why did THIS happen to me? Why am I 2 inches?', you ask.\n The doctor shrugs and says,'I think he overdosed it a bit on the Pym Particles. Hang on, I'm calling him.' Your doctor picks up the phone and dials the number for Hank.\n\n You feel relived....😮‍💨 Finally, you know now who and what caused this! And, a solution is coming up... soon..."
        + fore(13)
        + "\n\n\n\n Or, is it actually 3 solutions?\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    storyLocation = "18"
    saveGame()
    treatments()


# If the player dies, give them a chance to play again. They can access any plot point they would like to do


def playAgain():
    os.system("clear")
    global userStrDelay, numDeaths
    printt("1. Yes", userStrDelay)
    printt("2. No", userStrDelay)
    while True:
        try:
            print(f"One more chance?")
            reSpawn = int(fkey.getchars(chars=["1", "2"]))
            if reSpawn == 1:
                printt(
                    f"{fore(6)}>>Respawning...\n\nPlease wait...{style(0)}", userStrDelay)
                loadGame()
            elif reSpawn == 2:
                printt(f"I feel bad that you gave up! 😓", userStrDelay)
                quit(0)
        except ValueError:
            printt("Error respawning, please try again!\n\n", userStrDelay)
            continue


def saveGame():
    global user, hasAccount, username, storyLocation, numDeaths, bestFriend, userStrDelay

    if hasAccount == 1:
        db["storyLocation" + username] = storyLocation  # type: ignore
        db["numDeaths" + username] = numDeaths  # type: ignore
        db["bestFriend" + username] = bestFriend  # type: ignore
        db["userStrDelay" + username] = userStrDelay  # type: ignore

        storyLocation = db["storyLocation" + username]  # type: ignore
        numDeaths = db["numDeaths" + username]  # type: ignore
        bestFriend = db["bestFriend" + username]  # type: ignore
        userStrDelay = db["userStrDelay" + username]  # type: ignore

        printt(
            f"\n\a{fore(14)}>> Database Save found.\n   Updating data...{style(0)}",
            userStrDelay,
        )

    else:
        if os.path.exists(f"users/{user}.txt"):
            printt(
                f"\n\a{fore(4)}>> Save file: {user}.txt found.\n   Retrieving data...{style(0)}",
                userStrDelay,
            )
            time.sleep(2)
            os.system("clear")

        # Retrieve user's data
        filename = "users/" + user + ".txt"

        w = open(filename, "w")

        w.write(user+"\n"+str(storyLocation)+"\n"+str(numDeaths) +
                "\n"+str(bestFriend)+"\n"+str(userStrDelay))
        w.close()


def loadGame():
    global user, hasAccount, username, storyLocation, numDeaths, bestFriend, userStrDelay
    if hasAccount == 1:
        try:
            storyLocation = db["storyLocation" + username]  # type: ignore
            numDeaths = db["numDeaths" + username]  # type: ignore
            bestFriend = db["bestFriend" + username]  # type: ignore
            userStrDelay = db["userStrDelay" + username]  # type: ignore
            storyLocation = int(storyLocation)
            numDeaths = int(numDeaths)
            bestFriend = str(bestFriend)
            userStrDelay = float(userStrDelay)
            if bestFriend != "":  # type: ignore
                bestFriend = db["bestFriend" + username]  # type: ignore
                bestFriend = str(bestFriend)
            else:
                bestFriend = input(
                    "Enter the name of your best friend (Even though the name is considered useless from starting the game, this only appears if you wish to go deeper into the story....): \n"
                )
                db["bestFriend" + username] = bestFriend  # type: ignore
                bestFriend = db["bestFriend" + username]  # type: ignore
            if storyLocation == 1:
                os.system("clear")
                game()
            elif storyLocation == 2:
                os.system("clear")
                encounterOne()
            elif storyLocation == 3:
                os.system("clear")
                longJourney()
            elif storyLocation == 4:
                os.system("clear")
                plotPointOne()
            elif storyLocation == 5:
                os.system("clear")
                sewerPlot()
            elif storyLocation == 6:
                os.system("clear")
                waterBugPlot()
            elif storyLocation == 7:
                os.system("clear")
                waterBugPlot2()
            elif storyLocation == 8:
                os.system("clear")
                heaven()
            elif storyLocation == 9:
                os.system("clear")
                plotPointTwo()
            elif storyLocation == 10:
                os.system("clear")
                plotPointThree()
            elif storyLocation == 11:
                os.system("clear")
                insideStory()
            elif storyLocation == 12:
                os.system("clear")
                plotPointFour()
            elif storyLocation == 13:
                os.system("clear")
                encounterTwo()
            elif storyLocation == 14:
                os.system("clear")
                nextDay()
            elif storyLocation == 15:
                os.system("clear")
                plotPointFive()
            elif storyLocation == 16:
                os.system("clear")
                docOffice()
            elif storyLocation == 17:
                os.system("clear")
                endGame()
            elif storyLocation == 18:
                os.system("clear")
                treatments()
            elif storyLocation == 19:
                os.system("clear")
                safeCombination()
            elif storyLocation == 20:
                os.system("clear")
                typeMessage()
            elif storyLocation == 21:
                os.system("clear")
                antSize()
            elif storyLocation == 22:
                os.system("clear")
                sockPlot()
            elif storyLocation == 23:
                os.system("clear")
                backYard()
            elif storyLocation == 24:
                os.system("clear")
                encounterThree()
            elif storyLocation == 25:
                os.system("clear")
                plotPointSix()
            elif storyLocation == 26:
                os.system("clear")
                foundAntidote()
            elif storyLocation == 27:
                os.system("clear")
                journeyHome()
            elif storyLocation == 28:
                os.system("clear")
                closeToHome()
            elif storyLocation == 29:
                os.system("clear")
                endGame2()
            elif storyLocation == 30:
                os.system("clear")
                microscopicSize()
            elif storyLocation == 31:
                os.system("clear")
                encounterFour()
            elif storyLocation == 32:
                encounterZero()
            elif storyLocation == 33:
                grasshopperEncounter()
            elif storyLocation == 34:
                sparrowEncounterOne()
            elif storyLocation == 35:
                sparrowEncounterTwo()
        except KeyError:
            printt(f"{fore(1)} Error loading data!{style(0)}", userStrDelay)
            time.sleep(0.5)
            printt("New game? (y/n)", userStrDelay)
            newGame = int(fkey.getchars(chars=["y", "n"]))
            if newGame == "y":
                game()
            elif newGame == "n":
                pass
    else:
        try:
            user = input("Enter your username: ")
            if os.path.exists(f"users/{user}.txt"):
                printt(
                    f"\n\a{fore(2)}>> Save file: {user}.txt found.\n   Retrieving data...{style(0)}",
                    userStrDelay,
                )
                time.sleep(2)
                os.system("clear")

                # Retrieve user's data
                filename = "users/" + user + ".txt"

                r = open(filename, "r")

                # List
                save_list = r.read().split("\n")  # Split into a list

                # Set variables
                # print("DEBUG INFO FOLLOWS THIS LINE:")
                # print(f"save list OK ({save_list})")
                # print("accessing name...")
                user = save_list[0]
                # print(f"user OK ({user})")
                # print("accessing story")
                storyLocation = int(save_list[1])
                # print(f"story OK ({storyLocation})")
                # print("accessing deaths")
                numDeaths = int(save_list[2])
                # print(f"deaths OK ({numDeaths})")
                # print("accessing friend")
                bestFriend = save_list[3]
                # print(f"friend OK ({bestFriend})")
                # print("accessing delay")
                userStrDelay = float(save_list[4])
                # print(f"delay OK ({userStrDelay})")
                time.sleep(1)

                # Run game from storyLocation
                if storyLocation == 1:
                    os.system("clear")
                    game()
                elif storyLocation == 2:
                    os.system("clear")
                    encounterOne()
                elif storyLocation == 3:
                    os.system("clear")
                    longJourney()
                elif storyLocation == 4:
                    os.system("clear")
                    plotPointOne()
                elif storyLocation == 5:
                    os.system("clear")
                    sewerPlot()
                elif storyLocation == 6:
                    os.system("clear")
                    waterBugPlot()
                elif storyLocation == 7:
                    os.system("clear")
                    waterBugPlot2()
                elif storyLocation == 8:
                    os.system("clear")
                    heaven()
                elif storyLocation == 9:
                    os.system("clear")
                    plotPointTwo()
                elif storyLocation == 10:
                    os.system("clear")
                    plotPointThree()
                elif storyLocation == 11:
                    os.system("clear")
                    insideStory()
                elif storyLocation == 12:
                    os.system("clear")
                    plotPointFour()
                elif storyLocation == 13:
                    os.system("clear")
                    encounterTwo()
                elif storyLocation == 14:
                    os.system("clear")
                    nextDay()
                elif storyLocation == 15:
                    os.system("clear")
                    plotPointFive()
                elif storyLocation == 16:
                    os.system("clear")
                    docOffice()
                elif storyLocation == 17:
                    os.system("clear")
                    endGame()
                elif storyLocation == 18:
                    os.system("clear")
                    treatments()
                elif storyLocation == 19:
                    os.system("clear")
                    safeCombination()
                elif storyLocation == 20:
                    os.system("clear")
                    typeMessage()
                elif storyLocation == 21:
                    os.system("clear")
                    antSize()
                elif storyLocation == 22:
                    os.system("clear")
                    sockPlot()
                elif storyLocation == 23:
                    os.system("clear")
                    backYard()
                elif storyLocation == 24:
                    os.system("clear")
                    encounterThree()
                elif storyLocation == 25:
                    os.system("clear")
                    plotPointSix()
                elif storyLocation == 26:
                    os.system("clear")
                    foundAntidote()
                elif storyLocation == 27:
                    os.system("clear")
                    journeyHome()
                elif storyLocation == 28:
                    os.system("clear")
                    closeToHome()
                elif storyLocation == 29:
                    os.system("clear")
                    endGame2()
                elif storyLocation == 30:
                    os.system("clear")
                    microscopicSize()
                elif storyLocation == 31:
                    os.system("clear")
                    encounterFour()
                elif storyLocation == 32:
                    encounterZero()
                elif storyLocation == 33:
                    grasshopperEncounter()
                elif storyLocation == 34:
                    sparrowEncounterOne()
                elif storyLocation == 35:
                    sparrowEncounterTwo()

                else:
                    pass
        except FileNotFoundError and IndexError and NameError:
            printt("The file wasn't found! ", userStrDelay)


def register():
    global storyLocation, numDeaths, bestFriend, userStrDelay, user

    print(
        "You may choose a name to create a save file under. You must remember it later on."
    )
    user = input("Enter your username: ")

    # Checks if file exists, ask for username again.
    if os.path.exists(f"users/{user}.txt"):
        register()
    else:
        # Continues to create new save file
        f = open(f"users/{user}.txt", "x")  # type: ignore
        f.close()
        os.system("clear")

    print(f">> New save file '{user}.txt' created.\n")

    # Acceptable input
    valid = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "10",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35"
    ]

    # Asks user to enter plot point until it is valid ^
    while storyLocation not in valid:
        storyLocation = input(
            "Enter your current plot point. \nLeave blank if you are new to start from the beginning (valid plot points are from 1-33):\n"
        )

    if storyLocation == "":  # No plot point, start from beginning
        storyLocation = "1"
        game()
    else:
        pass
    if bestFriend == "":
        bestFriend = input(
            "Enter the name of your best friend (Even though the name is considered useless from starting the game, this only appears if you wish to go deeper into the story....): \n"
        )
    # Name the user's save file
    filename = "users/" + user + ".txt"

    # Write in the file, then close
    w = open(filename, "w")
    w.write(user + "\n" + storyLocation + "\n" + str(numDeaths) + "\n" +
            bestFriend + "\n" + str(userStrDelay) + "\n")  # type: ignore
    w.close()
    os.system("clear")
    printt("You have made a save file!", userStrDelay)
    time.sleep(1)


def options():
    global userStrDelay, numDeaths, bestFriend
    os.system("clear")
    printt(fore(3) + " ⚙️  OPTIONS  ⚙️" + style(0), userStrDelay)
    printt("1. Credits", userStrDelay)
    printt("2. Change text speed", userStrDelay)
    printt("3. View Stats", userStrDelay)
    printt("4. Back to the main menu", userStrDelay)
    option = int(fkey.getchars(chars=["1", "2", "3", "4"]))
    while True:
        try:
            if option == 1:
                os.system("clear")
                printt(
                    f"{fore(6)}Programmed by:{style(0)} TG 101\n\n", userStrDelay)
                time.sleep(0.5)
                printt(
                    f"{fore(7)}Game 💾ving support: @Reykr, The Lone 🐺{fore(2)}(Thanks for helping me!){style(0)}\n\n",
                    userStrDelay,
                )
                printt(
                    f"{fore(130)}Improved game menus (and other small tweaks): {style(0)} @Firepup650 🐶🔥\n\n",
                    userStrDelay,
                )
                printt("Original Story: Also by TG 101\n\n", userStrDelay)
                printt(
                    f"\n\n{fore(5)} This game was made with lots of ❤️ !{style(0)} \n Returning to the main menu...",
                    userStrDelay,
                )
                os.system("clear")
                mainMenu()
            elif option == 2:
                os.system("clear")
                userStrDelay = float(
                    input(
                        f"Enter your desired text speed. Hint: Right now, its at {str(userStrDelay)} seconds...\n"
                    )
                )
                printt(
                    "Current text speed, which is " + str(userStrDelay) + "\n",
                    userStrDelay,
                )
                printt("Saving text speed... Please wait...", userStrDelay)
                db["userStrDelay"] = userStrDelay  # type: ignore
                printt(fore(2) + "💾 Text speed saved! 💾 \n\n" +
                       style(0), userStrDelay)
                printt("Returning to the main menu", userStrDelay)
                os.system("clear")
                mainMenu()
                return userStrDelay
            elif option == 3:
                os.system("clear")
                printt("🏆 OVERALL STATS 🏆\n\n", userStrDelay)
                time.sleep(0.5)
                printt("☠️ Number of deaths: " + str(numDeaths), userStrDelay)
                time.sleep(0.5)
                printt("Time played: ", userStrDelay)
                print("Would you like to return to the main menu? (y/n) ")
                exitMenu = int(fkey.getchars(chars=["y", "n"]))
                if exitMenu == "y":
                    os.system("clear")
                    mainMenu()
                else:
                    os.system("clear")
                    printt("OK! Exiting the game....\n\n Goodbye!", userStrDelay)
                    quit(0)

            elif option == 4:
                os.system("clear")
                printt("Exiting to the main menu...", userStrDelay)
                os.system("clear")
                mainMenu()
            else:
                pass
        except ValueError:
            pass


def docOffice():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "You have to wait for a normal-sized person to open the front door, since there's no pet door visible.\n You then swiftly go inside the medical center.",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n\n The waiting room isn't even that crowded, so that's a good thing... for your ears actually, since they're a lot more prone to even louder noises that make a person go deaf!\n\n You try to gaze up in order to see the receptionist, but the towering desk blocks your view."
        + fore(3)
        + "\n\n You REALLY, AND DESPERATELY need some help... AND YA NEED IT NOW!"
        + style(0),
        userStrDelay,
    )
    printt("1. Try to get the receptionist's attention", userStrDelay)
    printt(
        "2. Dash through the hallway in order to find your family doctor", userStrDelay
    )
    while True:
        try:
            print("These are your two sources of help.\n Choose wisely:")
            decision = int(fkey.getchars(chars=["1", "2"]))
            if decision == 1:
                os.system("clear")
                printt(
                    f"First off, {style(3)}HOW{style(0)} do you even get up that desk?\n That's the question that flashes in your brain as you try to think.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Then, you see a chair 🪑 next to you. Could you use it as a ladder to get to the desk? Probably. \n\n And so, you grab the one of the chair legs and climb upwards.\n\n CHARACTER DEVELOPMENT ALERT! ==> You have no fear of heights at all, and a better climber!😉\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "After a few minutes, you reach the top of the chair.Looking up, you see that the desk is about 10 cm away from you.\n\n YOU CAN DO THIS! DON'T GIVE UP!\n\n You run and with enough momentum and force, you lift yourself of the ground, leaping towards the edge of the desk...\n"
                    + fore(2)
                    + "... and hoist yourself up in no time!"
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "'I- I did it!', you think to yourself in excitement.\n You walk towards the receptionist. She's still busy typing on her laptop. But, that doesn't matter. You're 5.08 cm tall and need help right away. You silently clear your throat, and move closer to the receptionist.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"'Ahem... Excuse me...'\n The receptionist then looks at you.... And lets out a piercing scream.... {fore(1)}And faints!{style(0)}\n 'MA'AM!', you call out.'MA'AM, ARE YOU OK?!'. No response. Is she dead?\n Well, not really, as she gains consciousness and gets up from the floor. 'Am I seeing things?', she asks to herself.\n\n 'Well,' you reply. 'You really aren't seeing stuff, I am really here...'.\n 'After all, I was the one that called you... but you couldn't hear me. I really need help here. Where's the doctor?'. 'Ok,ok, I'm calling him', the receptionist says, shaking as she dials your physician.",
                    userStrDelay,
                )
                os.system("clear")
                printt(
                    "Your family doctor arrives, after 5 minutes.'Sorry, Marth, I'm a little late today. You called me, what's the reason?'. Marth, the receptionist points to you, and your physician's jaw drops wide open.\n\n 'Oh. My. God.... I have never seen anything like this before, and I'm shocked to see it.'\n\n The doctor reaches out for you, and puts you in his left palm. 'D-Did you-- Did you lose weight?', he asks you. 'Sort of...', you answer, 'In reality, I shrunk.'\n You let out a frustrating sigh.\n 'Man, I can't believe that I was so stupid... I shouldn't have drank that fat-burner...This is why I'm in this state...', you mutter to yourself and start to 😢😭. The doctor then strokes you with his finger, calming you down eventually.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "'C'mon.', your doctor says to you. \n\n 'You can tell me later on what happened, right after I'll do a checkup on you.' Therefore, the two of you go straight to the examination room. You're one step closer from being normal again!",
                    userStrDelay,
                )
                time.sleep(0.5)
                storyLocation = "17"
                saveGame()
                endGame()
                break

            elif decision == 2:
                os.system("clear")
                printt(
                    "You run into the dim hallway, calling out your doctor's name. No one hears you, though.\n\n (Man, I am absolutely tired of saying THAT over and over again... I hate my job, LOL)\n\n\n That's when you find yourself in a dimly lit room, with the door open. Maybe your physician is in there...\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Turns out he's not really in there, so where the heck is he anyway?\n\n\n A sound then startles you, and its a sound that you wouldn't even want to hear...\n **SLAM** \n The door just slammed shut!\n\n"
                    + fore(1)
                    + " YOU'RE TRAPPED! \n"
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "\n You gaze straight at the bottom. Could you escape through the crack of the door? \n\n You try to squeeze through. Nope, its too narrow to slip through.\n\n\n And, then you hear another sound... behind you!😬\n\n",
                    userStrDelay,
                )
                printt(
                    "You wheel around, but its impossible to see since its extremely "
                    + fore(0)
                    + " dark in here...\n😖"
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\n Your pupils adjust to the lack of light in the room, and you scream! A rat, 3 times the size of you, with green glowing eyes, is looking at you! 🐀",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\n The rat just stares at you, twitching its whiskers. You stay still, like a statue, with your body shaking. You have no option, but to either do the following:\n ",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt("1. Run", userStrDelay)
                printt("2. Fight the rat", userStrDelay)
                printt("3. Try to squeeze through the door crack again", userStrDelay)
                print("What would you do right now?\n Select an option: ")
                decision = int(fkey.getchars(chars=["1", "2", "3"]))
                if decision == 1:
                    os.system("clear")
                    printt(
                        "You spin on your heels and dash to the other side of the dark room. Since the rat's a nocturnal animal, it follows your footsteps!\n\n Still running like you never ran before, you spot a gaping hole in the wall. Could you escape through it? Maybe...\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "You then leap towards the wall, and push yourself through the hole!\n"
                        + fore(10)
                        + "You finally escaped!"
                        + style(0)
                        + "\n\n But, WHERE are you now?",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    os.system("clear")
                    printt(
                        "You're still running at this moment, and that's when you trip over something. It's a mouse trap!🪤\n But, before you can make your next move, the mouse trap's sharp blade beheads you. You've now been executed -- French Revolution fore. Your miniature severed head rolls on the ground, and sure enough, the rat eats the head.\n",
                        userStrDelay,
                    )
                    printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                    numDeaths += 1
                    saveGame()
                    playAgain()
                elif decision == 2:
                    os.system("clear")
                    printt(
                        fore(0)
                        + "Even though its dark in here, you find a pushpin 📌, which is equivalent to a dagger, according to a tiny person like you. Maybe you can use this to fight the rat!\n"
                        + style(0),
                        userStrDelay,
                    )
                    printt(
                        "'OK! DON'T MOVE!', you yell to the rat, pointing the sharp edge of the pin towards its furry face. Nothing happens. Its just staring at you...\n.... Still twitching its whiskers...\n And minding his (or her?) business....\n... Then, you make a stabbing motion with the pin, therefore stabbing it! The rat reaches out for you and you dodge it.... \n\n{Intense Fight scene continues}\n\n\n After somewhat of a few minutes, you finally kill the rat with all your might....\n",
                        userStrDelay,
                    )

                    print("██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗██╗")
                    print("██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██║")
                    print("██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ██║")
                    print("╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ╚═╝")
                    print(" ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ██╗")
                    print("  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝")
                    time.sleep(0.5)
                    os.system("clear")
                    printt(
                        f"Now you need to get out of this room, but HOW?\n\n And, that's when the door opens! Good, now you can finally get out of here! You then dash to the door, screaming,'THANK YOU! THANK YOU FOR LETTING ME ESCAPE!'. The figure that opened the door, looks down at you, and screams! 'IT'S A MOUSE! SOMEONE KILL IT!'. Wait, mouse? Does that mean... you?!\n\n Yep, the janitor of the medical center thinks you're nothing but a mouse...🐭, even though you're a human being!\n The janitor takes out a can of mace, and sprays it at you!\n\n\n But, you dodge it in no time!\n'Please, don't hurt me!', you yell in your tiny voice. That's when the janitor sprays the mace again....\n\n And you try to steer away from that spray. Unfortunately, your itty-bitty eyes get burned by the mace! You scream in pain, sticking out the middle finger @ the stupid janitor.\n\n Great, now you CAN'T see anything! Well then....",
                        userStrDelay,
                    )
                    printt("🦯 BLIND END? 🦯", userStrDelay)
                    numDeaths += 1
                    saveGame()
                    playAgain()
                elif decision == 3:
                    os.system("clear")
                    printt(
                        "You duck downwards into the door crack and try to push yourself through. That's when the rat uses its claws to grab your calves! 'HEY! LET GO!',you protest in anger.\n\n Pushing again, you crawl on the floor even more, and kick the rat in its stomach.\n\n You finally slip through the dimly lit room and back in the hallway! Turns out you actually did fit in there, after all! You just rushed through the process...\n\n Now that you're free from the rat's grasp, maybe you ought to continue finding your physician...",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    os.system("clear")
                    printt(
                        "Continuing to run down the hallway, you stop short of something as a familiar tightening sensation shoots throughout your body...",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        fore(1)
                        + "Oh great....\n You're still shrinking, right?"
                        + style(0)
                        + "\n\n\n\n RIGHT?! (I am so bored of making the player suffer.... I give up!)",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "But, there's no time to think about that. You need help, ASAP! Maybe you cou-",
                        userStrDelay,
                    )
                    os.system("clear")
                    printt(
                        "Too late. You eventually disappear out of sight FOREVER.... Thanks to the narrator's fudging writer's block....\n\n It would've been better if you seeked attention above... (In other words... get the receptionist the damn attention she deserves!)",
                        userStrDelay,
                    )
                    printt(fore(5) + "🧱 TO BE CONTINUED...? 🧱" +
                           style(0), userStrDelay)
                    numDeaths += 1
                    saveGame()
                    quit(0)
        except ValueError:
            printt("That's not a number, try again!", userStrDelay)


def heaven():
    global userStrDelay, numDeaths
    os.system("clear")
    printt("\n'Huh, where am I?'\n", userStrDelay)
    time.sleep(0.5)
    printt("\n'Aren't I supposed to be dead?!'", userStrDelay)
    time.sleep(0.5)
    printt(
        fore(6)
        + "WaitASec!\n\n Ha! I tricked you again, into thinking that you'll be dead, right?"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{style(3)}{style(4)}By the way, you're already dead, you're just in the afterlife.{style(0)} \n\nYou are now staring at a blinding light, questioning your existence...\n Well, WHERE are you, exactly?\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "My friend!\n\n\n" +
        fore(3) + f" {style(3)}{style(1)}{style(4)}WELCOME  TO  HEAVEN! " +
        style(0), userStrDelay
    )
    time.sleep(0.5)
    printt("1. Why am I here?", userStrDelay)
    printt("2. What if I'm an atheist and don't believe in God?", userStrDelay)
    printt("3. Are you here to give me another chance in life?", userStrDelay)
    while True:
        try:
            print("What do you wish to ask?\n")
            question = int(fkey.getchars(chars=["1", "2", "3"]))
            if question == 1 or question == 3:
                os.system("clear")
                printt(
                    "\nWell, I literally feel bad for you, based on what you suffered, so I have a favour to tell you...\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    fore(10)
                    + "Would you like to return to your normal size?\n\n"
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "'Yes', you say with enthusiasm,'I would like to return to normal...'",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Soon, you are then whisked away back to Earth in a bright "
                    + fore(11)
                    + " FLASH "
                    + style(1)
                    + style(0)
                    + "\n\n And...."
                    + fore(2)
                    + "You are back to your normal size!"
                    + style(0)
                    + "\nYou don't even need to go the doctor at all!\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\n\n You happily head home, full of joy. You then decide to make yourself chocolate fudge 🍨 when you get home.",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(fore(2) + "🎉 THE END 🎉" + style(0), userStrDelay)
                quit(0)
            elif question == 2:
                os.system("clear")
                printt(fore(1) + "THEN GET DA HELL OUT OF HERE!" +
                       style(0), userStrDelay)
                time.sleep(0.5)
                printt(
                    "\n You are eventually thrown into the lowest depths of hell, and burn constantly...\n\n🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥\n",
                    userStrDelay,
                )
                printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                numDeaths += 1
                saveGame()
                playAgain()
        except ValueError:
            printt("That's not a number! Try again!", userStrDelay)


def waterBugPlot():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    time.sleep(0.5)
    printt(
        "Its a water bug... a really " +
        fore(3) + " slimy " + style(0) + " water bug.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("\nBut, it's not one or two water bugs...", userStrDelay)
    printt("It's FIVE.\n FIVE WATER BUGS.\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        "And, you're surrounded by many water bugs.\n You remember how you really can't even stand these slimy insects!\n Now, that you've seen them up close, you really, really, can't f**king stand them even more!🤢\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n'EEEEEWWWWWWWWWWW!', you gross out at the sight of them, even though the water bug family of 5 doesn't care about whether you hate them or not.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n That's when you notice, that these water bugs have wings on them!\n Maybe... just maybe... you can use one of them and fly out of the sewer, and straight to the doctor's office!",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n However, your pet peeve of hating water bugs will not stop you from trying to puke. Ughhh...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Get on the water bug and steer it to the doctor's office", userStrDelay)
    printt("2. Jump into the dirty water and commit suicide", userStrDelay)
    print("Would you rather get to safety or just die?\n")
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            "\n You run towards the water bug, and touch its slimy body. You feel like 🤮, but this is the only way to save yourself time, and not to get stuck in the sewer all day.\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n You then hoist yourself on the bug, and sit on its back, and wait for a few seconds...",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n.... Suddenly, you feel a sharp jolt, and find that the water bug you're on is preparing to take off!\n It might have been friendly to you or maybe it doesn't care that you're riding on it.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "And, then its rising...\n Up, Up, UP!\n\n Within 5 seconds, you're going towards the opening of the gutter...",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(2)
            + "You're flying, now! You can finally get out of this dark, and putrid place..."
            + style(0)
            + "\n But, how would you control the water bug to get to your destination?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You notice the antennas of the water bug, and pull on the left one. As a result, your water bug steers to the left. You try the other antenna, and sure enough, the water bug steers right. Pretty interesting...\n The antennae controls a lot like the reins of a horse!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n Knowing where the location of your local medical center, you steer the water bug in the exact directions you've memorized.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("*********", userStrDelay)
        storyLocation = "7"
        saveGame()
        waterBugPlot2()
    elif decision == 2:
        os.system("clear")
        printt(
            "You jump into the mucky water and drown...I guess that they'll never find your body, and you lost your chance to be fully normal again...\n\n",
            0.05,
        )
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()


def waterBugPlot2():
    global numDeaths, storyLocation, userStrDelay
    os.system("clear")
    time.sleep(0.5)
    printt(
        "\nAfter your long journey, you see that the medical center is in close view.\n ",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n You try to lower your water bug downward, but you fail. Sheesh, it doesn't want to listen to you at all!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You try again, and fortunately, the bug gives in, and you dive a little lower to the medical center's entrance.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You glance down at the ground... and see that the overall distance between you and the ground is large!\n\n You also notice the blades of grass is right next to the hard cement pavement...\n",
        userStrDelay,
    )
    printt(
        "\n That's when you are faced with a deadly decision: Jump from your water bug and free fall straight to the ground...\n\n But would you expect a hard/soft landing?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "1. Land in the soft dirt (with the catch that you have to walk to the entrance)",
        userStrDelay,
    )
    printt(
        "2. Land on the hard pavement (alongside the advantage of getting to the entrance faster)\n",
        userStrDelay,
    )
    print("Which place will you land?\n")
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            "You jump off the water bug and brace for a hard landing...\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n ... Which actually doesn't, as you're a lot more lighter than you were before...\n You hit the grass once and bounce off the dirt."
            + fore(2)
            + "At least you survived though!\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt("\n Finally! You can go straight to the doctor's office!", userStrDelay)
        storyLocation = "16"
        saveGame()
        docOffice()
    elif decision == 2:
        os.system("clear")
        printt(
            "You jump off the water bug and brace for a hard landing...\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "... Which actually does, as you hit the pavement with a huge **SMACK** \n\n Even though you're bleeding and in critical condition, you're still alive. As you try to get up, you fall back down again.\n"
            + fore(1)
            + "Bad news! You dislocated your femurs and you CAN'T WALK.\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You start to crawl by pushing with your hands, and shoulders, but you don't have enough strength to get to the entrance!\n I mean, you're battered and bruised from hitting the walkway.\n Blood continues to drip down your face.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "That's when you hear a loud, STAMP!\n You look up, and see that its a gigantic man walking towards you!\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(3)}{style(3)}You have to do something! And I mean, FAST!\n\n{style(0)}", userStrDelay)
        time.sleep(0.5)
        printt(
            "You try to shout for help, but your tiny voice comes out weak and hoarse...\n You then see the sole of the man's shoe, and scream! \n You're going to be squashed, and IT'S TOO LATE!\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("**SQUUUUIIIISSSHHHHH**\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n\n What happens next is something that I can't even describe.\n Right in the center of the walkway,there is a small disfigured person, lying down, with all the blood drained out of his/her body. His/her eyeballs have fallen out of their sockets, and the person's joints are badly severed and dislocated... All surrounded by a pool of blood...😵",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "And that person who suffered a pretty disturbing death is... \n\n you.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        storyLocation = "8"
        saveGame()
        heaven()


def sewerPlot():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "'Unnhhh', you let out a groan.\n Did you injure your back or some sort?\n Probably...",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nYou sit up, and gaze at your legs and arms. You test them out by flexing them."
        + fore(2)
        + "\nGood, no broken bones.\n"
        + style(0),
        userStrDelay,
    )
    printt(
        "\nYou stand up, trying to understand where you were before you fell...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Looking around, you find yourself in one opposite side of the sewers. You then stare across the stream of dirty water. Pale light is visible from where you're standing. From your perspective, its about the length of the Pacific Ocean!\n You crane your neck and see the open gutter that you fell from. \n\n The problem is, the space between you and the 'river' is too far, and there's NO WAY to climb up and to get the heck out of here.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Great.\n\n{fore(1)}{style(3)} You're stuck.\n What now?{style(0)}\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        "\nYou sit down again, wondering what to do... How to get out.... How to get out....\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n Then, an idea flashes in your mind. Maybe you can call for help.",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n\n'HELP! SOMEBODY! HEY! I'M DOWN HERE! HEEELLLLPPP!', you shout. No response. That's because your voice is tiny and faint, so there's ZERO chance that someone will hear you from the depths of the sewer.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You pinch your nose. It sure is stinky down here! \nTrust me, you're smelling random strangers 💩, toilet water, and urine. Gross...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You then pace frantically for a Plan B, but what is Plan B?\n\n That's when you hear a chittering sound... on your left...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n'Aw, c'mon', you think to yourself. 'Please don't let it be another lizard...'\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You turn to your left. Good thing it's NOT A LIZARD, BUT WORSE...",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "\n... It's a scorpion....🦂\n Oh, sh*t.\n You're dead meat, now. Like, serious dead meat...\n Because scorpions can be poisonous,they say...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n'G-Get away from me!', you stammer. But, the scorpion doesn't understand English, so what's the use of talking to it?",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(11)
        + "\n Well, you have to do something now, would you rather get stung and eventually die from poisoning? I guess NOT!\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Surrender", userStrDelay)
    printt("2. Hide", userStrDelay)
    print("Which option do you select?\n")
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            "You raise your hands above your head, saying, 'Fine! I give up and I don't want to live anymore!'\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("'J-Just take me in, Scorpie...Take me in...'", userStrDelay)
        time.sleep(0.5)
        printt(
            "The scorpion comes closer to you, with its arms constantly moving up and down.\n You bend over, staring at the scorpion, quivering with fear...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "The scorpion then examines you, and rotates its body, therefore swinging its tail, knocking your socks off!\n\n You are then sent flying backwards, and hit the hard cement floor (just a few cm to the edge of the stream) with a hard SLAM!\n That must've hurt didn't it?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "You get up, sprawled on the cold floor, as the scorpion ventures even more closer, with its claws open, snapping like hedge-clippers.\n\n You realize that you're next to the murky water, and looking to the right, its a dead end.\n\n\n"
            + fore(1)
            + "YOU CAN'T ESCAPE!\n"
            + style(0)
            + "There's only one option, though: Dive into the dirty sewer waters.\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "And, with the scorpion about 3 cm from you, you have no choice.\n\n You take the plunge, just as the scorpion is in the same location you were before... and sink into the cold, dirty water...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "At least you should be happy that you got away from that terrifying scorpion! \n The bad news is, its actually hard to swim in this water, as the stench of it is horrible. \n Secondly, the water is moving like those rivers for white-water rafting....\n Wait ...\n"
            + fore(6)
            + "Aha! You need a raft in order to traverse the waters instead of just drowning!"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Then, a familiar object floats past you,as you struggle to stay buoyant.\n What is that object? Is it:\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("1. A popsicle stick", userStrDelay)
        printt("2. A crushed soda can", userStrDelay)
        print("Which one is it?\n")
        decision = int(fkey.getchars(chars=["1", "2"]))
        if decision == 1:
            os.system("clear")
            printt(
                "It's a popsicle stick.\n You then grab it, and try to get on it. To you, it looks a kayak. Maybe that will keep you afloat?\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "You stand on the long stick, and unexpectedly, you lose control and fall off the popsicle stick! Seems like it couldn't support your weight!",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "You then drown and sink like a paper bag slowly in the dirty water. Maybe if you shrank a little more, then the possibility of being buoyant on a thin popsicle stick would be a good thing...\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
            numDeaths += 1
            saveGame()
            playAgain()
        elif decision == 2:
            os.system("clear")
            printt("It's a crushed soda can, alright.\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                "Fortunately, that metal can does support your weight (If you chose the popsicle stick, you'll know why).\n You get on the soda can, and lie down in exhaustion.\n Being 5.08 cm tall sure is tiring!\n Glancing at the current, you find out that its going in one direction: right.\n That means, you're going to the opening of the sewers! Maybe you can get out of here in the nick of time!\n\n But how?",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "You start to get up, and look towards in the direction the dirty stream is going. After a few minutes, you see pale light...\n"
                + fore(2)
                + "You're back to where you were!\n Now's your chance!"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "\n You then squat your legs and with a running start, you jump towards the cement platform.",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                fore(2)
                + "\n\n And you land on your feet!\n At least you didn't scrape your knees.\n Yay!"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "\n And, that's when you hear a familiar tapping sound... Another spider?\n\n",
                userStrDelay,
            )
            storyLocation = "6"
            saveGame()
            waterBugPlot()

    elif decision == 2:
        os.system("clear")
        printt(
            "You make a run for the other side of the sewer, hide in a corner, and expect the scorpion to follow you...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"Luckily, it doesn't. Seems like it has forgotten about you. Whew!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You peep around the corner, and see that there's no scorpion or any other giant animal there!\n\n You're safe and sound!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Or, are you?...\n Just then when you are so relieved to not come across any insect, bird, rabbit, etc., you hear a tapping sound.... Shoot.\n\n Another spider? Or a praying mantis?...What could it be?",
            userStrDelay,
        )
        time.sleep(0.5)
        storyLocation = "6"
        saveGame()
        waterBugPlot()


def plotPointOne():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "You lower yourself off the stoop, and jump off the sidewalk into the blades of grass. Those blades pinch your cheek, so you have to push constantly as you run.",
        userStrDelay,
    )
    printt(
        "\n Admit it, its like fighting through a jungle, even though your front yard is more of a jungle...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "After what seems to be like forever, you hear a rustling sound next to you.\n It turns out you're not the only one in the front yard!\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Pretty soon, you see something coming towards you, and that something is....\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(fore(1) + "...A DINOSAUR! 🦖\n\n" + style(0), userStrDelay)
    os.system("clear")
    time.sleep(0.5)
    printt(
        "No... wait a sec...That looks absolutely nothing like a dinosaur.\n You're not J.Jonah Jameson (If you saw Spider-Man: No Way Home, BTW) to confuse a dinosaur with a lizard...",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nYep, that's what you ACTUALLY are seeing...\n A really "
        + fore(3)
        + "scaly"
        + style(0)
        + " lizard --> 🦎\nGreen in color, with black beady eyes staring at you...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(3)
        + "Like I said, the lizard's coming towards you, and you have to find a way to deal with this creature that's literally the size of a T-Rex...\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Run", userStrDelay)
    printt("2. Poke it with a stick", userStrDelay)
    printt("3. Hitch a ride on the lizard", userStrDelay)
    printt("4. Kill it", userStrDelay)
    print("Which option would you like to select?\n")
    decision = int(fkey.getchars(chars=["1", "2", "3", "4"]))
    if decision == 1:
        os.system("clear")
        printt(
            "\n You run away from the lizard in the opposite direction instead of the diagonal path you decided to take.\n You look back and see that the lizard hasn't caught up to you...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "That's when you exit the tall grass, running on the tarmac.\n Suddenly, a car comes out in front of you, and before its too late, you're roadkill. You eventually die of stupidity...\n",
            userStrDelay,
        )
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\nSeriously? You thought you were dead?🤣\n You're not dead actually, the tire missed you by a few cm! There are benefits of being smol, after all!\n But, with what cost? ",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"\nThe answer is: You have became a human cannonball and is flying towards the opposite end of the sidewalk...All thanks to the airflow of the weather...\n It's a 🌧️ and 💨 day today!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"\n...Then, you land on a flowing stream with a big SPLASH.\n You then swim upwards, gasping for air, and try to swim in the opposite direction, but fail to do so.\n\n At this point, you're far away from the bus stop. You have lost all hope in getting there! Could you make it back after all?",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(1)}\nNo.\n\n You CAN'T... the current is pushing you to the right, but to where?{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"You blink and scream in horror...\n {fore(1)}You're going towards the sewers! IT'S TOO LATE! {style(3)}Is this the end of the world?{style(0)}, you ask...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n'AAAAAUUUUUGGGHHHH!', you let out a scream as you tumble into the darkness of the sewer...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("..........................\n", userStrDelay)
        time.sleep(0.5)
        storyLocation = "5"
        saveGame()
        sewerPlot()
    elif decision == 2:
        os.system("clear")
        printt(
            "You look around for a stick in order to poke the big lizard.\n Unfortunately, there isn't one.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("Too late, you're eaten alive by the lizard...", userStrDelay)
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    elif decision == 3:
        os.system("clear")
        printt(
            "You reach out to the lizard with an outstretched hand, like Hiccup did to Toothless in 'How To Train Your Dragon.'\n 'It's OK, I'm not going to hurt you...', you say in a soothing voice. The lizard looks at you patiently, and tilts it head, as if it was trying to understand you.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n Then you feel the lizard lick your face with its thin tongue. The lizard is actually friendly!\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Then, you hoist yourself on the lizard, and guide it with directions on how to get to the local medical center. Reluctantly, the lizard agrees (which is weird) and the two of you make way to your destination...",
            userStrDelay,
        )
        storyLocation = "16"
        saveGame()
        docOffice()
    elif decision == 4:
        os.system("clear")
        printt(
            "The lizard eats you alive, because you really don't have any weapon with you....",
            userStrDelay,
        )
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    else:
        printt("Invalid choice! Try again!", userStrDelay)


def plotPointTwo():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "You walk on the solid cement pavement in a straight line. Figuring out that walking across the pavement will take several hours (or days?!) in order to get to the bus stop, you decide to run.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "After a staggering 15 minutes, you arrive @ the bus stop, panting.\n\n No one sees you at this point. However, you have to wait FOREVER till the bus arrives, since time is a lot more slower after you shrunk...⏳\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"...Then the bus comes into full view, rising high like a skyscraper according to your POV!\n\n{fore(3)}You're finally at the bus stop, but how would you get on the bus itself?{style(0)}\n\n There's no possible way to get on the front steps!\n It's KILOMETRES above your head!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Then, you get an idea. You see a person walk to the entrance of the bus. You try shouting out to her.'Hey! I need help to get on the bus! Can you hear me? Hello? HEEEEYYYY!'. The woman doesn't listen to you, since you completely forget that no one can hear you. Another plan....\n\n Wait... Could you latch onto her? Sounds risky...\n\n You move to action,by planning to aim for the leg and run towards the woman, and then take the mighty leap--",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n-- And "
        + fore(1)
        + " misses the legs. "
        + style(0)
        + "\n You're now sliding onto her jeans! \n With a fast reaction time you hold onto the fabric of the pants.\n\n"
        + fore(2)
        + " Yesss!"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n You still hang onto her jeans for dear life, as she shows her bus pass to the bus driver.\n\n Suddenly, you lose your grip and fall to the floor! At least there was NO use holding onto that person, she'd freak out if she saw you!",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n You find the nearest pole on the bus, and stayed still, holding the pole...\n The inside of the bus stretched like an ocean liner...\n\n At this moment, more people are getting on the bus (which possibly means a likely chance to get trampled, due to your miniature proportions). Luckily, you aren't stepped on as you've found a safe place!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Therefore, the bus starts up. You still hold onto the pole, as the bus shifts and jolts constantly. To a regular passenger, its normal for the trip to be bumpy, but to you, who's 2 inches tall, it sure is a really BIG PROBLEM!\n\n The bus hits a bump, and you fly up in the air!\n\n Just then, the bus takes a turn to the left, and you also sail... to the LEFT!\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'Whoooaaaahhhh!!!', you yell as you fall. No one hears you, since everyone is busy with their own things.\n You're still falling at this moment! {style(3)}Oh, great... I'm gonna die{style(0)}, you think to yourself.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You then land.... in some random person's baby stroller...\n You hit the hard surface of the stroller's food tray, which should've broke your spinal cord, but you're still alive!\n But, be prepared for what's about to come...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "The next thing you know, a 11-month old baby 👶 8 times your size, is staring at you!\n\n 'Hey! What're you looking at?', you ask to the Godzilla-sized baby.\n\n The baby still fixates on you, and smiles! Seems like it found a new toy to play with!",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'NO, WAIT!', you shout out in vain as his fat baby hands wrap around you.'I'M NOT A TOY TO PLAY WITH! I'M JUST A REGULAR PERSON!'\n\n The baby doesn't listen to you, as it doesn't have the knowledge to differentiate a very small person to a toy rattle. He shakes you constantly, and you feel that your ribcage is about to burst. No one hears your feeble, tiny voice as you try to call out for help. \n 'LET ME GO! PLEASE, I CAN'T EVEN BREATHE!', you shriek. The baby doesn't listen, AGAIN...",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(11)
        + "You have to do something... FAST!\n Or you'll never get the chance to get medical attention!\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Bite the baby's hand", userStrDelay)
    printt("2. Wait until the baby drops you", userStrDelay)
    print("Which option do you want to select?\n")
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            "Even though you feel dizzy from all that shaking, you bite the baby's fingers with your teeth.\n\n And sure enough, the baby starts crying, and lets go of you!\n"
            + fore(2)
            + "You're free!\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n You fall to the exact same location where the baby found you. The baby's cries deafens your small ears, and you cover them, because you seriously can't STAND that noise!\n That's when you hear the baby's mother rushing to her loved one. Still covering your ears, you see that the mother notices the tiny bite mark you had just made on the baby. And then....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            ".... Notices you, as she turns around, facing the front of the stroller. 'Hi', you say when you turn to face her enormous face.\n Then the mother screams in horror at the sight of you!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n'AAAAAIIIIIEEEEEEEEEEEE! WHAT IS THAT?!', she bellows, pointing a trembling finger at you. Startled by the woman's scream, the bus driver screeches the bus to a halt. Other people come to investigate at what made her freak out all of a sudden.\n\n Great. The mother of that baby that wanted to play with you created a scene, and now you're the center of attention. What now?!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("1. Stay where you are", userStrDelay)
        printt("2. Get the heck out of here!", userStrDelay)
        print("What's your escape route?\n Select an option:\n")
        decision = int(fkey.getchars(chars=["1", "2"]))
        if decision == 1:
            os.system("clear")
            printt(
                "You see around 5-7 eyeballs staring at you in shock. They really couldn't believe their eyes by seeing a 5.08 cm tall person like you!\n 'Is this real?', a guy mutters to himself.'I can't even believe it!', another person says.'Are you even Ant-Man?', he asks you. You then cover your ears again... You can't stand the commotion! People are asking questions on how you shrank so much, and all that jitters!\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "'Quick! Someone call CBC News! They have to see it to believe it!', someone yelled from the back of the bus.\n'Ohhhh', you moan.\nYou really have to get back to normal size, and now THIS?! \n\n Within a few minutes, the local newspaper pen up a story about your impossible size, and you're interviewed by news reporters on how you feel about being the smallest person in the whole world. You don't answer. Why would being tiny be a good thing? It's actually a bad thing!",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "\n\nDays pass, and you have a formed a new identity: The Incredible Tiny Person, most often due to you being famous about your height. You decide to stay like this forever, because that's what the public wants, right?\n\n",
                userStrDelay,
            )
            printt(fore(3) + "🤩 THE END 🤩" + style(0), userStrDelay)
            quit(0)
        elif decision == 2:
            os.system("clear")
            printt(
                "With quick timing, you then jump off the stroller, leap to the nearest pole, and slide down... You're afraid that your little hands will burn as you continue to slide!\n People notice you escaping, however, and these people are interested in you, after all!\n\n",
                userStrDelay,
            )
            time.sleep(0.01)
            printt(
                "'GET IT! GRAB THAT WEE LITTLE PERSON!', someone yells. Within a split second, you're shocked to see a hand, equivalent to the size of Master Hand from Smash Bros. reaching for you...\n"
                + fore(3)
                + "It's going to swat you... @ ANY MOMENT!"
                + style(0)
                + "\n You then jump off the pole, and fall to the floor. You see the passengers' shoes (every kind of shoe) going STAMP, STAMP, STAMP. These footsteps sound a lot like claps of thunder to you! You have to get out of the bus! They're coming for you, since they think you're nothing but a pest! You look at the bus's front door. Its closed and a person like you can't even open it! Only the bus driver can!\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "\n\nYou have to HIDE! But where would you find your hiding spot?\n Secondly, you also have to go to the doctor's office. With the bus not traveling to the next stop, you're doing absolutely nothing but wasting time!\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "1. Hide somewhere on the bus, up until everything is settled",
                userStrDelay,
            )
            printt(
                "2. Get the bus driver attention to go to the medical center and clear your name (to prove that you're not a pest)",
                userStrDelay,
            )
            print("Don't get noticed or get noticed? It's up to you now:\n")
            decision = int(fkey.getchars(chars=["1", "2"]))
            if decision == 1:
                os.system("clear")
                printt(
                    "You run towards the nearest bus seat, and run past the so-called passenger stampede. Your feet are paining from running a LOT!\n You then stay still, shutting your eyes, and waiting for the totally stupid maniac episode to die down...\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"'Hey! Where did that little simp go to?', the same guy shouted.\n\n 'Phew', you think to yourself.'That woman and everybody sure made a fool of themselves.'\n The bus driver commands everybody to sit down, since he is tired of waiting forever. You stay where you were, panting. Beads of sweat drips down your face.\n The bus then starts up again. What a close call...\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "Hours later, you finally arrive at the bus stop adjacent to the local medical center. You breathe a sigh of relief, and wait for people to get off the bus. You trail along afterwards, and hop off the front step, which might've been the most terrifying experience of your life."
                    + fore(2)
                    + "\n\n You did it! Give ya-self a pat on the back!\n\n"
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.05)
                printt(
                    "You run as fast you could across the street, looking terrified. Danger could come from ANYWHERE.\n\n And, at last, you arrive at your medical center, exhausted and tired.\n After taking a quick rest, you then make way to the medical center's entrance, determined to end this... NOW! ",
                    userStrDelay,
                )
                storyLocation = "15"
                saveGame()
                docOffice()
            elif decision == 2:
                os.system("clear")
                printt(
                    "You run to the front of the bus, calling out to the bus driver. Unfortunately, he doesn't hear you. \n That means you have to climb up something in order for him to see you, but what should you grasp on?\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "As you think about THAT, the passengers of the bus close on you!\n Moving to action, you scramble to your feet, and leap onto the pole that held the door switch for the bus driver. By the moment you're halfway up, you hear an extremely loud voice....",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "'I FOUND THAT LITTLE PERSON! I FOUND HIM!'\n 'PLEASE, DON'T HURT ME! PLEASE!', you pleaded in your small voice. But it's too late. That person's palm slams you, squashing you to your eventual death.\n Its better if you would've hid somewhere. No wonder others thought you were a bug or some sort...\n",
                    userStrDelay,
                )
                printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                time.sleep(0.5)
                numDeaths += 1
                saveGame()
                playAgain()
    elif decision == 2:
        os.system("clear")
        printt(
            "You wait patiently for the baby to stop playing with you...", userStrDelay
        )
        time.sleep(0.5)
        printt(
            "....Aaaannnndddd, he doesn't. You suffocate to your demise...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()


def endGame2():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    os.system("clear")
    printt(
        f"Entering your now extremely enormous house, you breathe a sigh of relief.{fore(6)} What a expedition it has been!{style(0)}\n\n Now, this is the moment! The moment to get back to normal once and for all!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Taking out the antidote, you decide to read its instructions {fore(11)}carefully:\n\n{style(0)}",
        userStrDelay,
    )
    os.system("clear")
    printt(
        f"{style(3)}HOW TO USE: TAKE AT LEAST {fore(11)}TWO DROPS OF THE {fore(4)}BLUE LIQUID.{style(0)} {style(3)}IF YOU OVERDOSE, EVEN MORE STRANGE THINGS WILL HAPPEN! {fore(1)}DON'T EVER OVERDOSE, Ya Filthy Animal!\n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"OK, you understood THAT? Following the instructions, you take exactly 2 drops of the antidote and wait for a few minutes.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "And, NOTHING HAPPENS...\n\n Weird....\n\n'Maybe I should drink some more... No! Why would I be this stupid?!', you say.\n\n You're split between following the rules or taking matters into your own hands....\n\n Would you rather:\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Overdose the antidote ", userStrDelay)
    printt("2. Drink a little more ", userStrDelay)
    print("Do you really want to grow, without messing it up?!\n\n Select an option:\n")
    drinkOption = int(fkey.getchars(chars=["1", "2"]))
    if drinkOption == 1:
        os.system("clear")
        printt(
            "You open the corkscrew, and drink 1-2 litres of the antidote. Then you wait for a moment...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(2)}Then you feel your 0.32 cm body.... start to stretch....\n\n... Is the antidote working?!\n\n YES, IT IS! IT IS WORKING!\n\n Every part in your body expands, and you see that everything's decreasing in size, and things are getting a little smaller...\n\n... Your head shoots up!\n\n YES, YES, YESSSSS!!!!!\n\n YOU'RE BACK TO YOUR NORMAL SIZE!🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You feel so happy for about 5 minutes!\n\n{style(3)} Guess I better continue studying for my exams!{style(0)}, you thought.{fore(9)} That's when you feel the same tingling sensation when you were growing (and shrinking)...\n\n'WHOAH!', you feel your head quickly hit the ceiling of your house!{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"'What the f**k is happening?', you question. Your voice comes out like a giant, in more of a loud and booming voice! In fact, you're now a giant!\n\n'Great! What would the public think of me NOW?! I'm Godzilla or some sort of alien?!?! 👽'\n\n{fore(9)} Suddenly, you hear a crashing sound, as you continue to grow! You're growing so quickly that you accidentally destroy your house!\n\n Congratulations on being homeless my friend!{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'I guess I must be 9-12 ft tall by now!', you mutter. That's when you hear your next-door neighbor, screaming, 'AAAAAAAAAAUUUUUGGGGGHHHH! IT'S A ALIEN! SOMEONE CALL JYOTI GONDEK!(The Mayor of Calgary) PLEASE CALL THE POLICE AND RUN FOR YOUR LIVES!'.\n\n 'No, wait! I'm not an alien! I'm your next door neighbor!', you boom.\n\n'Oh, man.... its happening again!', you think to yourself as you get bigger and bigger quicker by the minute!\n\n'I shouldn't have overdosed the antidote!', you think...\n\n BUT, ITS TOO LATE!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "After 30 seconds, you became so big that you rise into the depths of space, crushing the International Space Station.\n\n Your shoe also, by mistake, hits 🌎 so hard, that it explodes into bits.\n\n You get even more bigger after that! Since you're in space without protection, you fall unconscious...\n\n Your lifeless giant body exits the Milky Way, therefore destroying all humanity, and starting a second Big Bang!\n\n You eventually suffocate and explode to bits, therefore killing you....\n\n",
            userStrDelay,
        )  # The funniest death I'd ever written, LOL --@TG101
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    elif drinkOption == 2:
        os.system("clear")
        printt(
            "Opening the corkscrew, you take in 2 more drops of the antidote.... And wait....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(2)} That's when you feel your body aching.....\n\n.... And expanding!\n\n Is the antidote working....?\n\n IT IS!\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"After a few seconds, you feel like you're finally back to normal size!\n\n You pick up a nearby vase. It felt so good in your hands! Everything is the right size.... The world is the right size again!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Okay, what was the moral of the story?\n\n - Don't be stupid and read instructions properly\n\n - Size matters, duh!\n\n - Life is a gift. Even though you were on the verge of death, you still survived....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(f"Now, should we celebrate?\n\n", userStrDelay)
        time.sleep(0.5)
        printt(fore(2) + "🎉 THE END 🎉" + style(0), userStrDelay)
        quit(0)
    else:
        pass


def closeToHome():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    os.system("clear")
    printt(
        "Over time, the sky turned from a bluish, cloudy afternoon, to a deep, night purple. As you and Barry fly, winds continue to howl.\n\n But, that didn't matter. You are determined to end the situation that you're currently in!\n\n It's been about 4-5 hours since you got that on that bee, and its about a day, since you accidentally shrank back at home.\n\n'I can do this!', you think to yourself. 'I'm only a few blocks from home!'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(1)}Suddenly, you find yourself slipping off of Barry the bee!\n\n{style(0)} 'No!'. You let out a weak cry, and start to fall! Barry continues flying, leaving you behind...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"{fore(1)}Ok, you're so gonna die now, right?!{style(0)}\n\n {fore(2)}Luckily, you don't.{style(0)}\n\n Even though you landed on the hard cement pavement, you're actually fine, since you're 200 times shorter.\n\n Standing up, you ask a question to yourself:{fore(9)} Have I became more smaller at the moment?{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(1)}Turns out you are now!{style(0)}\n\n The pavement spread out like a football field, from your POV!\n\n 'Great, I must be about the size of a speck of dust!', you murmur.\n\n Truth be told, you're 1/8 of an inch tall now...\n\n Which doesn't seem like bad news at all,{fore(2)} since you have the {fore(4)} antidote {fore(2)}with you!{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(3)}But, where's Barry?{style(0)}\n\n 'BARRY!',you call out for the bee.{fore(1)} No response.\n\n OH-NO..... What even happened to him?!{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Go look for the bee", userStrDelay)
    printt("2. Don't mind about him, just go home!", userStrDelay)
    print("Do you care for your bug companion or not?\n Seriously.... think wisely!")
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            "You decide to look for Barry.\n\n Man, getting across the street would take AGES! But, you don't even care about that! You start to run at a fast pace.\n\n That's when you hear voices in the distance....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You turn around and gasp!\n\n{fore(1)} Two gigantic people on gigantic bikes are pedalling towards you! \n\n NOW WHAT?!{style(0)}\n\n There's no way that you can outrun it... Oh wait, actually you can....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "The answer is.....\n\n RUN FOR YOUR FRICKIN' LIFE!🏃‍♂️👟\n\nWhich you do anyway....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "The bike tire comes closer and closer.... AND CLOSER!\n\n Could you make it?!\n\n COULD YOU MAKE IT?!?!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(2)} AND YOU DID! YOU FINALLY OUTRAN THAT BIKE STAMPEDE!{style(0)}\n\n Now, ya gotta look for Barry. You're close to the house!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "You continue to call out the bee's name.\n\n After a few minutes, you see Barry lying on the ground.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"'Barry! You OK?', you ask, rushing to his side.\n\n Turns out the bee is actually A-OK, so that's good!\n\n Soon, you then fly to your doorstep, and with all your strength, attempt to open the pet door.\n\n{fore(1)}...Unfortunately, you actually can't...\n\n You're stuck outside!\n\n{style(0)}\n\n You're going to have to find a way to get in!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(2)}Wait a second....\n\n You're about 0.32 cm, so that means its easy to slip in the door!{style(0)} But, what about Barry? Guess you have to leave your companion behind....\n\n'Goodbye Barry...', you say, shedding a tear.\n\n 'It was nice knowing you...'\n\n Barry flies away after you say goodbye.....\n\n",
            userStrDelay,
        )
        storyLocation = "29"
        saveGame()
        endGame2()
    elif decision == 2:
        os.system("clear")
        printt(
            "Wow, what a bad person you are!\n\n You don't even care about your 🐝 buddy! You start to run at a fast pace.\n\n And, all of a sudden.... you feel more strange!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "I guess you're getting more smaller.... right?\n\n RIGHT?!?!\n\n As you run, everything around you is rising on both sides, slowly...and slowly...\n\n ... the ground is being more spread out than ever.\n\n\n You start to feel extremely cold 🥶, as you're getting more smaller (more small = more larger surface area, which means more loss of body heat... unless you eat something!) by every hour, minute, and second...\n\n You're astonished by how extremely tiny you are.\n\n\n A single blade of grass is equivalent to the size of an oak tree!\n\n You get dizzy from just seeing it and assume you might be dreaming...\n\n But you're not dreaming. You're about 2mm  tall now!\n\n 'Man, WHEN WILL IT END?!?', you ponder in fear...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\nYou stop running by the moment you reach the front walkway of your house, and lie down in the middle of the pavement. You can't take the pain anymore, as your whole body is tightening, physically contracting in size.\n Your teeth are constantly chattering as your body temperature drops faster and faster as you continue to shrink...\n Your heart's BPM is rising fast!\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\nThat's when you have to make a very difficult choice: Accept your inevitable fate or deny it....\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n You then deny the fact that you're going sub-atomic for a few minutes, but as you attempt to hug yourself tightly, to prevent from freezing to death, you realize that...\n It's too late...\n\n"
            + fore(11)
            + "You will never be back to your normal size EVER AGAIN..."
            + style(0),
            userStrDelay,
        )
        time.sleep(1)
        printt(
            "\nLooking up at the sky, you fear that nobody will find a single trace of you -- AT ALL! You're still shrinking....\n Going....\n\n...... Going.......\n.... going ....\n going.....\n\n\n\n ....going.....\n....going!....\n\n\n....What a world.... What a wonderful world..... What a wonderful world.....\n\n... what a wonderful world.....\n\n what a world....\n\n what a wonderful, beautiful world....",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n\nAfter several minutes, you see the sky has disappeared. You're now the size of an atom, and you are now close to death. Even though you know that you really don't exist in this world right now, you know one thing for sure...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'To God, I am no zero. But I still exist', you say out loud as you breathe your last breath.... or is it really your last breath?\n\n.....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(4) + "⚛️ THE END? ⚛️" + style(0), userStrDelay)
        quit(0)
    else:
        pass


def journeyHome():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    os.system("clear")
    printt("Alright....\n\n", userStrDelay)
    question = rf"""{fore(11)}
          _______
|\     /|(  ___  )|\     /|
| )   ( || (   ) || )   ( |
| (___) || |   | || | _ | |
|  ___  || |   | || |( )| |
| (   ) || |   | || || || |
| )   ( || (___) || () () |
|/     \|(_______)(_______)

          _______           _        ______
|\     /|(  ___  )|\     /|( \      (  __  \
| )   ( || (   ) || )   ( || (      | (  \  )
| | _ | || |   | || |   | || |      | |   ) |
| |( )| || |   | || |   | || |      | |   | |
| || || || |   | || |   | || |      | |   ) |
| () () || (___) || (___) || (____/\| (__/  )
(_______)(_______)(_______)(_______/(______/

          _______
|\     /|(  ___  )|\     /|
( \   / )| (   ) || )   ( |
 \ (_) / | |   | || |   | |
  \   /  | |   | || |   | |
   ) (   | |   | || |   | |
   | |   | (___) || (___) |
   \_/   (_______)(_______)

 _______  _______ _________
(  ____ \(  ____ \\__   __/
| (    \/| (    \/   ) (
| |      | (__       | |
| | ____ |  __)      | |
| | \_  )| (         | |
| (___) || (____/\   | |
(_______)(_______/   )_(

          _______  _______  _______   _____   _
|\     /|(  ___  )(       )(  ____ \ / ___ \ ( )
| )   ( || (   ) || () () || (    \/( (   ) )| |
| (___) || |   | || || || || (__     \/  / / | |
|  ___  || |   | || |(_)| ||  __)       ( (  | |
| (   ) || |   | || |   | || (          | |  (_)
| )   ( || (___) || )   ( || (____/\    (_)   _
|/     \|(_______)|/     \|(_______/     _   (_)
                                        (_)
{style(0)}    """
    time.sleep(0.5)
    print(question)
    time.sleep(0.5)
    os.system("clear")
    printt(
        "'That's it! I could ride on an insect.... If it NOT SEES ME AS A THREAT....', you exclaim.\n\n But, where would find an insect with wings?!\n\n Also, where are you now?!?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You then see a flower in the distance, which rose up like a oak tree!\n\n",
        userStrDelay,
    )
    flower = r"""
      .--.
    .'_\/_'.
    '. /\ .'
      "||"
       || /\
    /\ ||//\)
   (/\\||/
______\||/_______

    """
    time.sleep(0.5)
    print(flower)
    time.sleep(0.5)
    printt(
        "Could you climb up that flower?\n\n You have to try!\n\n Rushing to the flower, you leap onto the first leaf, then the second one.\n\n You then try to grasp onto its petal, but its high above you!\n\n Understanding that you have to climb onto its long, thin stalk, you then move to action....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "After 5 seconds, you finally made it to the top of the flower!\n\n You then walk on the flower.🌸 Pollen covers your shoes as soon as you step into it!\n\n Wait....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(1)
        + "Aren't you allergic to pollen?\n\n"
        + style(0)
        + "'Pfft', you shrug it off. 'I'm too small to breathe it in!'\n\n Karma dawns on you within nanoseconds as you sneeze from the pollen.😂\n\n Okay, should I stop mocking you? 'Kay.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "'Alright, concentrate! Focus on getting home and being my regular self again...', you then say. Looking around, you find out that you have not traveled far from "
        + bestFriend
        + "'s deck.\n\n You have to make it home in a pinch! But, based on what you realize, walking is not better than riding....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(1)}Suddenly, you hear a buzzing sound..... That's getting louder and louder by the moment!\n\n A helicopter? Nope! It's even worse (or not...)!--{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "It's a bee!🐝 A bee the size of a helicopter!\n\n You then see it hovering above you!\n\n 'NOOOOOO!', you scream....\n\n But, its too late!\n\n Its smol feet, which felt like small darts piercing your skin, lifts you up in the air!\n\n The bee then flies away with you, away from "
        + bestFriend
        + "'s backyard!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'HEY!', you call out to the bee.'That's NOT how I want my ride home! Let me get on you, please!'\n\n{fore(6)} But, that's when you remember that you were covered in pollen.\n\n It must've snatched you by accident!{style(0)}{fore(1)} What if its taking to its hive?{style(0)}\n\n Maybe that could be a good thing, since you'll get nice hospitality there-- \n\n {fore(1)}Wait, what about the Queen Bee?! What will the bee colony do to you anyway?!{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"No time. You have to get on that bee. And, I mean on its back!\n\n 'Hey! Listen to me! DROP ME NOW!', you plead. The bee looks down at you, trying to understand you.\n\n It then descends fast, and then drops you. You then fall like a rock being dropped from a high place, and hit the grass with a THUD.\n\n The {fore(0)}black{style(0)} and {fore(3)}yellow{style(0)} insect sets down its wings and comes to you.\n\n Getting up, you stare into the bee's eyes.\n\n 'Do you trust me?', you say, lending an outstretched hand. 'I need you! I have to get home! Will you please allow me a ride?'\n\n The bee turns around, which means it has accepted your offer!\n\n 'Yes! Thank you so much!' You then hop on the bee's furry back.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Alright, what should I name you in order to celebrate?', you ask, as the bee starts to take off. 'Aha! I got it! I'll name you Barry Benson!', you say happily.\n\n Holding tight, you think to yourself on what happens now? You finally hitched a ride on a bee, but how would you get directions on getting home? You left your 📱 back there, so accessing the GPS and Maps can never be done!\n\n Wait--\n\n Luckily, you have an Apple Watch! You can actually use it to get directions!\n\n Which you do anyway, despite the fact that you're wasting your data....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    storyLocation = "28"
    saveGame()
    closeToHome()


def foundAntidote():
    global userStrDelay, storyLocation, numDeaths, bestFriend
    os.system("clear")
    printt(f"{fore(4)}--2 Hours Later --\n\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt(
        f"The rain stops....\n\n{fore(2)} That means you can crawl out of this hole and escape this backyard!{style(0)}\n\n Getting up, you use your strength to climb out of this hole and run.... again!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Then, you bump into something.... something hard!\n\n But, what is it? You feel the object. Must be a glass bottle....\n\n No, wait....\n\n You examine the structure again.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'Hang on a minute, I think I'd seen this before...', you say. Could it be? The fat-burner drink that started it all?\n\n It looks like it!\n\n But, the contents in the bottle aren't clear. They're {fore(4)} blue.... {style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    antidote = f"""
                                        mmm
    {fore(4)}                           )-(
                                       (   )
                                       |   |
                                       |   |
                                       |___|{style(0)}
    """
    os.system("clear")
    time.sleep(0.5)
    print(antidote)
    time.sleep(0.5)
    printt(
        "You couldn't believe it! The antidote is right in front of you!\n\n But, there's a problem....\n\n How you would pick it up. It's waaaayyyy too heavy!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Could you use some kind of rope, to pull it on the way home?\n\n No.... That would tire your arm muscles!\n\n That's when you see the once building-sized bottle has been reduced to the size of the same small medicine bottle you saw earlier!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Weird, why did it shrink?', you wonder. But, you don't mind what size it is. It had just made your life even easier!\n\n Rushing to the bottle, you pick it up and store it in your pant pocket.\n\n You better go home first, then you should at least get back to normal size! (A questionable choice, actually.... according to you guys....[My humble followers on Replit])\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    storyLocation = "27"
    saveGame()
    journeyHome()


def plotPointSix():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    os.system("clear")
    printt(
        f"{fore(3)} You continue to run across the backyard. How long have you ran? For hours? And, how many miles?{style(0)}\n\n You then stop running to get some rest.{fore(1)} Your mouth is sooooo dry, and you really need water! 💦{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(15)}That's when you hear the sound of thunder!⛈️\n\n{fore(2)} Is it a good thing....{style(0)} or a {fore(1)}bad thing, because of your tiny size?{style(0)}\n\n In fact, maybe you could get water.... from the rain 💧s?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Suddenly, a rain droplet, equivalent to the size of a car drops to the ground next to you. Its impact, as it hits the dirt, sends you flying with enough force.\n\n Yeah, that's the drawback right there! You're the size of an insect, and swimming in water would be a lot harder due to its viscosity.\n\n In other words....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    drownMessage = rf"""{fore(6)}
__   _______ _   _ _______ _____
\ \ / /  _  | | | ( ) ___ \  ___|
 \ V /| | | | | | |/| |_/ / |__
  \ / | | | | | | | |    /|  __|
  | | \ \_/ / |_| | | |\ \| |___
  \_/  \___/ \___/  \_| \_\____/


 _____ _____ _   _  _   _   ___
|  __ \  _  | \ | || \ | | / _ \
| |  \/ | | |  \| ||  \| |/ /_\ \
| | __| | | | . ` || . ` ||  _  |
| |_\ \ \_/ / |\  || |\  || | | |
 \____/\___/\_| \_/\_| \_/\_| |_/


____________ _____  _    _ _   _ _
|  _  \ ___ \  _  || |  | | \ | | |
| | | | |_/ / | | || |  | |  \| | |
| | | |    /| | | || |/\| | . ` | |
| |/ /| |\ \\ \_/ /\  /\  / |\  |_|
|___/ \_| \_|\___/  \/  \/\_| \_(_)

{style(0)}"""
    os.system("clear")
    time.sleep(0.5)
    print(drownMessage)
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"{fore(6)} That is, if you react fast enough! Otherwise, you have to take shelter...{style(0)}\n\n You then start running again, as the water droplets continue falling. Its like escaping from typhoons that fall from the sky instead of being underwater!\n\n Since you're a lot more smaller, you're actually pretty fast (If you watched the Vsauce3 video, you'd understood why), which is the only advantage being shrunk...?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        fore(3)
        + "Alright.... where would you take cover? WHERE?!"
        + style(0)
        + "\n\n You then see a hole in the distance. Maybe you could take shelter from those bomb-like(or hurricane like?) rain drops. Another water droplet sends you flying! You then skid on your stomach, and sure enough, fall into the hole itself!\n\n Yaaay?",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'Unngh!'\n\n Your back slams onto the bottom of the hole. Weak from the pain, you slowly roll over, eventually avoiding the chances of drowning a horrible watery death.{fore(11)} Nightmare fuel, isn't it?!\n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Staying where you are,{fore(2)} you realize that you can collect smaller water droplets, enough for you to drink!{style(0)} You then take large scoops of water and slurp it madly like a greedy dog.\n\n{style(3)}I've gotta stay in here, until the rain stops...{style(0)}, you thought. You sit inside the damp hole, waiting.....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    storyLocation = "26"
    saveGame()
    foundAntidote()


def encounterThree():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    os.system("clear")
    printt(
        "Your stomach loudly growls after 20 minutes of running. I guess you're hungry...?😋\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(3)}But, what would you eat?{style(0)}\n\n You come to a stop and look at what's around you. Unfortunately, there's nothing that you could chew on!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "A somewhat 'stupid' idea comes to your mind. Could you bite off a single blade of grass? At least you could try....\n\n You look at the nearest grass blade, and walk towards it. Kneeling down, you hold the damp palm-tree like structure, and with your teeth, you make a small incision.\n\n 'OWW!'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Yep. Chomping on some grass (which are the size of trees) when you're 0.635 cm (Yep, THAT SMALL) is a really really {fore(1)} BAD IDEA....{style(0)}\n Ya better go touch grass now! (🔥🔥🔥 😎 Epic Roast Ever 😎 🔥🔥🔥)\n\n You shrug off the idea of eating grass blades, and decide to search for something that your tiny teeth can actually eat...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "After trekking across "
        + bestFriend
        + "'s yard (Or, the first section of her yard, which consisted of the deck), you step into the blinding sunlight. Your eyes widen in disbelief at how extremely tiny you are.\n\n Flowers tower over you like trees, and everyday objects, like a baseball ⚾ are the size of urban buildings!\n\n It's like stepping into another world, or another universe?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "However, you're not sure if you can make it home, due to the fact that you're in a hostile environment, but at least you have to try!\n\n Taking a deep breath, you sprint across the forest-like backyard, searching for food and water.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "After several minutes, something huge, round and circular catches your eye. You stop and decide to check on what's there.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'I've died and I've gone to heaven!', you think to yourself, with your mouth watering.😋\n\n{fore(2)} What you're seeing now, is a giant Oreo cookie!\n\n Its big enough to eat at your heart's content! Turns out there are actual benefits being the size of an insect?!{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"You rush to the enormous cookie, and quickly indulge in the cream laced around it.{fore(2)} Mmmmm-- So good!{style(0)}\n\n You also take apart small crumbs of the Oreo, and dip in the sugary cream, as happy as ever.\n\n{fore(1)} You're so busy eating, when you suddenly hear a tapping sound from above!--{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You then stop eating and look up.\n\n 'OH MY GOD!'\n\n You feel your jaw drop wide open, as you're seeing a giant ladybug 🐞, perched onto the Oreo!\n\n 'Hi,', you say to the ladybug, and then offer a piece of the cookie. 'Want a bite?'\n\n The ladybug is still staring down at you.\n\n'Oooook, you don't want it, right?', you say in a low, soft voice.",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"\n\n'Then, I'll slowly back away....slowly.....'\n\n You step backwards, leaving the ladybug some space.\n\n The ladybug then spreads its wings and dives straight at you within seconds! 'HEY, WHA-'\n\n You're then thrown backwards by a few centimeters. 'Hey! What was that for? You hungry?', you question the insect. The ladybug scuttles towards you, looking at you....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"Hold on a sec.....\n\n{fore(1)} WHAT IF THE LADYBUG WAS HUNGRY NOT FOR THE OREO....\n\n .... But for you?!{style(0)}\n\n Your assumption is actually correct, as the 🐞 charges towards you with a running start and pushes you-- HARD!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'H-Hey! Stop pushing me! STOP!' You protest.\n\n Leaning on one side, you immediately push back, covering its eyes (if ladybugs do have eyes, I don't know if they do....), and move forwards. Its like pushing a huge rock, but that rock is alive!\n\n The ladybug reacts quickly, and pushes you more harder, which sends you flying!\n\n'WAAAAAAAAAHHHHHH!'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You hit the soft dirt with a hard *WHUMP*\n\n Realizing that you have to escape from that ladybug's grasp, you shoot your arms and try to crawl to safety...\n\n Too late. The bulldozer-sized insect comes to you again.\n\n 'Look, I'm sorry--', you plead.\n\n But, now.... You're helpless....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(f"{fore(3)} Or... Are you? {style(0)}\n\n Better find out!", userStrDelay)
    time.sleep(0.5)
    printt("1. Run", userStrDelay)
    printt("2. Try to ride on it (The ladybug, you confused?)", userStrDelay)
    printt("3. Give it the Oreo crumb", userStrDelay)
    print("What do you do? Think fast....")
    decision = int(fkey.getchars(chars=["1", "2", "3"]))
    if decision == 1:
        os.system("clear")
        printt(
            f"You get up and make a run for it!\n\n{fore(1)} The ladybug follows you after!{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"\n\n As you continue to run for your life, you suddenly hear a deafening STOMP! And a squawk!\n\n You then look up, and see that a giant bird 🦅 is coming! But... for WHO?\n\n 'SCREEEEEEAAAAWWWWKKKK!'\n\n The big bird swoops down and hits the ground with a hard THUD.\n\n Your tiny feet bounce on the dirt.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"{fore(1)} You realized that you might be lunch for that giant bird, that is, if you don't react fast enough!\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{style(3)}I have to hide!{style(0)}, you thought.{fore(3)} But where would you hide?{style(0)}\n\n You then see a small rock near you. Likely a good place to hide...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("Quickly dashing away, you dive next to the rock.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "Crawling on your knees, you rest your head on the rock (which is the size of a bush!).\n\n Lying down on the ground, you try not to make a sound.\n\n Any moment, the bird will mistake you for an actual insect, and you'd be dead!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You're not sure if you're going to get lucky by not being seen from that humongous bird (or the ladybug), but you're going to get lucky.\n\n You then hear a CRUNCHING sound next to you! It seems like the bird is eating the ladybug that you encountered earlier!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'Oh god, please don't let it notice me, please don't let it notice me.....!', you ponder in fear...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "You then hear another deafening squawk from that same bird....\n\n... Then the flapping of the wings...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"And.... pure silence....\n\n{fore(2)} Seems like the bird is gone now! 😮‍💨 You're safe now! {style(0)}\n\n You then get up and continue to run, hoping to find at least some water....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        storyLocation = "25"
        saveGame()
        plotPointSix()
    elif decision == 2:
        os.system("clear")
        printt(
            "You go towards the ladybug, and place your hand onto its lobster-like body.\n\n 'Hey... It's OK. Shhhhh...', you say, and the ladybug turns around unfortunately, and starts to eat you alive.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()

    elif decision == 3:
        os.system("clear")
        printt(
            "Shakily, you slowly give the ladybug the Oreo crumb.\n\n It stares at it, twitching its legs.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(2)} And, what a surprise! It actually takes it!{style(0)}\n\n The ladybug then leaves you alone!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You then get up and continue to run, hoping to find at least some water....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        storyLocation = "25"
        saveGame()
        plotPointSix()
    else:
        pass


def backYard():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    os.system("clear")
    printt(fore(1) + "Aw, great.... " + style(0), userStrDelay)
    time.sleep(0.5)
    printt(
        fore(1) + "You're still shrinking, right?" +
        style(0) + "\n\n\n\n RIGHT?!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{style(3)}How short am I now?{style(0)}, you wonder.\n\n You then rush back into the bathroom, hoping to find a scale that you could step on.... hopefully....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "You finally see a scale within your reach, but running towards it must've taken ages! Your feet are paining even more as you run.\n\n As you reach the scale, your eyes bulge in astonishment (by how small you are of course!)...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(9)
        + f"It's impossible to get onto the scale and weigh yourself now!\n\n Seems like you're more smaller than an ant....\n\n.... About 1/4 of an inch to be exact?\n\n Likely....\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"This is so NOT GOOD. How can you make your plight to everybody when you're smaller than a penny?🪙\n\n 'It's no use...', you thought. 'I have to get back home. I'll try to redo this again. Think properly....'\n\n You then start to run out of the bathroom, looking for the back door. {fore(1)}You think that maybe it's too late.....\n\n You're going to continue to get smaller and smaller until you die.....\n\n You'll no longer exist in this world anymore! 😱\n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"But, IS IT REALLY OVER?!\n\n You so cannot give up like this!\n\n Anyway, shall we go back to the exposition?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        "You look for a way to exit the house, so you can rethink your choices again once you arrive home.\n\n You gaze up at the back door. How would you open it?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"You look at the door-knob. Yep, there's NO way that you could open the door. That would mean turning the knob ABOVE the doorknob....\n\n Along with a pretty painful experience....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Aha!\n\n Why not the crack under the door? Since you're the size of an insect now....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "You run to the back door as fast as you can. Could you fit in there?\n\n That's the question!",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You then walk slowly to the crack of the door. Drum roll please......\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    drumRollFont = r"""
 __  __               ___    __  ____ __  __
 \ \/ /__  __ __  ___/ (_)__/ / / _(_) /_/ /
  \  / _ \/ // / / _  / / _  / / _/ / __/_/
  /_/\___/\_,_/  \_,_/_/\_,_/ /_//_/\__(_)
                                            """
    print(drumRollFont)
    time.sleep(0.5)
    os.system("clear")
    printt(
        "But, there's another hurdle-- Getting off the platform, and dropping onto the wooden deck....\n\n How would you pass that?!?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Could you lower yourself, slowly?.....\n\n Or just drop down?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Lower yourself", userStrDelay)
    printt("2. Just jump!", userStrDelay)
    print("Honestly, this costs your life....\n")
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            "You turn around, and slowly crouch down.\n\n You then dangle one foot in the air, grasping the metal platform.\n\n You also do the same with the other one.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"Now, you're holding on for dear life!\n\n You look down and start to shudder....\n\n{fore(1)} What a big drop you're seeing!\n\n There's no way that you would survive!{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("The only option left, is.....\n\n..... to let go.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"{fore(3)}But, SHOULD YOU EVEN DO IT?!{style(0)}\n\n Your hands are in tremendous pain, though....\n\n'Can't even hold on anymore', you think in vain.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1)
            + "All of a sudden, you lose your grip and fall!\n\n 'AAAAAAAAAAAAAAHHHHHHHHHHH!'\n\n Great.... you're going to die!"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"{fore(2)}And......\n\n....you don't?{style(0)}\n\n You hit the deck with your knees and then your stomach. That must've hurt - A LOT!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Lying down, you roll up your pant legs. Blood is dripping down from your knees, then to your calves!\n\n Seems like you scraped your knees! Gotta wrap a 🩹 on that, right?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "But, where would you find a bandage?\n\n No, wait. Scrap that. A regular bandage won't even fit your small knees! 'Don't worry, the cut will heal itself', you say out loud.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You then start to walk. Not knowing where you're going (and what you're stepping on), your foot touches air, and you fall..... {fore(1)}AGAIN!{style(0)}\n\n (You must be a fan of Tom Petty, LOL. Get it? Since you're '🎵freeeee.....\n\n Free-Falling.....🎵'😂)",
            userStrDelay,
        )
        os.system("clear")
        printt(
            "Luckily, your death-defying fall quickly ends, as you land on a blade of glass (which is as large as a playground slide, from your POV!), and slide down (Wheeeeee?)\n\n You tumble downwards and land in the soft dirt.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Okay.... where are you now?\n\n Getting up and looking around, you realize that you're under "
            + bestFriend
            + "'s deck in her backyard.\n\n The ambience now is like being in a dimly lit forest.\n\n ",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You look ahead, and find out that you have a long way to go!\n\n"
            + bestFriend
            + "'s backyard stretched around a mile! You could likely get lost easily!\n\n'Alright, here goes nothing', you thought as you start to run, exploring your surroundings, and hoping to get out of here before you shrink to nothing...\n\n",
            userStrDelay,
        )
        storyLocation = "24"
        saveGame()
        encounterThree()
    elif decision == 2:
        os.system("clear")
        printt("You take the mighty leap....\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "... and eventually die of stupidity and idiocy as you hit the hard, wooden deck.\n\n",
            userStrDelay,
        )
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()


def sockPlot():
    global userStrDelay, numDeaths, storyLocation, bestFriend
    os.system("clear")
    printt(
        fore(1)
        + "The whole room falls dead silent, as you wake up. Is there someone there? Or, are you all alone?\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You're still inside the sock, though. But, WHERE IS EVERYBODY?!\n\n You try to get up, but since you're 100 times smaller, the soft fabric ALSO feels 100 times heavier! Is it possible or impossible to move now?!?!\n\n You still feel cold , but not as intense like before.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Hello?', you croak. 'Is there somebody that can help me?'. No answer.\n\n You try to shout again, but much more louder:\n\n 'HELP ME! I'M TRAPPED IN THIS SOCK! PLEASE! HELLO?! HELLLLLPPPPPPP!'\n\n Your voice comes out extremely tiny, faint, and muffled. Once again, no-one responds back. 'Am I going to be stuck in a sock for the rest of my life?!', you think. The question is: Are you really doomed?! Maybe....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(3)
        + "But...\n\n How would you grow back to normal size?"
        + style(0)
        + "\n\n You have to start moving, but could you even move?\n\n Pale light poured from the mouth of the sock. You then slowly start to crawl towards the opening. The fabric of the sock acts like a huge burden on your shoulders as you try to push forward.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Secondly, the interior of the sock is spacious, as per your size. It's like finding your way out through a dark cave...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "'Unghh', you moan as you continue to crawl. This will take forever, just to get out of this sock! But, you're too tired, and weak.\n\n And then you hear a sound....\n\n WHAT WAS THAT?! SOMEONE'S THERE! Or... Something else?\n\n 'HEEEEYYYYY!', you start to shout. 'I'M IN HERE!'\n\n Nothing happens.\n\n That's when you fear that a real person might not be around! You immediately crawl back in the sock, and decide to stay still.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(1)}That's when you hear the sound... AGAIN!{style(0)}\n\n You still stay where you are, shivering. You're too scared to look, but you decide to anyway (to make sure the coast is clear of course!)",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You squint in the dark, and your jaw drops in horror. What did you just see that made you scared?! Is it: \n\n",
        userStrDelay,
    )
    printt("1. A giant snake", userStrDelay)
    printt("2." + bestFriend + "'s cat", userStrDelay)
    printt("3. Another spider", userStrDelay)
    printt("4. There's NOTHING there!", userStrDelay)
    print("Seriously, what did you see?")
    decision = int(fkey.getchars(chars=["1", "2", "3", "4"]))
    if decision == 1:
        os.system("clear")
        printt(
            f"{fore(1)} It's a snake alright!🐍 (How many pets does your best friend have already?!){style(0)}\n\n{fore(2)} But, it slithers past you....\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(2)} How lucky you are! You breath a sigh of relief.{style(0)} That's when you accidentally sneeze!\n\n{fore(1)} AND THE SNAKE STOPS MOVING.....\n\n Within a split second, the snake's eyes fixate on you!\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"'OH GOD NOOOOOO!'\n\n You let out a scream as the snake charges toward you! YOU HAVE TO GET OUT HERE-- FAST! \n\n Maybe you could poke a hole in the sock. Or, maybe there was a hole in the sock already?\n\n You start to roll over quickly, as the snake's head barely misses you.\n\n{fore(1)} You're fighting for your life now....\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            fore(2)
            + "At last, you see your escape route! There was a small hole in the sock. A hole that you can fit in!\n\n"
            + style(0)
            + "The snake turns it head to capture its prey, and then you swiftly exit the sock and start to run. Looking back, you see that the snake is trapped inside the sock."
            + fore(2)
            + " SUCCESS!"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Now, you gotta get help. But where?\n\n You quickly realize that getting attention is pointless, and that's when you decide to go home....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"That's when you hear a tearing sound. And a 'Sssss'....\n\n {fore(1)} The snake's still not done with you!\n\n YOU MUST RUN!{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "'Shoo! Go away!', you cry as you wheel around by the moment the snake catches up to you, with its pink tongue visible.\n\n The snake's the size of a train!\n\n Crawling on the floor, you try to shield yourself from the snake. 'Please... GO AWAY! DON'T EAT ME!'\n\n Talking to it will not work, so you run like the wind.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(
            f"The snake follows you... to the bathroom. You constantly trip over the thick carpet, which ran up to your thighs and scratched them a lot!\n\n Now, where do you have to hide?\n\n You're cornered now, and you have no way to go!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("1. Fight the snake", userStrDelay)
        printt("2. Surrender", userStrDelay)
        printt("3. Hide", userStrDelay)
        print(f"{fore(3)}WHAT DO YOU DO NOW?!{style(0)}")
        choice = int(fkey.getchars(chars=["1", "2", "3"]))
        if choice == 1:
            os.system("clear")
            printt(
                "You look around for a weapon in order to defend yourself from the large snake. Unfortunately, there isn't one....\n\n Seems like you have to use your fists, your weak and smol fists.\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt("The snake lunges at you and mauls you to death.", userStrDelay)
            time.sleep(0.5)
            printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
            numDeaths += 1
            saveGame()
            playAgain()
        elif choice == 2:
            os.system("clear")
            printt(
                "'Alright, just eat me! I give up!'\n\n You say to the snake. \n\n 'I'm fresh meat, Snakey. Freeessssshhhhh meaaaaattttt.....'\n\n The snake still has its tongue out, and is still staring at you with its black beady eyes.\n\n You shut your eyes, waiting for the grotesque death that'll eventually come......\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                f"{fore(2)}..... But, it doesn't even happen.{style(0)} 'Huh? Why you don't want me?', you ask. The snake just slithers away from you. Maybe, it recognized your voice or some sort. It must've had a good memory, LOL.\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Alright, you got to focus on getting back to normal. You start to walk out of the bathroom, but you stop short of another tingling sensation.....",
                userStrDelay,
            )
            storyLocation = "23"
            saveGame()
            backYard()
        elif choice == 3:
            os.system("clear")
            printt(
                "You spot a trashcan in the distance. Maybe you could hide here...\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "With the snake only a few cm from you, you Naruto-run to your desired hiding spot.\n\n And, the snake slowly slithers after you!\n\n Once you finally made it, you keep your back against the edges of the trash-can and hold still....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                fore(9)
                + "Did the snake catch up?"
                + style(0)
                + "\n\n You peep around the corner, and pump your fist in joy.\n\n"
                + fore(2)
                + " It is gone!\n\n"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Alright, you got to focus on getting back to normal. You start to walk out of the bathroom, but you stop short of another tingling sensation.....",
                userStrDelay,
            )
            storyLocation = "23"
            saveGame()
            backYard()
        else:
            pass
    elif decision == 2:
        os.system("clear")
        printt(
            fore(1)
            + "Ah, sh*t, here we go again (Is that a GTA reference?)....\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'Meoooowwwwww'\n\n You hear the cat meow....\n\n You then pray that it'll not notice you.\n\n 'Don't make a sound-- AT ALL!', you murmur silently.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Luckily, "
            + bestFriend
            + "'s cat doesn't notice you! Does that mean you can escape?\n\n Possibly....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You then dash out of the sock, and run... for your life!\n\n Then you hear a loud purr....\n\n Unfortunately, you also don't see the towering paw over your head.... and its too late...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("*SMACK!*\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "You are squashed to death by your friend's cat....\n\n How stupid you are!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    elif decision == 3:
        os.system("clear")
        printt(
            fore(1)
            + "Unlike the spider that you'd encountered earlier back at home, this spider is a poisonous black widow....\n\n Worse than that, since you're 1.27 cm, the spider's only 1X larger than you!\n\n"
            + style(0),
            userStrDelay,
        )
        os.system("clear")
        spider = rf"""

        {fore(0)}
                  _.._
                .'    '.
               /   __   \
            ,  |   ><   |  ,
           . \  \      /  / .
            \_'--`(  )'--'_/
              .--'/()\'--.
             /  /` '' `\  \
               |        |
                \      /
        {style(0)}        """
        time.sleep(0.5)
        print(spider)
        time.sleep(0.5)
        printt(
            f"And now its going towards you, along with the advantage (or disadvantage?) of its speed being faster!\n\n{fore(1)} It then quickly goes into the sock and leaps onto your body....\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"'GUHHHHHHHH!'\n\n The black widow attempts to stab you with its sharp thick legs. You quickly dodge them, even though it only takes milliseconds for you to react!\n\n 'GET AWAY FROM ME!', you scream at the spider. It does not let you go however, and it just stares at you, silently.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(3)
            + "You have get out of the sock, first!\n\n But, how would you protect yourself from that spider?!\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(f"You need a weapon....\n\n Something sharp.....\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "As you're thinking about how to fight the arachnid, the spider lures you in with its gaping jaws.\n\n 'NOOOOOOOOOO!'\n You raise your hands to push the hulking black widow away, and by doing so, its drool sticks to your hands!\n\n Gross....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'Ew. Do you also drool like that in your sleep?', you say out loud. The spider is now towering over you with its body bobbing up and down!\n\n And, you see that you can easily escape from its grasp by sliding under its body. But, what if it sees you?\n\n You have no choice but to do it anyway.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"With a running start, you quickly crawl underneath the spider, and start to run for your life....\n\n Sure enough, the spider chases you!\n\n {fore(3)}YOU HAVE TO KILL IT, FAST!{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You stop to catch your breath. That's when you see a sharp, long pin 📍. Could you use it as a sword?\n\n {fore(1)}{style(1)}That's when you're knocked over, and fall to the floor!\n\n THE SPIDER HAD CAUGHT UP TO YOU!\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"{fore(1)}You feel the spider's hot breath on you (and also its drool, dripping down on your forehead).{style(0)} Knowing that the straight pin's in your reach, you pick it up.\n\n Kicking the spider with your leg, you roll over, and point the sharp pin at the spider's face, sprawled on the ground.\n\n 'DIE! DIE!', you shriek.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"The spider continues to drool. It's not even threatened by the pin!\n\n You then run again....\n\n 'This is the end....', you think to yourself.\n\n 'It's over-- I'm doomed...'\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You hide in a corner, and hold still.\n\n Did the black widow find you?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"Your question is answered when you see a thick black leg, as big as a drinking straw!\n\n You make a stabbing motion with the pin.\n\n{fore(1)} But, the spider's not done for....{style(0)}\n\n It still crawls on the wall, slowly coming down, eyeing you!\n\n'PLEASE! SPARE ME!', you plead.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"Yelling at it will not even work, so the only option is to run.\n\n You spin on your heels and continue to bolt across the room.\n\n The spider then follows you afterwards.\n\n Man.... HOW LONG IS IT GOING TO CHASE YOU? FOREVER? FOR ALL ETERNITY?!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt("Wait a minute--\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "Running will only make you more tired.\n\n You have to kill the spider-- Once and for all!\n\n You come to a complete stop, turn back, and then charge towards the black widowed spider, with pin in hand.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'YAAAAAAHHHHHHHHHHHH! EN GARDE!'\n\n With all your strength, you leap and furiously stab the spider with the pin. Landing, you continue to stab it repeatingly, until it drops dead....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        print("██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗██╗")
        print("██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██║")
        print("██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ██║")
        print("╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ╚═╝")
        print(" ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ██╗")
        print("  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝")
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"{fore(2)}Great! The spider's dead!{style(0)}\n\n Now what?\n\n I guess you gotta focus on getting back to normal....\n\n... That's when you feel a bit... weird....\n\n",
            userStrDelay,
        )
        storyLocation = "23"
        saveGame()
        backYard()
    elif decision == 4:
        os.system("clear")
        printt(
            "There's nothing there.\n\n That's when you hear footsteps....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(2) + "Yes! Someone's there at last!\n\n" +
               style(0), userStrDelay)
        time.sleep(0.5)
        printt(
            "But, who could it be?\n\n 'HEY!', you shout at the top of your lungs.\n\n'I'M IN HERE!'\n\n But, your voice is a bit inaudible inside the sock. That stranger (likely,"
            + bestFriend
            + "'s mom or dad) can't even hear you.\n\n That's when you feel yourself being lifted....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'"
            + bestFriend
            + "!', you hear the stranger yell. 'How many times do I have to tell you NOT to keep your dirty socks on the floor?!'.\n\n As he lifts the sock you're in, you feel yourself swinging from side-to-side like a pendulum.\n\n 'HEELLP MEEEEE!', you shout out again..\n\n But, IT'S TOO LATE!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"That person dumps the sock.....\n\n{fore(1)} INTO THE WASHING MACHINE!{style(0)}\n\n You tumble out of the sock, screaming.\n\n"
            + bestFriend
            + "'s dad doesn't even notice you fall.\n\n Cold water sinks over you as you land into the tumbler of the washing machine.\n\n Admit it, its pretty difficult to swim in this mixture of Tide + Water. It's like swimming in thick soup or some sort.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'Hey! Down here!', you call out to "
            + bestFriend
            + "'s dad as you struggle to stay buoyant. But, NO!\n\n He slams the washing machine door, and now you're left alone..... in the dark....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "After a few minutes, the washing machine starts up, and you eventually drown.....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()

    else:
        pass


def encounterFour():
    global userStrDelay, numDeaths, storyLocation, bestFriend
    os.system("clear")
    printt(
        f"After 20-30 minutes, you see a dirty paper towel. The towel is as big as a football field from your POV!\n\n Not only that,the 🧻 contains amounts of bacteria, just vibing.\n\n{fore(3)} Now, how would you get past THAT?\n\n{style(4)} Maybe they're friendly, but who knows?\n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "1. Assume the bacteria are friendly and make sure they don't notice you",
        userStrDelay,
    )
    printt("2. Don't even go on that dirty surface!", userStrDelay)
    print(f"Select an option \n\n{fore(229)}> {style(0)}")
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            f"Assuming those green, slimy critters are nice and they won't eat you, you make a run for it, and (suddenly) a small object whizzes past you.\n\n{fore(3)}{style(4)} What was that?{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"'Eh, might be a small mosquito.... a creature that doesn't care about me.', you think.\n\n{fore(3)} But it is out of the ordinary....\n\n Be prepared!\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Continuing to run like the wind, despite the fact your feet are paining intensively, you see the bacteria, minding their own business. Likely, they don't see you since microbes don't have any eyes, or they don't even care about you.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"'Huh?', you mutter to yourself as you see that same small object, hovering over the culture of bacteria.\n\n{fore(3)}{style(4)} What could that object be? Looks...\n\n.... man-made.....\n\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You move closer to the bacteria, just to get a good view....\n\n... And then, the mysterious thing flies toward you!\n\n 'HEY! SHOO!', you protest.\n\n The object comes closer to you and now you can see it in full view!\n\n{fore(1)} You're looking at a {style(4)}BACTERIOPHAGE!{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        bacteriophage = rf"""{fore(248)}
     ,-^-.
     |\/\|
     `-V-'
       H
       H
       H
    .-;":-.
   ,'|  `; \
        {style(0)}"""
        print(bacteriophage)
        time.sleep(0.5)
        printt(
            f"As per the drawing above, its not even {style(4)}that{style(0)} big, LOL 😂.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"It's actually the size of a bat🦇,{fore(135)} bruh!{style(0)}", userStrDelay)
        time.sleep(0.5)
        printt(
            f"{fore(1)}{style(4)}But, its not leaving you alone, so what now?{style(0)}\n\n {fore(1)}Probably its trying to inject its DNA 🧬 into you, assuming you're a bacterium!{style(0)} 'Go away!', you shout out, waving your arms as the bacteriophage floats around you.\n\n But it doesn't listen....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(f"{fore(3)}Seems like you gotta deal with this pest of not-so terrifying proportions--\n\n", userStrDelay)
        time.sleep(0.5)
        printt("1.Swat the bacteriophage", userStrDelay)
        printt("2. Eat it (Seriously?)", userStrDelay)
        printt("3. Ignore this weird creature", userStrDelay)
        time.sleep(0.5)
        print("Now what?\n\n >")
        decision = int(fkey.getchars(chars=["1", "2", "3"]))
        if decision == 1:
            pass
        elif decision == 2:
            pass
        elif decision == 3:
            pass
    elif decision == 2:
        os.system("clear")
        printt(
            "You then walk past that paper towel, and then continue to run....\n\n...FOR AGES!\n\n And so....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(fore(4) + "--35 minutes later--" +
               style(0) + "\n\n", userStrDelay)
        time.sleep(0.5)
        printt(f"{fore(3)}Oh, wait...\n\n Wrong time!🤭\n\n{style(0)}", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(f"{fore(4)}--3 hours later--{style(0)}\n\n", userStrDelay)
        time.sleep(0.5)
        printt("You finally arrive at your destination....Whew!\n\n", userStrDelay)
    else:
        pass


def microscopicSize():
    global userStrDelay, numDeaths, storyLocation, bestFriend
    os.system("clear")
    printt(
        f"{fore(0)}The sudden darkness in the room forces your eyelids to open.{fore(3)} What just happened?\n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'How long have I been here?', you thought. You try to get up, but something's preventing you from standing up!\n\n 'What the--'",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Looking down at your right leg, you see something spiky and {fore(2)}green.{fore(11)} Wasabi?--\n\n Wait a minute, wasabi can't be pointy....\n\n {fore(1)}AND, IT CAN'T BE ALIVE!{style(0)}\n It reminded you of the worm you encountered last night!--",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'GAAAAAAAAAUUUUGGGH! GROSS!'\n\n{fore(1)} You finally realize what it is.... IT'S BACTERIA!🦠{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Using your hands, you lift the slimy creature off your leg and chuck it across the kitchen counter.\n\n Okay....\n\n... That was weird....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"A horrifying thought comes to your mind: Are you more smaller?\n\n{fore(1)} Looking around, you notice everything has widened so much! The kitchen counter must've stretched for MILES!{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(1)}'Oh no, oh no, oh no, oh noooooo...', you moan.\n\n While asleep, you shrank even more! YOU'RE NOW MICROSCOPIC!{style(0)}\n\n Finding help would be {style(4)}more challenging{style(0)} as you're not visible to the naked eye!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'Okay. Relax.... This is all just a dream...', you think to yourself....\n\n You shut your eyes and constantly slap yourself, saying, 'WAKE-UP! WAKE-UP! WAKE-UP!'\n\n{fore(1)} But, no!\n\n THIS IS REALITY! 😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱{style(0)}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Dropping to your knees, you lie down, looking up at the ceiling, high above your head.\n\n'How am I going to make it out alive being about 1-2 mm tall?', you ponder.\n\n'Is this REALLY the end?'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(1)}{style(4)}Admit it, you can't even give up easily, no... NOT LIKE THIS!{style(0)}\n\n{fore(3)} You have to think-- fast!{style(0)}\n\n That's when you start to feel more cold than ever...\n\n{fore(1)}{style(4)} Are you gonna die here?!?\n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'So hungry...', you hoarsely moan. 'M-must e-eat s-something...'\n\n Alright, you have at least 3 hurdles to overcome:\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "1. Staying warm, by eating something and gaining metabolism\n", userStrDelay
    )
    time.sleep(0.5)
    printt("2. Getting back to normal at THIS extremely smol size\n", userStrDelay)
    time.sleep(0.5)
    printt(
        "3. Surviving in a more dangerous environment, as there are microbes around you. To make things worse, any ordinary insect will appear to you like a towering army tank. And, you're defenseless and extremely weak (The smaller you get, the more weak you become.)\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Getting up to your feet, you scan the entire room. What could you eat, in order to stay alive? The kitchen is eerie quiet, and darkness envelopes you. It must be in the evening, now!\n\n The only thing that you hear, is your 🫀 beating faster than the average person, emitting a humming sound (Again, it has to do with your size, and if you have studied Bio, you realize that you're in a critical, fatal situation!)\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You spot a chocolate cake on a plate. It's not that far from where you were! Could you make it?\n\n",
        userStrDelay,
    )
    cake = rf"""{fore(130)}

                   _____
           _..--'''@   @'''--.._
         .'   @_/-//-\/>/>'/ @  '.
        (  @  /_<//<'/----------^-)
        |'._  @     //|###########|
        |~  ''--..@|',|###########|
        |  ~   ~   |/ |###########|
        | ~~  ~   ~|./|###########|
         '._ ~ ~ ~ |,/`````````````
           ''--.~. |/
    {style(0)}
    """
    time.sleep(0.5)
    print(cake)
    time.sleep(0.5)
    printt(
        f"Running as fast your tiny feet can go, it seems like it'll take about {style(4)}days{style(0)} to get to the plate!\n\n That is, if bacteria don't find you, and take you for dinner....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "An hour has passed, and you only made 1/4th of the distance from the 🍰.\n\n Slow progress, eh?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You: *Pant*,*Pant*, Ohhhh.... How long w-will i-it take? {You keep on running after you come to a stop}\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("At least you burned some calories and exercised, right?\n\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    storyLocation = "31"
    saveGame()
    encounterFour()


def antSize():
    global userStrDelay, numDeaths, storyLocation, bestFriend
    os.system("clear")
    printt(
        "You leap off the laptop, and pace around on the tabletop.\n\n Looking for your friend could be pretty risky. After all, her cat might be still around....\n\n Maybe she(your friend) could be in the bathroom.... or the kitchen?\n You're not sure if you should get off the table, and risk it all, or if you should stay on the table, and hope for the best.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(6)
        + "Your final decision is this: Get off the table and look for your best friend in the kitchen....\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        "You carefully lower yourself off the table, sliding down the table leg. You jump off the table leg, and land on your feet. Since you passed the kitchen before, you know where the location is....\n Running as fast as you can, you make your way to the kitchen.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Rushing into the kitchen, you see your best friend, helping herself to some food. How can you make her see you?\n\n An idea comes to your mind as you see a step-stool. Could you get attention from there? 99 percent likely......\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You then climb onto the first step of the step-stool, and try to get attention, waving your arms frantically, shouting.'"
        + bestFriend
        + "? I need help. Can you hear me?'\n\n'"
        + bestFriend
        + "? Please, "
        + bestFriend
        + "!'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Unfortunately, your voice isn't loud enough, and your friend doesn't even notice you! Ok, another plan....\n\n That's when you feel strange..... A familiar sensation dawns on you.....\n\n .... Which isn't very good..... Your body is tightening even more! Wait a minute--\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(fore(1) + "Oh-No....\n YOU'RE STILL SHRINKING!\n\n" +
           style(0), userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"'Yaaarrrrrrgggggghhhhhhh!'\n\n You scream at the top of your lungs as everything's rising, the ground is being more spread out than ever, and you feel more dizzy by just looking up at the ceiling! You lie down, enduring the pain....\n\n Could you make it? COULD YOU MAKE IT?!?!\n\n ",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"The intense pain finally stops. You get up, and look around. Your best friend is still there, though.{fore(2)} Yes! You can at least get help now!\n\n{style(0)} Standing on that lower step isn't working, so maybe you could climb up higher...\n\n ",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"{fore(3)}Huh? Why is the top corner of the step-stool so far away from your reach?\n\n{style(0)} And, the step that you're standing on has spread so much!",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"This is really, really weird.....\n\n{fore(1)} AND BAD! {style(0)}\n\n 'Ohh noooooooooo', you think to yourself. You feel more lightheaded as you try to think: Are you the same size as before....?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(1) + "Turns out you're not!" +
        style(0) + "\n\n Seems like .....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    warning = Figlet(font="doom")
    os.system("clear")
    print(warning.renderText("YOU'RE THE SIZE OF AN ANT!"))
    time.sleep(0.5)
    os.system("clear")
    printt(fore(12) + "Ok, panic? \n\n Maybe....\n\n" + style(0), userStrDelay)
    time.sleep(0.5)
    printt(
        f"Getting attention will be a LOT HARDER now! And, that's a fact! You're so small to be seen with the naked eye, people will have to use a 🔎 in order to see you.\n\n That's when you feel chilly.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        fore(4) + "Brrrr...... Why is it so cold all of a sudden? 🥶" + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Did someone turn off the heater or some sort?\n\n The answer to your question is a big fat, 'NO'.... It has to do with your size, actually....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "1. Yes I would like to know why this is happening to me, cuz knowledge is power, they say 🧐",
        userStrDelay,
    )
    printt("2. No, I don't even give a damn!", userStrDelay)
    print("Care for an explanation?")
    explanation = int(fkey.getchars(chars=["1", "2"]))
    if explanation == 1:
        longExplanation()
        printt(
            "Ok, ya got that? Using this newfound knowledge, you plan to try to get attention, and eat something.\n\n Now, where is your friend? The bad news is, she's not there!\n\n Oh wait, my assumption was incorrect as you start to hear the loud thunderclaps of her shoes hitting the floor. Seems like she's doing the chores.\n\n'"
            + bestFriend.upper()
            + "? DOWN HERE!' Your voice, comes out, in an uncomfortable high-pitched squeak...",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "No use. You're too small to be heard (and seen?). NOW WHAT SHOULD YOU DO?!\n\n Seems like you have to eat something, as your tiny body's still cold.\n\n You gotta gain energy by moving straight to action!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You look up, seeing the towering kitchen counter. How would you make it up? Your stomach growls more louder as you try to think.\n\n That's when you hear a sound-- an odd tapping sound.\n\n You spin around, and staying where you are, you try to let out a scream, but no sound comes out...\n\n You realize that you're in trouble! Well, why? Because.....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            fore(1)
            + "A cockroach 🪳 is coming towards YOU!\n\n"
            + style(0)
            + "Great, being the size of an ant just brings more troubles right?!\n\n 'Go away, I repeat.... STAY AWAY FROM ME!', you plead in your mouse-like voice. But, hell naw! It climbs up the step-stool and charges towards you like a horse!\n\n 'STAY AWAY FROM ME!', you yell at the roach again.\n\n Nope, nothing makes that pest afraid!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(3) + "And I mean it!\n\n" + style(0), userStrDelay)
        time.sleep(0.5)
        printt(
            "1. Let the cockroach assist you in getting up the kitchen counter",
            userStrDelay,
        )
        printt(fore(1) + "2. Run for your f**king life!" + style(0), userStrDelay)
        printt("3. Fight the roach", userStrDelay)
        print("This is gonna be pretty risky. Select an option:")
        decision = int(fkey.getchars(chars=["1", "2", "3"]))
        if decision == 1:
            os.system("clear")
            printt(
                "You lend an outstretched hand to the dirty (Excuse me?) insect.\n\n The roach just stares at you....\n\n'Can you help me get up the kitchen counter?', you ask.\n\n The cockroach just stands there, twitching its antennae.\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Shaking with fear,you just stay there....\n\n And to make a long story short, you eventually die from hypothermia because you were too scared.\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(4) + "🥶 GAME OVER 🥶" + style(0), userStrDelay)
            time.sleep(0.5)
            os.system("clear")
            printt(
                "Just kidding....🤣\n\n You thought you were dead? Right?\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                fore(2)
                + "In reality, the 🪳 accepted your offer and allowed you to climb on its hard, cold back.\n\n"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "After several minutes, you finally reach the top of the kitchen counter.\n\n But, as soon as you hop off the roach, you collapse to the floor, and pass out....\n\n",
                userStrDelay,
            )
            storyLocation = "30"
            microscopicSize()
        elif decision == 2:
            os.system("clear")
            printt(
                "You slide down the curved edges of the step-stool, and the cockroach follows you!\n\n Running with all your might, you plan to hide.... somewhere.....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(3) + "But, WHERE WOULD YOU HIDE?!\n\n" +
                   style(0), userStrDelay)
            time.sleep(0.5)
            printt(
                f"That's when you see {bestFriend}'s foot.{fore(2)} Maybe you could hide in her sock 🧦 and also try to get attention! A BRILLIANT IDEA!{style(0)} {fore(3)}(According to you, though. You don't even know what I planned....... Ehehehehehe){style(0)}",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                fore(3)
                + "You look behind you, and the cockroach is gaining speed! You've gotta go fast!"
                + style(0)
                + "\n\n Craning your neck, you gawk at the sight of your friend's shoe. It's the size of a cruise ship! 🛳️\n\n Climbing up will be pretty tricky....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Mustering all your ant-sized strength, you leap upwards, shoot your hands out to at least-- grab onto something, and then....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                fore(2)
                + "You grab onto the laces, as big as thick jump-ropes (My mind went blank when trying to think of it, so I typed it anyway....) and attempt to make your way up. \n\n The laces are pretty scratchy and make your hands red. Struggling to hold on, you dig your shoes into the thick shoe laces, and climb some more.\n\n"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                f"With your entire body in excruciating pain, you leap again, and grasp the soft, but actually heavy fabric of the sock. {style(3)}Ohhhhhhhhhhh....... This is hurting my hands so much!{style(0)}, you think to yourself. But, there's no way that you'll let go.... AT ALL!\n\n'HURRRRGGGGGHHHHH!'\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                f"You grunt as you try to get yourself into the sock by using all your strength. Has the roach found you?\n{fore(2)} You turn around and see that the bug's gone. Phew!\n\n{style(0)} Now, you better focus on getting inside that sock!\n\n",
                userStrDelay,
            )
            os.system("clear")
            time.sleep(0.5)
            printt(
                "After a few minutes of struggling , you finally lower yourself down, into the sock. Let's face it, it's dark, awfully smelly, and cramped. Catching your breath, you slump down, and rest your head on the fabric.\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Great, the next step is to shout out for "
                + bestFriend
                + ". \n\n You take a deep breath, and yell: 'YO,"
                + bestFriend.upper()
                + "!'\n\n Nope. Nothing happens. No realization that your friend recognizes your voice, nor feels anything in her foot. You try to get comfortable in the sock, but you're too weak to do so, especially from all that running.\n\n That's when the unthinkable happens....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "'Why do I feel warm?', your friend wonders. Within a couple of seconds, you feel a sudden bump as she takes off her shoe. You continue to shout her name in order to get attention, but it's too late!\n\n And, what do I mean by that?!\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                fore(1)
                + bestFriend
                + " takes off the sock (containing you)!"
                + style(0)
                + " \n\n'Waaauuuuggggh!'\n\n Startled by what's happening, you fall into the 'dead end' of the sock.\n\n 'LOOK INSIDE, IT'S ME!', you shriek. Unfortunately, you're too small to be seen, and your friend chucks the sock away!\n\n You scream all the way down, thinking that you'll be dead soon.\n\n The sock hits the floor with a hard **WHUMPPPP**.\n\n Good thing is you're still alive! But, what about your chances to be normal again?\n\n I assume that they're pretty slim....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Weak and tired from climbing up that looming shoe, and being tossed in a parabolic motion, you pass out...",
                userStrDelay,
            )
            time.sleep(0.5)
            storyLocation = "22"
            saveGame()
            sockPlot()
        elif decision == 3:
            os.system("clear")
            printt(
                "Unfortunately, the cockroach murders you as fast as possible. (Yeah, that was written in a lazy kind of way, but I don't give a damn)",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
            numDeaths += 1
            saveGame()
            playAgain()
    elif explanation == 2:
        os.system("clear")
        printt(
            "Seriously, by not listening to me, you're gonna be in BIIIIGGGGG TROUBLE....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "That's when you hear a sound-- an odd tapping sound.\n\n You spin around, and staying where you are, you try to let out a scream, but no sound comes out...\n",
            userStrDelay,
        )
        os.system("clear")
        printt(
            fore(1)
            + "A cockroach 🪳 is coming towards YOU!\n\n"
            + style(0)
            + "Great, being the size of an ant just brings more troubles right?!\n\n 'Go away, I repeat.... STAY AWAY FROM ME!', you plead in your mouse-like voice. But, hell naw! It climbs up the step-stool and charges towards you like a horse!\n\n 'STAY AWAY FROM ME!', you yell at the roach again.\n\n Nope, nothing makes that pest afraid!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(3) + "And I mean it!\n\n" + style(0), userStrDelay)
        time.sleep(0.5)
        printt(
            "Thinking quickly, you leap off the step-stool, screaming all the way down.....\n\n Which actually is a bad and totally stupid idea, as you crack your skull on impact. You completely forget that you're the size of a bug, and TBH falling from that step-stool when you're 1.27 cm is equivalent to falling from a five-story building. Just Sayin'.😏",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()


def typeMessage():
    global userStrDelay, numDeaths, storyLocation, bestFriend
    os.system("clear")
    printt(
        fore(3)
        + "Well, at least typing on the keyboard when you're an inch tall should be easy...... Right?"
        + style(0),
        userStrDelay,
    )
    printt(
        "\n\n Bah, who cares?\n\n You type the following message, bashing the first key you're standing on, and walk to the next key(rinse and repeat!): \n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    keyboard = r"""
  _______ _______ _______ _______
 |\     /|\     /|\     /|\     /|
 | +---+ | +---+ | +---+ | +---+ |
 | |   | | |   | | |   | | |   | |
 | |H  | | |E  | | |L  | | |P  | |
 | +---+ | +---+ | +---+ | +---+ |
 |/_____\|/_____\|/_____\|/____\ |
                                            """
    punctuation = r"""
 _______
|\     /|
| +---+ |
| |   | |
| |,  | |
| +---+ |
|/_____\|
         """
    os.system("clear")
    time.sleep(1)
    print(keyboard)
    time.sleep(1)
    os.system("clear")
    print(punctuation)
    time.sleep(1)
    keyboard2 = r"""
 _______ _______ _______
|\     /|\     /|\     /|
| +---+ | +---+ | +---+ |
| |   | | |   | | |   | |
| |I  | | |'  | | |M  | |
| +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|
                            """
    keyboard3 = r"""
 _______ _______ _______
|\     /|\     /|\     /|
| +---+ | +---+ | +---+ |
| |   | | |   | | |   | |
| |T  | | |H  | | |E  | |
| +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|
                         """
    keyboard4 = r"""
 _______ _______ _______ _______
|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | |
| |S  | | |I  | | |Z  | | |E  | |
| +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|
                                 """
    keyboard5 = r"""
 _______ _______
|\     /|\     /|
| +---+ | +---+ |
| |   | | |   | |
| |O  | | |F  | |
| +---+ | +---+ |
|/_____\|/_____\|
                 """
    time.sleep(2)
    os.system("clear")
    print(keyboard2)
    time.sleep(2)
    os.system("clear")
    time.sleep(2)
    print(keyboard3)
    time.sleep(2)
    os.system("clear")
    print(keyboard4)
    time.sleep(2)
    os.system("clear")
    print(keyboard5)
    keyboard6 = r"""
 _______
|\     /|
| +---+ |
| |   | |
| |A  | |
| +---+ |
|/_____\|
         """
    time.sleep(1)
    os.system("clear")
    print(keyboard6)
    time.sleep(1)
    keyboard7 = r"""
 _______ _______ _______
|\     /|\     /|\     /|
| +---+ | +---+ | +---+ |
| |   | | |   | | |   | |
| |B  | | |U  | | |G  | |
| +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|
                         """

    os.system("clear")
    print(keyboard7)
    time.sleep(0.5)
    os.system("clear")
    printt(
        fore(2)
        + "Perfect! Let's hope that she'll notice it anytime soon...\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(fore(4) + "--5 minutes later--\n\n" + style(0), userStrDelay)
    time.sleep(0.5)
    printt(
        bestFriend
        + " finally arrives, pulls in her chair, and sees the message.\n\n'What the--'\n\n'Who wrote THIS?'\n\n You stay where you are, and try to call out for her, loud and clear.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Yoo-Hoo!', you call out, waving your arms. 'DOWN HERE!'\n\n Your friend can hear you! She then looks down.....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        ".... And "
        + fore(1)
        + " screams in horror!"
        + style(0)
        + "\n\n Or in shock?\n\n 'EEEEEEEEEEEEEEEEEEEEEEEEKKKKKKKKKKKKKKKKK!' \n\n That sound deafens your ears, as if your eardrum's about to f**king explode!\n\n 'HEY! Calm down, would ya?', you beg. Shakily she sits down. "
        + bestFriend
        + " stares at you, wide eyed. 😧\n\n 'Calm down, please! Listen to me, I-'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"'Dude....', your friend squeals. '{username}-- You're sooooo tiny!' She then attempts to grab you by the fingers, but you stop her.\n\n 'DON'T!', you shout, and raise both hands to protect yourself. 'Don't pick me up, I'm very very fragile...', you warn.\n\n Your best friend stops what she's doing, thinks for a few seconds, and opens her palm right in front of you. You then hop onto her hand and sit down cross-legged.\n\n Your friend holds you close to her mouth, that it felt like as if you're staring into a dark cave. Seems like as if she was about to swallow you whole or some sort!\n\n"
        + bestFriend
        + " is still staring at you. 'How on earth did THIS happen to you?!', she asks. 'Can't you just whisper?', you moan faintly. 'You're loud, and EVERYTHING is loud....'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Ok....', your best friend responds (in a whisper). 'If you want to know how did THIS happen to me..... it's because I was stupid....'.\n\n You let out a sigh....\n\n{Insert record scratch sound here}\n\n 'You're so cute!', your friend says, giggling, interrupting you.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'HEY! WHADDYA MEAN I'M CUTE?!', you snap back.\n\n 'DON'T YOU UNDERSTAND HOW MUCH I'VE SUFFERED?!? No?!?!'\n\n'Hey, sorry about that...', your friend says. And, this is how the conversation goes.....\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(bestFriend + ": So, what do you mean you've suffered?\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        "You: You really don't want to believe it, but I endured so much.... I encountered a spider, dangerously hitched a ride with a crow, got eaten alive by a human--\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        bestFriend + ": Hold on.... you were INSIDE a human?!? O-M-G....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You: I know. Unsettling isn't it? I'm still sweating now after so many hours.... *Sigh*\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("{You look down, feeling gloomy and sort of depressed}\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        "You: Listen.... I need YOU to help me fix this! I- I can't even stand being like this anymore!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        bestFriend
        + ": But, HOW CAN I HELP YOU? Why did you come here, risking your own life? You could've died--\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You: You want to know what shrank me? You really, really, desperately want to know? Fine, I'll tell you....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "You: Lemme ask you a question.... Has a mysterious package been delivered to your house lately?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(bestFriend + ": Uhhhh, NO.\n\n", userStrDelay)
    time.sleep(0.5)
    printt("You: Whuh--- YOU DON'T EVEN F**KING KNOW?!\n", userStrDelay)
    time.sleep(0.5)
    printt(
        bestFriend
        + ": Whoah, whoah, whoah, calm down! Your tiny voice is hurting my ears. Anyway, go on.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You: It was one of those liquid triple fat-burners. The one that comes in a clear small bottle. Unfortunately, I overdosed it and as a result, I started to shrink.... I really regret this now, and please! YOU HAVE TO HELP ME! I need to get an antidote.... FAST!\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(bestFriend + ": But why this quick? Are you in a hurry?\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt("You: I really hate to say this.... but-- But--\n\n", userStrDelay)
    time.sleep(0.5)
    printt(bestFriend + ": But what? Just tell me!\n\n", userStrDelay)
    time.sleep(0.5)
    printt(
        "You: *Sigh*...... Within any moment, my size will decrease even more.... I'll disappear out of sight-- FOREVER! You won't even see me at all ever again! So, please.... tell me, do you know this so-called fat burning drink? Or... potion?-\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        bestFriend
        + ": Wait a second! I think I know what you're talking about. My Dad helped in creating the antidote with Hank Pym--\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You: WHA-- HANK PYM?! {🤯} I mean-- Seriously?!\n\n{You beam with pride}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        bestFriend
        + ": Yep, that Hank Pym, the one who's responsible for the creation of Pym Particles, and this weight-loss remedy.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You: Alright, tell me where can I get the antidote, I can't stand being an inch tall any longer. Here's hoping.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        bestFriend
        + ": Well.... My dad locked the antidote in a safe for protection purposes, and to also NOT put it in our food by mistake.\n\n",
        userStrDelay,
    )
    os.system("clear")
    printt(
        "You: Damn it! {You slap your forehead in frustration} How'll I get back to normal size now?! Also, do you know the safe combination?",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        bestFriend
        + ": Well, I don't know. I don't know if I can help you, but maybe I can guess....",
        userStrDelay,
    )
    os.system("clear")
    time.sleep(0.5)
    printt(
        "Your friend lifts you up off the desk, and inserts you into her shirt pocket. Then, "
        + bestFriend
        + " walks to the basement door and opens it.\n\n 'So, the safe is in there?', you ask. 'Of course! Why would I not know. My father's not secretive.', your friend responds.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    storyLocation = "19"
    saveGame()
    safeCombination()


def safeCombination():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    os.system("clear")
    printt(
        f"Creeping down the stairs, the two of you arrive at the basement.\n\n'Where's the safe?', you ask {bestFriend}. 'I believe its right.... there!', she responds.\n\n 'The safe is just on the old dining table we used to have.'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"'Okay....', you trail off. Your friend lifts you out of her shirt pocket, and sets you down next to the safe.\n\n 'Know the combination?', you question her.\n\n'Like I said, I dunno what it could be.....', she responds. 'I think it has to be {style(4)}3-digits{style(0)}....Hmmm.'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(3)
        + "You're one step closer to being cured, and now the only hurdle is figuring out the safe combination...."
        + style(0),
        userStrDelay,
    )
    while True:
        try:
            combination = 336
            print("Enter a 3-digit combination:")
            combinationInputPreHandle = ""
            while len(combinationInputPreHandle) < 3:  # type: ignore
                combinationBit = fkey.getchars(
                    chars=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                )
                combinationInputPreHandle += combinationBit  # type: ignore
                print(combinationBit, end="", flush=True)
            print("")
            time.sleep(0.5)
            combinationInput = int(combinationInputPreHandle)
            if combinationInput == combination:
                os.system("clear")
                printt(
                    "You: My best guess is 336... Let's see what happens now.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"{bestFriend}: Okay...[She enters the combination you had guessed]\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(fore(2) + "✅ GRANTED ACCESS! ✅\n\n" +
                       style(0), userStrDelay)
                time.sleep(0.5)
                printt("You: *Gasp*, It worked!\n\n", userStrDelay)
                printt(bestFriend + ": Good! Lemme open the 🔒 now!", userStrDelay)
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "Your friend opens the safe, and sees that there are several antidotes! Perfect!\n\n She then opens one bottle and sets it down next to you. But, the bottle is too big for you to drink!\n\n Thinking hard, she takes out a measuring spoon and fills it up with the antidote.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "You then lap up the contents of the antidote like a dog, and then wait for your body to feel different.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    f"After 5 seconds....\n.... You hear a loud{fore(205)} **POP**{style(0)}\n\n{fore(3)}{style(4)} Did it work?{style(0)}\n That's when you find yourself on the floor, looking stunned.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"{fore(84)}You hear your friend gasp.'You're back to your old, more familiar size, buddy!', she calls out.{style(0)}\n\n'I-I did?', you say hoarsely.\n\n Looking at your hands, you slowly get up.\n\n{fore(156)} Looking around the basement, you notice that not every object looks alien, weird, and tall!{style(0)}\n\n'Yessss!', you pump out your fist in joy.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"{bestFriend} then responds, 'I think you need to get home now. Also, you need to take a shower. You reek...'\n\n 'Okaaayy, that's not the compliment I was expecting....', you say smugly.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "'See you later!', you shout out as you make way upstairs, planning to head home, as happy as ever....\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(f"{fore(2)}🎉 THE END 🎉{style(0)}", userStrDelay)
                quit(0)
            elif combinationInput == 666:
                os.system("clear")
                printt("You: I believe the combination is 666....\n\n", userStrDelay)
                time.sleep(0.5)
                printt(
                    "Your friend enters your guess, and it turns out....\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(fore(1) + "❌ ACCESS DENIED! ❌\n\n" +
                       style(0), userStrDelay)
                time.sleep(0.5)
                printt(
                    f"'That combination is dead wrong!', {bestFriend} says.\n\n And then, the two of you hear cackling in the distance...\n\n{fore(9)} Unknowingly, you accidentally summon the devil! 👿{style(0)}\n\n{fore(124)} Things get even worser when your best friend is eventually vanquished into thin air!{style(0)}\n\n'NOOOOO!', you scream.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"{fore(1)}{style(4)}Great, your friend is GONE....\n\n NOW WHAT?!\n\n{style(0)}",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt("1. Make a deal with the devil", userStrDelay)
                printt("2. Blame your situation on the narrator", userStrDelay)
                print(f"{fore(2)} >{style(0)}")
                choice = int(fkey.getchars(chars=["1", "2"]))
                if choice == 1:
                    os.system("clear")
                    printt(
                        f"You: Alright, what do {style(4)}you{style(0)} want with me? Bring back {bestFriend}, RIGHT NOW!\n\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt("😈:Well, well, well....", userStrDelay)
                elif choice == 2:
                    os.system("clear")
                    printt("", userStrDelay)
                else:
                    pass
            elif combinationInput == 420:
                os.system("clear")
                shockedText = Figlet(font="slant")
                print(shockedText.renderText("Seriously?\n\n"))
                time.sleep(0.5)
                printt("Are you this stupid?!\n\n Try again!\n\n", userStrDelay)
                os.system("clear")
                continue
            elif combinationInput != combination:
                os.system("clear")
                printt("Not quite right...\n\n Try again!\n\n", userStrDelay)
                os.system("clear")
                continue

        except ValueError:
            os.system("clear")
            printt("Not a valid safe combination....\n\n TRY AGAIN!\n\n", userStrDelay)
            os.system("clear")
            continue


def longExplanation():
    global userStrDelay, bestFriend, numDeaths, storyLocation
    os.system("clear")
    printt(
        "Since you're currently a fraction(1/2 to be exact) of an inch tall, you're 100 times more shorter than you were before, and your surface area is a lot larger (about 1000X times), this is why you're freezing cold....\n\n.... Don't ask me, I didn't make it up. It's the laws of physics, and you're breaking the Square Cube Law, duh!",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Secondly, you're losing heat quickly, due to to a lack of energy, based on your ant-size proportions of course. How would you NOT freeze to death? \n\n By eating of course!",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "But, there's a catch! \n\n You have to eat 24/7..... every hour ...... every day! Well, since I'm the narrator of this game, I'll spare your life, for now.....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")


def plotPointFive():
    global userStrDelay, numDeaths, storyLocation, bestFriend
    os.system("clear")
    printt(
        "Continuing to run, you call out for your best friend. '"
        + bestFriend
        + "? "
        + bestFriend
        + "?' Your voice comes out so tiny, (and thank God, NOT HIGH-PITCHED, cuz people hate that...) despite the fact you know anyone in the house can't hear you...\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "After several minutes, you finally arrive at her room. "
        + bestFriend
        + " is typing on her laptop, which does shows that she's busy with other things...\n You then make way to her desk, and immediately start shouting, with your voice loud and clear, in order to get attention. ' "
        + bestFriend.upper()
        + " ? IT'S ME!'\n\n Nope. She doesn't notice you, and is still typing.\n\n You cup your hands to make yourself even more louder. 'LOOK DOWN! HEY! IT'S ME! DOWN HERE! "
        + bestFriend.upper()
        + " ?'",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"It's no use! Your best friend can't hear your tiny voice, but you're desperate to get attention!\n You start to run towards her foot, planning to hug it-- TIGHT! As you run, you notice that "
        + bestFriend
        + " is getting up! You then halt, panting.\n\n Darn......\n\n.....\n\n....."
        + fore(1)
        + "You missed your chance! NOW WHAT?!"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        "Hold on....\n\n If she doesn't see you, maybe you could "
        + fore(10)
        + "type "
        + style(0)
        + " a message so that your friend can notice! 💡 \n\n Sounds like a plan...",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        fore(12)
        + "But, HOW WOULD YOU GET TO HER LAPTOP?! If you fall, that could kill you instantly....\n\n However, you have no choice but to constantly risk your life-- Over and over again....\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You notice the table leg within your reach. Figuring out that you have to climb on it as usual, you quickly hoist yourself and climb upwards in a fast pace.\n\n",
        userStrDelay,
    )
    computer = r"""
   +--------------+
   |.------------.|
   ||            ||
   ||            ||
   ||            ||
   ||            ||
   |+------------+|
   +-..--------..-+
   .--------------.
  / /============\ \
 / /==============\ \
/____________________\
\____________________/"""
    time.sleep(0.5)
    os.system("clear")
    printt(
        "By the moment you reach the top of the desk, "
        + bestFriend
        + "'s computer is only a few metres away from you. \n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    print(computer)
    time.sleep(0.5)
    printt(
        "\n\n You rush straight to the computer, and gaze up. The edges feel more like a wall, blocking your path.\n\n Now, how would you get up there?\n\n Luckily, you can grip onto the sides of the laptop with ease, and then hoist yourself onto the keyboard, as big as floor tiles. You then see the brightly lit screen. The text appeared as big newspaper headlines. You also see that "
        + bestFriend
        + " is using Microsoft Word in order to type, so maybe you could type on it.... Or do something else?\n\n",
        userStrDelay,
    )
    printt("1. Type a message to get help", userStrDelay)
    printt("2. Conduct an AMA on Reddit (In order to get help)", userStrDelay)
    print("So, what would you like to do?")
    message = int(fkey.getchars(chars=["1", "2"]))
    if message == 1:
        storyLocation = "20"
        saveGame()
        typeMessage()
    elif message == 2:
        os.system("clear")
        printt(
            "Using your tiny hands, you log onto Reddit, and create a new post on r/AskReddit, titled as: 'Help, I've been shrunk to an inch tall, AMA ASAP!!!!'\n\n You quickly submit the post, and wait for several minutes for someone to respond....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You refresh the Reddit post constantly, waiting for someone to respond.....\n\n Unfortunately, nobody does.....\n\n For a few minutes of course!\n\n This is the first comment you see: \n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"u/ILiekMudkip&DeezNuts -- Sorry, can't help you @ this moment. BTW, what's it like being an inch tall, LOL\n\n ",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1)
            + "You've no time to respond to that comment!\n\n YOU NEED HELP RIGHT AWAY! Turns out that AMA isn't working at all!"
            + style(0)
            + "\nShould you give up?!",
            userStrDelay,
        )
        printt("1. Yes, I should give up!", userStrDelay)
        printt("2. Nope, I'm gonna wait for my friend!", userStrDelay)
        decision = int(fkey.getchars(chars=["1", "2"]))
        if decision == 1:
            os.system("clear")
            printt(
                f"You find a glock ︻╦╤─ in your pocket, and take it out.\n\n You pull the trigger, and the gun goes off with a {fore(3)}BANG!{style(0)}\n\n {fore(1)}Congratulations! You've committed suicide, all for just a Reddit AMA!{style(0)}",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(1) + "︻╦╤─ GAME OVER  ︻╦╤─", userStrDelay)
            numDeaths += 1
            saveGame()
            playAgain()
        elif decision == 2:
            os.system("clear")
            printt(
                "You sit down on the edge of the laptop, waiting for your friend to return....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                fore(1) + "And, she doesn't. What could be taking so long?" + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt("1. Look for your best friend", userStrDelay)
            printt(
                "2. Keep on waiting, and type a message to get help once she arrives",
                userStrDelay,
            )
            decision = int(fkey.getchars(chars=["1", "2"]))
            if decision == 1:
                storyLocation = "21"
                saveGame()
                antSize()
            elif decision == 2:
                storyLocation = "20"
                saveGame()
                typeMessage()

    else:
        pass


def refrigerator():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        fore(1)
        + "How would you open the refrigerator?\n\n HOW?!"
        + style(0)
        + "\n Maybe you should wait for someone to come in and open it for you.",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "First thing, is to get to higher ground. You see the kitchen counter, rising high above you. Therefore, you decide to climb upwards.\n\n After several-something minutes, you successfully make your way up and drop onto the counter.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"You wait for someone to open the fridge, which does happen, and you leap from the counter to the lower fridge drawers. {fore(1)}All within a few seconds, you hear a loud 'BANG!' and the door slams shut.{style(0)}\n\n'HEY! LET ME OUT OF HERE!', you protest.\n\n {fore(1)}{style(3)} But, its too late.{style(0)}\n\n You immediately die of frostbite. All due to the laziest plot point of all time.... (Just Kidding....)",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(fore(4) + "🥶 GAME OVER 🥶" + style(0), userStrDelay)
    numDeaths += 1
    saveGame()
    playAgain()


def nextDay():
    global userStrDelay, numDeaths, storyLocation, bestFriend, best
    os.system("clear")
    time.sleep(0.5)
    printt(fore(4) + "--The Next Day--\n" + style(0), userStrDelay)
    time.sleep(0.5)
    printt(
        "You open your eyes....\n\n Did you disappear?\n\n Are you still there?\n\n You touch your body parts.\n\n They're fine!\n\n Shafts of light shone through the blades of grass. It's morning. And, best of all, they're (the grass blades) still the same height as before! \n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(2)
        + f"{style(3)}Yes! I didn't shrink to nothing!{style(0)}, you thought to yourself.\n\n Now, you gotta get to your friend's house, despite the risks!\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    text = Figlet(font="epic")
    print(text.renderText("Are you ready?"))
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Despite the fact that you're tired and its just 9 am in the morning, you stand up and see that you only have one block to go!\n\n You then grab a small stick and start to run in a frenzy, pushing the grass blades with that stick you're holding....",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "About 20 minutes has passed, and you step out of the tall grass, past the flower bed, and onto the sidewalk.\n\n By the moment you reach the front porch, you feel a shudder down your back....\n\n"
        + fore(9)
        + "There's NO WAY THAT YOU COULD GET UP THERE!\n\n The first step rose as high as a fortress!"
        + style(0)
        + "\n You search frantically for a plank or a piece of wood. Could you use it as a bridge?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "NO.\n\n The only option is to get up.... the HARD WAY....\n\n You do a running start, and leap towards the first step. You make a grab for the edge of the step.....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(2)
        + "Which you successfully do!\n"
        + style(0)
        + "(Alongside with the disadvantage of your entire body slamming onto the cement, and also the amount of pain in your arms/legs)\n\n Dangling in the air, you immediately hoist yourself up onto the first step.\n\n Panting, and drenched with sweat, you crane your neck. Only two steps left, and then the front door....\n\n You continue to do the same, long, and pretty painful climb up the steps....",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        f"With your entire miniature body aching, you finally reach the front door.\n\n The distance between you and the doormat seemed like 1-3 km! \n\n You brush off the sweat and start to run. Your feet are paining from the long climb, and you're starting to feel lightheaded.\n\n Geez, being an inch tall is more exhausting than ever!\n\n'I don't even think I can do this any longer...', you think to yourself.\n\n Will getting from point A to point B be tiring? What about doing daily activities, like getting to your university, or working on your part-time job? I believe that you won't survive....\n\n You know what, forget about what I said.\n\n You need help, so I'll leave everything to you.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "You stumble towards the front door, with your palms on the pet door in front of you.\n\n Your best friend has a pet cat, so you better watch out for it.\n\n THAT..... was a long run! Or walk?\n\n You're extremely tired, and you gaze at your hands. They're scraped with the bits of cement from the porch.\n\n Could you open the pet door? You've done it before, but now when you're more smaller? \n\n Maybe.... even though you're tired, and have no strength left.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "With your last bit of strength (though its not really the last), you push the latch of the pet door, and enter the house!\n\n You then collapse to the floor, tired and panting. You then look up, and see a "
        + fore(0)
        + "mysterious black-colored object "
        + style(0)
        + " blocking your path.\n\n What is that thing?\n\n The object rose up like a mountain!\n\n Or a hill....\n\n No... A hill cannot be black..... and.... furry?\n\n That's when your blood runs cold....😨",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    cat = (
        fore(0)
        + r"""
                           |\__/,|   (`\
                           |_ _  |.--.) )
                           ( T   )     /
                         (((^_(((/(((_/            """
        + style(0)
    )
    print(cat)
    printt(
        fore(1)
        + "\n\n You're right in front of your best friend's cat!"
        + style(0)
        + "\n\n Luckily, she's sleeping soundly, but one sound, one sneeze, one cough,and one scream will wake her up! The only option is to tiptoe.... quietly...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    bestFriend = input(
        "Oh, sorry for bothering you, but what's the name of your best friend?\n"
    )
    time.sleep(0.5)
    db["bestFriend"] = bestFriend  # type: ignore
    os.system("clear")
    printt("1. Go around " + bestFriend + "'s cat", userStrDelay)
    printt("2. Get on top of it, if you're adventurous and like danger", userStrDelay)
    decision = int(fkey.getchars(chars=["1", "2"]))
    if decision == 1:
        os.system("clear")
        printt(
            "You slowly, and carefully tiptoe past "
            + bestFriend
            + "'s cat.\n\n You eye her closely, waiting for the moment that she'll wake up and start chasing you.\n\n"
            + fore(2)
            + " Surprisingly, she doesn't.\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Knowing where "
            + bestFriend
            + "'s room is located, which is downstairs, so at least you don't have to climb up the steps like you did with the porch. That's when your stomach growls. You're hungry, and haven't eaten in a while.\n\n As you walk past the kitchen, you see the fridge, as tall as the Burj Khalifa. But, there'e no time! You're an inch tall, and need help right away!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("1. Eat something from the refrigerator", userStrDelay)
        printt("2. Find " + bestFriend, userStrDelay)
        decision = int(fkey.getchars(chars=["1", "2"]))
        if decision == 1:
            refrigerator()
        elif decision == 2:
            saveGame()
            storyLocation = "15"
            plotPointFive()
            return bestFriend
    elif decision == 2:
        os.system("clear")
        printt("Pfft, how dumb you are!\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            fore(1) + "I mean.... WHY WOULD SOMEONE DO THIS?!\n\n" +
            style(0), userStrDelay
        )
        time.sleep(0.5)
        printt(
            "Anyhoo, you grip the smooth fur of"
            + bestFriend
            + "'s cat and start to climb. By the moment you reach the top, you hear a loud purring sound below you!\n\n "
            + fore(1)
            + "GREAT.... YOU MADE IT WAKE UP!"
            + fore(13)
            + " Oh wait... she's going back to sleep.\n\n"
            + style(0)
            + "That's when she cleans herself with her paws, and then touches you!-- Almost.... as you're still slowly crawling on her.\n\n You then leap off the feline, and fall to the floor.\n\n 'Purrrrrrrr....'\n\n Lying on the ground, you slowly get up, and your eyes widen in horror....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Two, large, emerald colored eyes fixates on YOU....\n\n"
            + fore(1)
            + "THE FURRY FELINE BEAST HAS AWAKENED! \n\n NOW WHAT?!\n\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'Nice kitty, nice kitty', you say, slowly backing away.'Nice kitty, niiiiiccceee kitty, nic- MMMFFFF!'\n\n Your friend's cat lifts her paw and tries to make you shut up somehow, or maybe asserting dominance on you, since all cats have this weird trait...\n\n"
            + fore(1)
            + " Or maybe is trying to KILL YOU?!🙀\n\n"
            + style(0)
            + "With all your might, you attempt to lift her paw as if it was a boulder, therefore making you even more weak and tired.\n\n Once you're free, you try to crawl to safety.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'HEEEY! SOMEBODY HEEELLLLPPP!', you scream. Your voice comes out extremely faint. No one can help you.... You're all alone!\n\n As you try to run, "
            + bestFriend
            + f"'s cat lifts her paw AGAIN, attempting to squash you.\n You roll over, just like you did with the praying mantis last night, and dodges it in no time! Gaining back your strength, you start to run and {fore(1)}{style(3)}that's when you hear an odd, deafening whirring sound....\n\n And worse than that, the cat's coming closer! Great, the dangers never end, right?{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt("'MYOOOWWRRRRR!'\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            bestFriend
            + f"'s cat menacingly growls at you.\n\n 'NO-NO-NO-NO-NO!', you try to shield yourself, but it's too late. The black beast lifts her paw for the damn third time... And instead of smashing you, it tries to flick you, which successfully happens, due to you being 2.54 cm tall of course.\n\n You're thrown backwards, and land on the thick carpet of the living room. The whirring sound gets louder and louder.... A table fan? Sounds just like it...\n\n But IT'S NOT, as you turn around, and gasp...",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "'OHH-NOOOOOO!'\n\n"
            + fore(1)
            + "It's a vacuum cleaner. And it's not one of those old ones that have a bag in it. It's one of those tube-like ones, yeah, those plastic ones. The ones made by Dyson and many others....\n\n"
            + style(0)
            + "And, now you're in front of it....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(3)
            + "YOU HAVE TO MOVE! NOW!"
            + style(0)
            + "\n\n You get up, scrambling to your knees, and you RUN. The wind from the vacuum blew like a hurricane, stalling you. You continue to move forward by a couple of steps, BUT IT'S TOO LATE!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Blown away by the roaring wind speed of the vacuum cleaner, you swiftly grab the bristles and skid on the carpet, hanging for dear life. However, you're afraid even though you'll survive the ordeal of the vacuum cleaner, "
            + bestFriend
            + "'s cat might be looking for you again!\n\n 'AAAAAAAIIIIII!'",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1)
            + "\n\n You lose your grip, and fly up..... and UP! But, to where?\n Why, of course, the INTERIOR of the vacuum cleaner!\n\n You're still airborne, as you make way into the cylinder (the one that picks up all the dust/dirt, I forgot the name). You try to shout for help, but your voice is inaudible from the depths of the cylinder."
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"Admit it, being inside a vacuum cleaner is pretty dizzy, terrifying, and is like being in a tornado. A MESSY, BLURRY TORNADO.\n\n You're spun around repeatingly, along with the dust balls, as big as cars (or any other object, like a mouse or whatever...). Also, the contents in the vacuum are continuously going up-and-down, up-and-down, up-and-down....\n\n You get knocked out by a flying dust ball, all thanks to the rapid winds! Cuz, physics, right?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            fore(1)
            + "WHEN WILL THIS STOP?!"
            + style(0)
            + "\n\n That's exactly the question you're asking as you continue to spin. You shut your eyes, thinking that this IS THE END. Your life flashes before your eyes.... \n\n The whirring sound deafens your tiny ears....\n\n IT IS OVER! IT'S OVER!.....\n\n Noooooooooooooooooooo!--(Just joking, LOL 😂)",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            fore(10) + "\n\n The whirring sound.... STOPS. Whew!" +
            style(0), userStrDelay
        )
        time.sleep(0.5)
        printt(
            "\n\n You fall to the bottom of the vacuum's cylinder with a hard SLAM...\n\n At least the terror's OVER though!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(11)
            + "But, how the heck are you gonna get out of here?!\n\n"
            + fore(1)
            + "YOU'RE TRAPPED INSIDE A F**KING VACUUM CLEANER!"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"You bang the curving walls of the cylinder container, shouting for help, but its completely pointless! Why? Well... It's tiring and your voice is tiny, nuff said!\n\n {fore(1)}That's when the ground suddenly shifts underneath you... AGAIN!\n\n {style(0)}Someone's picking up the vacuum cleaner! Likely, he/she will empty it out of the container and then dump it in the garbage.\n\n  Would you rather NOT be dumped in the trash? I guess not!\n\n"
            + fore(11)
            + " Ya better think fast! Which you do so anyway..."
            + style(0)
            + "\n\n As soon as the container at last finally opens, you start to slide down and JUMP!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n'GEROMINOOOOOOOOO!'\n\n You hit the kitchen tiles, roll over, and come to a stop, with your back paining from just hitting the floor. Ouch....\n\n You breathe a sigh of relief, get up, and make your way to "
            + bestFriend
            + " 's room....",
            userStrDelay,
        )
        storyLocation = "15"
        saveGame()
        plotPointFive()


def encounterTwo():
    global userStrDelay, bestFriend, numDeaths, storyLocation
    os.system("clear")
    printt(
        "After about 10 minutes, you see a body of water. Must be a small puddle.\n\n You come closer to it and see the outline of your reflection in the water.\n\n"
        + fore(2)
        + "Finally! You've found water, and that'll quench your thirst!\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You cup your hands to collect the water, and drink it in big gulps.\n\n You're now feeling refreshed, and you're ready to go!\n\n That's when you're suddenly knocked off your feet by a large creature! Or is it something else?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "'HEY!', you shout. 'WHO GOES THERE?!'\n\n No response. The mysterious (creature/whatever that is) comes into view... slowly....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'Who's there?', you question again. And that's when you see IT--\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "It's a praying mantis, which is the size of a cargo truck.\n\n Staring at you, silently....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You don't even move a bit, as you don't know what's gonna happen...\n\n The mantis then spits out a large,"
        + fore(2)
        + " sticky, green substance,"
        + style(0)
        + "which hits you in the face!\n\n'Yuck!', you say in disgust. Is that the defense mechanism? Or a way for the mantis to attack its prey?\n\n 'Don't ever do that to me AGAIN!', you warn. That's when the mantis lifts its thick exoskeletal leg, and you're thrown into the air!\n\n 'WHOAAAAAHHHHHHHHHH!'\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You then are sent backwards, and the mantis is coming for you!\n\n You try to shield yourself, but it's too late!\n\n The mantis throws you in the opposite direction...\n\n You then fall to the ground, weak from being tossed over and over.\n\n Terrified, you try to crawl to safety.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        f"The praying mantis comes to you again.... eyeing its prey: You! \n\n 'NO! PLEASE! STOP!', you scream in terror. But, its too late. You're flown in the air for a third time....\n\n{fore(1)} That praying mantis might've been trying to capture you, and then.... EAT YOU.....\n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        f"**THUD**\n\n\n You hit the nearest blade of grass, and slide down in a quick pace. You're weak.... very weak....\n\n You see the mantis's head towering over you.\n\n{style(3)}'Oh man, it's over....'{style(0)}, you thought.\n\n The mantis sets down its right leg... and as you turn to face the ground (in order to see a weapon that you could reach), it clasps onto your whole head! You feel it cut into your skin...\n\n{fore(1)} The leg pins you to the ground, and you can't move.{style(0)}\n\n 'I'm sorry, I'm sorry, I'm sorry, I'm sorry, I'm sorry', you think as you try to endure the pain.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(3)
        + "Well, what now? You're in grave danger, its now nighttime, and you're not sure if you'll make it out alive!\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Wait until the mantis lifts its leg and try to run", userStrDelay)
    printt("2. Try to scare the mantis away", userStrDelay)
    printt(
        "3. Do nothing, maybe you'll not be mantis chow, as it'll ignore you later",
        userStrDelay,
    )
    escapeRoute = int(fkey.getchars(chars=["1", "2", "3", "4"]))
    if escapeRoute == 1:
        os.system("clear")
        printt("You wait for the praying mantis to lift its leg...\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            fore(2)
            + "And sure enough, it does!"
            + style(0)
            + "\n\n With a groan, you roll over slowly, just as the mantis lifts its leg...\n\n And sets it down again, chittering in bewilderment.",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(
            f"You then start to roll over, crawl on your knees, and roll again. You continue this pattern in order to escape...\n\n {fore(1)}But, the praying mantis is NOT DONE WITH YOU YET! It's coming for you!{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You roll over again.... and that's when you fall!\n\n You then land on something warm....something soft...\n\n"
            + fore(12)
            + " And ALIVE!"
            + style(0)
            + f" You feel a sea of pulsating bodies below you-- What's going on?Not only THAT, but you feel the prick of tiny feet crawling on your back. Your heart starts to race as you're constantly trampled over!\n Squinting in the moonlight (which answered your question on what's currently happening), you realize what you're lying down on: an ant 🐜 .\n\n And, there are multiple ants around you, spread out like a carpet. Ants as big as dogs!\n\n 'At least I found a hiding place', you mutter. But, what will the ant colony do to you?\n\n Take you prisoner? Eat you alive?\n That's when another ant comes on top of you, and you open your mouth to scream, and the ant's hairy head dives into your open mouth!\n\n The disgust of tasting an ant's head forces you to GET OUT OF HERE-- FAST! You chuck the ant's body away, and start to push several ants as you start to run, flinging their lifeless bodies. You try to get the metallic taste of the ant's head off your mind, but you can't stop thinking about throwing up.🤢\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "You continue pushing away the ants and try to find a way out of this hole. Like an insect searching for light, you find an underground tree root, and grasp onto it.\n\n"
            + fore(1)
            + " That's when something slimy curls onto your leg! You still dangle there, holding onto the root. What was that? Another ant? But it feels sticky....\n\n Then, you realize what it is...."
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(fore(5) + "A worm.\n\n" + style(0), userStrDelay)
        time.sleep(0.5)
        printt(
            "Just a regular worm, right?\n\n But not when you're 2.54 cm tall! To you, its size of a big anaconda.\n\n\n You remember those pictures that you Googled online about what a worm looks like.... under a microscope (Don't Google it, its really really gross and terrifying, but this is God's creations, and we should acknowledge it).\n\n The good thing is that worm looks less scary, with its creepy mouth looking like a blobfish combined with a snake. But, the bad thing is, its slithering slowly onto your body. And, its pulling you down! -- slowly...\n\n 'LET GO OF ME !', you screech at the top of your lungs. The worm still continues to crawl on your body, and you can feel its slimy body on you. You start to shiver.\n\n"
            + fore(3)
            + " Ya gotta focus on getting out of here!\n\n"
            + style(0)
            + " Despite the worm being on your leg, you still muster with all your strength to get out of this dim, dark hole.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You finally pull yourself up, with your arms/legs aching. The worm's still on your leg, though.{fore(14)} Now, where did the praying mantis go to?{style(0)}\n\n{fore(1)}\n\n Your question is answered when you hear a chitter, and see that you're face to face with the mantis! OK, Round 2, isn't it?{style(0)}\n\n'Please don't hurt me...', you moan. The mantis coldly stares at you with its buggy eyes.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "That's when you get an idea. You pull the worm off your thigh. It feels heavy, like grabbing a pouch of flour.\n\n'Ya wanted a snack?', you ask the praying mantis, and you then throw the worm at the mantis. 'THEN GO GET IT!'\n\n Therefore, the mantis grabs the worm and leaves the area.\n\n"
            + fore(2)
            + "Success!\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(
            "No time to celebrate though. That praying mantis could likely come after you... especially after it eats the worm....\n\n Secondly, you have to find a place to sleep in for the night. And, the worse part is that it'll be in the front yard....\n\n Danger could could be lurking ANYWHERE...\n\n You stagger to the puddle where you drank water from, and lay down next to it, hugging yourself in order to not freeze to death...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You fear several things.....\n\n 1. Will I survive the night? \n\n 2. Am I gonna die? \n\n 3. Will I be able to get out of here? \n\n And, lastly, within any moment.... you're going to start shrinking even more! Think about it.....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You try to fall asleep, but the fear of being eaten by any insect or any kind of animal keeps you awake. You're not sure if you're going to survive the night, but you're definitely going to be alright.....\n\n'You're gonna be A-OK,', you say to yourself.\n\n 'You'll be back... soon!'\n\n Closing your eyes, you repeat these words over and over again, and within a few minutes, you doze off.....😴\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        storyLocation = "14"
        saveGame()
        nextDay()
    elif escapeRoute == 2:
        os.system("clear")
        printt(
            "The praying mantis lifts its leg, and with a fast reaction time, you run!\n\n That's when you realize that you have a lighter in your pocket.\n\n You pull it out, come to a stop, and flick it open.\n\n The mantis is still standing on all fours.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "'BACK! BACK OFF!', you bellow, waving the flickering light at the mantis.\n\n Nothing happens. The fire's too small in order to make it scared!\n\n You need a bigger, brighter light source, but from where?\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "That's when you hear a deafening sound of a door being opened. Someone's outside! This is it!\n\n You stand up tiptoed, and see that a man is smoking a 🚬. You move closer and start to shout in order to get attention.\n\n'HEY! LOOK DOWN! I NEED HELP HERE! CAN YOU HEAR ME? A PRAYING MANTIS IS TRYING TO KILL ME! PLEASE, SAVE ME!'\n\n You wave your hands above your head constantly. You try again, but the man doesn't even see you,"
            + fore(1)
            + "and throws the cigarette towards the ground, and leaves.\n\n"
            + style(0)
            + "'WAAAIIIIITTT! DON'T GO!', you squeak. It's no use. Your voice is too small, it just comes out very very faint.\n\n The cigarette lands next to you, which makes you jump!\n\n You turn around and see that the mantis is moving closer..... and closer....\n\n You then see that cigarette which just fell. It's the size of a limousine, and smoke is coming out of it.\n\n",
            userStrDelay,
        )
        os.system("clear")
        time.sleep(0.5)
        print("(̅_̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅_̅̅_̅()ڪے")
        time.sleep(0.5)
        printt(
            fore(2)
            + "\n\n Hmmm, maybe you could use it like a grenade. You switch on your lighter, set fire to the cigarette , lift it up with all your might, and throw it at the mantis.\n\n 'TAKE THIS!', you shout. The cigar only travels a few feet, but it's enough to burn the mantis.\n\n The mantis is now dead, and you can move on!\n"
            + style(0),
            userStrDelay,
        )
        os.system("clear")
        printt(
            "Now, you have to find a place to sleep in for the night. And, the worse part is that it'll be in the front yard....\n\n Danger could could be lurking ANYWHERE...\n\n You stagger to the puddle where you drank water from, and lay down next to it, hugging yourself in order to not freeze to death...\n\n",
            userStrDelay,
        )
        printt(
            "You fear several things.....\n\n 1. Will I survive the night? \n\n 2. Am I gonna die? \n\n 3. Will I be able to get out of here? \n\n And, lastly, within any moment.... you're going to start shrinking even more! Think about it.....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You try to fall asleep, but the fear of being eaten by any insect or any kind of animal keeps you awake. You're not sure if you're going to survive the night, but you're definitely going to be alright.....\n\n'You're gonna be A-OK,', you say to yourself.\n\n 'You'll be back... soon!'\n\n Closing your eyes, you repeat these words over and over again, and within a few minutes, you doze off.....😴\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        storyLocation = "14"
        saveGame()
        nextDay()
    elif escapeRoute == 3:
        os.system("clear")
        printt(
            "The praying mantis attempts to burrow your head to the ground.....\n\n.... And then SNAPS YOUR NECK IN HALF.....\n\n See how assumptions can be deadly?!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    else:
        os.system("clear")
        printt(
            fore(1)
            + "That praying mantis finally had its chance......\n\n Strangely, it knocks you out cold, and you fall into a deep sleep...."
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "....................................................................................................................\n\n.........................\n\n............",
            userStrDelay,
        )
        os.system("clear")
        time.sleep(0.5)
        printt(
            fore(3)
            + "You open your eyes.....\n\n What the heck just happened?"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"The first thing that you see is {fore(1)} the praying mantis staring down at you!{style(0)}\n\n 'W-What do you want?', you ask in a raspy voice.",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"\n\n The praying mantis doesn't even respond. It just stares at you.... silently......\n\n 'I SAID WHAT DO YOU WANT FROM ME!', you shout as you try to get up. Something is stuck to your arm.....\n\n You pluck it out, and find it's a.....\n\n....tranquilizer dart? Da F-",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"'OK, so-- you kidnapped me?', you ask the mantis. The praying mantis tilts its head, as if it was trying to listen to you.\n\n{fore(3)} Alright, this is pretty weird.....\n\n{style(3)} WHY WOULD AN INSECT KIDNAP YOU?!{style(0)}\n\n But, you saw the tranquilizer dart, so you have to investigate....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You find yourself in some kind of deep hole. Must the home of the praying mantis!\n\n You also try to find 'the light at the end of the tunnel', or in other words, an escape route....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"But, that tranquilizer dart.....\n\n WHY did it target you?\n\n A realization comes to your mind:{fore(1)} Has the government found you in this state, and plan to experiment on YOU?! 😱{style(0)}\n\n Sounds Orwellian....🫢\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"{fore(5)}Seriously, why would the Canadian government do that, LOL.\n\n Are you that dumb? 😂\n\n You ain't no conspiracy theorist--\n\n {style(0)}{fore(3)} Then it must be something else.....\n\n It might've stabbed you by accident or without intention....\n\n Hmmm.....{style(0)}",
            userStrDelay,
        )
        os.system("clear")
        printt(
            f"Suddenly, you hear some chattering outside... and some barking, meowing, squawking, and squeaking?\n\n Odd.....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You step outside of the hole, and gasp! Turns out that hole was fake! Everything around you (except the praying mantis) is {fore(9)} artificial! {style(0)}\n\n The realization of where you are hits you like a pile of bricks (or getting hit by a truck/bus/car?)....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        realization = Figlet(font="doom")
        time.sleep(0.5)
        print(realization.renderText("YOU'RE AT A PET STORE!"))
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"{fore(1)}And, you're like.... Seriously, TG 101..... SERIOUSLY?!?{style(0)}\n\n Why..... THIS?!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(3) + "YOU HAVE TO GET OUT OF HERE! But......\n\n How?!" + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "The sounds of the animals in the pet store disturbs you at a great pace. Why did they, the owners found you?! 😱\n\n Maybe they were aiming for the praying mantis, but not by intention, took you also!\n\n The praying mantis also exits the hole, and is now right next to you, staring at what's outside. 'Seems like we have to escape....', you tell the mantis, who doesn't even respond, 'I'm not even sure what to do NOW.... but, its nice talking with you.'\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You start to move forward, and that's when you bump into a glass wall! Or..... a glass cage?\n\n 'No,problem, I can just tip it over', you thought. But, you're not sure.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"With all your strength, you try to push the container over, but you're small, and the cage doesn't even budge!\n\n Panting, you try to push harder and harder.... but its no use!\n\n{fore(1)}{style(1)}{style(3)} You're trapped!{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(
            "There's another option though: Shout for help!\n\n 'HEY! LET ME OUT OF HERE! PLEASE!', you shriek, banging the glass container with both fists. No one hears you. People are too busy checking out the pets!\n\n Should you panic? Or not?!\n\n You try to get your brain thinking, but you're too tired to think.\n\n Suddenly, a mysterious voice rings in your head.......\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        message = f"""{fore(168)}
▓█████▄  ██▓▓█████
▒██▀ ██▌▓██▒▓█   ▀
░██   █▌▒██▒▒███
░▓█▄   ▌░██░▒▓█  ▄
░▒████▓ ░██░░▒████▒
 ▒▒▓  ▒ ░▓  ░░ ▒░ ░
 ░ ▒  ▒  ▒ ░ ░ ░  ░
 ░ ░  ░  ▒ ░   ░
   ░     ░     ░  ░
 ░                 {style(0)}"""
        time.sleep(0.5)
        print(message)
        time.sleep(0.5)
        message2 = f"""{fore(168)}
 ▄▄▄▄▄ ▄       ▄▄▄▄▄      ▄▄▄▄▀      ██▄   ▄█ ▄███▄
▄▀  █    █    █     ▀▄ ▀▀▀ █        █  █  ██ █▀   ▀
    █ █   █ ▄  ▀▀▀▀▄       █        █   █ ██ ██▄▄
 ▄ █  █   █  ▀▄▄▄▄▀       █         █  █  ▐█ █▄   ▄▀
  ▀   █▄ ▄█              ▀          ███▀   ▐ ▀███▀
       ▀▀▀

            {style(0)}"""
        time.sleep(0.5)
        print(message2)
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Without realizing what the in the world you're doing, you bang your head on the glass about three times in a row, then stagger backwards. The praying mantis then comes back into its hole.\n\n Then, you do a running start, and hit your head severely on the glass, having a third degree bruise.\n\n You then quickly fall unconscious.",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "About 12 minutes later, the owner of the pet store passes by the clear, glass container, and sees your teeny, limp body.\n\n Shocked by what he's seeing, he opens the container, picks you up, assuming that you're an action figure that has been misplaced, goes outside, and chucks you.\n\n Even though you actually are still alive, you're going to be dead within the next few seconds....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You hit the hard cement pavement, which cracks your skull, and you die from the impact.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
        numDeaths += 1
        storyLocation = "8"
        time.sleep(0.5)
        saveGame()
        heaven()


def plotPointFour():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "As you continue to float, something pops your bubble! And, then ANOTHER GUST OF WIND BLOWS YOU AWAY!\n\n History just repeats itself, right?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(3)
        + "Alright, WHERE will you end up now?"
        + style(0)
        + "\n\n Let's just hope it won't be inside another human....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Something grabs your back!😱\n What is it? \n\n You turn around and see that a fly is carrying you 🪰 , a fly as big as a dog!\n\n The worst part is, since you're larger, the fly cannot support your weight, and the fly.... NOSEDIVES!",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        fore(1)
        + "The whole room is spinning as you and your fly fall. You're gonna hit the pavement, and possibly DIE!\n\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "The fly lets go of you.... AT THE LAST MOMENT, and you're thrown into some random stranger's front yard. You slide and skid onto the brown dirt as you land, and come to a stop.",
        userStrDelay,
    )
    printt(
        "As you get up, you hear a crunching sound in the distance. You run over to investigate.\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Turns out that fly hit the pavement and got killed!\n\n Well then, I guess its time to mourn and say goodbye 😢--",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Oh, wait. NO TIME.\n\n You're two inches tall--\n\n Or are you?....\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You find out that the distance from the sidewalk to whose front yard has expanded a bit--\n\n NO! IT CAN'T BE!--\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(1)
        + "To your eventual horror, you realized that you shrunk even more.... to about an inch tall! 😱😱😱\n\n (which is about 2.54 cm)"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Great.... Are you going to shrink to nothing?! ARE YOU?!?\n\n", userStrDelay
    )
    time.sleep(0.5)
    printt(
        f"You try to calm down, in order to get your 🧠 working....\n\n 'C'mon..... think..... THINK!', you thought. You're nearby the city, you're waaay too small, and you need help right away....",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "That's when you recognize a house located 2 blocks away from where you're standing. It's your best friend's house! Maybe she can help you get back to normal. \n\n But, what about the bus stop? The doctor's office?\n\n You look to your left, and see that the bus stop is only a block away.\n\n\n This choice depends on if you're adventurous.... or NOT!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Go to your friend's house (If you dare!)", userStrDelay)
    printt("2. Take the bus", userStrDelay)
    destination = int(fkey.getchars(chars=["1", "2", "3"]))
    if destination == 1:
        os.system("clear")
        printt("'OK, here goes...', you think to yourself.\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "You drag your feet on the sidewalk, and start to run. You constantly leap over pebbles as you ran across the sidewalk, panting. It seems like running a pretty long marathon, while being barefoot! Your shoes slap the pavement, but they BARELY make a sound....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You come to a stop, being tired , and take off one of your shoes, then your socks.\n\n And you're shocked by what you see...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1)
            + "Your feet are swollen, and is in extreme pain.\n\n All because of running... A LOT! (And, also other stuff too...)\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(6)
            + "But, you don't care on how much pain you endure throughout your journey... \n\n You're just going to keep running, and running, and running, and running, and running,until you reach that house!"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(
            "Realizing that it'll take forever just by being on the sidewalk, you decide to take a shortcut... in the grass...\n\n Also, your mouth is dry, and you desperately need water.\n There might be an 'oasis' nearby.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        printt(
            f"You enter the tall grass, which now rose high as tree trunks.{fore(3)} How would you find your way?{style(0)}\n\n You're not sure, but you only have to depend on your instincts, or luck 🍀 .\n\n Sprinting as fast you can, you push the sharp blades of grass quickly.\n\n You gaze up, and see that its getting dark. Guess you have to stay in for the night! But where?\n\n {style(9)}It's dangerous to go out alone, take--{style(0)}(Ah, forget it. You have nothing in your inventory)\n\n Since the sun's setting, seems like you need a light source, a torch. But, where would you find it?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        saveGame()
        storyLocation = "13"
        encounterTwo()

    elif destination == 2:
        os.system("clear")
        printt(
            "Spinning on your heels, you turn around and head to the bus stop.\n You wait for a car to pass by, and cross the road, free from danger.",
            userStrDelay,
        )
        storyLocation = "10"
        saveGame()
        plotPointTwo()


def planB():
    global userStrDelay, numDeaths, storyLocation
    printt("1. Use a 💣", userStrDelay)
    printt("2. Escape through the esophageal sphincter", userStrDelay)
    printt(
        "3. Exit out the other end "
        + fore(4)
        + "(Yes, THAT other end.... if you have a pretty dirty mind.... 🫢 )"
        + style(0),
        userStrDelay,
    )
    escapeRoute = int(fkey.getchars(chars=["1", "2", "3"]))
    if escapeRoute == 1:
        os.system("clear")
        printt(
            "Surprisingly, you have a ⚛️mic bomb in your pocket, and you implant near the stomach wall. You then wait for a few minutes....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("And then....\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        kaBoom = Figlet(font="slant")
        print(kaBoom.renderText("KA-BOOM!"))
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Pretty much everything explodes! Especially the person that just ate you.....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1)
            + "Congratulations, you idiot! You've committed murder! Would you like to be chased by the cops and get sentenced to life in prison--\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt("Oh, wait.....", userStrDelay)
        os.system("clear")
        printt(
            "YOU ARE ALSO EXPLODED TO BITS. Guess you underestimated the power of the atomic bomb, just like how America did back in 1945....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "💣 GAME OVER 💣", userStrDelay)
        numDeaths += 1
        time.sleep(0.5)
        saveGame()
        playAgain()
    elif escapeRoute == 2:
        os.system("clear")
        printt(
            "You try to find some kind of 🪜 that you could use to climb up. Maybe you could open the esophageal sphincter like a trapdoor 🤔\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"That's when you see the folds in the stomach walls. It's the rugae! This can be likely be your ladder!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "You immediately grip the stomach wall and climb upwards as if you were Spider-Man.\n\n The wall feels sticky, so it actually helps you from not slipping and falling to your death....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n After carefully climbing up, you reach the esophageal sphincter, and dig your shoes into the rugae, leaning while you're upside down. Could you open the sphincter? You try by using one hand.\n\n Nope, its too heavy for your little hands. You then try both hands, and sure enough, it doesn't work.\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"That's when you realize that the esophageal sphincter MUST DETECT FOOD from outside the body.\n\n But, that would mean waiting forever in order to escape! You could die from this intense heat!\n\nYou wipe away the sweat from your brow as you try to think....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"\n .....Hey, remember the 🥤 that got you in trouble in the first place? It might be the perfect time to get burped out....\n\n You look down, and to your luck, gas bubbles are rising from the stomach acid, coming towards you!",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "You're so excited to see what's happening below you, that you accidentally let go and fall!\n\n 'GAAAAAAHHHHHH!'\n\n"
            + fore(1)
            + "Is this THE END?!\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(2)
            + "Fortunately, one of the 🫧 s engulfs you. You're now INSIDE IT! YES! YOU CAN FINALLY GET OUT OF HERE!\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "The esophageal sphincter finally opens, and therefore....", userStrDelay
        )
        os.system("clear")
        time.sleep(0.5)
        soundEffect = Figlet(font="larry3d")
        print(soundEffect.renderText("**BUUURRRRPPPP**"))
        time.sleep(0.95)
        os.system("clear")
        time.sleep(0.5)
        printt(
            fore(2)
            + f"{style(3)}{style(1)}🥳 YOU DID IT! YOU'RE FINALLY OUT OF THAT GUY'S BODY! HOORAY! 🥳"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"However, you're still in your little bubble, and you have absolutely no idea where will you end up next!",
            userStrDelay,
        )
        storyLocation = "12"
        saveGame()
        plotPointFour()
    elif escapeRoute == 3:
        os.system("clear")
        printt(
            "OK, I have absolutely NO idea on why you selected this, but I hate to say this....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n YOU'RE IN FOR A " +
            fore(1) + "NOT " + style(0) + "REALLY FUN RIDE...\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "Looking across the stomach acid, you see the pyloric sphincter in front of you.... Could that be an exit? Kind of...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "But, how would you get there? You need some kind of boat...", userStrDelay
        )
        time.sleep(0.5)
        printt(
            f"Then, you spot a graham cracker in the distance, floating towards you.\n\n Maybe that could be your 'boat'.\n\n You make the leap, and land on the cracker, feet first.\n\n The problem is that, the cracker can dissolve in the stomach acid... at any time!\n\n Figuring out that you have to hop on one food 'platform' to the other in a fast pace, you constantly jump from one random food piece to the other, as if you're walking on hot bricks.",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n\n And, with that, you finally make it to the other side of the stomach, landing on a Dairy Milk Bar. The pyloric sphincter's in your reach!",
            userStrDelay,
        )
        printt(
            "But, that's when you see the stomach walls curving "
            + fore(1)
            + " inward....\n\n"
            + style(0),
            userStrDelay,
        )
        printt("\n Uh-oh, what's happening?😨😰", userStrDelay)
        time.sleep(0.5)
        printt(
            f"\n 'WAAAAUUGGHH!'\n Your chocolate boat (and you) veer to the left! And to the right!\n\n You're thrown upwards into the air, and oddly... the 'room' tilts! Seems like the guy who unknowingly ate you alive is getting up from his chair, and the titling proves it! (Alongside with the stomach churning like a blender...)\n\nYour entire body hits the lining of the stomach, and the wall sends you flying backwards! Like a coil in a spring, the shifting walls push you around constantly, with a high chance that your eventual death will be in the stomach acid below....\n\n You don't even know where you're going, you're just being tossed in the dark...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "As you continue falling, something sucks you in, like a vacuum. Is that the pyloric sphincter?\n\n\nIt might be...\n\n",
            userStrDelay,
        )
        os.system("clear")
        time.sleep(0.5)
        printt(
            "You tumble downwards, and the ground feels a bit ticklish.\n\n It feels like fingers touching your back!... Or something else....?",
            userStrDelay,
        )
        printt(
            "\n\n Sprawled on your back, you look at what's in front of you, and also what in the world is touching your back....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "That's when a "
            + fore(10)
            + " green-"
            + fore(3)
            + "yellow "
            + style(0)
            + "like liquid drenches you. Worse than that, you accidentally gulp it down! Ewww...\n\n You realize what it is.... its bile from the pancreas!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "At this moment, you literally feel like vomiting....\n\n But the leftover churned up bits (and liquid) from the stomach has entered the duodenum and is coming towards you!\n\n\n You run away from that stream as fast as you can, but no!\n\n"
            + fore(1)
            + "It takes you in!\n\n\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Sputtering in the thick bile-acid mixture, you try to swim in it, but it tires your arms and legs...\n\n You're constantly ascending, descending, and doing loop-de-loops in the small intestine."
            + fore(0)
            + "Its a lot like a roller-coaster, except the fact that its pitch black, smelly and ticklish....."
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            fore(6)
            + "Wait.... those finger-like projections were villi! Maybe you could grasp onto it!\n\n Despite the fact that your vision is terrible (Not because that you have bad eyesight, its because the interior of the human body is dark and hot)...."
            + style(0)
            + ""
            + fore(1)
            + "\n\n Suddenly, the peristalsis starts!"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1) + "\n\n Oh-No..... YOU'RE GONNA GET CRUSHED!" +
            style(0), userStrDelay
        )
        time.sleep(0.5)
        printt(
            f"You shoot out your tiny arms, trying to grab on something.... And you do latch onto something!\n\n But, WHAT is it?....",
            userStrDelay,
        )
        os.system("clear")
        time.sleep(0.5)
        printt(fore(2) + ".... IT IS ONE OF THOSE VILLI!\n\n" +
               style(0), userStrDelay)
        printt(
            "\n\nBut, ya better hang tight!\n\n The small intestine is moving up and down like a wave as you try to hold on. You almost lose your grip as you're tossed into the air.... And then you can't hold it anymore!\n\n\n 'NOOOOOOOOOOOOOOOOOOOO!'\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"You sail into the air, and continue in a falling-flying pattern as you venture into the deeper depths of the small intestine. Man, WHEN WILL THIS END?!",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(f"\n\n\nWHEN?!!!!?\n\n", userStrDelay)
        os.system("clear")
        printt(
            "After what seemed like half an hour, you hear a squelching sound...... Gross!\n\n\n And then....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(13) + "**POP!**" + style(0), userStrDelay)
        os.system("clear")
        printt(
            "The sphincter connecting the small intestine w/ the large intestine flings you toward the inner crevice of the ascending colon. You grab onto the edge, and hoist yourself upwards. Everything feels so dry, damp, and.....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(11)
            + ".... Its pretty stinky in here! You're smelling absolutely nothing but poop....\n\n"
            + style(0),
            userStrDelay,
        )
        printt(
            r"You gaze downwards, and see the appendix, which is the size of a rope! Or something else.... I can't even find the words for it ¯\(ツ)/¯",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n\nYou look up, and see that you've a LOOOOONNNNGGGG way to go, in order to find the exit!\n\n That's when you hear another sound....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("'Yeeaaaaghhhh!'\n\n\n", userStrDelay)
        printt(
            f"You're thrown upwards into the air, and collapse onto the intestinal floor. It seems like the effects of peristalsis pushed you towards the middle of the ascending colon!\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"Then, you tumble and start to slide down. You continuously cough out feces, as your lungs are filled up with it! Yeah, I am grossing you out a bit, but this is TOO MUCH--\n\n",
            userStrDelay,
        )
        os.system("clear")
        time.sleep(0.5)
        printt(
            f"You then rapidly free fall in the descending colon. As you fall, you feel some movement outside the body, and come to a horrifying thought....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n.... You're gonna be defecated out of someone's "
            + fore(0)
            + "[CENSORED]!(In order to avoid moderator warnings)"
            + style(0)
            + "\n\n You've made a mistake! YOU HAVE TO GET OUT OF HERE, BUT IN ANOTHER WAY!\n\n But, you can't stop your fall!-",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            "'Unngh!'\n\n You hit the curved section of the descending colon..... And you start to roll over, with your body being weak and tired.....\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "(DON'T PICTURE IT, DON'T PICTURE IT....... JUST DON'T PICTURE IT!!!)\n\n.... You plop right into the rectum, with the two sphincters squeezing your body!\n\nAnd, that's when you hear the guy's pants UNZIP.....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("(PLEASE DON'T PICTURE IT, PLEASE!)\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "You look up, and scream! A ball of 💩 is rolling towards you! Its like an Indiana Jones situation, but worse (and more dirty/inappropriate actually).\n\n Could you escape?! COULD YOU?!?\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        badSituation = Figlet(font="doom")
        print(badSituation.renderText(
            fore(1) + "NO \n YOU CAN'T ESCAPE....." + style(0)))
        time.sleep(0.5)
        os.system("clear")
        printt(
            "The lump of crap barely crushes your legs. You then feel the tightness of the rectum's sphincters, pushing you towards Uranus.... GET IT?!\n\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "Pretty soon, your head pops out of the guy's anus (OH GOD, PLEASE DON'T PICTURE IT! PLEASE DON'T!), and you see the toilet water down below....",
            userStrDelay,
        )
        printt(
            "'HEY! DON'T FLUSH THE TOILET AFTER YOU EXPEL ME! I NEED HELP! PLEASE!', you bellow. But the guy's still busy taking a dump. Suddenly, the tightening sensation you were experiencing is gone! You're free! You land into the toilet water.",
            userStrDelay,
        )
        printt("**SPLOOOSH**", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            f"The water feels cold... really cold....\n\n You gasp for air, and try to get the guy's attention, if he sees you as he flushes the 🚽.\n\nWaving your arms frantically, you shout out to him. 'DOWN HERE! YOU HAVE TO HELP ME!'\n\n He doesn't hear you, and you hear the sound of the toilet flushing! 'NO! WHY CAN'T YOU JUST SEE ME?! YOU'LL PAY FOR THIS!'\n\n\n You try to outrun it, but you can't! You're swept away, and get flushed down the toilet....",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(1) + "\n....And, into the sewers.....\n" +
               style(0), userStrDelay)
        time.sleep(0.5)
        storyLocation = "5"
        saveGame()
        sewerPlot()


def insideStory():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt("OK.... Are you dead?\n Maybe....", userStrDelay)
    printt(
        fore(3)
        + "\n\n... After all you're still falling, but where are you falling, actually?"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(0) + "\n\n Looking around, its pretty dark in here." +
        style(0), userStrDelay
    )
    time.sleep(0.5)
    printt(
        f"You attempt to stop your free fall by grabbing onto the wall, but its smooth, slimy, and slippery.\n That means there's no way to climb back up, and since its pitch black, you don't even know which way is up, or down--\n\n",
        userStrDelay,
    )
    os.system("clear")
    time.sleep(0.5)
    printt(
        fore(9)
        + "That's when.... the walls of the pink and slimy tube...\n\n ENGULF YOU?!\n\n Strange....\n Really strange...\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Realizing what the heck's going on, you finally put the puzzle pieces together...",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(1)
        + "\n\n YOU'RE IN THAT GUY'S ESOPHAGUS!\n\n\n And, pretty soon, you will be digested!\n\n\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"What's even worse, is that due to the effects of peristalsis, you're being squeezed extremely HARD... AND TIGHT.\n\n You gasp for air and try to wriggle out of the lump of smooth muscle tissue, but its no use.... You're stuck.\n\n Your ribcage is almost about to be crushed...\n\n ",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "'OOOOWWWWWWWWWWWWWWWWWWWW!', you scream as you're in extreme pain. You can't even stand this at all... You're going to die!\n\n\n Or, are you?\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"{fore(2)}The smooth muscle entrapped your arms and chest.\n\n Your legs aren't, as you can move them freely!{style(0)}",
        userStrDelay,
    )
    printt(
        "\n Using the amount of strength you have left, you try to lift yourself upwards by putting your feet on the opposite end of the esophageal lump and insert your foot into the hole.\n\n 'AAARRRRGGGGHHHHH!'\n\n No use.\n You've moved only a few centimeters. You're still in excruciating pain.\n ",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    printt(
        "You try again...\n 'C'MON! YOU CAN DO THIS!', you think to yourself. \n... and you move a little bit again.\n You try again....\n\n\n ... And again...\n\n And again ...\n\n And again....\n You still move at least 5 cm.\n Half of your body is out!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "The only thing left is the legs. Even though you're halfway out of that soggy lump, you're still in pain...\n\n But, who cares? You're almost there! You look up and see the roof of the stranger's mouth, high above you.\n\n And then you hear a **BUMP**\n\n\n What was that?!\n\n\n ",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "You find yourself sitting on some kind of sphincter. The good news is your smol legs are free (despite the intense pain). You stand up and that's when you start to fall! ",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "\n\n'AAAAAAAAAAAAAAAAHHHH!'\n You slide onto a wall filled with folding sections (and mucus), and fly towards the opposite direction. Thank heavens you missed the acid!",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "'Ooogh!'\n\n Your back slams onto the stomach floor. You get up and try to see where you fell from, but its "
        + fore(0)
        + "still dark in here!"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "You hear gurgling sounds in the place you're in. Seems like you're in the stomach....\n\n Your eyes finally adjust to the pitch black darkness. The distance between the esophageal sphincter and you is too far, so that means its impossible to get out of here!\n Secondly, its a sauna in here!\n\n\n Well, what do I mean? Since the interior temperature of the human body is 30-34 degrees Celsius, which is equivalent to a pretty hot day (And possibly climate change? 🌡️ ).... 🥵\n\n\n That means a 50% possibility of you dying from heat stroke....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    print("  _   _                __        ___           _  ___ ")
    print(r"| \ | | _____      __ \ \      / / |__   __ _| ||__ \\")
    print(r"|  \| |/ _ \ \ /\ / /  \ \ /\ / /| '_ \ / _` | __|/ /")
    print(r"| |\  | (_) \ V  V /    \ V  V / | | | | (_| | |_|_| ")
    print(r"|_| \_|\___/ \_/\_/      \_/\_/  |_| |_|\__,_|\__(_)")
    time.sleep(0.5)
    os.system("clear")
    printt(
        "You drop to your knees, rest your head on the stomach wall, and start to sob....\n\n YOU HAVE LOST ALL PERSEVERANCE IN ORDER TO GET BIGGER....\n As you're enclosed in the abdominal cavity and the stomach, between layers and layers of fat... \nwith the possibility that no one will hear you....",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("But, you can't give up right away?\n\n\n Right?\n\n", userStrDelay)
    printt("1. Yes, I give up!", userStrDelay)
    printt("2. Find a way to get out of here... despite the risks", userStrDelay)
    printt("3. I'd rather commit suicide", userStrDelay)
    desperateSituation = int(fkey.getchars(chars=["1", "2", "3"]))
    if desperateSituation == 1 or desperateSituation == 3:
        os.system("clear")
        printt(
            "Oh, so you gave up?\n\n\n Mmmmmmmmmmmmmmmmmmmmmmmmm................\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "............. kay.\n You continue to cry.... And you cry so much that you drown in a pool of tears...",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(6) + "💧 GAME OVER 💧" + style(0), userStrDelay)
        numDeaths += 1
        saveGame()
        playAgain()
    elif desperateSituation == 2:
        os.system("clear")
        printt(
            "Alright.......\n" +
            fore(11) + "HOW WOULD YOU GET OUT OF HERE?!" + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            "\n\n First off,you lost weight in an odd way @ the beginning, encountered a 🕷️ , had the feeling of what it meant (physically) to be isolated from the rest of the world, you believed that you could fly, got lifted by a crow, fell from a pretty high place, got swallowed whole, and you have endured the worst elevator of your life, and now put yourself into a situation that'll likely leave you dead.... What to do....\n What to do...\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("1. Holler for help", userStrDelay)
        printt("2. Try to escape through the esophageal sphincter", userStrDelay)
        printt(
            "3. Exit out the other end "
            + fore(4)
            + "(Yes, THAT other end.... if you have a pretty dirty mind.... 🫢 )"
            + style(0),
            userStrDelay,
        )
        escapeRoute = int(fkey.getchars(chars=["1", "2", "3"]))
        if escapeRoute == 1:
            os.system("clear")
            printt("You yell at the top of your 🫁 s:\n\n", userStrDelay)
            printt("\n 'HEY! YA HEAR ME!'\n\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                "'I'M DOWN HERE! INSIDE YOUR BODY! WHY'D YOU HAVE TO GODDAMN EAT ME?! WHYYYY!'",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(fore(1) + "No response.\n\n" + style(0), userStrDelay)
            time.sleep(0.5)
            printt(
                "Do I really have to say this AGAIN?! YOUR VOICE IS TINY, SO THAT'S WHY NO-ONE CAN HEAR YOU!🤬",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            time.sleep(0.5)
            printt("Alright, another plan! But what will it be?", userStrDelay)
            planB()
        elif escapeRoute == 2:
            os.system("clear")
            printt(
                "You try to find some kind of 🪜  that you could use to climb up. Maybe you could open the esophageal sphincter like a trapdoor 🤔\n\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "That's when you see the folds in the stomach walls. It's the rugae! This can be likely be your ladder!",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "You immediately grip the stomach wall and climb upwards as if you were Spider-Man.\n\n The wall feels sticky, so it actually helps you from not slipping and falling to your death....",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "\n\n After carefully climbing up, you reach the esophageal sphincter, and dig your shoes into the rugae, leaning while you're upside down. Could you open the sphincter? You try by using one hand.\n\n Nope, its too heavy for your little hands. You then try both hands, and sure enough, it doesn't work.\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "That's when you realize that the esophageal sphincter MUST DETECT FOOD from outside the body.\n\n But, that would mean waiting forever in order to escape! You could die from this intense heat!\n\nYou wipe away the sweat from your brow as you try to think....",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "\n .....Hey, remember the 🥤 that got you in trouble in the first place? It might be the perfect time to get burped out....\n\n You look down, and to your luck, gas bubbles are rising from the stomach acid, coming towards you!",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "You're so excited to see what's happening below you, that you accidentally let go and fall!\n\n 'GAAAAAAHHHHHH!'\n\n"
                + fore(1)
                + "Is this THE END?!\n\n"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                fore(2)
                + "Fortunately, one of the 🫧 s engulfs you. You're now INSIDE IT! YES! YOU CAN FINALLY GET OUT OF HERE!\n\n"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "The esophageal sphincter finally opens, and therefore....",
                userStrDelay,
            )
            os.system("clear")
            time.sleep(0.5)
            soundEffect = Figlet(font="larry3d")
            print(soundEffect.renderText("**BUUURRRRPPPP**"))
            time.sleep(0.5)
            os.system("clear")
            time.sleep(0.5)
            printt(
                fore(2)
                + "🥳 YOU DID IT! YOU'RE FINALLY OUT OF THAT GUY'S BODY! HOORAY! 🥳"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "However, you're still in your little bubble, and you have absolutely no idea where will you end up next!",
                userStrDelay,
            )
            storyLocation = "12"
            saveGame()
            plotPointFour()
        elif escapeRoute == 3:
            os.system("clear")
            printt(
                "OK, I have absolutely NO idea on why you selected this, but I hate to say this....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "\n\n YOU'RE IN FOR A "
                + fore(1)
                + "NOT "
                + style(0)
                + "REALLY FUN RIDE...\n",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "Looking across the stomach acid, you see the pyloric sphincter in front of you.... Could that be an exit? Kind of...\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "But, how would you get there? You need some kind of boat...",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Then, you spot a graham cracker in the distance, floating towards you.\n\nMaybe that could be your 'boat'.\n\n You make the leap, and land on the cracker, feet first.\n\n The problem is that, the cracker can dissolve in the stomach acid... at any time!\n\n Figuring out that you have to hop on one food 'platform' to the other in a fast pace, you constantly jump from one random food piece to the other, as if you're walking on hot bricks.",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "\n\n And, with that, you finally make it to the other side of the stomach, landing on a Dairy Milk Bar. The pyloric sphincter's in your reach!",
                userStrDelay,
            )
            printt(
                "But, that's when you see the stomach walls curving "
                + fore(1)
                + " inward....\n\n"
                + style(0),
                userStrDelay,
            )
            printt("\n Uh-oh, what's happening?😨😰", userStrDelay)
            time.sleep(0.5)
            printt(
                "\n\n 'WAAAAUUGGHH!'\n\n Your chocolate boat (and you) veer to the left! And to the right!\n\n You're thrown upwards into the air, and oddly... the 'room' tilts! Seems like the guy who unknowingly ate you alive is getting up from his chair, and the titling proves it!\n\nYour entire body hits the lining of the stomach, and the wall sends you flying backwards! Like a coil in a spring, the shifting walls push you around constantly, with a high chance that your eventual death will be in the stomach acid below....\n\n You don't even know where you're going, you're just being tossed in the dark...\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "As you continue falling, something sucks you in, like a vacuum. Is that the pyloric sphincter?\n\n\nIt might be...\n\n",
                userStrDelay,
            )
            os.system("clear")
            time.sleep(0.5)
            printt(
                "You tumble downwards, and the ground feels a bit ticklish.\n\n It feels like fingers touching your back!... Or something else....?",
                userStrDelay,
            )
            printt(
                "\n\n Sprawled on your back, you look at what's in front of you, and also what in the world is touching your back....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "That's when a "
                + fore(10)
                + " green-"
                + fore(3)
                + "yellow "
                + style(0)
                + "like liquid drenches you. Worse than that, you accidentally gulp it down! Ewww...\n\n You realize what it is.... its bile from the pancreas!\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "At this moment, you literally feel like vomiting....\n\n But the leftover churned up bits (and liquid) from the stomach has entered the duodenum and is coming towards you!\n\n\n You run away from that stream as fast as you can, but no!\n\n"
                + fore(1)
                + "It takes you in!\n\n\n\n"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Sputtering in the thick bile-acid mixture, you try to swim in it, but it tires your arms and legs...\n\n You're constantly ascending, descending, and doing loop-de-loops in the small intestine."
                + fore(0)
                + "Its a lot like a roller-coaster, except the fact that its pitch black, smelly and ticklish....."
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                fore(6)
                + "Wait.... those finger-like projections were villi! Maybe you could grasp onto it!\n\n Despite the fact that your vision is terrible (Not because that you have bad eyesight, its because the interior of the human body is dark and hot)...."
                + style(0)
                + ""
                + fore(1)
                + "\n\n Suddenly, the peristalsis starts!"
                + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                fore(1) + "\n\n Oh-No..... YOU'RE GONNA GET CRUSHED!" + style(0),
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "You shoot out your tiny arms, trying to grab on something.... And you do latch onto something!\n\n But, WHAT is it?....",
                userStrDelay,
            )
            os.system("clear")
            time.sleep(0.5)
            printt(fore(2) + ".... IT IS ONE OF THOSE VILLI!\n\n" +
                   style(0), userStrDelay)
            printt(
                "\n\nBut, ya better hang tight!\n\n The small intestine is moving up and down like a wave as you try to hold on. You almost lose your grip as you're tossed into the air.... And then you can't hold it anymore!\n\n\n 'NOOOOOOOOOOOOOOOOOOOO!'\n\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "You sail into the air, and continue in a falling-flying pattern as you venture into the deeper depths of the small intestine. Man, WHEN WILL THIS END?!",
                userStrDelay,
            )
            time.sleep(0.5)
            printt("\n\n\nWHEN?!!!!?\n\n", userStrDelay)
            os.system("clear")
            printt(
                "After what seemed like half an hour, you hear a squelching sound...... Gross!\n\n\n And then....",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(13) + "**POP!**" + style(0), userStrDelay)
            os.system("clear")
            printt(
                "The sphincter connecting the small intestine w/ the large intestine flings you toward the inner crevice of the ascending colon. You grab onto the edge, and hoist yourself upwards. Everything feels so dry, damp, and.....\n\n 'Ewww---'",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                fore(11)
                + ".... Its pretty stinky in here! You're smelling absolutely nothing but poop....\n\n"
                + style(0),
                userStrDelay,
            )
            printt(
                r"You gaze downwards, and see the appendix, which is the size of a rope! Or something else.... I can't even find the words for it ¯\(ツ)/¯",
                userStrDelay,
            )
            printt("\n\n", userStrDelay)
            printt(
                "You look up, and see that you've a LOOOOONNNNGGGG way to go, in order to find the exit!\n\n That's when you hear another sound....\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt("'Yeeaaaaghhhh!'\n\n\n", userStrDelay)
            printt(
                "You're thrown upwards into the air, and collapse onto the intestinal floor. It seems like the effects of peristalsis pushed you towards the middle of the ascending colon!",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Then, you tumble and start to slide down. You continuously cough out feces, as your lungs are filled up with it! Yeah, I am grossing you out a bit, but this is TOO MUCH--\n\n",
                userStrDelay,
            )
            os.system("clear")
            time.sleep(0.5)
            printt(
                "You then rapidly free fall in the descending colon. As you fall, you feel some movement outside the body, and come to a horrifying thought....",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "\n\n.... You're gonna be defecated out of someone's "
                + fore(0)
                + "[CENSORED]!(In order to avoid moderator warnings)"
                + style(0)
                + "\n\n You've made a mistake! YOU HAVE TO GET OUT OF HERE, BUT IN ANOTHER WAY!\n\n But, you're hurtling too fast, and you can't stop your fall!",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            printt(
                "'Unngh!'\n\n You hit the curved section of the descending colon..... And you start to roll over, with your body being weak and tired.....\n\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "(DON'T PICTURE IT, DON'T PICTURE IT....... JUST DON'T PICTURE IT!!!)\n\n.... You plop right into the rectum, with the two sphincters squeezing your body!\n\nAnd, that's when you hear the guy's pants UNZIP.....",
                userStrDelay,
            )
            time.sleep(0.5)
            printt("(PLEASE DON'T PICTURE IT, PLEASE!)\n\n", userStrDelay)
            time.sleep(0.5)
            printt(
                "You look up, and scream! A ball of 💩 is rolling towards you! Its like an Indiana Jones situation, but worse (and more dirty/inappropriate actually).\n\n Could you escape?! COULD YOU?!?\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            os.system("clear")
            time.sleep(0.5)
            badSituation = Figlet(font="doom")
            time.sleep(0.5)
            print(badSituation.renderText("NO \n\n\n YOU CAN'T ESCAPE....."))
            time.sleep(0.5)
            os.system("clear")
            printt(
                "The lump of crap barely crushes your legs. You then feel the tightness of the rectum's sphincters, pushing you towards Uranus.... GET IT?!\n\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(
                "Pretty soon, your head pops out of the guy's anus (OH GOD, PLEASE DON'T PICTURE IT! PLEASE DON'T!), and you see the toilet water down below....",
                userStrDelay,
            )
            printt(
                "'HEY! DON'T FLUSH THE TOILET AFTER YOU EXPEL ME! I NEED HELP! PLEASE!', you bellow. But the guy's still busy taking a dump. Suddenly, the tightening sensation you were experiencing is gone! You're free! You land into the toilet water.\n\n",
                userStrDelay,
            )
            time.sleep(0.5)
            printt("**SPLOOOSH**", userStrDelay)
            time.sleep(0.5)
            os.system("clear")
            printt(
                "The water feels cold... really cold....\n\n You gasp for air, and try to get the guy's attention, if he sees you as he flushes the 🚽.\n\nWaving your arms frantically, you shout out to him. 'DOWN HERE! YOU HAVE TO HELP ME!'\n\n He doesn't hear you, and you hear the sound of the toilet flushing! 'NO! WHY CAN'T YOU JUST SEE ME?! YOU'LL PAY FOR THIS!'\n\n\n You try to outrun it, but you can't! You're swept away, and is flushed down the toilet....",
                userStrDelay,
            )
            time.sleep(0.5)
            printt(fore(1) + "\n....And, into the sewers.....\n" +
                   style(0), userStrDelay)
            time.sleep(0.5)
            storyLocation = "5"
            saveGame()
            sewerPlot()


def plotPointThree():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "You decided to wait for a gust of wind to blow you away, but nothing happens.",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\n That's when you're lifted off the porch and is sent flying into the daylight!\n\n",
        userStrDelay,
    )
    printt(
        "Well, how high? I gotta say, REALLY HIGH. \n You look down, and is amazed by how far you are. You've flew past your house, the bus stop, and ....\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "... The medical centre.\n Darn it!\n"
        + fore(1)
        + "How would you make it back?\n\n"
        + style(0),
        userStrDelay,
    )
    printt(
        "The problem is... the wind current determines where you're going, and you can't go in the opposite direction.\n\n",
        userStrDelay,
    )
    os.system("clear")
    time.sleep(0.5)
    printt(
        fore(0)
        + "Suddenly, a black bird-like figure, equivalent to the size of a jumbo jet swoops down on you!\n\n The blinding sunlight blurs your vision, so it's impossible to see.\n You squint your eyes and your jaw drops open..."
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "It's a giant crow.\n\n\n The crow's beak opens-- and snaps!\n\n And the crow's sharp claws grab the back of your shirt collar.\n 'Hey!', you yelp. Why is it taking YOU? \n\n And..."
        + fore(3)
        + " where is it taking you?"
        + style(0)
        + "\n\n To its nest?\n\n Or to feed its young?\n\n\n Or to adopt you?!\n\n\n 'Please don't drop me! Please don't drop me!', you beg.\n\n You and the crow rise higher and higher, You look down again, and sure enough, you're traveling in a section of your city that you don't recognize. Or, in other words, the crow is taking you to its nest... But that's your assumption... right?\n ",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Assume that the crow doesn't want you", userStrDelay)
    printt("2. Assume that it does want you as a 🪱", userStrDelay)
    print("What's your guess about your eventual future? (THIS IS A TRICK QUESTION!)\n Select an option:\n ")
    assumption = int(fkey.getchars(chars=["1", "2"]))
    if assumption == 1:
        os.system("clear")
        printt(
            "You wait for the crow for drop you...\n And, it doesn't. Its still taking you to its nest.\n OK, new bird family member... it seems like you have to be one with the birds!\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(12) + "🕊️ THE END 🕊️" + style(0), userStrDelay)
        quit(0)
    elif assumption == 2:
        os.system("clear")
        printt(
            "You wait for the crow to take you to its nest...\n .... And, surprisingly, your crow dips down, lower and lower...\n\n Did it not care about you at all? Or is it being nice to you?\n\n The distance between you and the ground is slowly decreasing as you continue to descend...\n\n ",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(fore(2) + "\n The crow drops you and you fall free! " + style(0), 0.04)
        time.sleep(0.5)
        os.system("clear")
        printt(
            "You're falling... at an extremely deadly FAST RATE!\n 'This is the END...', you thought.\n 'Goodbye world...'. You shut your eyes and brace for a hard landing...",
            userStrDelay,
        )
        time.sleep(0.5)
        printt("\n**SPLAT!**\n", userStrDelay)
        time.sleep(0.5)
        printt(
            "\nYou land face first into a " +
            fore(2) + " greenish paste.\n\n" + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt("YAAY! You're saved by--\n\n", userStrDelay)
        time.sleep(0.5)
        printt(
            f"--guacamole?\n You realize that as you see an onion 🧅 slice in the distance, which is the size of a hula hoop.\n\n You try to get up, but the sticky Mexican dip locks you in place. However, you can move your arms, but not the inferior portions of your tiny body.\n\n Coming to your senses, you hear people chattering, laughing, and whatever they're doing.\n\n You're at Taco Time, the downtown one! And, you're in the outdoor patio!\n\n{fore(3)}{style(3)} But, you're kilometers away from the medical center! Now, how would you find your w-\n{style(0)}",
            userStrDelay,
        )
        time.sleep(0.5)
        os.system("clear")
        printt(
            fore(1)
            + "The ground beneath you shifts all of a sudden. An earthquake?\n\n"
            + style(0),
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            fore(1)
            + "\nNo... its even worse!\n\n You're lifted from the guacamole and find out that you not just landed in the dip itself, you landed on a tortilla chip! 🌮 \n\n\n And, you look at what's in front of you, and let out a terrifying scream! It's a mouth of a university student, planning to take a bite of the chip!"
            + style(0)
            + f"\n\n'HEEEY!', you start shouting and wave your hands above your head. 'STOOOP! DON'T EAT ME! STOP!'.\n\n You try to get the guy's attention, but unfortunately, he {style(4)}doesn't{style(0)} see you on the chip.\n\n\n 'NNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!'\n\n\n Within nanoseconds you're plopped into the person's mouth! You get up, and that's when you see another tortilla chip, coming towards you! You duck down, {fore(2)}but luckily, the tortilla chip doesn't even hit you. Phew!{style(0)}\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        printt(
            f"That's when the CHEWING starts. Bits of tortilla chips are flying, and they're about as sharp as a knife! (for now...)\n You are tossed and turned constantly by the mastication of these chips. You try to hold onto something, but fail to do so.\n\n\n And, you gasp in horror as the soda starts coming in! You can't outrun that, though! You have to get out of the guy's mouth!--\n\n",
            userStrDelay,
        )
        time.sleep(0.95)
        printt(f"{fore(1)} Too Late....\n\n{style(0)}", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        printt(
            "\n You're swept away by the soda tsunami, and slide on the epiglottis....\n\n\n And fall.... down...\n\n down...\n\n Screaming all the way....\n\n",
            userStrDelay,
        )
        time.sleep(0.5)
        storyLocation = "11"
        saveGame()
        insideStory()


def encounterOne():
    global userStrDelay, numDeaths, storyLocation
    time.sleep(0.5)
    os.system("clear")
    printt(
        "You decided to look around for something to eat, then you remember that a bag of Cheetos was on the table. Unfortunately, you realize that you have to get to higher ground in order to reach the desired destination.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nRunning towards the nearest table leg, you immediately wrap your legs around it, hoist yourself up and started to climb... Even though you aren't a really good climber, LOL.\n Also, you're terrified of heights.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Within a few moments, and some pain in your arms/legs here and there,{fore(2)} you finally made it to the top.\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(f"{fore(2)}At least the Cheetos is still there, though...Yay?\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt(
        "Walking towards the bag, you notice its still open and there is only one Cheeto in there.\nYou then reach for that piece and try to pick it up, but its too heavy for just one hand. You have to use both of them!\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"The very same moment you attempt to take a bite of the entire Cheeto, {fore(1)}you hear a tapping sound...\n... {style(3)}And its coming from behind you...😨\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("What could it be? You turn around and gasp...\n", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(f"{fore(1)}...It's a spider...🕷️\n ... {style(3)}{style(1)}{style(4)}A BIG-ASS SPIDER!\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt(
        f"{fore(3)}And, its coming directly for you... or the Cheeto?\n Better find out!\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Fight the spider with your bare hands", userStrDelay)
    printt("2. Run", userStrDelay)
    printt("3. Make friends with the spider", userStrDelay)
    printt("4. Give the spider the Cheeto", userStrDelay)
    while True:
        try:
            print("What would you do now? Select an option:\n")
            decision = int(fkey.getchars(chars=["1", "2", "3", "4"]))
            if decision == 1:
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "You drop the Cheeto and then charge toward the spider.\nThat's when the spider pins you to the ground with its thin legs...you now can't move your hands! And your chest!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\nStruggling to stay alive, you kick its butt which then eventually lifts its leg, and then you bolt across the tabletop at pure lighting speed.",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\nNot even realizing where you were going, your legs catch air, and then all of a sudden, you realize that you fell off the table and falling towards the ground! Could you stop your fa--\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "\nToo late, you hit the floor with a hard THUD...\n", userStrDelay
                )
                time.sleep(0.5)
                printt(
                    f"{fore(2)}The only good thing about this that the spider can't find you. {fore(1)}The bad news, however, is that you have to climb up the table AGAIN.{style(0)}\n",
                    userStrDelay,
                )
                printt(
                    f"Catching your breath, you see the spider climbing down the table leg and {fore(1)}{style(1)}its going towards you!\n Turns out the spider {style(4)}is{style(0)}{fore(1)} going for you after all!\n{style(0)}",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Geez, you forgot that spiders can climb, right?\n", userStrDelay
                )
                time.sleep(0.5)
                printt(
                    "\nWell, you really need to start thinking on how to get past the spider without getting killed...\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Without thinking straight, you run past the spider, and eventually continue sprinting towards the table leg.\n ",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\nOddly, it seems to take an HOUR to get from point A to point B.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\nAs soon as you reach the table leg,you look back and see the spider coming towards you. You again hoist yourself upwards and climb in a fast pace.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Pretty soon enough, the spider is ALSO following your route to safety!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "\nAs you reach the top of the table, you realize that you have to kill the spider with something....\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "But with what? You pace frantically to find a weapon.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"{style(3)}Hey, why not use the corkscrew from that bottle?{style(0)}, you thought.",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Running towards the place where you placed the bottle earlier, you find the open corkscrew and lift it up with your tiny hands.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Carrying the anvil-sized corkscrew, you walk straight to the edge of the tabletop, and see that the spider's still climbing upwards.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Still holding the corkscrew, you let go of it, and it falls, therefore crushing the spider to death."
                    + fore(10)
                    + "Success!"
                    + style(0),
                    userStrDelay,
                )
                printt(
                    f"\n\n Well, at least {style(3)}{style(4)}that{style(0)} was taken care of...", userStrDelay)
                time.sleep(0.5)
                printt(
                    "\nYou then decide to continue eating your Cheeto, and try to find what was in that bottle, which made you 5.08 cm tall...",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(" *****\n", userStrDelay)
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "After eating the Cheeto,you plan to investigate the contents of the bottle.",
                    userStrDelay,
                )
                bottle = """
                             mmm
                             )-(
                            (   )
                            |   |
                            |   |
                            |___|                           """
                time.sleep(0.5)
                print(bottle)
                time.sleep(0.5)
                printt(
                    " \nWalking towards the opposite side of the table, you see the bottle, which is the size of a natural landmark, you try to look at the recommended dosage for this dieting potion (or remedy, or whatever it is).\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "That's when something catches your eye...\n You see a label for the recommended dosage:\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"{style(3)}   HOW TO USE:\n TAKE AT LEAST ONE DROP OF THE TRIPLE FAT BURNER. IF YOU OVERDOSE...\n STRANGE THINGS WILL HAPPEN.\n"
                    + fore(1)
                    + f"{style(3)} DO NOT OVERDOSE! "
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "\nThen you realize how"
                    + fore(14)
                    + " STUPID "
                    + style(0)
                    + "you are in the first place!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"YOU {fore(3)}{style(3)}HAVE{style(0)} TO FIX THIS! At least find an antidote or something that can make you big again!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "You examine the bottle again... Could there be a specific brand/company name that had made this?\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Nope. There isn't a company name on the bottle! Then, who the hell made THIS liquid? \n The narrator of this game?\n A mad scientist? \n Your best friend? \n A doctor?",
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(fore(10) + "Wait..." + style(0) +
                       "A doctor...\n💡", userStrDelay)
                time.sleep(0.5)
                printt("You NEED to see a doctor!", userStrDelay)
                printt(
                    f"{fore(2)}{style(3)}You have to call your physician. Maybe he can help you get back to normal.{style(0)}",
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "\nLuckily, your phone is on the very tabletop you're standing on, so you walk straight to it.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Staring at your enormous phone 📱(which is the latest iPhone), you wonder if you can turn it on.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "The power button is on the very left side of your phone. You kneel down and try to turn the phone on by pressing the button with both hands...",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"{fore(1)}{style(1)}\n But, it doesn't even click.{style(0)}", userStrDelay)
                time.sleep(0.5)
                printt(
                    "\n You press harder to at least give your hands more strength,and unfortunately, the power button never budges...\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "Then, an idea comes to your mind...\n Instead of using your hands, use your feet instead!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\n Lying down on your back, you put your foot on the power button, and push that same foot downwards.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    fore(10)
                    + "And it works!😁\n You finally switched on your phone!\n"
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "Getting up, you then climb to your feet and step on the phone.",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "No need for Face ID, since you can literally enter the passcode of your phone with those little hands of yours.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "You then tap on your calls list in order to speed dial your physician quickly.",
                    userStrDelay,
                )
                printt(
                    "Then, you see your local physician's phone number, and click on it.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\n You then hear the ringing as you're dialing your physician. The sound is REALLY loud that you almost fall off the phone.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Then you hear a sharp click. It's the receptionist at your community's doctor's office. Her voice comes out as a roaring sound in your tiny ears.",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt("Anyway, here's how the conversation goes...\n", userStrDelay)
                time.sleep(0.5)
                os.system("clear")
                printt("Receptionist: Hello?\n", userStrDelay)
                time.sleep(0.5)
                printt("You: HI, I NEED YOU TO HELP ME!\n", userStrDelay)
                time.sleep(0.5)
                printt("\nReceptionist: Uhh, who is this?", userStrDelay)
                time.sleep(0.5)
                printt(
                    "\nYou: YEAH? I WOULD LIKE TO BOOK AN APPOINTMENT WITH MY FAMILY DOCTOR?",
                    userStrDelay,
                )
                printt(
                    "\nReceptionist: Ok... why am I not hearing anything? Never mind, what issue do you have?\n", userStrDelay
                )
                time.sleep(0.5)
                printt(
                    "\nYou: I SHRANK TO THE SIZE OF AN INSECT! YOU GUYS HAVE TO HELP ME!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    f"\nReceptionist:Sorry, I'm not sure what you're saying. Your name came up, {username}. Is this a complete joke?\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\nYou: NO... It's not a joke, it really did happen!...\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\nReceptionist: I guess its a bad connection. You can call back or you can book an appointment in our building...Bye and take care!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt("\nYou: NO, WAIT! DON'T HANG UP--\n\n", userStrDelay)
                time.sleep(0.5)
                printt(" **CLICK** ", userStrDelay)
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "A deafening click....\n...Like a clap of thunder...\n", userStrDelay)
                time.sleep(0.5)
                printt(
                    "You couldn't believe it. The receptionist hanged up on you! Your ears ring from the loud voice.\n Now what? Wait for another package to be delivered to your door that contained an antidote? Or to wait for your parents to come back home?",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\nThat's when you remember that you can book an appointment in person.\n\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "But wait a minute! You're too small to risk the journey to the doctor's office!\n However,you are determined to risk your own life and make things right again.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt("1. Yes, I would risk the expedition", userStrDelay)
                printt("2. No, I'm waaay too scared!", userStrDelay)
                print("Would you risk it?")
                decision = int(fkey.getchars(chars=["1", "2"]))
                if decision == 1:
                    storyLocation = "3"
                    saveGame()
                    longJourney()
                    break
                elif decision == 2:
                    os.system("clear")
                    printt(
                        "Oh, really? What a chicken you are...\n Goodbye for now!\n You eventually die of depression of being tiny forever...",
                        userStrDelay,
                    )
                    printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                    numDeaths += 1
                    saveGame()
                    playAgain()
            elif decision == 2:
                os.system("clear")
                printt(
                    "Holding the Cheeto with both hands, you make a run for it across the tabletop...\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt("...And you" + fore(9) +
                       " stop..." + style(0), userStrDelay)
                time.sleep(0.5)
                printt(
                    "Looking down, you see that the distance between you and the ground is too high! You could fall to your (possible) eventual death...😱",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Glancing to the right, you see the couch. Its right next to the table...",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "And, looking back, the spider is coming closer.... and closer... and closer...\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    fore(3) + "YOU HAVE TO DO SOMETHING... QUICK!!!\n" + style(0),
                    userStrDelay,
                )
                printt(" 1. Jump down from the table", userStrDelay)
                printt(" 2. Try to jump straight to the couch", userStrDelay)
                decision = int(fkey.getchars(chars=["1", "2"]))
                if decision == 1:
                    os.system("clear")
                    printt(
                        "Taking a deep breath, you jump off the table, screaming all the way...",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "... And you eventually suffer from a head injury and die from the impact...\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                    numDeaths += 1
                    saveGame()
                    playAgain()
                elif decision == 2:
                    os.system("clear")
                    printt(
                        "Making a run for the couch, you eventually leap over that gap, and.... And...\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        fore(6) + "YOU'RE ON THE EDGE OF THE COUCH...\n" + style(0),
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "...Hanging for dear life. Your Cheeto is your only support that stops you from falling...",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "With your last bit of strength, you immediately hoist yourself up to the top of the couch..."
                        + fore(2)
                        + "YES!"
                        + style(0),
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "\nHowever, the spider has seen your whereabouts, and climbs up the couch! \nWhat now?!\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "You have no weapon to fight against the spider!\n You only have your Cheeto...\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "But, there is no time to think now...\nThe spider's next to you...\n\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(
                        "\n...And then you die from being ripped apart by the spider's fangs...\n",
                        userStrDelay,
                    )
                    time.sleep(0.5)
                    printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                    numDeaths += 1
                    saveGame()
                    playAgain()
            elif decision == 3:
                os.system("clear")
                printt(
                    "Dropping the Cheeto from your hands, you walk towards the spider with outstretched arms, waiting to embrace him/her, if spiders do have a gender.\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "The spider stares at you..."
                    + fore(5)
                    + "\n... And continues scuttling towards you...\n"
                    + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "At last! You had found" +
                    fore(13) + " TRUE LOVE! 💓\n" + style(0),
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "... Which quickly turns into betrayal as you are torn apart by the spider, bleeding to death...\n",
                    userStrDelay,
                )
                printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                numDeaths += 1
                saveGame()
                playAgain()
            elif decision == 4:
                time.sleep(0.5)
                os.system("clear")
                printt(
                    "You give the spider the Cheeto, but it seems like its"
                    + fore(1)
                    + " not "
                    + style(0)
                    + "hungry for the Cheeto... Or is it?\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Then, the spider lunges AT YOU, and you (plus spider) get knocked off the tabletop!\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "Hurtling towards the ground, you struggle to let go of the spider's prying fangs...\n",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt("...And then...", userStrDelay)
                time.sleep(0.5)
                printt("\n**THUD**\n", userStrDelay)
                time.sleep(0.5)
                printt(
                    "You hit the ground,weak and tired...\n The spider stares at you...menacingly!",
                    userStrDelay,
                )
                time.sleep(0.5)
                printt(
                    "\n And brings you towards its gaping jaws...\n Then rips your head off,so that you suffer a pretty gruesome death.",
                    userStrDelay,
                )
                printt(fore(1) + "💀 GAME OVER 💀" + style(0), userStrDelay)
                numDeaths += 1
                saveGame()
                playAgain()
            else:
                printt("Not a valid choice...Please try again!", userStrDelay)
        except ValueError:
            printt("That's not a number...Please try again!🙄", userStrDelay)


def longJourney():
    global userStrDelay, numDeaths, storyLocation
    os.system("clear")
    printt(
        "Ok, so you have decided to go to the next location... the doctor's office...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    docName = input(
        "Oh, and what's the name of your family physician? (Real or imaginary)\n"
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "\n\n Alright, let's hope that the journey will be successful, and easy, despite the fact that you're 5.08 cm tall...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("\nAfter all, its just 3 simple steps!\n", userStrDelay)
    time.sleep(0.5)
    printt("Step 1: Get out of the house...\n", userStrDelay)
    time.sleep(0.5)
    printt("\nStep 2: Take the bus...\n", userStrDelay)
    time.sleep(0.5)
    printt(
        "\nAnd, Step 3 : Find Dr." + docName + " and get back to normal size!\n",
        userStrDelay,
    )
    printt(
        "What could possibly go" +
        fore(1) + style(4) + " wrong?🫤\n" + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        f"{style(4)}First off, you really need to get off the table without dying,{style(0)} so you decided to lower yourself off the table, slowly...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nAnd, therefore, within a few minutes, you're off the table and land on the floor, free of injuries.",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "\n\n Next, you run towards the front door of your house, and see that you can easily exit, since there's a pet door! Good for you!",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Pushing the latch of the pet door, you swing it open, and drop onto the doormat.\n Your butt gets sore on impact. \n Ouch...",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nLooking across your front yard, and knowing that the bus stop is about a block away (even though from your perspective, its kilometers away), you wonder on what is the fastest way to get to the bus stop?\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nWalking/running diagonally in the grass may be faster (along with the risks of facing more dangers), or what about the pavement to be on the safe side (minus the long distances)?🤔\n After all, the choice is yours...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Take the grass pathway", userStrDelay)
    printt("2. Walk on the pavement", userStrDelay)
    printt("3. Be one with the wind (Just do it....)", userStrDelay)
    decision = int(fkey.getchars(chars=["1", "2", "3"]))
    if decision == 1:
        storyLocation = "4"
        saveGame()
        plotPointOne()
    elif decision == 2:
        storyLocation = "9"
        saveGame()
        plotPointTwo()
    elif decision == 3:
        storyLocation = "10"
        saveGame()
        plotPointThree()


def game():
    global userStrDelay, numDeaths, storyLocation, username
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Let's face it... You are 100 percent bored, and have absolutely nothing to do since you're home alone. You've binge watched '"
        + fore(5)
        + "She"
        + style(0)
        + "-"
        + fore(2)
        + "Hulk"
        + style(0)
        + ":Attorney at Law' on Disney Plus, played some video games, studied for your university exams, and now you're lying on the couch, like a useless potato 🥔.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"But....\n That's when you hear the doorbell ring.\n{fore(136)}{style(4)} You wonder who could it be at this hour?\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("Probably the pizza guy 🍕. Or the mail-man.✉️", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(
        "After walking to the front door, you open it and find out that there's no one there!😮",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nYou look down and see a cardboard box on your porch. 📦\n A package perhaps...\n",
        userStrDelay,
    )
    printt(
        f"{fore(6)}{style(3)}But, who the god damn hell would drop a package here and leave immediately?!\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("\nProbably someone that was in a rush.", userStrDelay)
    printt(
        f"But who even cares about {style(3)}that?🤷🏽‍{style(0)}\n You eventually carry the package to the living room of your house, and decided to open it, because you are one curious person.😁\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "\nOpening the package, you find a small bottle with a corkscrew on it.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("\n🍾<-- Yes, like the ones on champagne bottles, duh!\n", userStrDelay)
    time.sleep(0.5)
    printt("\nLooking at the contents of the bottle, the label reads:", userStrDelay)
    time.sleep(0.5)
    printt(f"{style(3)}    DRINK ME: I AM VERY GOOD FOR DIETING PURPOSES    {style(0)}", userStrDelay)
    time.sleep(0.5)
    os.system("clear")
    printt(
        "Since you literally are on a diet (and don't even care about who the heck sent you the package), you decided to drink the contents of the bottle anyway...",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "\nYou unscrew the cork and chugged down the entire bottle like its vodka and slammed the glass bottle to the table. You don't care about reading the instructions on how to take a proper dose of this so called dieting drink.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        "Right after drinking that strange mixture (which tasted bitter and sour like vinegar), you sit down on the couch, and scroll through Reddit on your phone to kill your boredom.\n",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        fore(9) + "After 15 minutes, you feel ...\n Strange...\n" +
        style(0), userStrDelay
    )
    time.sleep(0.5)
    printt(
        fore(105)
        + "You really don't mind it, because after all, it was a stomach ache, so you'll be fine...\n"
        + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(1) + style(1) + "And then you start to feel dizzy 😵‍💫\n" + style(0),
        userStrDelay,
    )
    time.sleep(0.5)
    printt(f"{fore(125)}Like, {style(4)}really dizzy...{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt(
        f"{fore(204)}\nSuddenly, you feel your skin is tightening quickly, and your body is stiffening...\n... Your toes are tingling as if it fell asleep or some sort...{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        fore(125)
        + "The pain is unbearable now. You scream at the top of your lungs, because its like being crushed by a steam roller or being squeezed into a pulp like an orange!🍊",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"\nYou decide to get some Tylenol from the medicine cabinet, but just as you start to get off the couch and walk,{fore(1)}{style(4)} you blackout and collapse to the floor...\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    os.system("clear")
    printt(
        "\n................................................................\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"\nYou wake up, and adjusting your vision, {style(3)}you realize that something is off...\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"\nGazing at the floor, you notice its a few centimeters above your head.{style(3)} Weird...\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(f"Looking up, the ceiling is a lot more higher than usual.\n", userStrDelay)
    printt(
        f"And looking what's around you, everything is pretty HUGE. The table, couch, etc, and the floor is more spread out... Does this sounds like a case of the Mondays?\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("You finally realize what the heck happened...\n", userStrDelay)
    time.sleep(0.5)
    printt("\nYOU\n", userStrDelay)
    time.sleep(0.5)
    printt("\nHAVE\n", userStrDelay)
    time.sleep(0.5)
    printt("\nBEEN\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"\n{fore(1)}{style(1)}{style(3)}SHRUNK...😱\n{style(0)}...To at least 2 inches (approximately 5.08 cm)\n", userStrDelay
    )
    time.sleep(0.5)
    os.system("clear")
    printt(fore(12) + "Alright... What now?\n" + style(0), userStrDelay)
    time.sleep(0.5)
    printt(f"{fore(1)}Panic and do absolutely nothing?\n{style(0)}", userStrDelay)
    time.sleep(0.5)
    printt("Well, why would you do that, BTW?\n", userStrDelay)
    printt("At least you should think about what caused this mishap...\n", userStrDelay)
    time.sleep(0.5)
    printt("Right?\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"Oh well, it might be the drink that caused this...\n All because you never cared about the recommended amount...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"That's when you hit the nail on the head. It was the clear liquid you drank earlier! But.. what was in it? Some kind of potion🍶, you suppose...\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(f"\nThen, your stomach growls. You are extremely hungry😋\n", userStrDelay)
    time.sleep(0.5)
    printt(
        f"\nBut, you have to focus and get back to your normal size! ASAP!\n",
        userStrDelay,
    )
    printt(
        "So, you have an important decision to make... But it'll cost your own life... Choose wisely...",
        userStrDelay,
    )
    time.sleep(0.5)
    printt("1. Find food and get back to normal", userStrDelay)
    printt("2. Get back to normal size, without eating anything", userStrDelay)
    while True:
        try:
            decision = int(fkey.getchars(chars=["1", "2"]))
            if decision == 1:
                storyLocation = "2"
                saveGame()
                encounterOne()
            elif decision == 2:
                storyLocation = "32"
                saveGame()
                encounterZero()

        except ValueError:
            printt("That's not a number...Please try again!🙄", userStrDelay)


def subMenu():
    global hasAccount
    os.system("clear")
    printt("1. New Game", userStrDelay)
    printt("2. Load Game", userStrDelay)
    printt("Select any key to exit", userStrDelay)
    gameLoad = int(fkey.getchars(chars=["1", "2", "3"]))
    if gameLoad == 1:
        os.system("clear")
        accountCheck()
        if hasAccount == 1:
            registerData()
        else:
            register()
        print()
        loadGame()
    elif gameLoad == 2:
        os.system("clear")
        accountCheck()
        print()
        loadGame()
        os.system("clear")
    else:
        os.system("clear")
        printt("Exiting to the main menu....\n\n", userStrDelay)
        time.sleep(0.5)
        os.system("clear")
        mainMenu()


def readDisclaim():
    print(
        f"{fore(1)}Do you want to read the disclaimer before proceeding? (y/n)\n >{style(0)}"
    )
    disclaimerRead = str(fkey.getchars(chars=["y", "n"]))
    if disclaimerRead == "y":
        os.system("clear")
        disclaimer()
        mainMenu()
    else:
        os.system("clear")
        mainMenu()


def disclaimer():
    printt(
        f"{fore(1)}{style(5)}⚠️  DISCLAIMER: PLEASE READ THIS CAREFULLY! ⚠️ \n\n{style(0)}",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(
        f"Before playing this game, its {style(4)}highly{style(0)} recommended to read the 'guide.md' in the 📁Guide, so you won't get confused!\n\n",
        userStrDelay,
    )
    time.sleep(0.5)
    printt(fore(125) + style(1) + style(4) +
           "Understood?!\n\n" + style(0), userStrDelay)
    os.system("clear")


def mainMenu():
    global userStrDelay, numDeaths, bestFriend, storyLocation
    printt(fore(14) + "TG 101 presents...\n\n\n" + style(0), userStrDelay)
    time.sleep(1)
    print("███████ ██   ██ ██████  ██    ██ ███    ██ ██   ██ ")
    print("██      ██   ██ ██   ██ ██    ██ ████   ██ ██  ██  ")
    print("███████ ███████ ██████  ██    ██ ██ ██  ██ █████   ")
    print("     ██ ██   ██ ██   ██ ██    ██ ██  ██ ██ ██  ██  ")
    print("███████ ██   ██ ██   ██  ██████  ██   ████ ██   ██ ")
    time.sleep(0.5)
    printt("\n Welcome to this game...\n\n", userStrDelay)
    time.sleep(0.5)
    printt("1. Start", userStrDelay)
    printt("2. Options", userStrDelay)
    printt("3. Exit", userStrDelay)
    while True:
        try:
            print("Would you like to start your adventure or quit?\n")
            choice = int(fkey.getchars(chars=["1", "2", "3"]))
            if choice == 1:
                subMenu()
                break
            elif choice == 3:
                printt("Goodbye!", userStrDelay)
                quit(0)
            elif choice == 2:
                options()
        except ValueError:
            printt("Invalid input! Try Again!", userStrDelay)
            continue


readDisclaim()
