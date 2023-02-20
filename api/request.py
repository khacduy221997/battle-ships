class Request:
    def __init__(self):
        self.boardHeight = 8
        self.boardWidth = 20
        self.sessionId = ""
        self.token = ""
        self.ships = []

    def init(self, sessionId, token, data):
        self.sessionId = sessionId
        self.token = token
        self.boardWidth = data['boardWidth'] if data['boardWidth'] else 20
        self.boardHeight = data['boardHeight'] if data['boardHeight'] else 8
        self.ships = data['ships'] if data['ships'] else []
