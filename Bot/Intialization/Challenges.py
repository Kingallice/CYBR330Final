from datetime import datetime, timedelta
import requests

LiChessAPI = 'https://lichess.org/api/'


class Challenger:
    """Holds information about the challenger to a Challenge"""

    def __init__(self, key, name):
        info = requests.get(LiChessAPI + "user/" + name, headers={"Authorization": "Bearer " + key}).json()
        self._id = info['id']
        self._userName = info['username']
        self._online = info['online']
        self._perfs = info['perfs']
        self._creationDate = info['createdAt']
        if 'disabled' in info.keys():
            self._disabled = info['disabled']
        if 'tosViolation' in info.keys():
            self._tosViolation = info['tosViolation']
        if 'profile' in info.keys():
            self._profile = info['profile']
        if 'title' in info.keys():
            self._title = info['title']
        self._url = info['url']

    def getId(self):
        """Returns the id of the User"""
        return self._id

    def getUserName(self):
        """Returns the username of the User"""
        return self._userName

    def isOnline(self):
        """Returns whether the User is online"""
        return self._online

    def getPerformance(self, type=''):
        """Gets the performance of the User (Can pass a game type to pull only data related to that mode)"""
        try:
            return self._perfs[type]
        except KeyError:
            return self._perfs

    def getAge(self):
        """Returns a timedelta object that represents the age of the User account"""
        return timedelta(seconds=(round(datetime.now().timestamp()) - self._creationDate // 1000))

    def getAgeDays(self):
        """Returns the age of the User account in days"""
        return self.getAge().days

    def getAgeYears(self):
        """Returns the age of the User account in years"""
        return round(self.getAge().days / 365, 1)

    def getUrl(self):
        """Returns the URL for the profile of the User account"""
        return self._url

    def __str__(self):
        return str({"id": self._id, "username": self._userName, "online": self._online, "perfs": self._perfs,
                    "age": {"createdAt": self._creationDate, "days": self.getAgeDays(), "years": self.getAgeYears()},
                    "url": self._url})


class Challenge:
    """Holds information about individual challenges"""

    def __init__(self, bot, info):
        self._id = info['id']
        self._url = info['url']
        self._color = info['color']
        self._dir = info['direction']
        self._challenger = Challenger(bot.getKey(), info['challenger']['name'])
        self._rated = info['rated']
        self._status = info['status']

    def getId(self):
        """Returns the Id for the Game related to the Challenge"""
        return self._id

    def getURL(self):
        """Returns the URL for the Game related to the Challenge"""
        return self._url

    def getColor(self):
        """Returns the color information for the Challenge"""
        return self._color

    def getDirection(self):
        """Returns the direction of the Challenge"""
        return self._dir

    def getChallenger(self):
        """Returns the Challenger of the Challenge"""
        return self._challenger

    def isRated(self):
        """Returns whether the Game is rated or not"""
        return self._rated

    def getStatus(self):
        """Returns the status of the Game"""
        return self._status
