define j = Character("James")

image James:
    "images/James.png"
    zoom 10

image Salad:
    "images/Salad.jpg"

image SaladMonster:
    "images/SaladMonster.png"
    zoom 0.5

label start:
    show James
    j "Heya! I'm James."
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
            j "Ok, Mr. Long-words."
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
            "*Proceeds an onslaught of maniacal salad-beings created from the salad fusing with your DNA.*"
            "*You've successfully ended the world.*"
            "*Aren't you proud? You caused all this... Carnage. Wreckage. Salad.*"
            "*You. Not me. Not Gerald. Not John. Nor Jame—*"
            j "Ok. idiot."
            j "You awake?"
            "*Blinks awake.*"
            j "That salad put you in a salad coma. It's been 15 years."
            menu:
                "I... uh...":
                    pass
                "I swear that—":
                    pass
            j "What? Did you think you caused some sort of salad-appocalyse?"
            j "Don't be ridiculous."
            j "That was of COURSE King Henry the XXI half a year ago."
            define e = Character("Salad Monster")
            show SaladMonster
            e "*Runs full speed into the hospital window.*"
        "DON'T. DAMN IT. DON'T. IT'S DISGUSTING.":
            j "Uhh... who are you saying that to? If it was a thought you should have contained the message in brackets, like:"
            j "(*faint sounds that you can't make out*) and that is how you cure world hunger."
            j "Damn, did I forget to close the brackets? Oh well."
    return

label jHome:
    j "So... like my place?"
    return

label sbHome:
    j "So... respectfully..."
    j "WHY THE HELL ARE WE HERE?!?!"
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
            return
        "Don't worry. I... uh... honestly no clue... want to go to a restaurant or something?":
            jump happy

label happy:
    "Well done. You got the happy ending. Are you proud?"
    "A restaurant... how lovely of a 'first date' location."
    "Also..."
    "You."
    "Got."
    "SALAD! AT LAST! AT LONG LAST! SALAD!"
    return

label tSecret:
    j "You know what? Imma join your sister in her next adventure to Narnia."
    "Well done. You got the secret ending. James went to Narnia. He became the king."
    "He lived the life you never could."
    "And got the salad you never had but always wanted. This salad? A—"
    j "C'mon. Wrap it up. I've got a kingdom to run."
    return

label bad:
    "You... you got the ONLY bad ending. You. Monster."
    return

label horrid:
    "You got THE ONLY horrid ending..."
    "which makes you kind of unique..."
    "Well done, actually!"
    "(You're still a monster. ;3)"
    return