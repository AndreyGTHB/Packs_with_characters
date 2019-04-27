from Character import *
from random import *

class Pack:
    def __init__(self, size):
        self.size = size
        self.is_open = False

    def open(self):
        coins = 0
        points_forces = []
        character = {}
        prize = []
        if self.is_open:
            return prize

        for n in range(3):
            probability = randint(1, 10000)
            if probability in range(1, 9508):
                if randint(0, 1) == 0:
                    coins = randint(25 * self.size, 50 * self.size)
                    prize.append(coins)

                else:
                    points_forces = randint(10 * self.size, 19 * self.size)
                    prize.append(points_forces)
            elif probability in range(9509, 9683):
                character = Character(input("Вам выпал Редкий персонаж. Придумайте ему имя!"), "Редкий", randint(200, 300))
                prize.append(character)
            elif probability in range(9684, 9802):
                character = Character(input("Вам выпал Сверхредкий персонаж. Придумайте ему имя!"), "Сверхредкий", \
                                      randint(320, 420))
                prize.append(character)
            elif probability in range(9803, 9892):
                character = Character(input("Вам выпал Эпический персонаж. Придумайте ему имя!"), "Эпический", \
                                      randint(500, 600))
                prize.append(character)
            elif probability in range(9893, 9960):
                character = Character(input("Вам выпал Мифический персонаж. Придумайте ему имя!"), "Мифический", \
                                      randint(685, 785))
                prize.append(character)
            else:
                character = Character(input("Вам выпал Легендарный персонаж. Придумайте ему имя!"), "Легендарный", 900)
                prize.append(character)

        self.is_open = True

        return prize
