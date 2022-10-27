import PySimpleGUI as sg


def run_gui():
    bot_list = ["Dumb Bot", "Smart Bot", "Random Bot", "<bot4>", "<bot5>"]

    font_title = ('Phosphate', 72, 'bold')
    font_h1 = ('American Typewriter', 16)

    layout_main = [[sg.Text("Chess Bots 3000",
                            auto_size_text=True,
                            font=font_title,
                            justification='center',
                            pad=(50, 0),
                            text_color='gold',
                            expand_x=True,
                            key='-TITLE-')],
                   [sg.Text('Created by Garret, Noah, and Jake',
                            text_color='white',
                            font=('American Typewriter', 16, 'bold'),
                            pad=((0, 0), (0, 50)),
                            key='credit')],
                   [sg.Text('Choose your chess bot below:',
                            auto_size_text=True,
                            font=font_h1,
                            justification='center',
                            expand_x=True,
                            key='-SUBHEADING-')],

                   [sg.InputCombo(bot_list,
                                  default_value='<choose a bot>',
                                  size=15,
                                  readonly=True,
                                  font=('American Typewriter', 26),
                                  pad=((0, 0), (0, 50)),
                                  button_background_color='blue',
                                  text_color='darkblue',
                                  button_arrow_color='gold',
                                  key='-BOT_INPUT-')],

                   [sg.Text('',
                            key='-OUTPUT-',
                            auto_size_text=True,
                            font=('American Typewriter', 20),
                            text_color='gold',
                            justification='center',
                            expand_x=True)],

                   [sg.Button('START',
                              size=7,
                              button_color='darkgreen',
                              font=('American Typewriter', 20, 'bold'),
                              key='-START-')]]

    #              [New GUI elements can be added between brackets like this]

    window = sg.Window("Chess Bots 3000",
                       layout_main,
                       resizable=True,
                       element_justification='center',
                       auto_size_text=True,
                       alpha_channel=0.95,
                       size=(1000, 400)
                       )

    input_list = [None]

    while True:  # This is the event loop, where all events are handled. It's unfinished and can be fleshed out later
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        choice = window['-BOT_INPUT-'].get()
        input_list[0] = choice
        if input_list[0] == 'Dumb Bot':
            window['-OUTPUT-'].update('You have chosen ' + input_list[0] + '. It seems you have chosen death... '
                                                                           'Sending your champion to battle!')
        else:
            window['-OUTPUT-'].update('You have chosen ' + input_list[0] + '. Sending your champion to battle!')

    window.close()
    return input_list


print(run_gui())
