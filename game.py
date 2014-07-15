class Game():
    """The game class"""

    def __init__(self, game_id, map_id, nr_of_players):
        self.game_id = game_id
        self.map_id = map_id
        self.nr_of_players = nr_of_players
        self.players = []

    @staticmethod
    def fromString(s):
        s = ''.join(s.split()) # Remove all whitespace
        a = s.split(',')
        if len(a) != 3:
            return ''
        return Game(int(a[0]), int(a[1]), int(a[2]))


class Player():
    """The player class"""

    def __init__(self, player_id, member_id, player_name, player_color, player_team):
        self.player_id    = player_id
        self.member_id    = member_id
        self.player_name  = player_name
        self.player_color = player_color
        self.player_team  = player_team

    @staticmethod
    def fromString(s):
        s = ''.join(s.split()) # Remove all whitespace
        a = s.split(',')
        if len(a) != 5:
            return ''
        return Player(int(a[0]), int(a[1]), a[2], int(a[3]), int(a[4]))


if __name__ == '__main__':
    import main
    main.main()
