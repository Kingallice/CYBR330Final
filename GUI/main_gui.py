import PySimpleGUI as sg


bot_list = ["Dumb Bot", "Smart Bot", "Random Bot", "<bot4>", "<bot5>"]

font_title = ('American Typewriter', 72, 'bold')
font_h1 = ('American Typewriter', 16)

layout_main = [[sg.Text("Chess Bots 3000",
                        auto_size_text=True,
                        font=font_title,
                        justification='center',
                        pad=(50, 0),
                        text_color='gold',
                        expand_x=True,
                        key='title')],
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
                        key='h2')],

               [sg.InputCombo(bot_list,
                              default_value='<choose a bot>',
                              size=15,
                              readonly=True,
                              font=('American Typewriter', 26),
                              pad=((0, 0), (0, 50)),
                              button_background_color='blue',
                              text_color='darkblue',
                              button_arrow_color='gold',
                              key='bot_choice')],

               [sg.Button("Start",
                          size=7,
                          button_color='darkgreen',
                          font=('American Typewriter', 20, 'bold'),
                          key='start'),
                sg.Button("Quit",
                          size=7,
                          button_color='darkred',
                          font=('American Typewriter', 20, 'bold'),
                          key='quit')],

               # [New GUI elements can be added between brackets like this]

               ]

window = sg.Window("Chess Bots 3000",
                   layout_main,
                   resizable=True,
                   element_justification='center',
                   auto_size_text=True,
                   )

window.read()

while True:  # This is the event loop, where all events are handled. It's unfinished and can be fleshed out later
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    

window.close()

