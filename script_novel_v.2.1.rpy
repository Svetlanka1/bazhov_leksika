# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define pn = Character('[pn]', color="#ff80ff")
define n = Character('Настасья', color="#bf40bf")
define t = Character('Танюшка', color="#ff9900")
define b = Character('Барин', color="#33ccff")
define ba = Character('Дед Слышко', color="#33ccff")
define hz = Character(cb_name=None) #слова автора


init:
    define znanie = 0
    define error = 0
    # для игры про хитника
    default man_clicked = False
    default wolf_clicked = False
    default vor_clicked = False
    default bear_clicked = False
    default game_active = True

    python:
        # Словарь для хранения состояния каждой морфемы (для игры про наушниц)
        word_parts = {
            "prefix": {
                "available": ["на", "за", "под", "до"],
                "selected": None,
                "checked": False,
                "pos": (0.2, 0.3),
                "label": "Приставка"
            },
            "root": {
                "available": ["нос", "сказ", "ябед", "уш"],
                "selected": None,
                "checked": False,
                "pos": (0.4, 0.3),
                "label": "Корень"
            },
            "suffix": {
                "available": ["к", "ниц", "тель"],
                "selected": None,
                "checked": False,
                "pos": (0.6, 0.3),
                "label": "Суффикс"
            },
            "ending": {
                "available": ["и", "ы", "а"],
                "selected": None,
                "checked": False,
                "pos": (0.8, 0.3),
                "label": "Окончание"
            }
        }

        correct_word = {
            "prefix": "на",
            "root": "уш",
            "suffix": "ниц",
            "ending": "ы"
        }

screen build_word_game():
    # Заголовок
    text "Собери слово по морфемам" ypos 0.05 xalign 0.5 size 80 color "#fff"

    # ОБЩАЯ КАРТИНКА-ОСНОВА
    add "images/word_frame.png":
        xalign 0.5
        ypos 0.17
        xysize (1400, 160)

    # Приставка - фиксированная область для текста
    frame:
        background None
        xpos 0.256
        ypos 0.236
        xanchor 0.5
        yanchor 0.5
        xysize (150, 60)  # фиксированный размер области

        if word_parts["prefix"]["selected"]:
            if word_parts["prefix"]["checked"]:
                $ text_color = "#2a6f2a"
            else:
                $ text_color = "#2a8f8f"

            text word_parts["prefix"]["selected"]:
                xalign 0.5
                yalign 0.5
                size 50
                color text_color
                bold True
        else:
            text "Приставка":
                xalign 0.5
                yalign 0.5
                size 25
                color "#888"

    # Корень
    frame:
        background None
        xpos 0.44
        ypos 0.236
        xanchor 0.5
        yanchor 0.5
        xysize (150, 60)

        if word_parts["root"]["selected"]:
            if word_parts["root"]["checked"]:
                $ text_color = "#2a6f2a"
            else:
                $ text_color = "#2a8f8f"

            text word_parts["root"]["selected"]:
                xalign 0.5
                yalign 0.5
                size 50
                color text_color
                bold True
        else:
            text "Корень":
                xalign 0.5
                yalign 0.5
                size 25
                color "#888"

    # Суффикс
    frame:
        background None
        xpos 0.595
        ypos 0.236
        xanchor 0.5
        yanchor 0.5
        xysize (150, 60)

        if word_parts["suffix"]["selected"]:
            if word_parts["suffix"]["checked"]:
                $ text_color = "#2a6f2a"
            else:
                $ text_color = "#2a8f8f"

            text word_parts["suffix"]["selected"]:
                xalign 0.5
                yalign 0.5
                size 50
                color text_color
                bold True
        else:
            text "Суффикс":
                xalign 0.5
                yalign 0.5
                size 25
                color "#888"

    # Окончание
    frame:
        background None
        xpos 0.73
        ypos 0.236
        xanchor 0.5
        yanchor 0.5
        xysize (150, 60)

        if word_parts["ending"]["selected"]:
            if word_parts["ending"]["checked"]:
                $ text_color = "#2a6f2a"
            else:
                $ text_color = "#2a8f8f"

            text word_parts["ending"]["selected"]:
                xalign 0.5
                yalign 0.5
                size 50
                color text_color
                bold True
        else:
            text "Окончание":
                xalign 0.5
                yalign 0.5
                size 25
                color "#888"

    # Горизонтальный ряд кнопок внизу
    frame:
        xalign 0.5
        ypos 0.4
        xsize 1600
        ysize 400
        background None

        hbox:
            xalign 0.5
            spacing 60

            # Приставки
            frame:
                xysize (350, 350)
                background Solid("#333")
                vbox:
                    text "Приставки:" color "#ffaa00" size 30 xalign 0.5
                    spacing 15
                    box_wrap True
                    for pref in word_parts["prefix"]["available"]:
                        button:
                            text pref size 35
                            xysize (300, 60)
                            background "#444"
                            hover_background "#555"
                            action Return(["prefix", pref])
                            sensitive (not word_parts["prefix"]["checked"])  # НЕЛЬЗЯ КЛИКАТЬ, ЕСЛИ УЖЕ ПРОВЕРЕНО И ПРАВИЛЬНО

            # Корни
            frame:
                xysize (350, 350)
                background Solid("#333")
                vbox:
                    text "Корни:" color "#ffaa00" size 30 xalign 0.5
                    spacing 15
                    for root in word_parts["root"]["available"]:
                        button:
                            text root size 35
                            xysize (300, 60)
                            background "#444"
                            hover_background "#555"
                            action Return(["root", root])
                            sensitive (not word_parts["root"]["checked"])

            # Суффиксы
            frame:
                xysize (350, 350)
                background Solid("#333")
                vbox:
                    text "Суффиксы:" color "#ffaa00" size 30 xalign 0.5
                    spacing 15
                    for suff in word_parts["suffix"]["available"]:
                        button:
                            text suff size 35
                            xysize (300, 60)
                            background "#444"
                            hover_background "#555"
                            action Return(["suffix", suff])
                            sensitive (not word_parts["suffix"]["checked"])

            # Окончания
            frame:
                xysize (350, 350)
                background Solid("#333")
                vbox:
                    text "Окончания:" color "#ffaa00" size 30 xalign 0.5
                    spacing 15
                    for end in word_parts["ending"]["available"]:
                        button:
                            text end size 35
                            xysize (300, 60)
                            background "#444"
                            hover_background "#555"
                            action Return(["ending", end])
                            sensitive (not word_parts["ending"]["checked"])

    # Кнопка проверки
    textbutton "ПРОВЕРИТЬ":
        xalign 0.5
        ypos 0.8
        xysize (360, 80)
        background "#2a6f2a"
        hover_background "#3a8f3a"
        text_size 50
        text_bold True
        action Return("check")

# Для игры про хитника - экран с кликабельными картинками
screen hitnik_choice():
    # Текст-задание внизу
    text "Выберите хитника," ypos 0.75 xalign 0.5 size 60 color "#fff"
    text "забравшегося к ним в дом." ypos 0.82 xalign 0.5 size 60 color "#fff"

    # Картинка мужчины
    imagebutton:
        idle ("images/man_1.png" if not man_clicked else "images/man_2.png")
        hover ("images/man_1.png" if not man_clicked else "images/man_2.png")
        hover_background Frame(Solid("#ff0000"), 10, 10)
        action Return("man")
        sensitive (not man_clicked)  # НЕ кликается, если уже выбрано
        xpos 0.127
        ypos 0.4
        anchor (0.5, 0.5)
        xysize (465, 615)

    # Картинка волка
    imagebutton:
        idle ("images/wolf_1.jpg" if not wolf_clicked else "images/wolf_2.png")
        hover ("images/wolf_1.jpg" if not wolf_clicked else "images/wolf_2.png")
        hover_background Frame(Solid("#ff0000"), 10, 10)
        action Return("wolf")
        sensitive (not wolf_clicked)
        xpos 0.373
        ypos 0.4
        anchor (0.5, 0.5)
        xysize (465, 615)

    # Картинка вора
    imagebutton:
        idle ("images/vor_1.png" if not vor_clicked else "images/vor_2.png")
        hover ("images/vor_1.png" if not vor_clicked else "images/vor_2.png")
        hover_background Frame(Solid("#ff0000"), 10, 10)
        action Return("vor")
        sensitive (not vor_clicked)
        xpos 0.620
        ypos 0.4
        anchor (0.5, 0.5)
        xysize (465, 615)

    # Картинка медведя
    imagebutton:
        idle ("images/bear_1.png" if not bear_clicked else "images/bear_2.jpg")
        hover ("images/bear_1.png" if not bear_clicked else "images/bear_2.jpg")
        hover_background Frame(Solid("#ff0000"), 10, 10)
        action Return("bear")
        sensitive (not bear_clicked)
        xpos 0.866
        ypos 0.4
        anchor (0.5, 0.5)
        xysize (465, 615)

"""
# Игра начинается здесь:
label start:

    scene bg black
    with fade

    menu:
        "В какой сказ отправитесь?"

        "Малахитовая шкатулка":
            jump skaz1

        "Каменный цветок (в работе)":
            pass

        "Синюшкин колодец (в работе)":
            pass
"""

label start:

    scene bg town
    with fade

    show bazhov
    with dissolve

    ba "Здравствуйте, гости дорогие."
    ba "За историей интересной поди пришли? Да ко мне все так приходят, чего уж."

    hide bazhov
    show bazhov_smile
    with dissolve

    ba "Много историй я слыхивал. От того и зовут меня дедом Слышко, хе."
    ba "Я занятно сказываю. Про девку-Азовку, про Полоза, про всякие земельные богатства..."
    ba "Есть у меня одна история и для вас: про малахитовую шкатулку."

    hide bazhov_smile
    show bazhov
    with dissolve

    ba "Для этого давайте в избу заглянем."

    scene bg izba
    with fade

    show nastya_smile
    with dissolve

    ba "Это Настасья — хозяйка добрая и порядочная."
    ba "Был у неё муж — Степаном звали. Да не стало его недавно..."
    ba "Сильный он был да рукастый. А ещё хорошим {b}горщиком{/b} считался."
    ba "Работал Степан в горах на износ."

    hide nastya_smile
    show nastya
    with dissolve

    ba "И недавно {b}в доски ушёл{/b}. Или по-простому: умер. Бедная Настасьюшка с таким горем..."
    ba "Но добра ей от Степана досталось немало — целая шкатулка с драгоценностями."
    ba "Хорошая семье {b}памятка{/b} осталась."
    ba "А они с дочкой к {b}экому-то{/b} богатству непривыкшие."
    ba "Да и {b}моду выводить{/b} Настасья не любительница."
    ba "Но что поделать. Память о муже."

    # + 1 задание на выбор слова - моду выводить

    scene bg black
    with fade

    show bazhov at right
    with dissolve

    ba "А? Поди не поняли, что Настасья не любила?"
    ba "Ну давайте разбираться!"

label choice_1:

    show bazhov at right
    with dissolve

    menu:
        "Значится, {b}моду выводить{/b} Настасья не любила. Это ж как понимать?"

        "Выгонять стиль":
            $ error += 1
            jump error1

        "Задавать тренды":
            $ error += 1
            jump error1

        "Модничать":
            $ znanie += 1
            pass

    hide bazhov
    show bazhov_smile at right
    with dissolve

    ba "Правду молвите! Всё верно."
    ba "{b}Моду выводить{/b}, значит, модничать."
    ba "По-другому можно сказать: наряжаться. Девицы любят это обычно, а вот Настасья наша не такая."
    ba "Ладно, отвлеклись. Давайте дальше расскажу."

    hide bazhov

    jump shkatulka

    return

label error1:

    hide bazhov
    show bazhov_sad at right
    with dissolve

    ba "Ох... Ошибаетесь, робята..."
    ba "Ну-ка, покумекайте ещё."

    hide bazhov_sad

    jump choice_1

    return


label shkatulka:

    scene bg izba
    with fade

    show nastya
    with dissolve

    ba "Так вот, носить она эти драгоценности по началу пыталась, да умаялась вся."
    ba "И решила убрать с глаз долой. Так скажем, {b}прихранить{/b}. То есть спрятать по-нашенски."
    ba "От домочадцев своих, да и чтоб чужие не зарились."

    hide nastya
    show nastya_smile
    with dissolve

    ba "Но пока не спрятала, подойдите посмотреть. Полюбуйтесь хоть."

    jump sunduk

    return

label sunduk:
    scene bg sunduk
    with fade

    ba "А вот и Степанова шкатулка с богатствами!"
    ba "Ой, а одно украшение пропало, кажись..."
    ba "Поможете найти?"
    jump ex_1

label ex_1:

    scene bg sunduk_1
    with fade

    hz "Все слова рассыпались как драгоценные камни..."
    hz "Посмотрите на текст вокруг пропавшего слова: какая часть речи нам нужна? Какого члена предложения не хватает?"

    scene bg sunduk_2
    with fade

    hz "А теперь обратите внимание на время глаголов в реплике. Глагол в каком времени нам точно НЕ подойдёт?"

    scene bg sunduk_3
    with fade

    hz "Посмотрите на оставшиеся глаголы: какой из них подходит для того, чтобы дать совет? Какой вопрос можно к нему задать?"

    scene bg sunduk_4
    with fade

    hz "Ежели верно на все вопросы ответили, то вот что получилось."
    hz "Мотнуть — это \"продать за бесценок\". Вот и говорили Настасье по дешёвке шкатулку не продавать."

    jump znakomstvo
    return


label znakomstvo:
    scene bg izba
    with fade

    show nastya_smile
    with dissolve

    ba "Так вот... Глаз на шкатулку эту не только чужие люди положили, но и родня."
    ba "Дочурка в особенности. Как не уйдёт Настасья из дому и накажет дочке {b}домовничать{/b} , так та дела сделает да с украшениями играется."

    scene bg black
    with fade

    show bazhov at right
    with dissolve

    ba "Вижу по вам — не знакомы ещё с этим словечком."
    ba "Скажите, так ли это? Хотя...{w} Чего языком молоть. Докажите-ка лучше!"
    ba "Расскажите, чем Настасья наказывала своей дочке заниматься?"

    jump choice_2

    return

label choice_2:

    show bazhov at right
    with dissolve

    menu:
        "Значится, {b}домовничать{/b} велела. Это как?"

        "Сидеть дома без дела":
            $ error += 1
            jump error2

        "Присматривать за домом":
            $ znanie += 1
            pass

        "Домового вызывать":
            $ error += 1
            jump error2

    hide bazhov
    show bazhov_smile at right
    with dissolve

    ba "Правду молвите! Всё верно."
    ba "{b}Домовничать{/b}, значит, оставаться для присмотра за домом."
    ba "Обычно ещё дела домашние делают, за хозяйством следят."
    ba "Ладно, отвлеклись. Давайте про юную хозяюшку-то вам и расскажу."

    hide bazhov

    jump shit

    return

label error2:

    hide bazhov
    show bazhov_sad at right
    with dissolve

    ba "Ох... Ошибаетесь, робята..."
    ba "Ну-ка, покумекайте ещё."

    hide bazhov_sad

    jump choice_2

    return

label shit:

    scene bg izba
    with fade

    show tanya
    with dissolve

    ba "Вот и Танюшка — доченька Настасьи и Степана."
    ba "Со своими холодна, а с чужими  тем более."
    ba "Чернявенькая, зеленоглазая и уж больно {b}басенька{/b}."
    ba "Помните, что Настасья шкатулку прячет обычно?"
    ba "Так вот, это всё потому, что приключилась с Танюшкой такая история, когда она одна дома осталась..."

    jump ex_2

label ex_2:

    scene bg black
    with fade

    show bazhov at right
    with dissolve

    ba "Раз к ней забрался {b}хитник{/b}... Ах, да, вы ж не знаете, кто это..."
    ba "Мудрёно звучит, а? Но боятся не стоит. Для начала поглядите-ка на слово хорошенько, найдите корень."

    jump ex_2_menu


label ex_2_menu:
    menu:
        "Как думаете, какое слово будет являться однокоренным для \"{b}хитника{/b}\"?"

        "Хихикать":
            jump no

        "Похитить":
            pass

    ba "Верно! В слове \"{b}хитник{/b}\" корень \"{b}хит{/b}\", как и в слове \"похитить\"."
    ba "А какие однокоренные слова вы ещё можете подобрать? Что интересное можно заметить?"
    ba "В некоторых однокоренных словах происходит чередование согласного в корне {b}хит/хищ{/b}. Например: похиЩать."

    jump pred_game

label pred_game:

    # Сброс переменных
    $ man_clicked = False
    $ wolf_clicked = False
    $ vor_clicked = False
    $ bear_clicked = False
    $ game_active = True

    ba "Зная корень данного слова и его особенность, давайте подумаем, кто же всё-таки забрался к Танюшке в дом. Кто такой этот {b}хитник{/b}?"

    hide bazhov
    with dissolve

label choice_loop:
    # Вызываем экран - он сам показывает картинки
    call screen hitnik_choice

    if _return == "man":
        $ man_clicked = True
        show man_2 at Position(xpos=0.127, ypos=0.7)
        ba "Рабочий? Нет, всамделишные работники ничего не {b}похищают{/b}!"
        ba "Давайте я вам историю чуть дальше расскажу, может она вас натолкнёт на кой-какие мысли."
        ba "Так вот... Забрался, значится, к Танюшке хитник. То ли он в ограде спозаранку спрятался, то ли потом где незаметно пролез..."
        ba "Но из суседей его никто не видал. Да и не знал."
        ba "Поняли уже поди про кого речь-то?"
        hide man_2
        jump choice_loop

    elif _return == "vor":
        $ vor_clicked = True
        show vor_2 at Position(xpos=0.620, ypos=0.7)
        ba "Именно! Это человек, желающий {b}похитить{/b} что-то у другого."
        ba "{b}Хищники{/b} — вроде волка и медведя — похищают жизни! А {b}хитник{/b} ценности всякие."
        ba "Проще говоря, хитник — это {b}вор{/b}. Пришёл он как раз за драгоценностями."
        ba "Напугал Танюшку жутко... С тех пор, Настасья шкатулку и прячет. От таких \"гостей\" подальше."
        hide vor_2
        jump barin1

    elif _return == "wolf" or _return == "bear":
        $ wolf_clicked = True
        $ bear_clicked = True  # меняем и медведя тоже
        show wolf_2 at Position(xpos=0.373, ypos=0.7)
        show bear_2 at Position(xpos=0.866, ypos=0.7)
        ba "Почти верно! \"{b}Хитник{/b}\" действительно похож на слово \"{b}хищник{/b}\", к которому можно отнести и волка, и медведя."
        ba "Корень у слов один, отличается только одна буква. Как же их различить?"
        ba "А я вам историю чуть дальше расскажу, вы сами и поймете, почему это не волк и не медведь."
        ba "Так вот... Не знаком никому этот хитник был, а по делу видать — кто-то навёл его, про весь порядок рассказал. Где да что лежит..."
        ba "Поняли уже поди про кого речь-то?"
        hide wolf_2
        hide bear_2
        jump choice_loop

label no:

    hide bazhov
    show bazhov_sad at right
    with dissolve

    ba "Ох... Неверно, робята."
    ba "Разве ж у \"{b}хитника{/b}\" и \"{b}хихикать{/b}\" один корень?{w} Вот и я думаю, что нет."

    hide bazhov_sad
    show bazhov at right
    with dissolve

    ba "В слове \"{b}хитник{/b}\" корень \"{b}хит{/b}\", как и в слове \"{b}похитить{/b}\". А какие однокоренные слова вы ещё можете подобрать? Что интересное можно заметить?"
    ba "В некоторых однокоренных словах происходит чередование согласного в корне {b}хит/хищ{/b}. Например: похиЩать."

    jump pred_game

    return


label barin1:

    scene bg izba
    with fade

    show tanya
    with dissolve

    ba "Вот такая история про Танюшку. А так она у нас, конечно, своенравная девица."

    hide tanya
    with dissolve

    show tanya at left
    with dissolve

    show barin_smile at right
    with dissolve

    ba "Нравилась Танюшка всем. Как-то и барину одному приглянулась. Да так, что он жениться на ней захотел."

    hide barin_smile
    show barin at right
    with dissolve

    ba "Танюшка поставила барину условие непростое: показать ей в Санкт-Петербурхе кое-чего."
    ba "Саму царицу да малахитовую комнату."

    scene bg zamok
    with fade

    show tanya at left
    with dissolve

    show barin at right
    with dissolve

    ba "Делать нечего — решил её барин во дворец везти, чтобы Танюшка в его чувствах {b}не сумлевалась{/b}."

    # + 1 задание на выбор слова - сумлеваться

    scene bg black
    with fade

    show bazhov at right
    with dissolve

    ba "Поняли, с какой целью? "
    ba "Сейчас я вас и проверю!"

    jump choice_3

    return

label choice_3:

    show bazhov at right
    with dissolve

    menu:
        "Значится, повёз барин Танюшку во дворец, чтобы она {b}не сумлевалась{/b}. Это как?"

        "Не сомневалась":
            $ znanie += 1
            pass

        "Не сутулилась":
            $ error += 1
            jump error3

        "Не умничала":
            $ error += 1
            jump error3

    hide bazhov
    show bazhov_smile at right
    with dissolve

    ba "Правду молвите! Всё верно."
    ba "{b}Сумлеваться{/b}, значит, сомневаться."
    ba "На ваше словечко похоже, али нет?"
    ba "Ладно, давайте скорее узнаем, что там дальше было."

    hide bazhov

    jump zamok

    return

label error3:

    hide bazhov
    show bazhov_sad at right
    with dissolve

    ba "Ох... Ошибаетесь, робята..."
    ba "Ну-ка, покумекайте ещё."

    hide bazhov_sad

    jump choice_3

    return


label zamok:

    scene bg zamok
    with fade

    show tanya at left
    with dissolve

    show barin at right
    with dissolve

    ba "Так вот, стали они ждать царицу во дворце. Да только не в той зале, которая была интересна Танюшке... Не в Малахитовой."

    hide tanya
    show tanya_sad at left
    with dissolve

    ba "Нельзя было в Малахитовую комнату ходить просто так."
    ba "Не по нраву это было Танюшке. Так она и заговорила барина..."

    scene bg zamok1
    with fade

    show tanya at left
    with dissolve

    show barin at right
    with dissolve

    ba "И в конце концов попали они в малахитовую комнату."

    #scene bg black
    #with fade

    jump word_game


label word_game:

    scene bg black
    with fade

    # Сброс состояния
    python:
        word_parts["prefix"]["available"] = ["на", "за", "под", "до"]
        word_parts["root"]["available"] = ["нос", "сказ", "ябед", "уш"]
        word_parts["suffix"]["available"] = ["к", "ниц", "тель"]
        word_parts["ending"]["available"] = ["и", "ы", "а"]
        for part in word_parts:
            word_parts[part]["selected"] = None
            word_parts[part]["checked"] = False
            word_parts[part]["commented"] = False

    # Убираем диалоговое окно
    window hide

    show screen build_word_game

    ba "А царицыны... скажем, доносчицы... обо всём прознали. Как думаете, как они тогда назывались?"

    label game_loop:
        # === ЗАЩИТА ОТ KeyError ===
        python:
            for part in ["prefix", "root", "suffix", "ending"]:
                if "commented" not in word_parts[part]:
                    word_parts[part]["commented"] = False
                if "checked" not in word_parts[part]:
                    word_parts[part]["checked"] = False

        $ result = ui.interact()

        if result == "check":
            # Проверяем, все ли части слова выбраны
            if (word_parts["prefix"]["selected"] == None or
                word_parts["root"]["selected"] == None or
                word_parts["suffix"]["selected"] == None or
                word_parts["ending"]["selected"] == None):
                
                ba "Нужно выбрать все части слова!"
                jump game_loop

            # Счетчик правильных частей
            $ correct_count = 0
            $ new_comments = []  # список для НОВЫХ комментариев

            # Проверяем приставку
            if word_parts["prefix"]["selected"] == correct_word["prefix"]:
                $ word_parts["prefix"]["checked"] = True
                $ correct_count += 1
                # Если еще не комментировали эту часть
                if not word_parts["prefix"]["commented"]:
                    $ new_comments.append("Приставка {b}НА{/b} — верно! Она указывает на направление действия — {b}на{/b} ушко царице шпионки все новости и передавали.")
                    $ word_parts["prefix"]["commented"] = True
            else:
                $ word_parts["prefix"]["checked"] = False
                if word_parts["prefix"]["selected"]:
                    $ word_parts["prefix"]["available"].append(word_parts["prefix"]["selected"])
                    $ word_parts["prefix"]["available"].sort()
                    $ word_parts["prefix"]["selected"] = None

            # Проверяем корень
            if word_parts["root"]["selected"] == correct_word["root"]:
                $ word_parts["root"]["checked"] = True
                $ correct_count += 1
                if not word_parts["root"]["commented"]:
                    $ new_comments.append("Корень {b}УШ{/b} — верно! Они ведь {b}ушками{/b} своими все новости и подслушивали.")
                    $ word_parts["root"]["commented"] = True
            else:
                $ word_parts["root"]["checked"] = False
                if word_parts["root"]["selected"]:
                    $ word_parts["root"]["available"].append(word_parts["root"]["selected"])
                    $ word_parts["root"]["available"].sort()
                    $ word_parts["root"]["selected"] = None

            # Проверяем суффикс
            if word_parts["suffix"]["selected"] == correct_word["suffix"]:
                $ word_parts["suffix"]["checked"] = True
                $ correct_count += 1
                if not word_parts["suffix"]["commented"]:
                    $ new_comments.append("Суффикс {b}НИЦ{/b} — верно! Обычно он означает род деятельности. Да-да, у кого-то это доносы.")
                    $ word_parts["suffix"]["commented"] = True
            else:
                $ word_parts["suffix"]["checked"] = False
                if word_parts["suffix"]["selected"]:
                    $ word_parts["suffix"]["available"].append(word_parts["suffix"]["selected"])
                    $ word_parts["suffix"]["available"].sort()
                    $ word_parts["suffix"]["selected"] = None

            # Проверяем окончание
            if word_parts["ending"]["selected"] == correct_word["ending"]:
                $ word_parts["ending"]["checked"] = True
                $ correct_count += 1
                if not word_parts["ending"]["commented"]:
                    $ new_comments.append("Окончание {b}Ы{/b} — верно! В предложении слово пропущенное во множеств. числе должно быть, а после \"ц\" в окончании у нас только буковка \"{b}ы{/b}\" бывает.")
                    $ word_parts["ending"]["commented"] = True
            else:
                $ word_parts["ending"]["checked"] = False
                if word_parts["ending"]["selected"]:
                    $ word_parts["ending"]["available"].append(word_parts["ending"]["selected"])
                    $ word_parts["ending"]["available"].sort()
                    $ word_parts["ending"]["selected"] = None

            # Выдаем ТОЛЬКО НОВЫЕ комментарии
            if new_comments:
                python:
                    for comment in new_comments:
                        renpy.say(ba, comment)

            if correct_count == 4:
                # Все части правильные
                if not new_comments:  # если все комментарии уже были сказаны
                    ba "Поздравляю! Ты собрал всё слово 'наушницы' целиком!"
                hide screen build_word_game
                window show
                jump game_end
            elif correct_count > 0:
                # Некоторые части правильные
                ba "Эти части верны и останутся на месте. Подберите остальные!"
                jump game_loop
            else:
                # Все части неправильные
                ba "Намудрили чего-то. Покумекайте ещё."
                jump game_loop

        else:
            # Выбрана морфема
            $ part_type = result[0]
            $ selected_value = result[1]

            # Проверяем, можно ли кликать (не проверено ли уже)
            if word_parts[part_type]["checked"]:
                # Если уже проверено и правильно - не даем кликать
                jump game_loop

            # Если уже было выбрано другое значение для этой морфемы
            if word_parts[part_type]["selected"]:
                $ old_value = word_parts[part_type]["selected"]
                $ word_parts[part_type]["available"].append(old_value)
                $ word_parts[part_type]["available"].sort()

            # Убираем выбранное из доступных
            $ word_parts[part_type]["available"].remove(selected_value)
            # Устанавливаем новое выбранное
            $ word_parts[part_type]["selected"] = selected_value

            jump game_loop

label game_end:
    scene bg black
    with fade

    show bazhov at right
    with dissolve

    ba "Да, доносчиц в то время бывало {b}наушницами{/b} называли."
    ba "Вот так-то! Как думаете, что дальше приключилось с Танюшкой и барином, а?"

    scene bg town
    with fade

    show bazhov_smile
    with dissolve

    ba "Хе-хе-хе! Не скажу ничего! Вы лучше сами почитайте в сказе, больно интересно, да времени у нас нет..."
    ba "Пора нам прощаться."
    ba "Пытался я вас подловить на словечках мудрёных!"
    ba "Да больно ловкие и умненькие вы. Не так просто вас {b}оплести{/b}!"
    ba "Будет вам тогда интересно ещё больше дивных слов в Бажовском Словаре изучить."

    return

