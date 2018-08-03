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

define fade = Dissolve(.5) 

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

    scene bg dreamscape with fade
    
    play music "nightmare.ogg" fadein 1.0 
    
    l sad "I know you are here."
    
    "It's nowhere near me, yet I can hear it my thoughts." 
    
    "The heavy thumps upon cobblestone fill both my ears. Its presence hangs over me like damp, draped cloth."

    "It’s not real, as far as I can tell. But it's always there, in my head, awaiting the moment I shut my eyes." 
    
    "And then comes the humming." 
    
    "It's a lullaby, meant to soothe young children into peaceful sleep. 
     My mother's humming fills my ears with a familiar tune; the same one she used when she had cradled me tight in her arms."
    
    "But it's not soothing at all.{w=.3} Such things would only be soothing if my mother was still alive." 
    
    "The creature paces around me, and the tune moves with it. I cannot move from my spot in the foreign street."
    
    "The lamplight occasionally reflects a wayward shadow."
    
    l tears "W-what is it you {i}want{/i} from me?!"
    
    "It does not give me a reply." 
    
    scene bg black
    stop music
    play sound "thump.mp3"
    
    "A sharp bump in the road saves me from my torment." 
    
    "The carriage is dark, the curtains on the windows drawn tightly shut. I find myself sitting upright with my hands tangled in them, but luckily, I had not thrown open the door." 
     
    "I disentangle my hands, folding them tightly together in my lap as though that would keep them from moving against my will again."
    
    "I hadn’t meant to sleep, anticipating that something like this would happen if I did." 
    
    "But my nausea from the ship was only worsened by looking out the window to the rolling emerald plains of the Old Continent. And besides, the sunlight was not supposed to be up at this hour."
    
    "My hair feels heavy and knotted, as is typical after these bouts of dreams—I hope I do not look worse than I feel." 
    
    "As the carriage slows, I risk a look through a curtain."
    
    "The stately mansion coming into view does nothing to allay my mood. I fear the mansion's inhabitants more than anything."

    l sad "Perhaps it is not too late to request we turn back?"
    
    "No, that is no longer an option."
    
    "The nightmares are the only reason I’ve made this cross-sea voyage to 'Miss Bullard’s haven for supernaturally troubled women', or whatever it is she calls it."
    
    "They have never stopped, not since the first evening I awoke breathless and in a terrible sweat thinking it was the damp summer air getting to me."
    
    "I have them any time I attempt sleep, and during particularly terrible fits, I move in my sleep as if possessed. Dozing off in class once had me nearly stabbing a fellow student with a fountain pen."
    
    "The nightmares have robbed me of any chance at contentment back home, and I will do anything to find the cure. {w=.3} Even if it means going to a boarding school. {w=.3} In the Old Continent."
                    
    "I still a shudder as the carriage slows further to a stop. It is time for my grand entrance."
    
    "It has to be worth it. The rigid clothes, the poor weather, the cruel instructors, the pompous students…it will be terrible, but not as terrible as my nightmares, right?" 
    
    scene bg mansion
    with fade
    play music "welcome.ogg" fadein 2 fadeout 2
    
    "I do not expect to be greeted with a face full of sunshine when I step down from the carriage with my bags and onto the gravel below." 
    
    show mbthoughtful 
    with fade
    
    "I see the front door of the mansion is already open. A woman whom I can only assume is the headmistress is already there to greet me."
    
    "I cast a nervous glance at my garb, which I have been wearing my first day of travel and still smells faintly of sea salt." 
    
    q "Good morning, are you perhaps Miss Graham?"
    
    l surprised "T-that would be me, yes."
    
    "Her accent is stiff and self-assured. My words feel clumsy in comparison." 
    
    hide mbthoughtful 
    
    show mbsmileclosed
    with fade
    
    "She smiles warmly." 
    
    mb "Wonderful! Welcome to my school! I’m Miss Bullard, the headmistress of this establishment, but you may call me Miss B."
    
    mb "Your father has been wonderful to work with, and rest assured, he is confident that I can provide you the help you need."
    
    "Miss B extends a hand to me, and her smile does not waver as we shake." 
    
    "I have not spoken to my father about my attendance here…or much at all. It was something he had worked out on his own when news of my issue reached him--wherever in the world he had been at the time."
    
    "All I know of him is his penmanship, having not seen or heard him speak in many months. I had only been informed to pack and prepare for the upcoming sea voyage just a week before today."
    
    hide mbsmileclosed 
    
    show mbinviting
    with fade
    
    mb "We are a small establishment, so it should be easy to acquaint yourself with the other students. The older and younger ones tend to keep to themselves, but I’m certain those of your age would love to meet you."
    
    hide mbinviting
    with fade
    
    show mersmile with fade

    "I hardly believe that—until a girl emerges from right behind her, as though she had been awaiting her cue."
    
    show mersmileclosed with fade
    hide mersmile
    
    "She has the brightest smile on her face as she clasps my hands in her own."
    
    m "Meredith Morticelli! It’s so wonderful to meet you, Lillian!"
    
    l surprised "{i}Oh!{/i}"
    
    "I pull back my hands in haste. Her fingers are like ice!"
    
    hide mersmileclosed
    
    show merblush
    with fade
    
    "Meredith gives a sheepish smile."
    
    m "Ahh, oops. I’m sorry, that does tend to startle new people!"
       
    l amused "O-oh, no, I’m sorry for pulling away so abruptly. Nice to meet you, Meredith." 
    
    "Now that I have been sufficiently woken up, I can see someone is standing just behind her."
    
    hide merblush
    show mersmileclosed 
    with fade
    
    m "Winnie, look! The new student I was telling you about is here!"
    
    hide mersmileclosed
    with fade
    
    show wneutral
    with fade
    
    "Meredith steps aside, revealing a frail and bespectacled girl to me. Her hair is a striking red, like hot coals, and her eyes are more honey than brown." 
    
    "In her arms she clutches a book tightly to her chest. She blinks wordlessly."
    
    "I give her what I hope is an encouraging smile."
    
    l normal "Hello there. My name is Lillian."
    
    "She does not smile back but dips her head. Her voice is scarcely a mumble."
    
    w "Winnifred. Nice to meet you, Lillian."
       
    l amused "And you. You have such beautiful hair!"
    
    hide wneutral
    show wsmile
    with fade
    
    "Her lips twitch into a smile, but she purses them tightly together."
    
    w "T-thank you."
    
    hide wsmile
    with fade

    
    show mbinviting
    with fade
    
    mb "Come along now, girls. We ought to bring Lillian inside. She has had a long journey!"
    
    scene bg mansioninterior 
    with fade 
    
    hide mbinviting with fade
    
    "Miss B led the way for me through the already open front door." 
    
    show vpout
    with fade
    
    "When I step inside, I catch the gaze of another lady. Her skin is unblemished as the surface of a pearl, and she is impeccably dressed, her hair styled up and pinned with impressive precision."
    
    "She is also the only student who is wearing a corset. I smile at her despite her disapproving look."

    l normal "Hello, I’m—"
    
    hide vpout
    show vthinking
    with fade
    
    q "Lillian. I heard."
    
    l surprised "Oh. And you are-?"
    
    q "Virginia Belvoir, of the Belvoir fortune."
    
    "I have a feeling that was supposed to mean something to me, but it doesn’t. Perhaps she doesn’t know I’m a foreigner? I thought at least my accent might give me away."
    
    l normal "It’s nice to meet you, Virginia."
    
    hide vthinking
    show vpout
    with fade
    
    v "I would prefer 'Miss Belvoir'."
    
    hide vpout with fade 
    
    "She sniffs and turns away without another word." 
    
    "So there {i}are{/i} some girls here that behave in the way I anticipated. The notion is oddly reassuring."
    
    q "Ohh, who's this?" 
    
    show gsmile
    with fade
    
    "Another student leans over to look at us from the railing."
    
    "In sharp contrast to Virginia, her hair isn't styled in any way: it falls in messy, off-gold tangles at her shoulders. Her clothes are equally wayward, the lace on her sleeves torn and her garment collar partially undone."
    
    "She does not bother to come down but waves at me. Miss B gestures to me."
    
    show mbsmileclosed at right
    with fade
    
    mb "Miss Faye, this is our new student."
    
    show gsmileclosed with fade
    hide gsmile
    
    g "Hello, new student! I’m Greta!"
    
    "Her voice echoes through the hall."
    
    l amused "A-and I’m Lillian!"
    
    "I shout the words back, hoping the act isn’t offensive. Thankfully, I only receive a disapproving look from Virginia. Even Miss B seems more amused than bothered by our exchange."
    
    hide gsmileclosed
    
    show gwink
    with fade
    
    g "Welcome to Miss B’s! I do hope you enjoy your time here!"
    
    "She gives me a wry grin, and I think I see her cross her fingers behind her back. Strange girl."
    
    hide gwink
    with fade
    
    hide mbsmileclosed
    with fade
    
    show mbinviting
    with fade
    
    mb "Now then, Miss Graham. You must be feeling quite weary from your journey. Allow me to show you where you will be staying." 
    
    hide mbinviting with fade
    
    "I follow dutifully behind her. We bypass the stairwell towards one of the westward doorways."
    
    mb "On this floor we have the classroom, dining room, library, and upper student bedrooms, and above we have the remaining bedrooms, balcony, and my study."
    
    mb "As you can probably tell, this mansion was not a school but a family home before I purchased it."
    
    "I had been expecting something a bit more like a traditional school, but even with the furnishings, it’s hard to say the mansion is homey. The architecture, while certainly beautiful, is also predominantly foreign."
    
    mb "The classroom is through the door to the right of the entrance. The dining room we just passed, and the set of bedrooms where you will be staying are just ahead."
    
    "Miss B leads me to a hall of doors, and opens the one furthest left."
    
    stop music fadeout 1.0 
    scene bg bedroomday
    with fade
    play music "calm.mp3"
    
    mb "Here is where you will be staying during your time here. Is it to your liking?"
    
    "The room is much larger than mine at home. The bed looks plenty comfortable—even though beds stopped being comfortable a while ago."
    
    l normal "It looks nice, thank you."
    
    show mbsmileclosed
    with fade
    
    mb "My pleasure. You can put your luggage down for now, and when you’re ready, I can provide you with everything you’ll need during your stay here."
    
    scene bg mansioninterior
    with fade
    
    hide sprite mbsmileclosed
    with fade
    
    show sprite mbinviting
    with fade
    
    "After setting everything down, Miss B leads me back through the entrance, and this time, heads toward the stairwell."
    
    mb "My study is this first door on the left."
    
    hide sprite mbinviting
    with fade
    
    "I wait at the top of the stairs, only seeing a glimpse of it when she goes in, but her study is not nearly as neat as I might have expected."
    
    "Papers are haphazardly stacked in piles and shoved off into corners. Her desk is a menagerie of notebooks, fabric scraps, and fountain pens."

    "She reappears in the doorway." 
    
    show mbthoughtful 
    with fade 
    
    mb "My apologies for the clutter. First, let me ask you something I ask of all my students: how much do you know about magic?"
    
    l curious "Well, I know it’s something we cannot properly control."
    
    mb "That is correct. It’s not something we fully understand, even though it surrounds us, and is in everything we do."
    
    mb "Though few can harness it, it certainly can harness {i}us{/} to its liking. Sometimes, it will even strike us with a terrible affliction."
    
    mb "Like an illness, the smallest amounts can have devastating effects if we become infected."
    
    mb "Now, why don’t you tell me more about your affliction? Nightmares, correct?"
    
    l sad "Yes. And sleep walking, on occasion. Sometimes the fits can get violent, especially if I feel I ought to defend myself." 
     
    mb "And all the dreams are the same?"
    
    l sad "They are. They all take place in the same alley, and I’m almost certain I’m being stalked within it."
    
    l sad "I have never seen the alley before, but I think it may be from a place in my youth? Or perhaps a place my mother used to take me."
         
    mb "All right, I understand. I have reason to believe your affliction is of New Continent origin."
    
    mb "Though I do not know exactly what yet, I have something that will certainly help end the nightmares, at least.  Let’s see."
    
    hide mbthoughtful 
    with fade
    
    "She vanishes back into her study for a moment. I can hear her rummaging around in a desk."
    
    show sprite mbinviting
    with fade
    
    mb "For your affliction, the item best suited for you would be this."
    
    "Upon returning, she stuffs a bundle of aromatic herbs into my hand."
    
    mb "This is fresh cut rosemary grown in Old Continent soil. Tie it over your bedpost, and you will experience no nightmares. It will not cure them, but keep them at bay." 
    
    mb "And you must change it out when it begins to wilt, as it will lose its potency."
    
    "I take the bundle gratefully and tuck it away. The idea of uninterrupted sleep sounds near fictional. Miss B catches the relief in my posture when I take it."
    
    hide sprite mbinviting
    
    show sprite mbsmileclosed
    with fade
    
    mb "You must be exhausted from your trip. Please do not worry about attending classes today. You may go straight to your room and unpack your items. Join us for supper at 8 o clock, if you would like."
    
    l amused "I-I will. Thank you, Miss B!"
    
    mb "The pleasure is all mine."
    
    hide sprite mbsmileclosed
    with fade
    
    "I leave to my room with a much lighter chest, the bundle of rosemary clasped tightly in my hand."
    
    "I sincerely hope she is correct."
    
    scene bg dinnight
    with fade
    
    "I choose to attend supper, which is a rather lavish affair. Miss B insists the students I'd met earlier all sit at the same table, for my better acquaintance."
    
    "Virginia chooses the same items as me, although she takes her time and cuts her food into tiny squares before eating."
    
    "Just across from her, Greta eats voraciously and is met with gentle reminders from Miss B to keep her mouth shut as she chews."
    
    "Meredith only has a bowl of soup, and Winnifred nothing at all, although she seems to enjoy our company nonetheless."
    
    scene bg bedroomnight
    with fade
    
    "Upon returning to my room, I lock my door, tuck the ends of my sheets under the mattress, and sprinkle salt from supper at the foot of my bed."
    
    "The odd ritual has never helped much; the nightmares still came, but I like to think it makes them shorter. And while Miss B was kind, I’m not certain how effective a little sprig of vegetation will be."
    
    "I hang the rosemary over my pillow as the final layer of protection."
    
    scene bg black 
    with fade
    stop music fadeout 1.0
    
    "Sleep comes swiftly. Once I had changed into my nightgown and climbed into bed, I quickly drifted off."
    
    play sound "knock.mp3"
    
    "It is not thuds upon cobblestone, but the sound of brief knocking that wakes me from my slumber."
    
    scene bg bedroomday
    with fade
    play music "school.ogg" fadein 2.0 
    
    m "Lillian?"
    
    "I yawn, rubbing the blurriness from my vision."  
    
    l nightsleepy "Mmm, yes?"
    
    m "Ah, good morning! Sorry to intrude on your rest!"
       
    m "Miss B wanted me to come and wake you. Breakfast has already been served, and class begins in fifteen minutes. Do you know how to get there?"
    
    "I rouse a bit more." 
    
    l nightnormal "I do. Miss B showed me. Thank you, I will be out soon."
    
    "It had been the most restful sleep I had ever experienced. My hair was only disheveled by the pillow this time. I change back into my day clothes and head out into the hallway."
    
    scene bg mansioninterior
    with fade
    
    "I eat breakfast with haste and make my way through the mansion’s lower floor to the apparent ‘classroom’."
    
    l curious "Let’s see… Miss B said the classroom was through the entrance and to the right… so it should be here."
    
    scene bg classroom 
    with fade
    
    "The room was likely meant to be some sort of family living room before its conversion to a classroom: the desks are a bit crammed, and the chalkboard is small." 
    
    "When I enter, everyone has already taken their seats."
    
    show mbthoughtful 
    with fade

    mb "Today, I will be teaching you all grammar for intermediate writing. While this does not pertain to re-entering society, it does make up for the missed schooling I’m certain you’ve all had in your absence."
    
    "I self-consciously run my fingers through my hair, book clutched tightly to my chest. Miss B stops her lecture when she notices me."
    
    hide mbthoughtful
    show mbinviting
    with fade
    
    mb "Ah, Miss Graham! Perfect timing, I was just about to begin class. Pick a seat, please."
    
    hide mbinviting 
    with fade 
    
    "I skim the few rows of desks for free spots."
    
    show mersmileclosed with fade
    
    "There is a space by Meredith, who brightens and gives me a smile as warm as sunlight."
    
    hide mersmileclosed 
    show wneutral with fade
    
    "Another is near Winnifred, who casts her gaze to the hands in her lap the moment our eyes meet."
    
    hide wneutral
    show vpout with fade 
    
    "All the desks by Virginia are unoccupied, but I can understand why: the brief glare she shoots me is made of pure ice."
    
    hide vpout
    show gwink with fade
    
    "There is a spot open besides Greta at the back corner of the class, and I could swear I see her wink when I catch her eye." 
    
    hide gwink with fade 
    
menu:
    "Sit by Meredith":
        jump choice1_M
            
    "Sit by Winnifred": 
        jump choice1_W
            
    "Sit by Virginia":
        jump choice1_V
            
    "Sit by Greta":
        jump choice1_G
            
label choice1_M:
    
    show mersmile with fade
    
    "I return Meredith’s smile and head over to the spot beside her desk."
    
    m "Morning again, Lillian!" 
    
    l normal "Good morning."
    
    "Though I try to return her enthusiasm a yawn overcomes me as soon as I sat down. Meredith gives a light laugh."
    
    hide mersmile
    
    show mersmileclosed
    with fade
    
    m "How is the change in time treating you?"
    
    l amused "Well, as good as it can, I suppose."
    
    "My thoughts still feel hazy, even with the improved night of rest."
    
    hide mersmileclosed
    
    show mersmile
    with fade
    
    m "That’s all right. Miss B is very sympathetic to new students. I’m certain she’ll understand if you need a day or two to adjust. You were very brave to come all the way out here on your lonesome!"
    
    "She sighs, looking down."
    
    hide sprite mersmile
    
    show mermelancholy
    with fade
    
    m "I would love to hear about the New Continent some time, if you’d like to share. I’ve always wanted to travel there but I… well, I ran out of time, you might say."

    "I did not expect a student here to take interest in the New Continent, much less a positive interest. The thought lifts my spirits a bit."
    
    l normal "I would definitely be willing to share, if you’d like!" 
    
    hide mermelancholy
    
    show mersmile
    with fade
    
    m "Please do! I’ll look forward to it, then."
    
    hide mersmile
    with fade
    
    "I cannot help but return her bright smile as class begins."
    
    "Though Meredith and I remain quiet, I can feel her gentle presence keeping track of me throughout."
                                                                                                        
    "She picks up every pen I drop in a sleepy stupor, and lets me look alongside her if I do not have the correct materials."
    
    "By the end of class, I am already feeling much better about my time here. Perhaps it will not be as terrible as I anticipated."
    
    show mersmile with fade
    
    m "Do you know where everything is, or would you like me to show you around?"
    
    l normal "Miss B already showed me, but thank you for the offer."
    
    m "Ah yes, she does give all new students tours. In that case, I will be heading to the front gardens for a time before our next class. Have you had a chance to visit them yet?"
    
    l curious "I believe I saw them on the way in, but I have not gotten more than a glance at them?" 
    
    show mersmileclosed with fade
    hide mersmile
    
    m "They’re very lovely here. Helps keep the mind at ease, I find. You’re more than welcome to join me, if you’d like."
    
    l normal "I’ll certainly consider it!" 
    
    hide mersmileclosed with fade
    
    "Meredith waves goodbye to me, leaving me standing in the hall as the other students walk past."
    
    "Though it has only been a short time, I already feel like I’m on my way to making a new friend."
    
jump choice1_done
    
label choice1_W:
    
    show wneutral
    with fade
    
    "I soften my expression as best I can and move to sit by Winnifred. Her shoulders tense when I sit beside her, but she does not protest."
    
    l normal "Hello!"
    
    "Winnie’s gaze darts to me for a fleeting moment."    
    
    w "Hello."
    
    "Her voice is awfully subdued."
    
    l amused "This class seems interesting."
    
    w "Yes."
    
    "I feel almost bad for her. Perhaps she does not want me to be here?"
    
    l curious "Uh…I’m sorry. If you’d like, I can move to another seat."
    
    show wworried
    with fade
    hide wneutral 
    
    "She straightens up immediately."
    
    w "N-no! No, here is all right."
    
    "Her voice falls once more."
    
    show wneutral
    with fade
    hide wworried
    
    w "I…I do not mind you here. I’m sorry if it seemed that way. I’m not used to being around new students."
    
    l curious "Oh. I see."
    
    "It is a more positive response than I had expected. But I know better than to push her."
    
    "Deciding to let her have my company rather than my words, I turn to a fresh page in my journal and begin to write."
    
    hide wneutral
    with fade
    
    "After class, I watch as Winnie gathers up her things and leaves with impressive speed. She heads off in the direction of the library."
    
    "I would not consider it a poor first impression. But Winnie does not exactly seem eager for new friends, either…"
     
    "Or perhaps she is most comfortable in places outside the classroom." 

jump choice1_done
     
label choice1_V:
    
    show sprite vpout
    with fade
     
    "Keeping my head down, I quietly take a spot beside Virginia."
    
    "She casts a brief disdainful glance to me as I take my seat, and then returns her gaze to the chalkboard."
    
    hide sprite vpout 
    with fade
     
    "I have no idea what I am trying to accomplish sitting beside her. She is the only student who had not shown me kindness upon my entrance."
      
    "But perhaps that is why I chose to sit beside her. She is, in her own strange way, a comfort. Just what I expected when I arrived here, what I had mentally prepared myself for."
      
    "As I take my notes, I catch her looking at me once again… or, rather, my notes."
    
    "When she glances up, I smile. She gives me a dubious look and does not return it."
    
    show sprite vthinking
    with fade
      
    v "Your penmanship is lacking."
      
    l surprised "I—oh."
      
    "I stare down at my writing. It is certainly nothing off a printing press, but it is legible enough. Writing is not something I do often, unless I’m giving notes to the milkmaid or making a schedule."
      
    hide sprite vthinking 
    with fade
    
    "Virginia returned to her own notes, and my gaze falls to her writing: unsurprisingly, her penmanship is impeccable, written in the smooth thin cursive one might expect from a woman so well kept."
      
    "I want to speak to her further, but know better than to interrupt Miss B’s talking. So I focus instead on her lecture."
    
    "By the end of it, Virginia neatly packs away her supplies into her handbag, and heads off in the direction of the dining room without a word or glance."
      
    "Sometimes, a meeting of expectation is the most reassuring thing in the world."
      
jump choice1_done
      
label choice1_G:
    
    show gsmileclosed
    with fade
      
    "Greta is the strangest of the girls here, which is perhaps why I find myself drawn to her. Her slouch on her desk doesn’t budge as I take a seat next to her."
      
    show gsmile with fade
    hide gsmileclosed
    
    g "Hello, hello!"
      
    "Greta gives me a wide smile, but it doesn’t have the warmth behind it that Meredith’s had. It looks more like a cat that has just gobbled up a mouse."
      
    l normal "Good morning!"
    
    "I return the smile as best I can and sit down beside her."
      
    "I feel Greta’s gaze on me as I pull out my supplies."
      
    l curious "Did you want to ask something?"
    
    show gsmileclosed
    with fade
    hide gsmile
      
    g "Oh, no, nothing." 
      
    "Greta tugs at loose strands of her curled hair. It resembles mine after a particularly bad nightmare. It must be a nuisance to brush… if she bothers to brush it at all."
      
    hide gsmileclosed 
    with fade
    
    "I turn back to my notes. A few minutes pass."
    
    "I try to ignore Greta’s stare, instead taking notes on Miss B’s lecture. Greta sighs, drawing my attention back to her."
      
    show gthought
    with fade
    
    g "It’s awfully boring, isn’t it?"
    
    l surprised "Pardon?"
    
    "Her gaze darts to Miss B."
      
    g "Class. This kind of teaching does nothing for us. I can think of ten other activities I’d rather do than be sitting here right now."
      
    l curious "Oh. Perhaps a bit…"
         
    "Miss B's instruction {i}was{/i} a bit dull. It may have been part of the reason I decided to sit this far back."
        
    "Greta nods solemnly."
        
    g "Perhaps the others feel the same, but they will not voice it. They do what’s expected of them. It’s always been the way with ladies here."
    
    l curious "The school?"
    
    show gpout
    with fade
    hide gthought  
    
    g "…{i}here{/i}."
    
    show gthought
    with fade
    hide gpout
    
    "She tilts her head curiously."
   
    g "What about where you’re from? Is your education this drab?"
    
    l curious "Somewhat, I suppose."
    
    "The New Continent’s schooling wasn’t as pressing on matters like etiquette, but I never took a particular interest in any subject."
    
    "Most of my interest lied in tending to the animals to on the estate, or reading the occasional novel I found in my father’s otherwise empty room."
    
    "Greta shrugs."
    
    g "I suppose that’s just how it is. At least you are honest enough to admit it, unlike everyone else."
    
    show gsmileclosed with fade
    hide gthought 
    
    "Her expression turns sly." 
    
    g "It’s all right, though, I’ve discovered a wonderful source of amusement!"

    hide gsmileclosed
    show mbthoughtful
    with fade
    
    mb "Miss Faye, the lecture."
    
    "Miss B’s voice is not cruel, but she’s staring at Greta with intent. I cover my own mouth, realizing I had been talking just as much as her."
    
    hide mbthoughtful 
    show gthought
    with fade
    
    g "Yes, yes, I know."
    
    show gwink 
    with fade
    hide gthought
    
    "She lowers her voice to a whisper."
    
    g "I’ll show you what I mean, so come by the dining room at class’ end!"
    
    "She gives me a wink before returning to ‘note-taking’: the notes looked suspiciously like drawings."
    
    hide gwink
    with fade
    
    "When class ends, she gathers her items and leaves without another word."
    
    "I stand by my initial summation. She’s an odd girl."
    
jump choice1_done

label choice1_done:
    
    scene bg mansioninterior with fade
    
    "There is an overwhelming amount to do."

    "If I wish to study the nature of magic and take problem solving into my own hands, the library is definitely the best place to start." 
    
    "But perhaps I do not want to dwell on my troubles my entire time here. Besides, a walk in the gardens after such a long day sounds pleasant."
    
    "Though I also have a bit of an appetite, and the dining room is only steps from my room." 
    
menu: 
    "Library":
        jump choice2winnie
            
    "Gardens": 
        jump choice2meredith
            
    "Dining Room":
        jump choice2dinroom
            
label choice2winnie: 
    scene bg libday with fade

"My first step is clear to me. I have to identify what exactly my affliction is, and there is no better place to do research than the school’s library."
    
"Seeing Winnie here is no surprise at all."

"She is sitting by the coffee table thoroughly engrossed in her book, studying the words with the precision of someone trying to thread a needle."

"The sound of my footsteps on the wooden floor makes her look up."

show  wsmile
with fade

w "Hello, how can I—oh!"

show wneutral
with fade
hide wsmile

"She startles when she recognizes me."

w "Lillian. Hello."

"Her voice goes quiet again, and she wrings her hands together as though washing them beneath a faucet. I suddenly feel like I should move."

l surprised "Sorry, I’m just here to browse!"

hide wneutral
with fade

"I move past her, hoping my very presence isn’t intruding upon her private sanctuary."

"The books are meticulously shelved and swept free of dust. I’m not certain what exactly I am looking for…but “Curses Through the Ages” sounds like a good place to start."

"I open it whilst standing, not wanting to encroach on her space any further than I had to. She only glances up once, but I keep myself busy with my book."

"Unfortunately, not one of the curses listed is related to nightmares. There are curses for insomnia, never-ending itch, flu symptoms… but nothing on dreams of any kind."

"I close the book with more force than I intend." 

show wneutral
with fade

w "Were you… looking for anything in particular?"

l sad "I wish I knew what I was looking for, honestly."

"I breathe a sigh, rubbing my knuckles against my temples. Winnie tilts her head."

w "Lillian, why are you here?"

"She doubles back the moment the words leave her barely-parted lips."

show wworried
with fade
hide wneutral

w "I-I mean, here at the school! Not the library! The library belongs to everyone, you can come here whenever you so please!"

l sad "In truth, I have no idea what I have. I came here in hopes of sorting that out."

"I push the book away."

l sad "But I’m not even certain where to begin."

show wneutral2
with fade
hide wworried

"I look up to see Winnie staring at me with surprising boldness."

w "What are your symptoms?"

l curious "Nightmares. Almost every night, without fail, and occasional sleepwalking to accompany them. Miss B’s rosemary seems to help, though."

w "I cannot make any promises, but I will do my best to look into this for you, myself."

l normal "Oh, thank you! I appreciate it."

"I glance at the book she is perusing."

l normal "Are you here to learn what sort of affliction you have, too?"

show wneutral
with fade
hide wneutral2

"She closes the book with haste."

w "Oh, no. I…know what I have." 

"I’m not certain if I ought to pry. There is a chance I could help her in kind, if I knew what it was. But is it too soon to ask?"


menu:
    "“'What is it that ails you?'”":
        jump choicew1_incorrect
            
    "'Are you looking for anything in particular?'": 
        jump choicew1_correct
            
label choicew1_incorrect:

l curious "What is it that ails you?"

show wworried with fade
hide wneutral

"Her skin seems to be turning a shade pinker."

w " I-I’m sorry. I’d really rather not say."

show wneutral with fade
hide wworried

"She purses her lips firmly together."

jump choicew1_done 

label choicew1_correct:
    
l curious "Are you looking for anything in particular?"


show wneutral2
with fade
hide wneutral

"A glimmer of relief shines through her eyes." 

w "Oh, no, not me. I already know all of these books quite well. And I’m not searching for any cures."

jump choicew1_done 

label choicew1_done: 

l curious "I see."

hide wneutral with fade
hide wneutral2 with fade

"Winnie doesn’t look like she has any more to say, and I don’t want to push her."

"Instead I search the shelves for another title. But nothing else sounds relevant to my affliction, and feeling Winnie’s gaze on my back, I have trouble focusing."

"Accepting defeat, I stand away from the shelves."

l normal "Well, I will be likely be back to search more tomorrow."

show wneutral2 with fade

w "O-okay. I will do some searching of my own in the meantime."

"She gives me a nod and adjusts her glasses. I smile at her—poor thing could probably use it—and head back out, feeling no more educated on my affliction."

hide wneutral2
with fade

"But at least, possibly, I have made the beginnings of a friend."

jump choice2winnie_done

label choice2meredith:
    scene bg mansion with fade

"While I had always thought the Old Continent had poor weather, Miss B’s location seems to be the consistent exception. I emerge from the front doors of the mansion and into rays of afternoon sunshine."

"The gardens are large and expertly kept, with trimmed hedges and blooming flowers that must be native to the Old Continent. Songbirds chitter away in the dense cluster of trees out by the gates."

"I spot Meredith crouched beside a flower patch with cupped hands. She hears my boots upon the dirt, and turns to face me."

show mersmile with fade

m "Oh, Lillian!" 

"She stands up immediately, dusting stray bits of soil off her skirt with the back of her hands. Her palms appear to be damp."

m "Good afternoon."

l normal "And you."

"I peer down at the flower patch."

l curious "What were you doing?" 

show merblush with fade
hide mersmile

"Meredith seems to blush: it’s a bit harder to tell, because in contrast to Winnie, the pink is duller. But it's certainly there." 

m "Oh, something frivolous. I noticed that some of the daisies had begun to wilt in the warm sun, so I was giving them a drink."

l amused "I think that’s very kind of you!"

"She scratches her cheek."

show mersmileclosed with fade
hide merblush

m "It’s nothing, really. But it makes me happy to know you appreciate it."

l normal "I grew up helping to raise animals, but I know very little about plants."

"Meredith glances back at the plants."

show mersmile with fade
hide mersmileclosed

m "Miss B taught me about all of the flowers here when I first came to the school. It helped take my mind off of…certain other things. And helped me get used to my new life here."

"She tilts her head at me slightly."

m "I am curious, though. As a newcomer, what do you think of Miss B as a teacher?" 

menu:
    "'She is very generous.'":
        jump choicem1_correct
            
    "'Something about her seems a bit odd.'": 
        jump choicem1_incorrect
        
label choicem1_correct:
    
l normal "She is very generous! Miss B has been exceptionally warm and accepting of me, and helpful with my affliction."

"Meredith nods."

show mersmileclosed with fade

m "She truly is! I find her inspiring. She has so much love to give to all of her students, I cannot imagine a better instructor for us!"

jump choicem1_done

label choicem1_incorrect:

l curious "Something about her seems odd. She is very kind, but… I cannot shake the feeling that there is more to her than we can see. Buying a mansion just to run a school is a bit strange, isn’t it?"

"Meredith’s bright expression falters briefly but she covers it up quick with her usual smile."

m "Lillian, I do understand that you are new here and came to this school with certain expectations. Your concern is certainly warranted."

m "But I can assure you, Miss B is incredibly benevolent. The amount of sacrifices she makes for us are astonishing. I believe, in time, you will come to see that."

jump choicem1_done

label choicem1_done:

l curious "Truthfully, I expected her to be much stricter. I read as much in the books back home."

show mermelancholy
with fade
hide mersmileclosed
hide mersmile 

"Her smile wavers and then fades."

m "Much as I hate to admit it, Miss B is quite unique. The instructors I had before the… incident, were a lot less warm."

m "They have a standard of how they believe Old Continent women ought to be, and if you don’t fit that standard, you are labeled as an outsider. Especially if you are not of high social standing."

show mersmile with fade
hide mermelancholy

m "Of course, by being at this school we are all outsiders, so I suppose conforming to those standards hardly matters anymore." 

show mersmileclosed with fade
hide mersmile

m "I feel incredibly fortunate to have ended up here, and I sincerely hope that you feel that way, soon, too."

show mersmile with fade
hide mersmileclosed

"She looks up to the mansion." 

m "I suppose we ought to head to class. Would you like to walk together?"

l normal "I would love to!" 

m "If you’d like, I can share a bit of my horticulture knowledge with you…"

hide mersmile
with fade

"We spend the remainder of the walk discussing flowers."

"Something about Meredith makes her exceptionally easy to talk to, even if I know nothing about the subject matter."

"Perhaps it is her welcoming demeanor, or her ever-inviting smile, or the way she apologizes profusely if her icy fingers brushed mine."

"Regardless, I cannot think of a more pleasant companion to have for my first day at Miss B’s."

jump choice2meredith_done
                                                                                   
label choice2dinroom: 
    
    scene bg dinday with fade

"In the dining room, both Virginia and Greta are seated. They are both by themselves." 

menu:
    "Sit by Virginia":
        jump choice2virginia
            
    "Sit by Greta": 
        jump choice2greta
        
label choice2virginia:

"I am not certain what horrible impulse has come over me as I cross the room towards Virginia. But much like how being told a plate is hot makes one want to touch it, I find myself drawn to her table."

"She is sitting all alone, after all. Perhaps she wishes for a friend?"

"A much younger student approaches her table. Virginia shoots them an icy stare, and they quickly turn the other way."

"Perhaps not."

"Regardless, she has already spotted me, and I have no choice but to follow through with my intentions. I take a seat across from her."

l normal "Hello."

show vpout
with fade

"Virginia stares at me disapprovingly, and it feels as if her eyes could wear holes into my own."

l amused "I…thought you looked lonely here. I wanted to give you some company!"

show vthinking with fade
hide vpout

"She closes her eyes." 

v "Miss B has become awfully desperate."

l surprised "Pardon?"

v "She is bringing in ladies from the New Continent onto her grounds. That alone is a mark of desperation."

show vpout
with fade
hide vthinking

"She eyes me up and down, from my boots to my hair."

v "A lady of lower social standing, no less. This is an etiquette school. I cannot see how a woman of your disposition can be enriched by etiquette. Or even improved. But Miss B knows best, right?"

"I bite my lip. Her words sting, as I expected…but I’m not certain if I should brush them away or fight against them."

"What did she anticipate me doing, and how could I do the exact opposite?"

menu:
    "Ignore Virginia's Remark":
        jump choicev1_correct
        
    "Protest Virginia's Remark":   
        jump choicev1_incorrect
        
label choicev1_correct:

"I return her words with a bright smile."

l normal "I do agree, Miss B is quite kind! We are fortunate to have such a benevolent instructor."

show vangry
with fade
hide vpout

"Virginia’s mouth twitches and her brow furrows. It appears she did not expect my compliance. Encouraged, I press on to a different subject."

jump choicev1_done 
    
label choicev1_incorrect:

l curious "I am more than able to pay for this school, but thank you for the {i}inquiry{/i}."

"I barb the final word. Virginia hums."

v "No, you are not able. But perhaps your parents are."

"I want to retort with it being the same case for her, but I bite my tongue. I mustn’t feed her appetite for this conversation any further. I press on to a different subject."

jump choicev1_done

label choicev1_done:

l curious "Perhaps you could tell me more about the Old Continent? This is my first time here, after all."

show vthinking
with fade
hide vangry 
hide vpout

"Her demeanor actually softens, if only a bit."

v "Oh, very well. It is my duty as your superior to provide higher knowledge, if you seek it. What do you wish to know?"

l surprised "A-ah, I am not certain…how you spend summers when you are not here, perhaps?"

show vneutral with fade
hide vthinking

"Virginia nods."

v "Summer is a lady’s season, so we must attend social gatherings."

v "Most women need to impress and make their name known, but that has never been an issue for me. The Belvoir title is highly coveted here, so I need only look the part."

l normal "I see! What are these gatherings like?"

show vthinking with fade
hide vneutral

v "Unlike anything you could hope to attend, that’s for certain."

"Lavishly decorated, scented with the finest flowers, served the finest food in the Old Continent. The men discuss politics, but that is hardly a woman’s interest, so we exchange gossip instead."

"And the clothing is absolutely exquisite. I have an entire wardrobe dedicated to these articles." 

"I frown."

l curious "Must you always wear such uncomfortable clothing?"

"Virginia laughs daintily at that remark."

show vsmile
with fade
hide vthinking

v "Oh, Miss Graham. There is great comfort in knowing that you are the most desired person in a room."

"I shift in my chair. Her gaze goes from amused to skeptical." 

show vpout
with fade
hide vsmile

v "It’s only fair I ask the same of you. What sort of {i}excursions{/i} would your quaint little group embark on?" 

"Fond memories of hot summertimes, buzzing flies, and picnics by the lakeside rise to my mind’s surface."

l normal "No gatherings like that. We always went camping, deep within the woods."

l normal "We would pack only our nightgowns and stay in leather tents and eat dried meat rations and foraged berries. But we had to keep them with us, or the bears would find them."

"Virginia wrinkles her nose."

v "That sounds absolutely abhorrent. It’s no sort of activity for a woman of propriety. I would die in such conditions."

l amused "You would certainly die without your wardrobe!"

show vangry 
hide vpout

"Her brows furrow, and I stifle a laugh. Then, she clears her throat."

v "Regardless. I am appalled by the lack of commitment of the students in this school."

show vpout
with fade
hide vangry

"She glances about the room disapprovingly."

v "Are we not here to learn feminine graces? To {i}remind ourselves{/i} of feminine graces?"
   
v "Miss B is so soft with everyone. It’s as though she does not understand the point of a boarding school at all."

"Virginia hails from a boarding school like those terrible stories, I’m certain of it. The teachings are still very much within her."

l curious "Do you truly believe your previous school superior to this one?"

show vpout
with fade
hide vthinking

v "I—{i}previous{/i} school?"

"The very notion is ridiculous to her."

v "And what gave you the idea I would have ever attended a school before now?"

l surprised "To…be educated?"

v "I received education from my governess. Only women who cannot afford private tutoring would go to such establishments."  

"Oh."

"No cruel headmistresses, and the stuffy students do not even attend schools in the first place…my novels truly were works of pure fiction." 

"Virginia is staring at me dubiously. I try to hide my sense of embarrassment." 

l surprised "I-if you don’t need school, why are you here?" 

show vangry
with fade
hide vpout

"She scoffs."

v "Such a frivolous question. The same reason everyone else is here. I’ve been inconvenienced by a magical affliction. That is all you ought to know."

l curious "What sort of affliction?"

v "One that is often called ‘no business of yours’."

l curious "You are awfully rude."

v "And you are awfully nosy."

show vneutral
with fade
hide vangry

"She takes a long sip of her tea, and then stares at the bottom of her teacup, as though I am not even there."

l curious "I…will be leaving, I suppose."

show vthinking
with fade
hide vneutral

v "Good. Only speak with me again if you have something relevant to share."

hide vthinking
with fade

"{i}Nothing is possibly more relevant at this school than magic!{/i}"

"But I dare not speak the words and provoke the beast further. Instead, I collect my dishes and stride off to the kitchens."

"Virginia is not kind. Nor is she genuine. I am certain there is something buried beneath that icy blue gaze…"

"…but perhaps it is best I do not uncover it." 

jump choice2virginia_done

label choice2greta:

"Greta makes eye contact with me immediately. I offer her what I hoped is a friendly smile as I make my way to her table."

show gsmileclosed
with fade

g "You chose well, Lillian."

l surprised "Pardon?"

show gsmile
with fade
hide gsmileclosed

"Greta just smiles back at me as I sit down across from her."

"Similar to what I’d seen at dinner, Greta has helped herself to far more food than anyone else. Most are various pastries and treats—but one could hardly tell even that, with the speed Greta is polishing them off."

show gthought
with fade
hide gsmile

g "Unfortunately, dining periods are often just as dull as class periods."

"Greta scoops up a liberal helping of jam on her knife."

l curious "What do you like to do to pass the time, then? Do you like to read?"

g "Eh." 

"She manages her next sentence through a mouthful of jam-covered pastry."

g "The novel topics are not of interest to me. Too stuffy."

l curious "So…what is it you enjoy doing?" 

show gwink
with fade
hide gthought

g "Oh, a bit of this and that." 

"Suddenly, she fixes her gaze on the table a few paces away from us. I follow it, noticing Virginia stirring a spoonful of sugar into her teacup."

show gsmile 
with fade
hide gwink 

g "Ah, it begins!"

l surprised "Begins…?"

"She taps the partially empty salt shaker on our table, which I could have sworn was full at breakfast." 

g "Watch."

hide gsmile with fade

"Virginia lifts the cup to take a long swallow of her tea. She stops mid-sip and gives a horrible sputter." 

show vpout 
with fade

v " W-what…{i}what is the meaning of this?!{/i}"

show gwink at left with fade

g "It is tea of the sea!"

show vangry 
with fade 
hide vpout

"I have never seen a woman grin so broadly. Virginia’s barbed glare does nothing to faze her. I hide my laughter behind a forced cough."

v "I should expect nothing less from you. What a wretched girl."

"Greta just shrugs and helps herself to another pastry. Virginia mutters something quite undignified for her under her breath." 

hide vangry 
with fade

hide gwink with fade
show gsmile with fade

"I cast a wary glance at the sugar bowl on our table." 

l curious "Have you put salt in all of them?"

"Greta shakes her head."

g "Oh, no, that was a jest exclusively for the lady Belvoir. She really ought to loosen her corset laces, don’t you think?"

g "Rest assured I would never pull that on someone like Meredith! But none are completely safe."

"She gives me a wry smile."

show gsmileclosed
with fade
hide gsmile

g "Soon, nor will you be!" 

l surprised "A-ah, I see…"

"Greta has a peculiar idea of fun, and I’m not certain what to make of it. No one ever dared to step out of boundaries at my old school, and this was the last sort of institution I’d expect to find a trickster in."

show gsmile with fade
hide gsmileclosed

"Greta is watching me carefully, anticipating some kind of response." 

menu:
    "'I suppose I ought to watch my back, then!'":
        jump choiceg1_correct
        
    "'I'd rather be exempt from your amusement.'":   
        jump choiceg1_incorrect
        
label choiceg1_correct:

l amused "I suppose I ought to watch my back, then!" 
    
show gwink 
with fade
hide gsmileclosed 

g "You know it, my dear Lillian."

hide gwink 
with fade

"Greta hums cheerfully as she goes back to eating."

jump choiceg1_done

label choiceg1_incorrect:
    
l curious "I’d rather be exempt from your amusement."

show gpout 
with fade
hide gsmileclosed

g "It’s not as if I was offering you a choice."

"She pouts somewhat childishly, but does not say more." 

hide gpout with fade

jump choiceg1_done

label choiceg1_done:

hide gpout with fade
hide gwink with fade

"I am only halfway through my meal when Greta finishes her own. She wipes the stray crumbs off her lip with a sleeve."

show gsmile
with fade

g "Well, I have other places to be before class resumes. Perhaps our paths will cross again."

hide gsmile
with fade

"Greta gives me another wink before leaving the table and dining room with impressive speed. I have no idea where she went, but she is no longer in the hall."

"Come to think of it, I have no idea why Greta is here."

"She does not seem to be troubled, from what I could tell. She is certainly having the most fun of everyone. It is comforting to meet such an honest person in the Old Continent."

"It makes me feel a little less like an outsider."

"I am not certain if I wish to see her again. But perhaps I will not have to seek her out for her to find me." 

jump choice2greta_done

label choice2winnie_done:
    
stop music fadeout 1.0
play music "calm.mp3" fadein 2.0

scene bg classroom with fade

"Returning to class, I find myself immersed in a rather uncomfortable activity." 

l surprised "Ouch!"

"I press my punctured thumb to my lips."

show mbsurprised
with fade

mb "Are you all right, Miss Graham?"

l curious "Y-yes, I’m fine." 

show mbinviting 
with fade
hide mbsurprised 

"Miss B returns to addressing the class."

mb "Upkeep of the ability to hand stitch is essential for any woman entering society. Luckily, none of you have ailments that should significantly impair this ability." 

hide mbinviting with fade

"I stare dubiously at the lopsided needlework on my lap. Even with some rest, leftover sleepiness and clumsy fingers were doing me no good." 

show mersmile with fade

m "It’s all right, try keeping your fingertips a bit more spread out. Like this."

hide mersmile with fade

"Meredith reaches over to gently guide my fingers with her own. She smiles apologetically when I flinch from the cold."

show vpout at right with fade

v "Is it really all that surprising Miss Graham is the one to struggle with this? Needlework requires delicate hands, not those calloused from a countryside life."

show mbthoughtful with fade

mb "Miss Belvoir, please try to be tolerant. She just joined us; of course she will need an adjustment period."

hide vpout at right with fade

hide mbthoughtful with fade

show wneutral
with fade

"Virginia sighs and returns to her needlework. Beside her, Winnie is looking at me, but quickly busies herself with the fabric on her lap when she catches my gaze."

hide wneutral
with fade

show gsmile at left 
with fade

g "Aaand done!"

show mbsurprised with fade

mb "Already, Miss Faye?"

show gsmileclosed at left
with fade
hide gsmile at left

"Greta holds up her fabric scrap for the class proudly. It is… certainly a colorful work. I can’t quite tell if the green and red spotted pattern is a bush of roses, an unusual dress design, or perhaps plumage of a rare breed of bird." 

show mbinviting 
with fade
hide mbsurprised

mb "It certainly has a lot of character. Although you may want to work on cleaning up the edges, they are fraying."

show gsmile at left
with fade
hide gsmileclosed at left

g "All right!"

hide gsmile at left with fade

"Greta returns to her needle and thread with impressive ferocity."

mb "How is everyone else?"

hide mbinviting with fade

show vthinking at right
with fade 

v "I will be done in ten minutes."

show wneutral at center
with fade

w "I…I’m taking a bit longer than usual. I’m sorry."

show mersmile at left
with fade

m "Don’t worry, Winnie! I can help you, if you’d like."

hide wneutral
with fade

hide vthinking
with fade

hide mersmile
with fade

"I am also behind, and with little to show for it. I hurriedly return to it, biting my lip when I jab myself once more."

"Miss B comes up behind me."

show mbthoughtful
with fade

mb "And you, Miss Graham?"

"She looks over to my lap."

mb "I see. Needlework is a new pursuit for you, I take?"

l sad "I-I’m afraid so. I’ve fixed ripped clothes in the past, but that’s the extent of my sewing ability."

"Miss B puts her hand on my shoulder."

show mbsmileclosed with fade
hide mbthoughtful

mb "That is all right. Please do not fret over it. I’m certain that in the time you spend in my institution, you will see much improvement."

l normal "T-thank you." 

hide mbsmileclosed
with fade

"She smiles warmly before moving on to look at the other students’ work."

"Never at any school have I had an instructor be so sympathetic of learning difficulties. I look down at my work with a smile of my own, despite the fresh bead of blood on the tip of my pointer finger." 

"Perhaps I can learn to like this place."

stop music fadeout 1.0

jump choice3winnie

label choice3winnie: 
    play music "school.ogg" fadein 2.0 
    scene bg mansioninterior with fade

"Uncertainly still hangs heavy in the air as I walk away from the classroom and down the hall."

"My past few nights here have been pleasantly dream-free, but I am acutely aware of every wilting petal or browning stem on each cut of rosemary. I have no idea where to begin next."

"Fortunately, I don’t have to begin anywhere."

w "Lillian!"

"Winnie’s voice, far louder than I’ve ever heard it before, attracts my attention. I turn to look at her."

show wworried
with fade

w "O-oh, sorry, did I startle you?"

"She flinches as I turn to look at her. It looks like I have startled {i}her{/i} far more." 

l curious "No, I’m all right. What is it?"

show wneutral 
with fade
hide wworried

w "Um…I know you probably want to go to lunch, but could you come to the library with me for a moment? I have something to give you." 

l normal "Oh, of course!"

hide wneutral
with fade
hide wworried

"I follow her. Winnie casts the occasional glance back, as though making certain I haven't left. Each time, I offer a smile; she just dips her head quickly and keeps walking." 

scene bg libday with fade

"At the library, some books are already set out on the table."

"I realize they are all books for curses; based on the thick layer of dust covering them, they have been pulled from far back in the shelves."

show wneutral2 
with fade

w "Well…it’s a start, at least. I hope they can help you in some way."

"I run my finger along the spines."

l curious "What are these?"

w "Books on nightmares. Some of them are novels over fact books, but I figured they could be just as helpful."

l amused "Oh, Winnie, thank you so much!"

show wsmile
with fade
hide neurtal2

"I’ve never had an acquaintance so willing to help me, much less believe the nightmares are worth curing. Winnie dips her head, bashful, but smiles."

w "You do not need to thank me. I have a lot of time to spend."

"I dust the books with a free hand. It is a modest stack, but the books are thick enough to occupy the greater end of my evening."

w "I have some I’ll be reading, as well. The denser ones. N-not that I don’t think you’d appreciate them! But I have a lot of time to spend, and this is a mystery I’d love to help you solve, if you’d like."

l amused "Of course! I very much appreciate the help, Winnie, truly."

"We look at each other in silence for a moment. I think to invite her to lunch, but she doesn’t seem the type to appreciate last-minute plans."

"Even still, I want to pay her back in some way, and potentially make my first friend here."

"In that case, a plan for the following day might be better."

l normal "Say…would you like to go on a picnic with me tomorrow?"

show wworried
with fade 
hide wsmile

w "O-oh!"

"Her eyes widen. Her face, already tinged in pink, seems to turn a shade deeper."

show wneutral2 with fade
hide wworried with fade

w "O-oh, yes. That would be r-really lovely..."

"I can’t tell if her stammering is from excitement, or embarrassment."

"Perhaps she doesn’t want to go and is just being polite. Maybe I am taking everything too quickly. She is awfully timid, and I don’t want to overwhelm her." 

menu: 
    "'I look forward to it, then!'":
        jump choicew2_correct
        
    "'On second thought, would you rather do something else?'":   
        jump choicew2_incorrect
        
label choicew2_correct:
    
l amused "I look forward to it, then!" 

show wworried
with fade
hide wneutral2

"Winnie clutches her book closer to her." 

w "R-really? You do?"

l normal "Of course! We can discuss our findings. Like detectives!"

show wsmile
with fade

w "Yes, exactly!" 

"In that moment, the eyes behind her thick glasses are impossibly bright."

jump choicew2_done

label choicew2_incorrect:

l curious "Well, the weather here is awfully temperamental from what I’ve heard; there is no telling what will come of it."

show wworried 
with fade 
hide wneutral2

"Winnie shakes her head with impressive speed."

w "O-oh no, no, a picnic is fine! I’m sorry if I seemed uninterested, that wasn’t my intention at all. I just…I’m sorry. I’m not good with this sort of thing."

show wneutral2 with fade
hide wworried

jump choicew2_done

label choicew2_done:
    
show wneutral2 with fade
hide wsmile 

"I take the stack of books from the table." 

l normal "I will see you tomorrow, then!"

w "Yes. I hope your night is nightmare-free."

l normal "And yours, too!"

show wsmile with fade
hide wneutral2

w "Y-yes, right… thank you."

"Winnie gives a small laugh, but not without covering her lips with a hand. Dipping my head, I carry the stack of books back to my room."

hide wworried with fade
hide wsmile with fade

"Even if Winnie is not outgoing, I believe that her heart is kind and her mind sharp. I could not hope for better assistance when it comes to determining what my affliction is."

"And perhaps, with the right encouragement, I can uncover her affliction, as well. She doesn’t seem to think she could be helped, but I have every reason to believe otherwise."

"After all, if mine can be abated with a bundle of herbs, it is only a matter of finding what could temper hers."

jump choiceend_done

label choice2meredith_done:
    
stop music fadeout 1.0
play music "calm.mp3" fadein 2.0
    
scene bg classroom with fade

"Returning to class, I find myself immersed in a rather uncomfortable activity." 

l surprised "Ouch!"

"I press my punctured thumb to my lips."

show mbsurprised
with fade

mb "Are you all right, Miss Graham?"

l curious "Y-yes, I’m fine..." 

show mbinviting 
with fade
hide mbsurprised

"Miss B returns to addressing the class."

mb "Upkeep of the ability to hand stitch is essential for any woman entering society. Luckily, none of you have ailments that should significantly impair this ability." 

hide mbinviting with fade

"I stare dubiously at the lopsided needlework on my lap. Even with some rest, leftover sleepiness and clumsy fingers were doing me no good."

show mersmile with fade

m "It’s all right, try keeping your fingertips a bit more spread out. Like this."

hide mersmile with fade

"Meredith reaches over to gently guide my fingers with her own. She smiles apologetically when I flinch from the cold."

show vpout at right with fade

v "Is it really all that surprising Miss Graham is the one to struggle with this? Needlework requires delicate hands, not those calloused from a countryside life."

show mbthoughtful with fade

mb "Miss Belvoir, please try to be tolerant. She just joined us, of course she will need an adjustment period."

hide vpout at right with fade

hide mbthoughtful with fade

show wneutral
with fade

"Virginia sighs and returns to her needlework. Beside her, Winnie is looking at me, but quickly busies herself with the fabric on her lap when she catches my gaze."

hide wneutral
with fade

show gsmile at left 
with fade

g "Aaand done!"

show mbsurprised with fade

mb "Already, Miss Faye?"

show gsmileclosed at left
with fade
hide gsmile at left

"Greta holds up her fabric scrap for the class proudly. It is… certainly a colorful work. I can’t quite tell if the green and red spotted pattern is a bush of roses, an unusual dress design, or perhaps plumage of a rare breed of bird." 

show mbinviting 
with fade
hide mbsurprised

mb "It certainly has a lot of character. Although you may want to work on cleaning up the edges, they are fraying."

show gsmile at left
with fade
hide gsmileclosed at left

g "All right!"

hide gsmile at left with fade

"Greta returns to her needle and thread with impressive ferocity."

mb "How is everyone else?"

hide mbinviting with fade

show vthinking at right
with fade 

v "I will be done in ten minutes."

show wneutral at center
with fade

w "I…I’m taking a bit longer than usual. I’m sorry."

show mersmile at left
with fade

m "Don’t worry, Winnie! I can help you, if you’d like."

hide wneutral
with fade

hide vthinking
with fade

hide mersmile
with fade

"I am also behind, and with little to show for it. I hurriedly return to it, biting my lip when I jab myself once more."

"Miss B comes up behind me."

show mbthoughtful
with fade

mb "And you, Miss Graham?"

"She looks over to my lap."

mb "I see. Needlework is a new pursuit for you, I take?"

l sad "I-I’m afraid so. I’ve fixed ripped clothes in the past, but that’s the extent of my sewing ability."

"Miss B puts her hand on my shoulder."

show mbsmileclosed with fade
hide mbthoughtful

mb "That is all right. Please do not fret over it. I’m certain that in the time you spend in my institution, you will see much improvement."

l normal "T-thank you." 

hide mbsmileclosed
with fade

"She smiles warmly before moving on to look at the other students’ work." 

"Never at any school have I had an instructor be so sympathetic of learning difficulties. I look down at my work with a smile of my own, despite the fresh bead of blood on the tip of my pointer finger." 

"Perhaps I can learn to like this place."

stop music fadeout 1.0

jump choice3meredith

label choice3meredith:
    play music "school.ogg" fadeout 1.0
    scene bg dinday with fade

    "I haven’t had a cup of tea since arriving, which is an absolute shame."
    
"The Old Continent may as well have had rivers of the drink. It is the lifeblood of the place; their preferred elixir to dull the sharpened edges of their society."

"The day I finally go to make myself a cup, I find Meredith with the kettle. Her entire face brightens the moment she sees me." 

show mersmile
with fade

m "Good afternoon, Lillian!"

"She glances down at my cup."

m "You are here for tea as well?"

l normal "I am! In fact, I have not yet had tea since arriving."

"She reaches out a hand towards my cup."

show mersmileclosed
with fade
hide mersmile

m "In that case, I will brew some for you! I have been told that I make an excellent milk tea."

hide mersmileclosed
with fade

"I sit at the table as Meredith goes to work."

"After pouring water over the tea and strainer, she adds a splash of milk and drops in a sugar cube, stirring all the while."

"She takes expert care throughout the process, as though she were handling something as delicate as cobweb. She brings it over to me with a saucer and plate of scones."

show mersmileclosed 
with fade

m "Here you are! Your very first cup of tea in the Old Continent. I hope it is to your taste."

"I take it gratefully and sip. It is warm and mild, the sugar only an aftertaste once I swallow. I give her my brightest smile."

l amused "It's {i}delicious!{/i}"

show merblush
with fade
hide mersmileclosed

m "Oh, I’m so pleased to hear that!"

"The full color returns to her cheeks for a fleeting moment. Then, she sits beside me with her own tea."

show mersmile
with fade
hide merblush

"Despite the rich cup she’d brewed for me, hers is completely clear. She drinks it in short, brief sips as I reach for a scone."

"An idea occurs to me. Meredith is so kind… I wish to do something for her as well."

"I gesture to the plate of scones after taking my own."

l normal "Would you like me to prepare you one? I have a preferred way of eating them myself! A cream and marmalade blend."

"Meredith looks intrigued for a moment, but then she pauses."

show merconcerned 
with fade
hide mersmile

m "That sounds lovely, but..." 

"She scratches her cheek."

m "Well, it’s not that I don’t like scones, per se. I’m just no longer able to comfortably enjoy them, as I used to."

l curious "Oh."

show mersmile
with fade
hide merconcerned

m "But thank you for the offer, that is awfully sweet of you."

"I think to ask Meredith what she means, but she moves on to another subject quickly."

m "But enough about me. I wish to hear about your time in the New Continent!"

m "What is your favorite meal from there? Or site that you visited? O-oh, but I don’t want to interrupt your scone eating! I could tell you about my experiences while you eat—"

l amused "Oh no, it’s all right! I’ll tell you, let me just finish this last piece."

"I pop it into my mouth, brush the crumbs from my hands, and begin to tell her about any experience that comes to mind from my country estate."

"I talk about the wheat fields that turned verdant to brown with the seasons. The mules that we rented out for carriages and field work on a daily basis." 

"The dogs that I had to hold back from jumping on the milkmaid, and the suppers of chargrilled corn, roasted apples, and cider I had on my own every evening."

"Meredith is hanging onto every word. I’m unused to someone giving me their full attention like this, but it is a nice distraction from class and the evenings."

"It even made me a bit homesick, at least for the place. I cannot say I miss any of the people."

show mersmileclosed
with fade
hide mersmile

"Meredith smiles fondly."

m "It sounds divine. I’m certain my siblings would love to visit just as much as me!"

l normal "You have siblings?"

m "Two younger sisters and a younger brother, yes. I haven’t seen them in a long time. I miss them, but I’m certain they’re doing all right."

l normal "They sound sweet. I’m an only child, though I’ve always wanted siblings."

m "They were a delight. Even if my parents had trouble keeping them in line sometimes!"

show mersmile
with fade
hide mersmileclosed

"Meredith looks at me with newfound interest."

m "Lillian, what would you say has been your favorite part of the Old Continent? I know you’ve only been here for a bit of time, but surely you’ve formed some opinions by now."

"I hum in thought. If I must choose..." 

menu:
    "The places":
        jump choicem2_incorrect
    "The people":
        jump choicem2_correct
        
label choicem2_incorrect:

l normal "The scenery on the trip here was certainly something. Those rolling hills and wide moors are unlike anything I’ve seen in the New Continent!"

"Meredith nods."

hide mersmile
show mersmileclosed

m "I do agree, the sights are quite spectacular!"

m "Occasionally, Miss B takes us out on excursions to view them. It helps us maintain a semblance of normalcy, I suppose. The other students seem to appreciate it, as least."

l amused "Y-yeah, I’m certain they would."

"It is only a slight exaggeration.  I have no interest in seeing those hills ever again, if I can help it."

jump choicem2_done

label choicem2_correct: 

l blushsmile "Honestly, I have enjoyed the company of the people. Miss B has been helpful, and, well…especially you, Meredith!" 

l blushsmile "You have just been so kind to me, I cannot help but pick you out as something I love about the Old Continent!"

show merblush
with fade
hide mersmile

"Meredith’s fingers nearly knock her teacup over. She glances up at me in surprise and then smiles."

m "O-oh! Thank you! I suppose I do know what it’s like to feel alone after being struck with some kind of unfortunate incident. I try my best to make certain my fellow students and newcomers do not feel alone as I did."

show mersmileclosed with fade
hide merblush

"She scratches her cheek again. It is something of a nervous habit with her, but I find it to be endearing."

jump choicem2_done

label choicem2_done:

show mersmile
with fade
hide mersmileclosed

m "Either way, I’m glad you are beginning to feel more comfortable here! Students adapt at different speeds, but you seem to be settling."

l curious "Admittedly, I know little about the other students our age. What are they like?"

show mersmileclosed
with fade
hide mersmile

"Meredith smiles warmly."

m "Well, the first to come to mind is sweet Winnie. That girl’s heart is full of tenderness. She has such a wonderful smile, but she doesn’t like to show it. I do wish she would more often."

show mermelancholy
with fade
hide mersmileclosed

"She sighs."

m "I fear that Virginia is ashamed of herself. But she doesn’t like intimacy, so it’s difficult to help her with her feelings."

m "Not least to mention she doesn’t think I’m… {i}qualified{/i} to offer her advice. I believe it would take a very special sort of person to crumble the walls she keeps around herself."

m "As for Greta…" 

show mersmile
with fade
hide mermelancholy

"Her lips twist sideways before she smiles." 

m "She is a peculiar sort of girl. There’s a lot about her that I do not understand. She seems to enjoy mischief, for mischief’s sake. Miss B does not protest, though."

l curious "So you’ve been here as long as they have?"

show mersmileclosed
with fade

m "Longer, in fact. I was one of Miss B’s first students!" 

l surprised "Oh! I had no idea."

m "This school was a blessing to me. In fact, after I-"

show mersmile
with fade
hide mersmileclosed with fade 

"Meredith stops herself. She focuses on a small group of students in the hall."

m "Oh, class time again. Perhaps I can tell you more another day? If you are interested, of course."

l normal "I would love to hear, yes!"

m "Then we must do this again!"

"Meredith gathers up our cups and empties the kettle. She hurries over in time to hold open the dining room door for me."

l amused "Ah, thank you!"

"Meredith dips her head. Somehow, her smile appears even wider than before."

show mersmileclosed with fade
hide mersmile

m "Of course! I very much look forward to the next time we speak!"

hide mersmileclosed with fade

"They are usual parting words, but strange and pleasant warmth blooms in my chest as she speaks them."

"Because I know that when said by Meredith, they are sincere."

jump choiceend_done

label choice2virginia_done: 
stop music fadeout 1.0
play music "calm.mp3" fadein 2.0

scene bg classroom with fade
    
"Returning to class, I find myself immersed in a rather uncomfortable activity." 

l surprised "Ouch!"

"I press my punctured thumb to my lips."

show mbsurprised
with fade

mb "Are you all right, Miss Graham?"

l curious "Y-yes, I’m fine..." 

show mbinviting 
with fade
hide mbsurprised

"Miss B returns to addressing the class."

mb "Upkeep of the ability to hand stitch is essential for any woman entering society. Luckily, none of you have ailments that should significantly impair this ability." 

hide mbinviting with fade

"I stare dubiously at the lopsided needlework on my lap. Even with some rest, leftover sleepiness and clumsy fingers were doing me no good." 

show mersmile with fade

m "It’s all right, try keeping your fingertips a bit more spread out. Like this."

hide mersmile with fade

"Meredith reaches over to gently guide my fingers with her own. She smiles apologetically when I flinch from the cold."

show vpout at right with fade

v "Is it really all that surprising Miss Graham is the one to struggle with this? Needlework requires delicate hands, not those calloused from a countryside life."

show mbthoughtful with fade

mb "Miss Belvoir, please try to be tolerant. She just joined us, of course she will need an adjustment period."

hide vpout at right with fade

hide mbthoughtful with fade

show wneutral
with fade

"Virginia sighs and returns to her needlework. Beside her, Winnie is looking at me, but quickly busies herself with the fabric on her lap when she catches my gaze."

hide wneutral
with fade

show gsmile at left 
with fade

g "Aaand done!"

show mbsurprised with fade

mb "Already, Miss Faye?"

show gsmileclosed at left
with fade
hide gsmile at left

"Greta holds up her fabric scrap for the class proudly. It is… certainly a colorful work. I can’t quite tell if the green and red spotted pattern is a bush of roses, an unusual dress design, or perhaps plumage of a rare breed of bird." 

show mbinviting 
with fade
hide mbsurprised

mb "It certainly has a lot of character. Although you may want to work on cleaning up the edges, they are fraying."

show gsmile at left
with fade
hide gsmileclosed at left

g "All right!"

hide gsmile at left with fade

"Greta returns to her needle and thread with impressive ferocity."

mb "How is everyone else?"

hide mbinviting with fade

show vthinking at right
with fade 

v "I will be done in ten minutes."

show wneutral at center
with fade

w "I…I’m taking a bit longer than usual. I’m sorry."

show mersmile at left
with fade

m "Don’t worry, Winnie! I can help you, if you’d like."

hide wneutral
with fade

hide vthinking
with fade

hide mersmile
with fade

"I am also behind, and with little to show for it. I hurriedly return to it, biting my lip when I jab myself once more."

"Miss B comes up behind me."

show mbthoughtful
with fade

mb "And you, Miss Graham?"

"She looks over to my lap."

mb "I see. Needlework is a new pursuit for you, I take?"

l sad "I-I’m afraid so. I’ve fixed ripped clothes in the past, but that’s the extent of my sewing ability."

"Miss B puts her hand on my shoulder."

show mbsmileclosed with fade
hide mbthoughtful

mb "That is all right. Please do not fret over it. I’m certain in the time you spend in my institution, you will see much improvement."

l normal "T-thank you." 

hide mbsmileclosed
with fade

"She smiles warmly before moving on to look at the other students’ work."

"Never at any school have I had an instructor be so sympathetic of learning difficulties. I look down at my work with a smile of my own, despite the fresh bead of blood on the tip of my pointer finger." 

"Perhaps I can learn to like this place."

stop music fadeout 1.0

jump choice3virginia

label choice3virginia:
    play music "school.ogg" fadein 2.0 
    
    scene bg libday with fade
    
    "I am not certain whether to be intrigued or abashed about the person I see inside the library today."
    
"For the first time since the day I arrived here, Winnie is nowhere to be seen. But in her usual spot, Virginia is crouched over a thick book, flipping pages and pouring over the contents with impressive voracity."

l surprised "Virginia?"

show vpout
with fade

"She startles, and just for a moment her eyes are full of genuine surprise. But she covers it up with a guarded stare in an instant."

v "I would prefer if you called me Miss Belvoir."

l normal "Whatever you say, Miss Bel."

"Virginia does not seem amused. She purses her lips, but says nothing further."

"I stand beside the table."

l curious "What are you reading?"

show vthinking
with fade
hide vpout

v "Nothing of importance."

"She tucks the book away before I could ask further."

show vpout 
with fade
hide vthinking

v "And why are you here at this moment? To see that unfortunate Winnifred girl?"

l normal "No, I like to come here to peruse the books. I find it peaceful."

"It usually is. Not so much with Virginia here."

v "Oh. I see."

hide vpout with fade

"At least she does not have the audacity to demand I leave the library." 

"After picking out a book, I take a seat a good distance from her and open it. I catch her peering at the title."

show vneutral with fade

v "That is not an etiquette book."

l normal "No, it’s not! I am studying spell and curse books, to see what might be the source of my nightmare affliction."

show vthinking with fade
with fade
hide vneutral

v "A mild issue. Hardly worth attendance in this school, if one were to ask me."

l curious "Is your affliction so drastic it does warrant attendance?"

"Virginia stiffens. She pushes the book she was reading further into her bag." 

show vpout with fade
hide vthinking

v "Mine is going to be cured soon. And then I will be rid of my time at this school and all of its desperate pupils, and enter back into society once more."

"Confidence peels off her statement. I ought not to pry, but Virginia is such a mystery, I cannot help myself." 

menu:
    "'What is it that needs curing?'":
        jump choicev2_incorrect
    
    "'What will you do then?'":
        jump choicev2_correct
        
label choicev2_incorrect:

l curious "What is it that needs curing? Perhaps I could assist—"

show vangry with fade
hide vpout

v "You cannot. And do not ask me about it again."

"Her answer is curt and leaves no room for protest."

jump choicev2_done

label choicev2_correct:

l curious "What will you do then? After being cured, I mean."

show vsmile with fade
hide vpout

"Virginia looks at me oddly, and then actually smiles."

v "What ladies my age ought to be doing. I will return to the gatherings and find myself a handsome suitor. Marry wealthy, and bear children to carry on the Belvoir title."

v "I will live the life of an affluent woman and it will be as though none of this magical business ever happened."

"She sounds wistful at the idea. Then, her gaze hardens." 

show vpout with fade
hide vsmile

v "That path will be much harder for everyone else here, so I hardly expect the same for others. As well as for you. The likes of you would not fare well at all in this continent."

l normal "It’s good I have no intentions of staying longer than I must, then!"

jump choicev2_done

label choicev2_done: 

hide vpout with fade
hide vangry with fade

"I return to reading my book, assuming Virginia is finished talking with me for now."

show vneutral with fade

v "I wonder why Miss B selected you of all people."

"She is not."

show vthinking
with fade
hide vneutral

v "You are hardly special. I am certain there are many girls with magical troubles in the New Continent. Why would she choose you?"

l curious "Perhaps it was luck?"

"Virginia scoffs."

v "Hmph. Luck. The crumbs that street children eat."

"She is so offended by the idea, I cannot help but laugh." 

show vpout 
with fade
hide vthinking

v "What is so funny?"

l amused "Oh, it’s just…you are the only lady here who is as unpleasant as I anticipated when coming to this school. It’s refreshing to have my expectations met, for once." 

v "{i}Refreshing{/i}?"

"As I look back my book, I can feel her eyes on me. After a moment, she shakes her head, as if rousing herself from a stupor."

show vneutral with fade
hide vpout

v "You are a very {i}peculiar{/i} girl, Lillian."

hide vneutral with fade

"She plucks her bag off the table and leaves the library."

"It is the first time she had said my name, and it had not been spoken out of spite, either."

"It is hardly safe on her tongue…"

"But it is nice to hear, regardless."

jump choiceend_done

label choice2greta_done: 
stop music fadeout 1.0
play music "calm.mp3" fadein 2.0

scene bg classroom with fade
    
"Returning to class, I find myself immersed in a rather uncomfortable activity." 

l surprised "Ouch!"

"I press my punctured thumb to my lips."

show mbsurprised
with fade

mb "Are you all right, Miss Graham?"

l curious "Y-yes, I’m fine..." 

show mbinviting 
with fade
hide mbsurprised

"Miss B returns to addressing the class."

mb "Upkeep of the ability to hand stitch is essential for any woman entering society. Luckily, none of you have ailments that should significantly impair this ability." 

hide mbinviting with fade

"I stare dubiously at the lopsided needlework on my lap. Even with some rest, leftover sleepiness and clumsy fingers were doing me no good."

show mersmile with fade

m "It’s all right, try keeping your fingertips a bit more spread out. Like this."

hide mersmile with fade

"Meredith reaches over to gently guide my fingers with her own. She smiles apologetically when I flinch from the cold."

show vpout at right with fade

v "Is it really all that surprising Miss Graham is the one to struggle with this? Needlework requires delicate hands, not those calloused from a countryside life."

show mbthoughtful with fade

mb "Miss Belvoir, please try to be tolerant. She just joined us, of course she will need an adjustment period."

hide vpout at right with fade

hide mbthoughtful with fade

show wneutral
with fade

"Virginia sighs and returns to her needlework. Beside her, Winnie is looking at me, but quickly busies herself with the fabric on her lap when she catches my gaze."

hide wneutral
with fade

show gsmile at left 
with fade

g "Aaand done!"

show mbsurprised with fade

mb "Already, Miss Faye?"

show gsmileclosed at left
with fade
hide gsmile at left

"Greta holds up her fabric scrap for the class proudly. It is… certainly a colorful work. I can’t quite tell if the green and red spotted pattern is a bush of roses, an unusual dress design, or perhaps plumage of a rare breed of bird." 

show mbinviting 
with fade
hide mbsurprised

mb "It certainly has a lot of character. Although you may want to work on cleaning up the edges, they are fraying."

show gsmile at left
with fade
hide gsmileclosed at left

g "All right!"

hide gsmile at left with fade

"Greta returns to her needle and thread with impressive ferocity."

mb "How is everyone else?"

hide mbinviting with fade

show vthinking at right
with fade 

v "I will be done in ten minutes."

show wneutral at center
with fade

w "I…I’m taking a bit longer than usual. I’m sorry."

show mersmile at left
with fade

m "Don’t worry, Winnie! I can help you, if you’d like."

hide wneutral
with fade

hide vthinking
with fade

hide mersmile
with fade

"I am also behind, and with little to show for it. I hurriedly return to it, biting my lip when I jab myself once more."

"Miss B comes up behind me."

show mbthoughtful
with fade

mb "And you, Miss Graham?"

"She looks over to my lap."

mb "I see. Needlework is a new pursuit for you, I take?"

l sad "I-I’m afraid so. I’ve fixed ripped clothes in the past, but that’s the extent of my sewing ability."

"Miss B puts her hand on my shoulder."

show mbsmileclosed with fade
hide mbthoughtful

mb "That is all right. Please do not fret over it. I’m certain in the time you spend in my institution, you will see much improvement."

l normal "T-thank you." 

hide mbsmileclosed
with fade

"She smiles warmly before moving on to look at the other students’ work."

"Never at any school have I had an instructor be so sympathetic of learning difficulties. I look down at my work with a smile of my own, despite the fresh bead of blood on the tip of my pointer finger." 

"Perhaps I can learn to like this place."

stop music fadeout 1.0

jump choice3greta 

label choice3greta:
play music "school.ogg" fadein 2.0 
scene bg mansioninterior with fade
    
"Throughout my first few days at this school, I have found that the entrance and hallways are often empty."

"I attest it to the lack of student body here: we could not have be more than 15 girls, if that. Younger students share bedrooms on the upper floor, whilst the older are in my hall."

"I’m on the upper floor now, retrieving an envelope of additional rosemary Miss B had set out for me at my request. Some of the leaves are browning, and I wanted extra to take additional caution." 

show mbinviting
with fade

"Miss B herself is at the top of the stairwell."

l normal "Good afternoon, Miss B! Thank you for the rosemary."

show mbsmileclosed
with fade
hide mbinviting

"She smiles warmly at me."

mb "Good afternoon, Miss Graham. Of course. How have your nights been?"

l normal "Much better. The rosemary has really been helping. I have had no nightmares since arriving!"

mb "That’s wonderful to hear. If you need anything, please do not hesitate to ask."

hide mbsmileclosed
with fade

"I nod to her as she enters her study/ As I prepare to go down the stairs to my room, when I hear a sound."

g "Psst!"

"I stop walking and glance around."

g "{i}Psst!{/i} Lillian!"

"I can hear Greta, but I cannot see Greta."

"Before I can question her, something grabs my arm and pulls me behind a column."

l surprised "G-Greta, what—?"

show gsmile at left with fade

g "Shh, keep quiet!"

"Greta nods to the door Miss B vanished into."

show gwink at left with fade
hide gsmile at left 

g "We mustn’t let her know I’m here."

l curious "Why? I thought-"

"She covers my mouth with her hand."

show gsmile at left with fade
hide gwink at left 

g "Shh! Don’t ruin the surprise."

"The moments of silence between us are fleeting before a startled gasp and loud thud follows. It appears to come from Miss B’s study."

show gsmileclosed at left with fade
hide gsmile at left

g "There it is."

"Moments later, a very small, very perturbed-looking weasel scampers down the hall, followed by the desperate calls of Miss B."

"Greta lets me go and steps out in front of her."

hide gsmileclosed at left with fade

show gsmileclosed with fade

g "Miss B here expressed interest in having a school pet. I thought to lend her a bit of assistance!"

show mbthoughtful at right with fade

"Miss B immediately straightens her posture."

mb "So you were responsible for this, Miss Faye?"

"I stiffen and cast Greta a nervous glance. But she remains completely at ease, giving a lackadaisical smile."

show gsmile with fade
hide gsmileclosed

g "Indeed! Do you like your new companion?"

"Miss B stares at her, and then casts a glance to me as well. My throat feels completely dry."

mb "Do you have something to do with this, Miss Graham?"

show gsmileclosed with fade
hide gwink with fade

g "Of course she does! She is my partner in jests!"

"I shoot Greta a look, but she is just smiling broadly at me."

menu:
    "'I have nothing to do with this.'":
        jump choiceg2_incorrect
        $ g2 = deny
    "'Remain quiet.'":
        jump choiceg2_correct
        $ g2 = quiet
label choiceg2_incorrect:

l curious "No, Miss B. Greta is responsible."

show gpout with fade
hide gsmileclosed

"Greta pouts at me. I give her an apologetic look."

jump choiceg2_done1

label choiceg2_correct:

    show gwink with fade
    hide gsmileclosed with fade
  
"I say not a word. I attribute it to my words being stuck, but the way Greta beams and winks at me tells me it means a lot more."

jump choiceg2_done2

label choiceg2_done1: 

mb "I see."

mb "As for you, Miss Faye."

show mbsmileclosed at right with fade
hide mbthoughtful

mb "It’s a kind gesture, but I’m afraid I’m much more partial to cats. Please consider a feline friend next time, all right?"

"Her smile is as warm as when I first met her."

show gsmile with fade
hide gpout with fade

g "Noted!"

l surprised "W-what of the weasel?"

"I cast an uncertain glance down the hall and stairwell. The creature is nowhere to be seen."

mb "Oh, do not worry about it. I’m certain it will turn up."

"It feels as if I am missing out on some sort of shared joke."

show mbinviting at right with fade
hide mbsmileclosed at right

mb "I will see you two in class."

hide mbinviting at right with fade
hide mbthoughtful at right

"She walks away without any further word."

g "Miss B is a splendid teacher, isn’t she?"

l curious "I suppose so."

show gpout with fade
hide gsmile

g "You could have played along, you know!"

l curious "But I was only speaking the truth."

show gthought with fade
hide gpout with fade

g "I suppose." 

"She sighs dramatically."

jump g2_finish

label choiceg2_done2: 
mb "I see."

mb "As for you, Miss Faye."

show mbsmileclosed at right with fade
hide mbthoughtful

mb "It’s a kind gesture, but I’m afraid I’m much more partial to cats. Please consider a feline friend next time, all right?"

"Her smile is as warm as when I first met her."

hide gwink with fade
show gsmile with fade

g "Noted!"

l surprised "W-what of the weasel?" 

"I cast an uncertain glance down the hall and stairwell. The creature is nowhere to be seen."

mb "Oh, do not worry about it. I’m certain it will turn up."

"It feels as if I am missing out on some sort of shared joke."

show mbinviting at right with fade
hide mbsmileclosed at right

mb "I will see you two in class."

hide mbinviting at right with fade
hide mbthoughtful at right

"She walks away without any further word."

g "Miss B is a splendid teacher, isn’t she?"

l curious "I suppose so."

show gwink with fade
hide gsmile 

"Greta winks."

g "Thank you for keeping quiet. It was not needed in the end, but I appreciate the assistance! We'll make a jester of you, yet!"

jump g2_finish

label g2_finish:

l curious "May I ask something?"

show gsmileclosed
with fade

g "Go ahead, no need for permission!"

l curious "Why do you play these tricks, Greta?"

show gthought with fade
hide gsmileclosed with fade

"Greta’s eyebrows crease."

g "Do you not find them amusing?"

l curious "N-no, I do. At least, I think they can be amusing, sometimes."

"Especially when they involve one Virginia Belvoir."

l curious "But do you not get in trouble for them?"

g "Not usually. Miss B says it’s all right for me to express myself in these halls!"

l "Regardless, they appear to be your favorite passtime."

show gsmile with fade
hide gthought

"Greta’s smile returns as she nods."

g "Yes, they are!"

"I am going nowhere quickly with this girl. She does not give me chance to question her further."

show gwink
with fade
hide gsmile

g "Alas, I ought to move along to my other duties. But I’m certain we will meet again, dearest Lillian."

hide gwink
with fade

"Once more, Greta is off and out of my sight. I sigh."

"It is hard to say if I enjoy her…peculiar presence. And I still have no idea why she would be at a place like this."

"Yet, as I head down the stairwell, I cannot help but hope that I might see her again soon." 

jump choiceend_done

label choiceend_done:
stop music fadeout 1.0
play music "calm.mp3" fadein 2.0
show bg bedroomnight
with dissolve 

"When I retire to my room for the evening, I feel content."

"Finally, I am beginning to settle in to my new route here."

"My nights are free from bad dreams. Miss B is kind. The students are relatively interesting; at least, they seem willing to interact with me despite my newness."

"This is also the first evening in which I take my time preparing for bed, feeling well rested for the first time in many, many weeks."

"I do not bother with my ritual. I feel as if nothing can shake me now."

"I am wrong."

stop music fadeout 1.0 
play music "nightmare.ogg" fadein 1.0 

"When I put on my nightgown, I feel the slightest chill brush my arm."

"Confused, I glance to the window, but it is shut. Furthermore, I have not opened the window once since arriving here."

"The door to my bedroom is also closed."

"But then another chill runs through me. And another, even as I pull back my sheets, like the press of cold iron. Something is in the room with me, I am certain of it—"

l nightsad "L-leave me alone!"

"The rosemary above me swings a bit, and then the chills stop. I lie awake, waiting to see if any more would show, but they have faded. Whatever was here seems to have left."

"Or, perhaps not left. I still feel the faint presence of {i}something{/i}, somewhere nearby the foot of my bed. But it can no longer come close to me."

"I will sleep easy this night. Even with the herbs above my head protecting me… the awful knowledge that something is still haunting me keeps my nerves tender." 

"And I know that no matter how far from my home I travel, or who I meet, or what I use to protect myself..."

"It has no intentions of letting me go."

scene bg black with fade
stop music fadeout 1.0

hide window



label credits:
    $ credits_speed = 11 #scrolling speed in seconds
    scene bg credits
    with dissolve
    stop voice
    stop sound
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    show cred at Move((0.5, 3.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide thanks
    
    "You've reached the end of the demo. If you enjoyed it, please consider supporting Miss B's School in the October kickstarter. Thank you so much for playing!"
    
    return
    
    # This ends the game.
