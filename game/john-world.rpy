default total_stress = 0.0
default total_happiness = 50.0
default total_energy = 5.0
default depressionModifier = 1.0
default gender = "John"
default name = ""
default dressed = False
default privacy = False
default wearing = {
    "Shirt": False,
    "Tie": False,
    "Blazer": False,
    "Skirt": False,
    "Shorts": False,
    "Trousers": False
}

define m = Character("Mother")

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


label overStressed:
    n "You're more stressed than not."
    John "And for that you've been banished back to your world."
    jump start

label john_world_Start:
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
        jump bedroom
    m "['Ah, you\'re up at long, long last.' if total_happiness < 50.0 else 'Ah, you\'re up! Want something to eat?']"
    return

label wardrobe:
    $ clothes = list(wearing.keys())
    python:
        for outfit in clothes:
            n("Do you wear your [outfit]?", interact=False)
            wearing[outfit] = renpy.display_menu([("Yes", True), ("No", False)], screen="choice")
    $ dressed = True
    jump bedroom

label bathroom:
    menu:
        "What do you do?"
        "Take a quick shower":
            n "You take a quick shower to wake yourself up."
            $ energy(5.0)
            $ happiness(2.0)
            jump bathroom
        "Brush your teeth":
            n "Minty fresh."
            $ happiness(1.0)
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
            jump bathroom
        "Use the toilet":
            n "Best not to skip that before school."
            $ stress(-2.0)
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
    "John! Back here. Now!"
    menu:
        n "Where do you look for John?"
        "His room.":
            pass
        "His personal bathroom.":
            pass
        "The livingroom.":
            pass
        "The kitchen.":
            pass