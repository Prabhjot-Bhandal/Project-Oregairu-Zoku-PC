init:
    #Set up audio channels.
    #default loop options are set up but use can be specified with
    #"loop" or "noloop" on playing audio in said channel
    $renpy.music.register_channel(name="footsteps", mixer="sfx", loop=False)
    $renpy.music.register_channel(name="ambient", mixer="sfx", loop=True)
    $renpy.music.set_volume(1,channel=u'footsteps')
    $renpy.music.set_volume(1,channel=u'ambient')
    define config.mouse = { 'default' : [ ('gui/cursor.png', 0, 49)] }

    #Possibly temporary.
    $harunoCafeFlag = False
    $yukino_menu = False
    $yui_menu = False
    $yumiko_menu = False
    $ebina_menu = False
    $haruno_menu = False
    $meguri_menu = False
    $hiratsuka_menu = False
    $iroha_menu = False
    $saki_menu = False
    $hayamaMarathonTalk = False
    $hayamaTalk = False
    $shrine_flag = ""
    $shrineMeetFlag = ""
    $komachiHelpFlag = ""
    $firstSchoolDayFlag = ""
    $totsukaTalkFlag = ""
    $chocoEventHelp = ""
    $chocoEventChoice = ""
    $cleaning_event = ""
    $ski_flag = ""
    $changeImagePara = [0, 0, 0, 0, 0]
    $url = ["none", "none"]
    $E3_SHI_03_Q_A = [False, False, False, False, False, False]
    $E3_SHI_03_result = 0
    python:

        import math
        import textwrap

        # calculating points
        # temporary
        def _calculate_points():
            # may be better to make it global
            points = {
                'saki' : 0,
                'yukino' : 0,
                'hiratsuka' : 0,
                'yui' : 0,
                'haruno' : 0,
                'meguri' : 0,
                'iroha' : 0
            }
            # using flags to count points
            flags = [
                shrineMeetFlag,
                komachiHelpFlag,
                firstSchoolDayFlag,
                totsukaTalkFlag,
                chocoEventHelp,
                chocoEventChoice,
                ski_flag
            ]
            for i in flags:
                if i == "saki":
                    points['saki'] += 1
                elif i == "yukino":
                    points['yukino'] += 1
                elif i == "hiratsuka":
                    points['hiratsuka'] += 1
                elif i == "yui":
                    points['yui'] += 1
                elif i == "haruno":
                    points['haruno'] += 1
                elif i == "meguri":
                    points['meguri'] += 1
                elif i == "iroha":
                    points['iroha'] += 1
                elif i == "haruno meguri":
                    points['haruno'] += 1
                    points['meguri'] += 1

            return points

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

        # # This is set to the name of the character that is speaking, or
        # # None if no character is currently speaking.
        # speaking = None

        # # This returns speaking if the character is speaking, and done if the
        # # character is not.
        # def while_speaking(name, speak_d, done_d, st, at):
        #     if renpy.music.is_playing('voice') and speaking == name:
        #         return speak_d, .1
        #     else:
        #         return done_d, None

        # # Curried form of the above.
        # curried_while_speaking = renpy.curry(while_speaking)

        # # Displays speaking when the named character is speaking, and done otherwise.
        # def WhileSpeaking(name, speaking_d, done_d=Null()):
        #     return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

        # # This callback maintains the speaking variable.
        # def speaker_callback(name, event, **kwargs):
        #     global speaking
        #     if event == "show":
        #         speaking = name
        #     elif event == "end":
        #         speaking = None

        # # Curried form of the same.
        # speaker = renpy.curry(speaker_callback)
