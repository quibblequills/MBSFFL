################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language


style input:
    properties gui.text_properties("input", accent=True)

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png")
    bottom_bar Frame("gui/bar/bottom.png")

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    ymaximum 413
    base_bar Frame("gui/bar/top.png")
    thumb Frame("gui/bar/bottom.png", xmaximum=29, xalign=0.4)
    xpos -100
    ypos 75

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
        add SideImage() xpos -16 ypos 0
        
    use quick_menu2

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("textbox2.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("namebox2.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
    
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.57

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    



## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.dialogue_xpos
            xanchor gui.dialogue_xalign
            ypos gui.dialogue_ypos
            xsize gui.dialogue_width

            text prompt style "input_prompt"
            input id "input"


style input_prompt is say_dialogue

style input_prompt:
    properties gui.text_properties("input_prompt")
    xmaximum gui.dialogue_width

style input:
    xmaximum gui.dialogue_width

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 300
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign gui.choice_button_text_yalign


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu2():


    ## Ensure this appears on top of other screens.
    zorder 100
    
    imagemap:

            ground "gui/quick-menu-inactive.png" 
            hover "gui/quick-menu-active.png"
            selected_idle "gui/quick-menu-active.png"


            hotspot (1174, 556, 67, 11) action Rollback()
            hotspot (1155, 574, 83, 11) action ShowMenu('history')
            hotspot (1174, 592, 64, 11) action Skip() 
            hotspot (1174, 611, 64, 11) action ShowMenu('save')
            hotspot (1174, 628, 64, 11) action ShowMenu('load')
            hotspot (1174, 646, 64, 11) action Preference("auto-forward", "toggle")
            hotspot (1117, 664, 123, 11) action ShowMenu('preferences')



################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    
    imagemap:

            ground "gui/navigation-inactive.png" 
            hover "gui/navigation-active.png"
            selected_idle "gui/navigation-active.png"


            hotspot (158, 680, 51, 20) action ShowMenu('save')
            hotspot (267, 680, 57, 20) action ShowMenu('load')
            hotspot (377, 680, 139, 20) action ShowMenu('preferences')
            hotspot (567, 680, 76, 20) action ShowMenu('about')
            hotspot (693, 680, 59, 20) action ShowMenu('help')
            hotspot (802, 680, 59, 20) action Quit(confirm=not main_menu)
            hotspot (911, 680, 82, 20) action Return()
            hotspot (1045, 680, 95, 20) action ShowMenu('history')
            
            hotspot (1180, 45, 53, 53) action Return()


style game_menu_navigation_frame:
    xsize 0
    
style game_menu_viewport:
    xsize 0



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    
init python:
    config.quit_action = Quit()


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        ground "gui/main-menu-inactive.png"
        idle "gui/main-menu-inactive.png"
        hover "gui/main-menu-active.png"

        hotspot (374, 580, 57, 22) action Start() 
        hotspot (475, 580, 57, 22) action ShowMenu("load")
        hotspot (575, 580, 126, 22) action ShowMenu("preferences")  
        hotspot (743, 580, 67, 22) action ShowMenu("about") 
        hotspot (857, 580, 53, 22) action ShowMenu("help")  

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill False

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill False

                        transclude

                else:

                    transclude

    use navigation


    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120


style game_menu_navigation_frame:
    xsize 0
    yfill False

style game_menu_content_frame:
    left_margin 0
    right_margin 0
    top_margin 0

style game_menu_viewport:
    xsize 0

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu
    use game_menu(_("")):
        pass    
        
    add "gui/save-menu-title.png"
    
    imagemap:
        ground "gui/saveload-boxes-idle.png"
        hover "gui/saveload-boxes-hover.png"
        selected_idle "gui/saveload-boxes-hover.png"
          
        hotspot (137, 234, 315, 192) clicked FileSave(1):
            use load_save_slot(number=1)

        hotspot (495, 234, 315, 192) clicked FileSave(2):
            use load_save_slot(number=2)

        hotspot (851, 234, 315, 192) clicked FileSave(3):
            use load_save_slot(number=3)
            
        hotspot (136, 456, 315, 192) clicked FileSave(4):
            use load_save_slot(number=4)

        hotspot (494, 456, 315, 192) clicked FileSave(5):
            use load_save_slot(number=5)

        hotspot (851, 456, 315, 192) clicked FileSave(6):
            use load_save_slot(number=6)
            
        
        
        hotspot (273, 163, 38, 21) action FilePagePrevious()
        hotspot (977, 163, 38, 21) action FilePageNext()
            
            
        hotspot (358, 163, 65, 32) action FilePage(1)
        hotspot (463, 163, 65, 32) action FilePage(2)
        hotspot (566, 163, 65, 32) action FilePage(3)
        hotspot (671, 163, 65, 32) action FilePage(4)
        hotspot (777, 163, 65, 32) action FilePage(5)
        hotspot (883, 163, 65, 32) action FilePage(6)




            


screen load():

    tag menu

    use game_menu(_("")):
        pass
        
    
        
    if main_menu:
        add "images/bg-mm.png"
        use mmnavi
        
    add "gui/load-menu-title.png"
    


    imagemap:
        ground "gui/saveload-boxes-idle.png"
        hover "gui/saveload-boxes-hover.png"
        selected_idle "gui/saveload-boxes-hover.png"
          
        hotspot (137, 234, 315, 192) clicked FileLoad(1):
            use load_save_slot(number=1)

        hotspot (495, 234, 315, 192) clicked FileLoad(2):
            use load_save_slot(number=2)

        hotspot (851, 234, 315, 192) clicked FileLoad(3):
            use load_save_slot(number=3)
            
        hotspot (136, 456, 315, 192) clicked FileLoad(4):
            use load_save_slot(number=4)

        hotspot (494, 456, 315, 192) clicked FileLoad(5):
            use load_save_slot(number=5)

        hotspot (851, 456, 315, 192) clicked FileLoad(6):
            use load_save_slot(number=6)
            
        
        
        hotspot (273, 163, 38, 21) action FilePagePrevious()
        hotspot (977, 163, 38, 21) action FilePageNext()
            
            
        hotspot (358, 163, 65, 32) action FilePage(1)
        hotspot (463, 163, 65, 32) action FilePage(2)
        hotspot (566, 163, 65, 32) action FilePage(3)
        hotspot (671, 163, 65, 32) action FilePage(4)
        hotspot (777, 163, 65, 32) action FilePage(5)
        hotspot (883, 163, 65, 32) action FilePage(6)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()


            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    
screen load_save_slot:
    $ file_text = "% 2s. %s\n%s" % (
                        FileSlotName(number, 3),
                        FileTime(number, empty=_("Empty Slot")),
                        FileSaveName(number))


    add FileScreenshot(number) xpos 20 ypos 13
    
    text FileTime(number, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("")):
        style "slot_time_text" ypos 190 xpos 147

    text FileSaveName(number):
        style "slot_name_text"
    
init -2 python:
    config.thumbnail_width = 261
    config.thumbnail_height = 147


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    
    use game_menu(_("")):
        pass
        
        
    if main_menu:
        add "images/bg-mm.png"
        use mmnavi

    

        
        
    imagemap:
            ground "gui/preferences-inactive.png" 
            hover "gui/preferences-active.png"
            selected_idle "gui/preferences-active.png"
            # This is so that everything transparent is invisible to the cursor.
        
            #Mute everything
            hotspot (717, 408, 26, 16) action Preference("all mute", "enable")
            hotspot (757, 408, 25, 16) action Preference("all mute", "disable")
            
            #Rollback Side
            hotspot (1008, 408, 57, 16) action Preference("rollback side", "disable")
            hotspot (1076, 408, 29, 16) action Preference("rollback side", "left")
            hotspot (1119, 408, 43, 16) action Preference("rollback side", "right")
            
            #Display
            hotspot (273, 552, 57, 16) action Preference("display", "window")
            hotspot (345, 552, 80, 16) action Preference("display", "fullscreen")
            
            #Skip
            hotspot (559, 552, 55, 16) action Preference("skip", "all")
            hotspot (627, 552, 97, 16) action Preference("after choices", "skip")
            hotspot (738, 552, 85, 16) action Preference("transitions", "none")
            
                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap False

                vbox:

                    bar value Preference("text speed") xpos 851 ypos 285

                    bar value Preference("auto-forward time") xpos 133 ypos 380

                vbox:

                    if config.has_music:

                        hbox:
                            bar value Preference("music volume") xpos -164 ypos 285

                    if config.has_sound:

                        hbox:
                            bar value Preference("sound volume") xpos 192 ypos 235

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing



style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 299


style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 284
    

        
        
style game_menu_navigation_frame:
    xsize 0
    
style game_menu_viewport:
    xsize 0



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html



screen history():

    tag menu
    

    ## Avoid predicting this screen, as it can be very large.
    predict False



    use game_menu(_("")):
        pass
        
    vpgrid:

        cols 1
        yinitial 1.0

        scrollbars "vertical"
        mousewheel True
        draggable True

        side_ysize 500
        side_xsize 1400
        side_xpos 0
        side_ypos 133


        style_prefix "history"
        

        for h in _history_list:
            
    

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.") xpos -400 yminimum 500 ypos 80
    
                

    add "gui/history-menu-title.png"
style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height
    bottom_padding 300
    bottom_margin 300





style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    bottom_padding 190
    

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font gui.history_name_text_font
    size gui.history_name_text_size
    bottom_padding 40

    

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    size gui.history_text_size
    top_padding 30



style history_label:
    xfill True

style history_label_text:
    xalign 1.0


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("")):
        pass
        
    if main_menu:
        add "images/bg-mm.png"
        use mmnavi

    add "gui/help-title.png"
    
    imagemap:
            ground "gui/help-menu-idle.png" 
            hover "gui/help-menu-rollover.png"
            selected_idle "gui/help-menu-rollover.png"

            hotspot (486, 209, 171, 43) action SetScreenVariable("device", "keyboard")
            hotspot (684, 209, 113, 43) action SetScreenVariable("device", "mouse")
            
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
                
                
screen keyboard_help():
    add "gui/keyboard-help.png"
    
screen mouse_help():
    add "gui/mouse-help.png"




################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    
    add "gui/yesno-bg.png"

    zorder 200

    on "show" action With(dissolve)
    
    
    imagemap:
            ground 'gui/yesno-inactive.png'
            hover 'gui/yesno-active.png'
            alpha True
            # This is so that everything transparent is invisible to the cursor.
        
        
            hotspot (556, 406, 81, 36) action yes_action 
            hotspot (685, 406, 75, 36) action no_action 
            hotspot (1085, 211, 54, 54) action no_action
  

    if message == layout.ARE_YOU_SURE:
        add "gui/are-you-sure.png"
        
    elif message == layout.DELETE_SAVE:
        add "gui/delete-save.png"
        
    elif message == layout.OVERWRITE_SAVE:
        add "gui/overwrite-save.png"
        
    elif message == layout.LOADING:
        add "gui/load-game.png"
        
    elif message == layout.QUIT:
        add "gui/are-quit.png"
        
    elif message == layout.MAIN_MENU:
        add "gui/return.png"
        

init python:
    config.quit_action = Quit()





## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"


    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    
    tag menu
    


    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"
        
    if main_menu:
        add "images/bg-mm.png"
        use mmnavi
            
    add "gui/about-menu.png"


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Main Menu Navigation ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen mmnavi():
    
    imagemap:

            ground "gui/mm-menu-idle.png" 
            hover "gui/mm-menu-rollover.png"
            selected_idle "gui/mm-menu-rollover.png"


            hotspot (335, 680, 57, 20) action ShowMenu('load')
            hotspot (445, 680, 139, 20) action ShowMenu('preferences')
            hotspot (636, 680, 76, 20) action ShowMenu('about')
            hotspot (762, 680, 59, 20) action ShowMenu('help')
            hotspot (873, 680, 82, 20) action Return()
            
            hotspot (1180, 45, 53, 53) action Return()


