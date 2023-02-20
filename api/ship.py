SHIP_INFO = {
    "CV": 4, # 5 Ô
    "OR": 2, # 4 Ô
    "CA": 3,
    "BB": 4,
    "DD": 2
}

ROW_OF_SHIP = {
    "CV": 2, # 5 Ô
    "OR": 2, # 4 Ô
    "CA": 1,
    "BB": 1,
    "DD": 1
}

class ShipPattern:
    def getShipPattern(self, type, row, col, isVertical):
        ret = []

        if type == "CV":
            if isVertical:
                for i in range(4):
                    ret.append([ row + i, col ])
                ret.append([ row + 1, col - 1 ])
            else:
                for i in range(4):
                    ret.append([ row, col + i ])
                ret.append([ row - 1, col + 1 ])
            return ret
        if type == "OR":
            for i in range(2):
                for j in range(2):
                    ret.append([ row + i, col + j ])
            return ret
        if type == "CA":
            length = 3
        elif type == "BB":
            length = 4
        else:
            # DD
            length = 2

        if isVertical:
            for i in range(length):
                ret.append({ row + i, col })
        else:
            for i in range(length):
                ret.append([ row, col + i ])
        return ret

class Ship:
    def __init__(self, type, row, col, isVertical):
        self.type = type
        self.length = SHIP_INFO[self.type]
        self.rows = ROW_OF_SHIP[self.type]
        pattern = ShipPattern()
        self.coordinates = pattern.getShipPattern(type, row, col, isVertical)

