init python:
    credits = ('Developer & Writer/Story', '{font=BOD_B.TTF}Quibble{/font}'), ('Sprite Artist', '{font=BOD_B.TTF}Teanao{/font}'), ('BG Artist', '{font=BOD_B.TTF}Exitmothership{/font}'), ('Composer', '{font=BOD_B.TTF}Leetmusic{/font}'), ('UI', '{font=BOD_B.TTF}Sasquatchii{/font}'), ('CG Artist', '{font=BOD_B.TTF}SimonAdventure{/font}'), ('Concept Artist & Editor', '{font=BOD_B.TTF}Dalsyke{/font}'), ('RenPy Engine', '{font=BOD_B.TTF}PyTom{/font}')
    credits_s = "{size=80}{font=BOD_B.TTF}Credits{/font}\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=30}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    

    
init:
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    #    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=90}{font=BOD_BI.TTF}End of demo {/font}", text_align=0.5)
    image thanks = Text("{size=70}{font=BOD_BI.TTF}Thanks for playing!{/font}", text_align=0.5)
    
    $ Positioncenter = Position(xpos=0.6, ypos=0.8)
    
    

# The script of the game goes in this file.

image bg credits = "gui/creditsbg.png"
image bg dreamscape = "dreamscapefinal.jpg"
image bg black = "black.jpg" 
image bg mansion = "mansion1.jpg"
image bg mansioninterior = "mansioninterior.jpg"
image bg libday = "mansionlibraryday.jpg"
image bg libnight = "mansionlibrarynight.jpg" 
image bg dinday = "diningroomday.jpg"
image bg dinnight = "diningroomnight.jpg"
image bg bedroomday = "mansionbedroomday.jpg"
image bg bedroomnight = "mansionbedroomnight.jpg"
image bg classroom = "classroom.jpg"
image splash = "splash-screen.png"
image sprite lilamused = "lilamused.png"
image sprite lilblushsmile = "lilblushsmile.png"
image sprite lilcurious = "lilcurious.png"
image sprite lildefault = "lildefault.png" 
image sprite lilsad = "lilsad.png"
image sprite lilsleepy = "lilsleepy.png"
image sprite liltears = "liltears.png"
image sprite lilsurprised = "lilsurprised.png" 
image sprite mbthoughtful = "mbthoughtful.png"
image sprite mbsmileclosed = "mbsmileclosed.png"
image sprite mbinviting = "mbinviting.png"
image mb thoughtful = "mbthoughtful.png" 
image sprite vpout = "vpout.png"
image sprite vsmile = "vsmile.png"
image sprite vthinking = "vthinking.png"
image sprite vangry = "vangry.png" 
image sprite vblush = "vblush.png" 
image sprite wneutral = "wneutral.png"
image sprite wneutral2 = "wneutral2.png"
image sprite wsmile = "wsmile.png"
image spirte wworried = "wworried.png"
image sprite wapologetic = "wapologetic.png"
image sprite meramused = "meramused.png"
image sprite merblush = "merblush.png" 
image sprite merconcerned = "merconcerned.png"
image sprite mermalncholy = "mermelancholy.png"
image sprite mersmile = "mersmile.png"
image sprite mersmileclosed = "mersmileclosed.png" 
image sprite ggensmile = "ggensmile.png"
image sprite gblush  = "gblush.png"
image sprite gpout = "gpout.png"
image sprite gsmile = "gsmile.png"
image sprite gsmileclosed = "gsmileclosed.png"
image sprite gthought = "gthought.png"
image sprite gmwink = "gwink.png"
image sprite nightlilsleepy = "side_nightlilsleepy.png" 
image bg villageday = "villageday.jpg" 

define fade = Dissolve(.5) 

show lneutral 

$ renpy.music.play(channel=7, fadein=2)
$ renpy.music.stop(channel=7, fadeout=2) 

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character ("Lillian", image = "l", who_bold=False)

image side l normal = "side_lildef.png"
image side l amused = "side_lilamused.png"
image side l sleepy = "side_lilsleepy.png"
image side l curious = "side_lilcurious.png"
image side l blushsmile = "side_lilblushsmile.png"
image side l tears = "side_liltears.png" 
image side l sad = "side_lilsad.png" 
image side l surprised = "side_lilsurprised.png"
image side l nightsleepy = "side_nightlilsleepy.png"
image side l nighttears = "side_nightliltears.png"
image side l nightnormal = "side_nightlildef.png"
image side l nightsad = "side_nightlilsad.png"

define mb = Character ("Miss B", who_bold=False) 
define m = Character ("Meredith", who_bold=False)
define w = Character ("Winnie", who_bold=False)
define v = Character ("Virginia", who_bold=False)
define g = Character ("Greta", who_bold=False)
define q = Character ("???", who_bold=False)

$ lady = "meredith"
$ lady = "winnie"
$ lady = "viginia"
$ lady = "greta"
$ g2 = "deny"
$ g2 = "quiet"


label splashscreen:
    scene black 
    with Pause(1)

    show splash with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(.5)

    return

# The game starts here.

label start:
    
    scene bg villageday 
    
    show gwink 
    
    "I hardly have the time to take the quaint scene in as Greta grabs my hand and bolts down the village street." 
