
class Game:
    """Class to hold information about a game"""
    def __init__(self, info):
        self._gameId = info['id']
        self._type = info['variant']['name']
        self._clock = info['clock']
        self._rated = info['rated']
        self._createdAt = info['createdAt']
        self._white = info['white']
        self._black = info['black']

    def getGameId(self):
        """Returns the gameId"""
        return self._gameId
    
    def getGameType(self):
        """Returns the game type"""
        return self._type
    
    def getClock(self):
        """Returns the clock"""
        return self._clock
    
    def isRated(self):
        """Returns true if rated else false"""
        return self._rated

    def createdAt(self):
        """Gets the creation timestamp"""
        return self._createdAt
    
    def getWhite(self):
        """Gets data regarding white"""
        return self._white
    
    def getBlack(self):
        """Gets data regarding black"""
        return self._black
    
    def getColorId(info):
        """Gets the id information from the json passed (or None if it can't be determined)"""
        if 'id' in info.keys():
            return info['id']
        elif 'aiLevel' in info.keys():
            return 'AI - Level '+str(info['aiLevel'])
        return None

    def getColorName(info):
        """Get the name information from the json passed (or None if it can't be determined)"""
        if 'name' in info.keys():
            return info['name']
        elif 'aiLevel' in info.keys():
            return 'AI - Level '+str(info['aiLevel'])
        return None


    def getColor(self, id):
        """Gets the color of the passed id (or None if not found)."""
        if 'id' in self._black.keys():
            if id == self._black['id']:
                return 'black'
        if 'id' in self._white.keys():
            if id == self._white['id']:
                return 'white'
        return None

    def getOpponent(self, id):
        if Game.getColorId(self.getWhite()) == id:
            return self.getBlack()
        return self.getWhite()
