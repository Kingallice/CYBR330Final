from datetime import datetime, timedelta
from traceback import print_exception
import requests

LiChessAPI = 'https://lichess.org/api/'

class ChessBot:
    """Class that holds information about the ChessBot"""
    def __init__(self, BOT_API_KEY = 'lip_LIRgnxQvamGWcKKIH9x7'):
        """Initializes a new instance of the Bot utilizing the information provided by the LiChessAPI"""
        try:
            info = requests.get(LiChessAPI + 'account', headers={'Authorization': 'Bearer '+BOT_API_KEY}).json()
            if 'title' not in info or info['title'] != 'BOT':
                raise ConnectionError('Account is not registered as a BOT')
            self._KEY = BOT_API_KEY
            self._id = info['id']
            self._userName = info['username']
            self._perfs = info['perfs']
            self._creationDate = info['createdAt']
            self._url = info['url']
        except KeyError:
            print_exception()
        except:
            print_exception()

    def getKey(self):
        """Returns the API key for the Bot"""
        return self._KEY

    def getId(self):
        """Returns the id of the Bot"""
        return self._id
    
    def getUserName(self):
        """Returns the username of the Bot"""
        return self._userName
    
    def getPerformance(self, type=''):
        """Gets the performance of the Bot (Can pass a game type to pull only data related to that mode)"""
        try:
            return self._perfs[type]
        except KeyError:
            return self._perfs

    def getAge(self):
        """Returns a timedelta object that represents the age of the Bot"""
        return timedelta(seconds=(round(datetime.now().timestamp()) - self._creationDate//1000))
    def getAgeDays(self):
        """Returns the age of the Bot in days"""
        return self.getAge().days
    def getAgeYears(self):
        """Returns the age of the Bot in years"""
        return round(self.getAge().days / 365, 1)

    def getUrl(self):
        """Returns the URL for the profile of the Bot"""
        return self._url