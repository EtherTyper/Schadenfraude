import time
import sys

oThree = 0

print "Welcome to Schadenfreude! The text adventure where I, the narrarator, will manipulate the outcomes of your adventure! Good luck..."

time.sleep(2)

print ""

print "Made by David Reichert - Not case-sensitive, just for you, ; ) "

print ""

time.sleep(2)

name = raw_input("Hi! My name is [UNIDENTIFIED]! What's your name?")

print ""

print name + "? Alright, I'll try to remember that... Welcome to..."

time.sleep(2)

print(" _____      _               _             __                     _      ")
print("/  ___|    | |             | |           / _|                   | |     ")
print("\ `--.  ___| |__   __ _  __| | ___ _ __ | |_ _ __ __ _ _   _  __| | ___ ")
print(" `--. \/ __| |_ \ / _` |/ _` |/ _ \ |_ \|  _| |__/ _` | | | |/ _` |/ _ \ ")
print("/\__/ / (__| | | | (_| | (_| |  __/ | | | | | | | (_| | |_| | (_| |  __/")
print("\____/ \___|_| |_|\__,_|\__,_|\___|_| |_|_| |_|  \__,_|\__,_|\__,_|\___|")
        
time.sleep(2)        
            
print ""
                                                                                                                                                                                                                                                                    
print "You wake up in a room, it's pitch dark and you can't see a thing, what do you do?"
time.sleep(2)

badAnswer = True

while badAnswer == True:
	one = raw_input("A: Get up and feel around the room for an exit B: Go back to sleep")
    
	if one == "A" or one == "a" or one == "B" or one == "b":
		badAnswer = False
	else:
		print "Hmm? Come again?"      
   
if one == "A" or one == "a":
	print ""
	print "You feel around the room looking for an exit, the walls are made of stone and feel rough and your fingers as you look for the exit. You finally come across a small passage, you keep walking through the passage until you come to an end, with two more passages to the left and the right."
elif one == "B" or one == "b":
	print ""
	print "Wait... What?? That's not an option... Are you really willing to be trapped here forever? Hahaha, fine, I'll give you a hand, let's drop your HP down to 0 real quick..."
	time.sleep(3)
	print "HP at 5"
	time.sleep(0.5)
	print "HP at 4"
	time.sleep(0.5)
	print "HP at 3"
	time.sleep(0.5)
	print "HP at 2"
	time.sleep(0.5)
	print "HP at 1"
	time.sleep(0.5)
	print "HP at 0"
	time.sleep(1)
	print "You were killed by [UNIDENTIFIED]"
	sys.exit()
else:
	print ""
	print "Didn't quite catch that, type one of the options above."
time.sleep(2)
if one == "A" or one == "a":
    
	badAnswer = True
    
while badAnswer == True:
	two = raw_input("Do you go A: Left or B: Right? *Cough* *Cough* Go right... *Cough* *Cough*")
    
	if two == "A" or two == "a" or two == "B" or two == "b":
		badAnswer = False
	else:
		print "Hmm? Come again?"
qTwo = ""
    
if two == "A" or two == "a":
	print ""
	print "You're no fun... Fine, left it is..."
	print ""
	qTwo = "one"
elif two == "B" or two == "b":
	print "Hehehe, you walk into the left passage, and meet a dead end..."
	time.sleep(1)
	print ""
else:
	print "Hmm? Come again?"

if qTwo == "one":
	while badAnswer == False:
		time.sleep(2)
		print "You walk into a gloomy but slightly-lit room, it's lit by a torch on the wall, you hear the sound of water drops dropping onto the floor one by one, you look over and see a bamboo shoot coming out of the wall, with the water slowly dripping out of it, the puddle on the floor is small, it only recently started dripping."
		print ""
		three = raw_input("What do you do? A: Touch the flame of the torch for a secret lever, afterall, it's just fire, completely harmless... B: Walk back C: Kick the bamboo shoot D: Check the walls for a secret passage")
    
		if three == "A" or three == "a" or three == "B" or three == "b" or three == "C" or three == "c" or three == "D" or three == "d":
			badAnswer = False
		else:
			print ""
			print "Hmm? That isn't an option."
			print ""
if three == "C" or three == "c":
	print ""
elif three == "B" or three == "b":
			print ""
			print "And... Done, I blocked the passage for you with a bunch of rocks, don't bother trying to get through, even if you could, I'd make sure you don't, no going back now. Hahaha. Time to choose another option"
			print ""
			time.sleep(3)
elif three == "D" or three == "d":
			print ""
			print "Good idea, go look around the room for a passage"
			time.sleep(1)
			print "1 hour"
			time.sleep(1)
			print "2 hours"
			time.sleep(1)
			print "3 hours"
			time.sleep(1)
			print "4 hours"
			time.sleep(1)
			print "Hahaha, alright, fine, I'm done, there was no secret passage, I lied. Choose another option."
			print ""
			time.sleep(3)
elif three == "A" or three == "a":
			print "You touched the fire, current health status: Burning"
			time.sleep(0.5)
			print "HP at 5"
			time.sleep(0.5)
			print "..."
			time.sleep(0.5)
			print "HP at 4"
			time.sleep(0.5)
			print "You..."
			time.sleep(0.5)
			print "HP at 3"
			time.sleep(0.5)
			print "You actually touched the flame??"
			time.sleep(0.5)
			print "HP at 2"
			time.sleep(0.5)
			print "I didn't even have to lower your HP myself, you did it for me, thanks, hahaha, goodbye now..."
			time.sleep(0.5)
			print "HP at 1"
			time.sleep(0.5)
			print "HP at 0"
			time.sleep(1)
			print "You were killed by-- No, no, no... I'll do this. Congratulations" + name + ", you burnt yourself by touching a flame. I, [UNIDENTIFIED], personally congratulates you."
			sys.exit()
else:
	print ""
