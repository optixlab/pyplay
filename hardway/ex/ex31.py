# Exercise 31
#------------

print "You enter a dar room with 2 doors. Do you want to go through?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear eating cake. What should I do?"
    print "1. Eat the cake"
    print "2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthuhlu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothespin"
    print "3. Understanding revolver melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives a tornado of jello"
    else:
        print "The insanity rots in your eyes"

else:
    print "You stumble around and fall on a knife and die."

