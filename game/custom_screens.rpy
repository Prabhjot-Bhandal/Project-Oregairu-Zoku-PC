style endingStyle is text:
    line_spacing 15
    text_align 0

style mail_text_sender is text:
    color gui.text_color
    font "DejaVuSans.ttf"
    size gui.name_text_size

style mail_text_subject is text:
    color gui.text_color
    font gui.text_font
    size gui.text_size

style mail_text_message is text:
    color gui.text_color
    font gui.text_font
    size gui.text_size

# cant implement the zoom when hovered


transform deal_card1:
    alpha 0
    easein 0.3 ycenter 0.4 alpha 1.0

transform deal_card2:
    alpha 0
    0.3
    easein 0.3 ycenter 0.4 alpha 1.0

transform deal_card3:
    alpha 0
    0.6
    easein 0.3 ycenter 0.4 alpha 1.0

screen two_minigame(word1, word2):
    fixed:
        imagebutton idle "images/minigame/card_unselected.png" at deal_card1:
            hover "images/minigame/card_selected.png"
            xcenter 0.255
            ycenter 0.255
            action Return(1)
        text word1 at deal_card1:
            size 50
            color "#000000"
            xcenter 0.255
            ycenter 0.255
    fixed:
        imagebutton idle "images/minigame/card_unselected.png" at deal_card2:
            hover "images/minigame/card_selected.png"
            xcenter 0.76
            ycenter 0.255
            action Return(2)
        text word2 at deal_card2:
            size 50
            color "#000000"
            xcenter 0.76
            ycenter 0.255

screen three_minigame(word1, word2, word3):
    fixed:
        imagebutton idle "images/minigame/card_unselected.png" at deal_card1:
            hover "images/minigame/card_selected.png"
            hover_sound gui.sound_click
            xcenter 0.255
            ycenter 0.255
            action Return(1)
        text word1 at deal_card1:
            size 50
            color "#000000"
            xcenter 0.255
            ycenter 0.255
    fixed:
        imagebutton idle "images/minigame/card_unselected.png" at deal_card2:
            hover "images/minigame/card_selected.png"
            hover_sound gui.sound_click
            xcenter 0.5
            ycenter 0.255
            action Return(2)
        text word2 at deal_card2:
            size 50
            color "#000000"
            xcenter 0.5
            ycenter 0.255
    fixed:
        imagebutton idle "images/minigame/card_unselected.png" at deal_card3:
            hover "images/minigame/card_selected.png"
            hover_sound gui.sound_click
            xcenter 0.76
            ycenter 0.255
            action Return(3)
        text word3 at deal_card3:
            size 50
            color "#000000"
            xcenter 0.76
            ycenter 0.255

screen three_minigame_all(list, ellipses):
    if len(list) > 2:
        $ word3 = list[renpy.random.randint(0, len(list)-1)]
        $list.remove(word3)
        $ word2 = list[renpy.random.randint(0, len(list)-1)]
        $list.remove(word2)


    if "..." in list:
        fixed:
            imagebutton idle "images/minigame/card_unselected.png" at deal_card1:
                hover "images/minigame/card_selected.png"
                hover_sound gui.sound_click
                xcenter 0.255
                ycenter 0.255
                action Return("...")
            text "..." at deal_card1:
                size 50
                color "#000000"
                xcenter 0.255
                ycenter 0.255
    else:
        fixed:
            if len(list) > 0:
                $ word1 = list[renpy.random.randint(0, len(list)-1)]
                $list.remove(word1)
            imagebutton idle "images/minigame/card_unselected.png" at deal_card1:
                hover "images/minigame/card_selected.png"
                hover_sound gui.sound_click
                xcenter 0.255
                ycenter 0.255
                action Return(word1)
            text word1 at deal_card1:
                size 50
                color "#000000"
                xcenter 0.255
                ycenter 0.255
    fixed:
        imagebutton idle "images/minigame/card_unselected.png" at deal_card2:
            hover "images/minigame/card_selected.png"
            hover_sound gui.sound_click
            xcenter 0.5
            ycenter 0.255
            action Return(word2)
        text word2 at deal_card2:
            size 50
            color "#000000"
            xcenter 0.5
            ycenter 0.255
    fixed:
        imagebutton idle "images/minigame/card_unselected.png" at deal_card3:
            hover "images/minigame/card_selected.png"
            hover_sound gui.sound_click
            xcenter 0.76
            ycenter 0.255
            action Return(word3)
        text word3 at deal_card3:
            size 50
            color "#000000"
            xcenter 0.76
            ycenter 0.255

#call the function using: the function in emailfunctionwrapper.rpy
#mail_function(partner, sender, subjectline, message)
#Let's give her a present and surprise her!

#Sometimes need to place a blank line afterwards like "" if there is no text
#between or else it will zoom through all the texts
#Temporary

#right now the mail locations are fixed, but can be modified to determine how far to move up as well.
#TO DO:
#Make the positions more dynamic based on length of message. Probably will require global variables.

    #We want to move the messages up based on the height of the newest message AND the previous message
        #Factors: Length of message, height of chat box, clearance from bottom of message to chat box
    #with each function call, we should store the location of that message to start old_message and oldest_message

transform moveup: #replace yoffset with moveup_distance when
    ease 0.5 yoffset -300

transform text_up: #replace yoffset with moveup_distance when
    ease 0.5 yoffset -1*(new_message_height)

screen mail_text(sender, subjectline, body, ydef):
    if (sender == "Hikigaya Hachiman") or (sender == "Hikki♥"):
        python:
            xpos = 230
    else:
        python:
            xpos = 1100

    python:
        ypos = ydef
        wrapped = "\n".join(textwrap.wrap(body, 24))
        yoffsetter = 126;

    fixed:
        add "images/texts/EmailHeader 556x126.png" at text_up:
            xoffset xpos
            yoffset ypos

        for i in range(len(textwrap.wrap(body, 24))):
            add "images/texts/EmailBody_line 556x50.png" at text_up:
                xoffset xpos
                yoffset (ypos + yoffsetter)
            python:
                yoffsetter = yoffsetter + 50

        add "images/texts/EmailBottom 556x46.png" at text_up:
            xoffset xpos
            yoffset (ypos + yoffsetter)

        text sender at text_up style "mail_text_sender":
            xoffset (xpos + 30)
            yoffset ypos + 10

        text subjectline at text_up style "mail_text_subject":
            xoffset (xpos + 30)
            yoffset ypos + 76

        text wrapped at text_up style "mail_text_message":
            xoffset (xpos + 30)
            yoffset ypos + 142

screen new_text(sender, subjectline, body):
    use mail_text(sender, subjectline, body, nm_bottom_loc)

screen old_text(sender, subjectline, body):
    use mail_text(sender, subjectline, body, second_m_loc)

screen older_text(sender, subjectline, body):
    use mail_text(sender, subjectline, body, third_m_loc)

screen oldest_text(sender, subjectline, body):
    use mail_text(sender, subjectline, body, fourth_m_loc)

screen end_card(route, end_type = ""):
    fixed:
        imagebutton idle "images/bg/endingcard.png" at truecenter:
            activate_sound gui.sound_start
            action [Hide("end_card", Dissolve(0.5)), Return(0)]
        if not end_type:
            text "{=endingStyle}{color=#6b92dd}" + route + " End\n{color=#000000}Cleared" at truecenter style "endingStyle":
                yoffset -100
                color "#6b92dd"
        else:
            text "{=endingStyle}{color=#6b92dd}" + route + " " + end_type + " End\n{color=#000000}Cleared" at truecenter style "endingStyle":
                yoffset -100
                color "#6b92dd"
