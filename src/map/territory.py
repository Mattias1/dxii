class Territory():
    """The territory is the atomary building block of a map"""

    def __init__(self, terr_id, name, x, y):
        self.id = terr_id
        self.name = name
        self.x = x
        self.y = y
        
        self.connections = []

    def addConnection(self, other)
        self.connections.append(other)