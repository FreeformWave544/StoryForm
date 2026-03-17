default total_stress = 0.0
default total_happiness = 50.0
default total_energy = 100.0
default depressionModifier = 1.0
default gender = "John"
default name = ""
default dressed = False
default privacy = False
default time_left = 2000.0
default wearing = {
    "Shirt": False,
    "Tie": False,
    "Blazer": False,
    "Skirt": False,
    "Shorts": False,
    "Trousers": False
}

image mirror:
    "images/Mirror.png"
    zoom 35

define m = Character("Mother")
define b = Character("Bestie")

screen timer():
    frame:
        xalign 0.95
        yalign 0.05
        if time_left < 5.0:
            text "Time Left: [int(time_left)]:[int((time_left % 1) * 60):02d]" color "#8f0404"
        else:
            text "Time Left: [int(time_left)]:[int((time_left % 1) * 60):02d]"

screen stressBar():
    bar:
        yalign 0.5
        value total_stress
        range 100
        xysize(25, 500)
        style "vertical_bar"

init python:
    from random import randint
    def stress(amount):
        global depressionModifier
        global total_stress
        total_stress = max(0, total_stress + (amount * depressionModifier))
        if total_stress > 100:
            renpy.jump("overStressed")
    def happiness(amount):
        global depressionModifier
        global total_happiness
        total_happiness += amount / depressionModifier
        if total_happiness < 0:
            renpy.say(n, "You've reached a state of depression.")
            depressionModifier = 2.0
    def energy(amount):
        global depressionModifier
        global total_energy
        total_energy += amount / depressionModifier
        if total_energy < 0:
            renpy.say(n, "You're too exhausted.")
            renpy.say(John, "I BANISH THY!")
            renpy.jump("start")
    def time(amount):
        global time_left
        time_left -= amount
        renpy.restart_interaction()
        if time_left <= 0.0:
            renpy.say(m, "C'mon. We're going to school.")
            renpy.jump("School")


label overStressed:
    n "You're more stressed than not."
    John "And for that you've been banished back to your world."
    jump start

label john_world_Start:
    show screen stressBar
    n "You've entered the school of John..."
    n "John is British 'cause I don't know American schools."
    menu:
        John "What is your age bracket?"
        "11-12 (Year 7)":
            $ stress(10.0)
        "12-13 (Year 8)":
            $ stress(5.0)
        "13-14 (Year 9)":
            $ stress(2.0)
        "14-15 (Year 10)":
            $ stress(12.0)
        "15-16 (Year 11)":
            $ stress(24.0)
    menu:
        John "What is your biological sex at birth?"
        "Male.":
            $ gender = "Male"
        "Female.":
            $ gender = "Female"
    
    John "And what is your name?"
    while len(name) < 1:
        $ name = renpy.input("Name: ").strip().title() or renpy.input("Name: ").strip().title()
    n "It is your first day at your new school after you moved house... you're at home."
    m "[name] wake up! School today! And you're not getting out of it!"
    n "*You hear a knocking on your door, presumably your mother attempting to wake you.*"
    menu:
        "Yes, mother. I'm awake.":
            m "Get ready quick. We're leaving in 20 whether you're clothed or not."
            $ time_left = 20.0
            show screen timer
            $ happiness(-5.0)
            $ energy(-0.5)
            n "*You slowly force yourself out of bed.*"
        "*Ignore your mother and get out of bed.*":
            $ energy(50.0)
            m "I hear you in there. Respond to me. {w=2.0}Don't. {w=0.5}Be. {w=0.5}Rude."
            $ energy(-5.0)
            $ happiness(-10.0)
        "Alright, mama! I'm up! *Jump out of bed.*":
            $ energy(95.0)
            $ happiness(30.0)
    jump bedroom

label bedroom:
    menu:
        "Where do you go?"
        "Bathroom.":
            jump bathroom
        "Wardrobe.":
            jump wardrobe
        "Livingroom.":
            jump livingroom

label livingroom:
    if not dressed:
        m "Get into your school clothes, darling."
        if total_happiness < 50.0: 
            n "*Her voice is clearly dripping with annoyance.*"
        $ time(2)
        jump bedroom
    m "['Ah, you are up at long, long last.' if total_happiness < 50.0 else 'Ah, you are up! Want something to eat?']"
    menu:
        "Can I have some pancakes?":
            m "Pancakes? Coming right up!"
            n "After a few minutes, the pancakes are done, and you are just about to eat them when your alarm goes off."
            m "Oh. Too late. School time. You can eat on the way."
            $ energy(15)
            $ stress(2)
        "Can I have some salad?":
            m "Salad? You're not going to follow in your brother's footsteps, are you?"
            m "We all know what happened when he ate all that salad..."
    $ time_left = 0.0
    $ time(0.0)
    return

label wardrobe:
    $ clothes = list(wearing.keys())
    python:
        for outfit in clothes:
            n("Do you wear your [outfit]?", interact=False)
            wearing[outfit] = renpy.display_menu([("Yes", True), ("No", False)], screen="choice")
        for _ in range(len(wearing.values())):
            time(1.5)
    $ dressed = True
    jump bedroom

label bathroom:
    menu:
        "What do you do?"
        "Take a quick shower":
            n "You take a quick shower to wake yourself up."
            $ energy(5.0)
            $ happiness(2.0)
            $ time(4.0)
            jump bathroom
        "Brush your teeth":
            n "Minty fresh."
            $ happiness(1.0)
            $ time(2.0)
            jump bathroom
        "Look in the mirror":
            if total_happiness < 30:
                n "You look tired... maybe school won't be so good today..."
                $ stress(5.0)
            elif total_happiness > 70:
                n "You feel pretty confident today."
                $ stress(-5.0)
            elif total_stress > 79:
                n "You look... stressed. Very stressed.."
                $ happiness(-5.0)
            else:
                n "You look... okay? I guess."
            $ time(1.0)
            jump bathroom
        "Use the toilet":
            n "Best not to skip that before school."
            $ stress(-2.0)
            $ time(2.0)
            if randint(0, 5) == 0 and not privacy:
                n "As you finish up, you notice the door a bit ajar and your phone is gone."
                if wearing["Blazer"]:
                    n "Along with your blazer! Which had your valuables."
                $ wearing["Blazer"] = False
                $ stress(15.0)
                $ happiness(-5.0)
                n "Must've been your little brother's doings."
                menu:
                    "Do you look for your brother?"
                    "Yes":
                        "John! Back here. Now!"
                        jump bChase
                    "No":
                        jump bathroom
            jump bathroom
        "Lock the door":
            n "Privacy first."
            $ stress(-1.0)
            $ privacy = True
            jump bathroom
        "Leave":
            jump bedroom

label bChase:
    $ time(1.75)
    menu:
        n "Where do you look for John?"
        "His room.":
            n "There he is! Lying on his bed! Playing on your phone!"
            "JOHN!"
            John "*Jumps up, hiding the phone in his shirt.* Y-Yes?!"

        "His personal bathroom.":
            n "Empty. As you should have been hoping."
            menu:
                n "Do you inspect something for signs of him?"
                "The shower...":
                    n "Although from the slight drip of water from the shower, you can tell he must have just been here recently."
                "The toilet...":
                    n "What did you expect? It's a toilet that is just... existing. No longer existing in peace since YOU disturbed it."
                "Under the sink...":
                    n "You see a note... \"Don't forget to brush your teeth - mum\""
                    menu:
                        n "It must be an encoded message... quickly, decipher it!{w=7.5}{nw}"
                        "Try decipher it...":
                            n "As you over analyse the note, you *note*ice something..."
                            "This can't be..."
                            n "You mutter as you realise something important."
                            n "John has a lie that has rooted so deeply into his mind that he can never say the truth."
                            n "The lie in question: he—"
                            n "The door slams shut and your brothers hurried footsteps can be heard."
                            n "You suddenly realise the time..."
                            $ time_left = 0.0
                            $ time(0.0)
                        "It is a note from mum to John. Take it at face value and ignore it.":
                            jump bChase
            jump bChase
        "The livingroom.":
            m "Darling, where's your blazer? You need to properly dress for school."
            $ time(0.5)
            jump bChase
        "The kitchen.":
            n "That little gremlin is eating your favourite cereal you were saving for today!"
            menu:
                "HEY!":
                    m "What's going on, this time?"
                    m "Actually. You know what? I don't want to know."
                    m "School. Now."
                    "But—"
                    jump School
        "Leave.":
            jump bedroom

default bGender = ""
label School:
    hide screen timer
    n "School..."
    b "Ah! [name]! I've SO much to talk to you about!"
    menu:
        n "Your bestie... say, what is their biological sex at birth?"
        "Female":
            $ bGender = "Female"
        "Male":
            $ bGender = "Male"
    menu:
        b "Ah! [name]! I've SO much to talk to you about!"
        "Not now.":
            b "Oh... okay..."
            "Well we've got PE... so..."
        "Go ahead!":
            b "So basically,"
            "Wait! PE! Quick!"
        "Maybe we should go to lesson first?":
            b "Oh... right!"
            b "What do we have?"
            menu:
                "P.E. - specifically swim lessons 'cause this school is amazing.":
                    b "Oh, AMAZING!"
    jump PE


label PE:
    n "You and your bestie enter the school changing rooms."
    if bGender == gender:
        b "C'mon! Let's find a stall."
        jump changingRoomTogether
    else:
        b "Welp... different changing rooms."
        jump changingRoomAlone

define bully = Character("Bully", color="#b11e1e85")

label changingRoomAlone:
    pass

label changingRoomTogether:
    b "Here's a nice stall! But... but only one..."
    menu:
        "You first.":
            b "Thank you."
        "I'll go first.":
            b "Oh... alright!"
        "Don't worry. I won't stare.":
            b "I mean..."
            menu:
                "S-Sorry!":
                    b "It's alright. I'll go first."
                "You-you can change first.":
                    b "Thanks~"
                "Please... I don't want to be alone...":
                    b "Okay."
                    n "You and your bestie enter the stall, and start changing together..."
                    n "Suddenly there is a loud knocking on the door."
                    b "Y-Yes? Who is it?"
                    bully "You two lovebirds having fun? *Snears a laugh.*"
                    b "DAMN - LEAVE US IN PEACE."
                    bully "Woah... ragebaited easy as always?"
                    menu:
                        b "GO. AWAY."
                        "Please... quieter... please....":
                            $ stress(10)
                            b "S-Sorry... *pulls you into a gentle hug.*"
                            $ happiness(5)
                            bully "Aww, is the noise getting to your quirky girlfriend?"
                            $ energy(-5.0)
                        "Yeah! Leave us in peace!":
                            bully "Wow. That was... pathetic. Have you NEVER been authoritative?"
                            bully "Adds up. Such a... unique mind could speak typically."
                            b "*Hugs you gently and whispers in your ear,* Don't listen to them..."
                    n "A loud bang on the door as they try kick down the door."
                    b "*Quickly wraps a towel around you and one around themselves, opens the door, and steps out, closing it behind them...*"
                    menu:
                        "Try follow...":
                            n "The door is jammed..."
                        "Finish changing...":
                            n "As you finish changing, the door opens."
                        "Listen...":
                            n "You hear a shrill scream - the scream of a chatterbox who is all talk and no show."
                            $ happiness(10.0)
                            $ stress(-1.0)
                    b "*Returns.* Well... let's finish changing."
                    n "After a few minutes, your bestie leads you through to the swimming pool - no sign of that dastardly bully."
            "T-Thank you."
            b "For what?"
            menu:
                "Never mind.":
                    b "Oh... alright!"
                "For helping me...":
                    b "You are my bestie. So it was, is, and will always be my great pleasure."
                "For... everything...":
                    b "*Faces flushes crimson.* I... sure... you're welcome... {w=1.0}Oh... alright! *gently takes your hand in theirs.*"
            "*I pause as we pass a mirror on the wall, staring at my own reflection.*"
            show Mirror
            b "*Rests their hand on your shoulder.* C'mon. You've seen a mirror before."
            "I...{w=1.0} they were right...{w=1.0} I'll never be great... {w=1.0}never be {w=0.5}typical... {w=1.0}never be {w=0.5}normal..."
            b "Listen...{w=1.0}{nw}"
            b "Every mirror has scratches, {w=0.5}smudges {w=0.5}and imperfections. Never,{w=1.0} and I repeat NEVER do they tell the full truth..."
            b "{w=1.0}no matter how real it looks."
            $ stress(5.0)
            n "A sense of unease fills you as that strange bar on the left you noticed quite some time ago fills further as that is said by your 'bestie'."
            menu:
                b "What's wrong, [name], you look a bit pale?"
                "I... I'm fine...":
                    b "Oh... alright!"
                "Just... a bit sick...":
                    b "Oh... alright!"
                "No. You are pale. Uno reverse.":
                    b "I... uh... WHAT?!"
                    n "You swear you see steam coming out of their ears."
            $ say("Teacher", "C'mon, everyone! Lesson starting! If you're changed come out here.")
            b "Well, guess that's our queue! Come on! *Takes your hand, leading you to the pool.*"
            "Yeah. Prepared to drown."
            b "Drown? I do not want to drown. Death would mean not being alive."
            n "Ugh, so monotone. When will they show more emotions?!"
            "*Laughs.*"
            b "What's funny? Death is not funny. It is the end of life."
            "*Chuckles.* Right."