from GUI.main_gui import run_gui
from Bot.Logic.Dumb import DumbBot
from Bot.Logic.Kill import KillBot
from Bot.Logic.Random import RandomBot
from Bot.Logic.Smart import SmartBot
from Bot.Logic.Stock import StockFish
from Bot.Intialization import ChessBot


def bot_select():
    """Run GUI, initialize a bot type based on input from GUI"""
    selection = run_gui()
    if selection[0] == 'Dumb Bot':
        bot = DumbBot()
    #if selection[0] == 'Random Bot':
     #   bot = RandomBot()
    #if selection[0] == 'Smart Bot':
     #   bot = SmartBot()
    #if selection[0] == 'Kill Bot':
     #   bot = KillBot()
    #if selection[0] == 'Stock Fish':
     #   bot = StockFish()
    return bot


bot_choice = bot_select()


