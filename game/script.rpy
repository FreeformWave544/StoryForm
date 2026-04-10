init python:
    import random
    bgm_tracks = [
        "theme1.wav",
        "theme2.wav",
        "theme3.wav"
    ]

default persistent.ending_happy = False
default persistent.ending_horrid = False
default persistent.ending_bad = False
default persistent.ending_secret = False
default persistent.geraldNone = False
default persistent.apocalypse = False
default persistent.finale = False
default persistent.oiia = False
define j = Character("James", image="images/James.png")
define g = Character("Gerald")
define os = Character("The Overseer")
define John = Character("John")
define n = Character("Narrator")

image salad_bg = Solid("#7CFC00")

image James:
    "images/James.png"
    zoom 10

image Salad:
    "images/Salad.jpg"

image SaladMonster:
    "images/SaladMonster.png"
    zoom 0.5

default pronoun = "Mr."
label start:
    $ selected_bgm = random.choice(bgm_tracks)
    play music selected_bgm fadein 1.0 loop volume 0.2
    menu:
        "How do you want to be addressed?"
        "Mr.":
            $ pronoun = "Mr."
        "Sir":
            $ pronoun = "Sir"
        "Mrs.":
            $ pronoun = "Mrs."
        "Ma'am":
            $ pronoun = "Ma'am"
        "Other":
            $ pronoun = renpy.input("Enter how you want to be addressed.").strip() or "Mr."
            if "gerald" in pronoun.strip().lower():
                $ pronoun = "⧫⨀⧖⨁⧘⨂"
            elif "freeformwave" in pronoun.strip().lower() or ("wave" in pronoun.strip().lower() and ("form" in pronoun.strip().lower() or "free" in pronoun.strip().lower())):
                "You have committed identity theft of the very developer you should be worshipping."
                "You will now be terminated and replaced with an identical clone."
                $ pronoun = renpy.random.choice(["Logan", "Safia", "David", "Kanokid", "John Smith", "Mehar", "Ghastly", "Ashmit"])
                "This clone shall be called... {w=1.0}\"[pronoun]\""
            elif pronoun.strip().lower() == "john":
                John "You... you remembered me?"
                John "I thank you..."
                John "As a reward..."
                $ pronoun = "John"
                "You feel gravity start to pull you from the ground,"
                "and as you float into the sky, you start to feel something."
                "Your body starts to warp and deform... change and improve."
                "Yet you feel no pain. {w=2.0} And then a temporary state of unconsciousness (sleep) takes a hold of you."
                jump john_world_Start
        "The Overseer" if renpy.random.randint(1, 200) == 1:
            $ pronoun = "TRAITOR!"
            g "The Overseer disapproves of you."
    show James
    j "Heya [pronoun]! I'm James."
    j "If you didn't know, I absolutely ADORE salad!"
    menu:
        "Where do you get salad?"
        "My place.":
            jump home
        "Your place?":
            jump jHome
        "My sister's bestie's house.":
            jump sbHome
    return

label home:
    j "So... lovely place you got here..."
    j "Does it like... have a kitchen, perhaps?"
    menu:
        "Indeed!":
            j "Great!"
        "Indubidubly!":
            j "Ok, [pronoun] Long-words."
        "Ind-":
            "(What's another ind- word?? Uhh... I know!)"
            "YES! THAT'S IT!"
            j "Wha— what's what?"
            "I mean... yes, it does have a kitchen..."
    j "Does it have salad?"
    menu:
        "Yes, I think so.":
            show Salad
            "*Walks to & opens fridge...*"
            "Oh... it spoiled..."
        "Yeah, but it's probably spoiled.":
            show Salad
        "Nah, only some mush of degraded salad leaves.":
            show Salad
    j "Damn... when did you buy it? 1901?"
    "15 minutes ago. ;-; :sob:"
    hide Salad
    menu:
        "*Eat it.*":
            j "HOLY."
            "What? It's just salad."
            hide James
            "*Proceeds an onslaught of maniacal salad-beings created from the salad fusing with your DNA.*"
            "*You've successfully ended the world.*"
            $ persistent.apocalypse = True
            "*Aren't you proud? You caused all this... Carnage. Wreckage. Salad.*"
            "*You. Not me. Not Gerald. Not John. Nor James.*"
            "*Think about that. Even GERALD did ABSOLUTELY nothing.*"
            $ persistent.geraldNone = True
            j "Ok. idiot."
            j "You awake?"
            "*Blinks awake.*"
            show James at truecenter:
                zoom 2.0
            j "That salad put you in a salad coma. It's been 15 years."
            menu:
                "I... uh...":
                    pass
                "I swear that—":
                    pass
            j "What? Did you think you caused some sort of salad-apocalypse?"
            j "Don't be ridiculous."
            j "That was of COURSE King Henry the XXI half a year ago."
            define e = Character("Salad Monster")
            show SaladMonster
            e "*Runs full speed into the hospital window.*"
        "DON'T. DAMN IT. DON'T. IT'S DISGUSTING.":
            j "Uhh... who are you saying that to? If it was a thought you should have contained the message in brackets, like:"
            j "(*faint sounds that you can't make out*) and that is how you cure world hunger."
            j "Damn, did I forget to close the brackets? Oh well."
            "Haha. Happens to the best of us."
            j "You know, you showed some good self-control back there with the salad..."
            j "Else you might've caused some sort of salad-apocalypse. *Laughs awkwardly in meta.*"
    jump endings

label jHome:
    menu:
        j "So... like my place?"
        "Yeah, I mean... it's cosy?":
            j "Drop the sarcasm. It doesn't suit you."
            menu:
                "Drop the sass. It doesn't suit you.":
                    j "Okay... if you insist."
        "Would look better without you in it.":
            j "WHA—"
            menu:
                "I mean I'm 'bouta kill you.":
                    "(For best experience of the following sequence, do not click.){w=4.0}{nw}"
                    j "No you're not.{w=2.0}{nw}"
                    "Yes I am.{w=2.0}{nw}"
                    j "No you're not.{w=2.0}{nw}"
                    "Why?{w=2.0}{nw}"
                    j "Copyrighted cat sounds.{w=2.0}{nw}"
                    "What?{w=2.0}{nw}"
                    j "Yes.{w=2.0}{nw}"
                    "You. {w=2.0} wouldn't. {w=2.0} dare.{w=1.0}{nw}"
                    play sound "audio/oiia.mp3"
                    j "I {w=3.0}would{w=3.0} dare.  *Maniacal laughter!*"
                    $ persistent.oiia = True
                "I mean I'm actually 'bouta kill you.":
                    j "..."
                    j "Wait..."
                    j "NOOOOOOOOOO"
                    python:
                        for i in range(3):
                            renpy.say(j, " OOOOOOOOO (X[i + 1])")
                    j "Not AGAIN."
                "I mean I'm moderately 'bouta kill you.":
                    j "You know what... let's calm down. Let's have some toast."
                    j "*Grabs a butter knife.*"
                    j "Y'Know, I'm quite the psycho..."
                    "Are you, now? I dou—"
                    jump endings
        "I guess...":
            j "Oh... :("
            j "You know what..."
            j "I think... I think I'll just go to bed... you should leave..."
            "Sorry! I didn't mean it."
            j "Well either way I am tired. Good night."
            menu:
                "What do you do?"
                "Sleep on the couch.":
                    pass
                "Sleep on his bedroom floor.":
                    pass
                "Sleep on his kitchen counter.":
                    pass
                "Sleep on the strange mat in the attic.":
                    pass
                "Sleep on the odd cage in the basement.":
                    pass
            "*James finds you in the morning.*"
            j "WHAT ARE YOU DOING?! OUT. NOW."
    jump endings

label sbHome:
    j "So... respectfully..."
    j "WHY ARE WE HERE?!?!"
    menu:
        "Don't worry. My sister is a Game Developer.":
            j "Hell's that?"
            menu:
                "You'll like it. So basically...":
                    jump tSecret
                "Some nerdy thing my sister does.":
                    jump bad
                "A club my sis' decided to go to.":
                    jump horrid
        "Don't worry. It's got a cool kitchen.":
            j "I... okay?"
            j "Tell me. Does it at least have salad?"
            menu:
                "Yes.":
                    j "GIMME!"
                    j "GIMME SALAD!"
                    j "NOW!"
                "No?":
                    j "Oh... well... want to go to the shops and... {w=1.0} buy some?"
                    menu:
                        "Sure!":
                            j "YIIIIIPPPPPEEEEEEE!!"
                        "Nah.":
                            j "But— I— uh... o-okay..."
                        "I am broke.":
                            j "I would offer to pay..."
                            j "But I too am broke..."
                            j "But I have experience in theft."
                            j "I once stole candy from a baby and used that to pop the only thing giving them joy — a red balloon. {w=5.0}{nw}"
                            menu:
                                "Oh... how... {w=0.5}cool?":
                                    j "Why, thank you!"
                                "WHA—":
                                    j "I know. Aren't I just the cutest?"
                                    "*Gerald nods.*{w=0.1}{nw}"
            jump endings
        "Don't worry. I... uh... honestly no clue... want to go to a restaurant or something?":
            jump happy

label happy:
    $ persistent.ending_happy = True
    "Well done. You got the happy ending. Are you proud?"
    "A restaurant... how lovely of a 'first date' location."
    "Also..."
    "You."
    "Got."
    "SALAD! {w=0.5} AT LAST! {w=0.5} AT LONG{w=0.75}, LONG {w=0.5}LAST!{w=1.0} SALAD!"
    jump endings

label tSecret:
    $ persistent.ending_secret = True
    j "You know what? Imma join your sister in her next adventure to Narnia."
    "Well done. You got the secret ending. James went to Narnia. He became the king."
    "He lived the life you never could."
    "And got the salad you never had but always wanted. This salad? A—"
    j "C'mon. Wrap it up. I've got a kingdom to run."
    jump endings

label bad:
    $ persistent.ending_bad = True
    "You... you got the ONLY bad ending. You monster."
    "The overseer will see you dealt with, [pronoun].{w=0.5}{nw}"
    jump endings

label horrid:
    $ persistent.ending_horrid = True
    "You got THE ONLY horrid ending..."
    "which makes you kind of unique..."
    "Well done, actually!"
    "(You're still a monster. ;3)"
    jump endings

label endings:
    scene salad_bg with vpunch
    stop music fadeout 2.0
    "{w=0.1}The.{w=1.0} Ending.{w=1.0} List."
    "Which...{w=0.5} is...{w=0.2} awfully salad-coloured?"
    if persistent.geraldNone:
        "Gerald! Did you ACTUALLY do something?"
    else:
        "James... this your doing?"
    if persistent.ending_happy:
        "Happy Ending: ✓"
    else:
        "Happy Ending: ???"
    if persistent.ending_bad:
        "Bad Ending: ✓"
    else:
        "Bad Ending: ???"
    if persistent.ending_horrid:
        "Horrid Ending: ✓"
    else:
        "Horrid Ending: ???"
    if persistent.ending_secret:
        "Secret (Narnia) Ending: ✓"
    else:
        "Narnia? Nah."
    if persistent.geraldNone:
        "Gerald did nothing? Certainly. ✓"
    else:
        "Gerald? What did they do?"
    if persistent.apocalypse:
        "Kinda apocalyptical. Or is it?"
    else:
        "Salad... at the end of humanity? The root cause?"
    if persistent.oiia:
        "Copyright laws hopefully don't prevent me from having done that."
    else:
        "Stay lawful!"
    $ endings = [persistent.ending_happy,
    persistent.ending_bad,
    persistent.ending_horrid,
    persistent.ending_secret,
    persistent.geraldNone,
    persistent.apocalypse, persistent.oiia]
    "That adds up to{w=1.0}.{w=0.9}.{w=0.6}. {w=2.0}[sum(endings)]/[len(endings)] endings!"
    if sum(endings) == len(endings):
        jump john_world_Start
        "You feel gravity start to pull you from the ground,"
        "and as you float into the sky, you start to feel something."
        "Your body starts to warp and deform... change and improve."
        "Yet you feel no pain. {w=2.0} And then a temporary state of unconsciousness (sleep) takes a hold of you."
    if persistent.geraldNone and persistent.apocalypse and persistent.geraldNone and persistent.ending_secret and persistent.ending_bad and not persistent.finale and not persistent.oiia:
        $ persistent.finale = True
        "The Overseer approves."
        "Older than time, Egypt's pyramids, and even my own father."
        "And yet they approve of you."
        "Gerald likes what you've done."
        "You will be rewarded severely yet with nothing of physical nor virtual material."
        "No monetary value."
        "No sentimental value."
        "No value of any sort."
        "Yet more longed for than anything you've yet to see.{w=3.0} More worshiped.{w=2.0} More...{w=2.0}{nw}"
        "exalted than you could ever know."
    scene black with fade
    menu:
        "Again?"
        "Restart.":
            jump start
        "Main Menu?":
            return
    return

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

default persistent.time_out = False
default persistent.the_chase = False
default persistent.the_note_is_a_lie = False
default persistent.unlucky_completionist = False

image mirror:
    "images/Mirror.png"
    zoom 35

image Gridfinity:
    "images/Gridfinity.png"

image keycaps:
    "images/keycaps.png"

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
            persistent.time_out = True
            renpy.say(m, "C'mon. We're going to school.")
            renpy.jump("School")


label overStressed:
    n "You're more stressed than not."
    John "And for that you've been banished back to your world."
    jump start

label john_world_Start:
    show screen stressBar
    $ total_stress = 0.0
    $ time_left = 2000.0
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
    jump JohnEndings

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
    $ privacy = False
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
        "Lock the door" if not privacy:
            n "Privacy first."
            $ stress(-1.0)
            $ privacy = privacy
            jump bathroom
        "Unlock the door" if privacy:
            n "Unlocked."
            $ privacy = not privacy
            jump bathroom
        "Leave":
            jump bedroom

label bChase:
    $ time(1.75)
    $ persistent.the_chase = True
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
                        n "It must be an encoded message... quickly, decipher it!"
                        "Try decipher it...":
                            n "As you over analyse the note, you *note*ice something..."
                            "This can't be..."
                            n "You mutter as you realise something important."
                            n "John has a lie that has rooted so deeply into his mind that he can never say the truth."
                            n "The lie in question: he—"
                            $ persistent.the_note_is_a_lie = True
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
            n "That little gremlin is eating your favourite cereal that you were saving for today!"
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
    n "After you finish changing alone, you have a strange feeling you missed a ton of lore..."
    $ persistent.unlucky_completionist = True
    jump pool

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
                    bully "You two lovebirds having fun? *Sneers a laugh.*"
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
                    jump pool

label pool:
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
        show mirror
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
        $ say("Teacher", "C'mon, everyone! Lesson starting! If you're changed, come out here.")
        b "Well, guess that's our cue! Come on! *Takes your hand, leading you to the pool.*"
        "Yeah. Prepared to drown."
        b "Drown? I do not want to drown. Death would mean not being alive."
        n "Ugh, so monotone. When will they show more emotions?!"
        "*Laughs.*"
        b "What's funny? Death is not funny. It is the end of life."
        "*Chuckles.* Right."
        n "An hour later... after P.E. - you got changed without any hassle and now it's D.T. (Design & Technology)."
        $ say("D.T. Teacher", "Okay, you all have three options of what to do today...")
        menu:
            n "What do you do?"
            "Make keycaps? (Resolution-Design reference!)":
                show keycaps
                n "And here it is!"
            "Make a Gridfinity? (Another Resolution-Design reference!)":
                show Gridfinity
                n "And here it is!"
            "Make art for a visual novel you're calling 'SaladPunk'. A game about—":
                show mirror
                n "Yeah yeah, you've already heard it. After all, you're playing it!"
                hide mirror
                n "*You make some amazing art...*"
                "Yes! Here it is! Perfect!"
                n "3...{w=0.5} 2...{w=0.5} 1..."
                n "And there still is no art!"
                n "That's intentional. Yes. Totally intentional. Don't question it."
        hide keycaps
        hide Gridfinity
        hide mirror
        menu:
            n "Are you PROUD of yourself?"
            "Yes!":
                n "Well your teacher isn't. Your friends aren't. {w=1.0}There will ALWAYS be someone who isn't proud of you. That's guaranteed."
                $ renpy.pause(0.5)
                b "You done staring off into oblivion? Or were you trying to unlock the 'Motivated Ending?'"
                b "All you're unlocking is the door to an aneurysm (however that is spelt)."
            "No, I should've done better!":
                $ say("FreeformWave (Developer)", "Ouch... just so you know, I put a lot of effort into that!")
        jump JohnEndings

image salad_bg = Solid("#00b5fc")

default persistent.burnt_out = False
default persistent.depressed = False
default persistent.motivated = False
default persistent.good_day = False

label JohnEndings:
    scene salad_bg with vpunch
    stop music fadeout 2.0
    "{w=0.1}The.{w=1.0} Ending.{w=1.0} List."
    "Which...{w=0.5} is...{w=0.2} awfully sky-coloured?"
    "Why? Well I don't know! Why you asking me? I'm only the developer."
    "But that is actually a really detailed sky. The birds... the sea in the background... the plane. So much depth!"
    if persistent.time_out:
        "Ran out of time to get ready... ✓"

    if persistent.the_chase:
        "Leave John Alone! ✓"
        if total_happiness < 30:
            "And chase what truly matters."
            "You chased vengeance."
            "Not happiness."
            "Righteous rather than ruthless."
            "Rest rather than rage."

    if persistent.the_note_is_a_lie:
        "THE CAK— NOTE IS A LIE!! ✓"
        if total_stress > 70:
            "Although this 'lie' was not a lie but rather a truth..."
            "A truth that weighs heavily upon your soul."

    if persistent.unlucky_completionist:
        "You done it! {w=1.0}...{w=1.0} Although you missed a TON of the lore..."
        if persistent.the_note_is_a_lie:
            "At least... {w=1.0}at least you learnt that one secret...{w=1.0} despite all the missed emotional context..."

    if total_stress > 80 and total_energy < 30:
        "You're completely burnt out."
        $ persistent.burnt_out = True

    if depressionModifier > 1.0 and total_happiness < 20:
        "You're completely depressed."
        $ persistent.depressed = True

    if total_happiness > 75 and total_energy > 70:
        "You're motivated! You've got this!"
        $ persistent.motivated = True

    if total_stress < 40 and total_happiness > 60:
        "Been a good day. Pretty good day."
        $ persistent.good_day = True

    if all([persistent.time_out, persistent.the_chase, persistent.the_note_is_a_lie, persistent.unlucky_completionist]):
        "You saw all but what mattered. {w=1.0}Your mind was scattered yet soft and oblivious to the truth that mattered."
        "You focused more on your brother than yourself. {w=1.0}A mistake."
        $ say("The Overseer", "I am disappointed... {w=1.0}very, very disappointed.")

    if total_stress < 50 and total_happiness < 50:
        "Nothing went terribly wrong."
        "Nothing went particularly right."
        "The day happened."
        "And so did you."
        "It was safe yet dull. {w=1.0}Fun yet not exhilarating."

    $ endings = [persistent.time_out, persistent.the_chase, persistent.the_note_is_a_lie, persistent.unlucky_completionist]
    "That adds up to{w=1.0}.{w=0.9}.{w=0.6}. {w=2.0}[sum(endings)]/[len(endings)] endings!"

    if total_happiness > 65 and not persistent.unlucky_completionist:
        "Through everything..."
        "You weren't alone."

    scene black with fade
    menu:
        "Again?"
        "Restart?":
            jump start
        "John again?":
            jump john_world_Start
        "Main Menu?":
            return
    return