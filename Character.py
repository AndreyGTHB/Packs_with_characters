
class Character:
    def __init__(self, name, rarity, damage):
        self.name = name
        self.rarity = rarity
        self.rank = 1
        self.trophies = 0
        self.strength = 1
        self.damage = damage

    def __str__(self):
        return self.name + "\n" + "Редкость:" + self.rarity + "\n" + "Трофеи:" + str(self.trophies) \
               + "\n" + "Ранг:" + str(self.rank) + "\n" + "Сила:" + str(self.strength) + "\n" + "Урон:" \
               + str(self.damage)