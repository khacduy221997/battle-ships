from .ship import Ship
import numpy as np
import random

class Board:
    def __init__(self):
        self.shot_map = []
        self.map = []
        self.height = 8
        self.width = 20
        self.ships = []
        self.target = []

    def init(self, boardWidth, boardHeight):
        self.width = boardWidth  # 20
        self.height = boardHeight  # 8
        self.map = np.zeros([self.height, self.width])
        self.shot_map = np.zeros([self.height, self.width])


    def place_ships(self, ships):
        for item in ships:
            type = item['type']
            quantity = item['quantity']
            for _ in range(quantity):
                self.place_ship(type)

    def place_ship(self, type):
        return
