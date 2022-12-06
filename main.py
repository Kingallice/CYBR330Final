from GUI.main_gui import run_gui
from Bot.Logic.Dumb import DumbBot
from Bot.Logic.Kill import KillBot
from Bot.Logic.Random import RandomBot
from Bot.Logic.Best import BestBot
from Bot.Logic.Stock import StockFish
from Bot.Intialization.ChessBot import ChessBot
from Bot.GameConnector import GameConnector
from Bot.ResultUtil import ResultUtil
from Bot.ChallengeUtil import ChallengeUtil
import random

bot = ChessBot("lip_FjFtfJSWH2mB8RH6g53L")#lip_dQJI4YyJYwytH4emLoyq")
ChallengeUtil.startAcceptingChallenges(bot, [BestBot])#[DumbBot, KillBot, BestBot, RandomBot, StockFish])


def bot_select():
    """Run GUI, initialize a bot type based on input from GUI"""
    ResultUtil.resetResultFile()
    opponentList =  [
        {"username":"ai","level":2},
        {"username":"ai","level":8}, 
        {"username":"dummyette"}]
    gameCount = 5

    selection = run_gui()
    username = selection[1]
    if not username and username != "":
        opponentList = [{"username": username}]

    if selection[0] == 'Dumb Bot':
        ChallengeUtil.testAlgorithm(bot, DumbBot, opponentList, gameCount)
    elif selection[0] == 'Random Bot':
        ChallengeUtil.testAlgorithm(bot, RandomBot, opponentList, gameCount)
    elif selection[0] == 'Best Bot':
        ChallengeUtil.testAlgorithm(bot, BestBot, opponentList, gameCount)
    elif selection[0] == 'Kill Bot':
        ChallengeUtil.testAlgorithm(bot, KillBot, opponentList, gameCount)
    elif selection[0] == 'Stock Fish':
        ChallengeUtil.testAlgorithm(bot, StockFish, opponentList, gameCount)
    else:
        for x in [DumbBot, KillBot, RandomBot, StockFish, BestBot]:
            ChallengeUtil.testAlgorithm(bot, x, opponentList, gameCount)
    return bot

bot_choice = bot_select()
