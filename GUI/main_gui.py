import PySimpleGUI as sg


def run_gui():
    bot_list = ["Dumb Bot", "Best Bot", "Random Bot", "Kill Bot", "Stock Fish"]

    sg.theme('Dark Teal 2')

    font_title = ('Arial', 72, 'bold')
    font_h1 = ('Arial', 16)

    layout_main = [[sg.Text("Chess Bots 3000",
                            auto_size_text=True,
                            font=font_title,
                            justification='center',
                            pad=(50, 0),
                            expand_x=True,
                            key='-TITLE-')],
                   [sg.Text('Created by Garret, Noah, and Jake',
                            font=('Arial', 16, 'bold'),
                            pad=((0, 0), (0, 50)),
                            key='credit')],
                   [sg.Text(text='Enter lichess.com username below:',
                            font=('Arial', 16, 'bold'),
                            key='username_label')],
                   [sg.InputText(font=('Arial', 16),
                                 pad=((0, 0), (0, 50)),
                                 key='username')],
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
                                  font=('Arial', 26),
                                  pad=((0, 0), (0, 50)),
                                  background_color='white',
                                  text_color='lime green',
                                  key='-BOT_INPUT-')],

                   [sg.Text('',
                            key='-OUTPUT-',
                            auto_size_text=True,
                            font=('Arial', 20),
                            justification='center',
                            expand_x=True)],

                   [sg.Button('SUBMIT',
                              size=7,
                              button_color='darkgreen',
                              font=('Arial', 20),
                              key='-SUBMIT-'),
                    sg.Button('BATTLE',
                              button_type=sg.BUTTON_TYPE_CLOSES_WIN,
                              size=7,
                              button_color='darkred',
                              font=('Arial', 20),
                              key='-BATTLE-')
                    ]]

    #              [New GUI elements can be added between brackets like this]

    window = sg.Window("Chess Bots 3000",
                       layout_main,
                       resizable=True,
                       element_justification='center',
                       auto_size_text=True,
                       alpha_channel=0.99,
                       size=(1000, 600)
                       )

    input_list = [None]

    while True:  # This is the event loop, where all events are handled. It's unfinished and can be fleshed out later
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        choice = window['-BOT_INPUT-'].get()
        input_list[0] = choice
        username = window['username'].get()
        input_list.append(username)
        if input_list[0] == 'Dumb Bot':
            window['-OUTPUT-'].update('You have chosen ' + input_list[0] + '. It seems you have chosen death... '
                                                                           'Sending your champion to battle!')
        else:
            window['-OUTPUT-'].update('You have chosen ' + str(input_list[0]) + '. Sending your champion to battle!')

    window.close()
    return input_list

