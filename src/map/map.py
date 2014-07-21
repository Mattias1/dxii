class Map():
    """The map class"""

    def __init__(self, map_id, name, w, h, imageUrl):
        self.id = map_id
        self.name = name
        self.width = w
        self.height = h
        # Todo, do something with the imageUrl

        self.territories = {}

    def addTerritory(self, terr):
        if terr.id in self.territories:
            return
        self.territories[terr.id] = terr

    def getTerritoryByID(self, terrID):
        if terrID in self.territories:
            return self.territories[terrID]
        return None
