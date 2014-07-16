# The log consants
START_TURN = 1
END_TURN = 9
WIN_GAME = 12
ROUND_START = 13
RUN_OUT_OF_TIME = 14
MISS_TURN = 15
GAME_CREATED = 16
JOINED_GAME = 17
GAME_STARTED = 18
LEFT_GAME = 19
RESIGNED_GAME = 20
ADD_TIME = 21
KICKED_MISSING_TURNS = 25
MISSED_TURN = 26
LOST_POINTS = 88
RECEIVED_POINTS = 89
RECEIVED_TOKENS = 91
POINTS_REVERSED_BY_ADMIN = 98
GAME_FINISHED = 99

RECEIVE_TROOPS_NR_TERRITORIES = 2
RECEIVE_TROOPS_REGION = 3
RECEIVE_TROOPS_TURN_IN_CARDS = 4
RECEIVE_TROOPS_OWN_CARD_TERRITORY = 10

PLACE_TROOPS = 5
ATTACK_STOP_EARLY = 6
ATTACK_SUCCEED = 61
FORTIFY = 7

RECEIVE_CARD = 8
KILL_PLAYER = 11


class Log():
    """The log class"""

    def __init__(self):
        self.logs = []

    def __len__(self):
        return len(self.logs)

    def getLog(self, i):
        return self.logs[i]

    def addLog(self, text):
        if text != '':
            self.logs.append(LogEntry.fromString(text))


class LogEntry():
    """ An entry of the log class"""

    def __init__(self, log_type, log_round, log_extra, log_player_id, log_against_player_id, log_from, log_to, log_num, log_num2, log_timestamp):
        self.log_type              = log_type
        self.log_round             = log_round
        self.log_extra             = log_extra
        self.log_player_id         = log_player_id
        self.log_against_player_id = log_against_player_id
        self.log_from              = log_from
        self.log_to                = log_to
        self.log_num               = log_num
        self.log_num2              = log_num2
        self.log_timestamp         = log_timestamp

    @staticmethod
    def fromString(s):
        s = ''.join(s.split()) # Remove all whitespace
        a = s.split(',')
        if len(a) != 10:
            return None
        return LogEntry(int(a[0]), int(a[1]), a[2], int(a[3]), int(a[4]), a[5], a[6], int(a[7]), int(a[8]), int(a[9]))


if __name__ == '__main__':
    import main
    main.main()
