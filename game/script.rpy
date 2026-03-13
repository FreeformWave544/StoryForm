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
define j = Character("James")

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
    play music selected_bgm fadein 1.0
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
    $ endings = [persistent.ending_happy,
    persistent.ending_bad,
    persistent.ending_horrid,
    persistent.ending_secret,
    persistent.geraldNone,
    persistent.apocalypse]
    "That adds up to{w=1.0}.{w=0.9}.{w=0.6}. {w=2.0}[sum(endings)]/[len(endings)] endings!"
    if persistent.geraldNone and persistent.apocalypse and persistent.geraldNone and persistent.ending_secret and persistent.ending_bad and not persistent.finale:
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