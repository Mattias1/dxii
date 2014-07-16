class Game():
    """The game class"""

    def __init__(self, game_id=0, map_id=0, nr_of_players=0):
        self.game_id       = game_id
        self.map_id        = map_id
        self.nr_of_players = nr_of_players
        self.players       = []

    def addPlayer(self, s):
        s = ''.join(s.split()) # Remove all whitespace
        if s == '':
            return
        p = Player.fromString(s)
        if len(self.players) == self.nr_of_players and self.nr_of_players > 0:
            self.players[p.player_id - 1] = p
        else:
            self.players.append(p)

    def initFromString(self, s):
        s = ''.join(s.split()) # Remove all whitespace
        a = s.split(',')
        if len(a) != 3:
            return None
        self.game_id = int(a[0])
        self.map_id = int(a[1])
        self.nr_of_players = int(a[2])
        if len(self.players) == 0:
            self.players = [None for _ in range(self.nr_of_players)]


class Player():
    """The player class"""

    def __init__(self, player_id, member_id, player_name, player_color, player_team):
        self.player_id    = player_id
        self.member_id    = member_id
        self.player_name  = player_name
        self.player_color = player_color
        self.player_team  = player_team
        self.stats        = None

    @staticmethod
    def fromString(s):
        s = ''.join(s.split()) # Remove all whitespace
        a = s.split(',')
        if len(a) != 5:
            return None
        return Player(int(a[0]), int(a[1]), a[2], int(a[3]), int(a[4]))


if __name__ == '__main__':
    import main
    main.main()
