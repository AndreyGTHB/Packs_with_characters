from time import sleep
from random import randint

# name = input("Как тебя зовут?")
# sleep(1)


def print_arr(arr):
    for i in arr:
        print("    " + str(i))


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


class Pack:
    def __init__(self, size):
        self.size = size

    def open(self):
        coins = 0
        points_forces = []
        character = {}
        prize = {
            "Монеты": 0
            "Очки_силы":[]
        }
        for n in range(3):
            probability = randint(1, 100)
            if probability in range(1, 78):
                if randint(0, 1) == 0:
                    coins = randint(25 * self.size, 50 * self.size)
                    prize[](coins)
                    
                else:
                    points_forces = randint(10 * self.size, 19 * self.size)
                    prize.append(points_forces)
            elif probability in range(79, 87):
                character = Character(input("Вам выпал Редкий персонаж. Придумайте ему имя!"), "Редкий", 200)
                prize.append(character)
            elif probability in range(88, 93):
                character = Character(input("Вам выпал Сверхредкий персонаж. Придумайте ему имя!"), "Сверхредкий", 320)
                prize.append(character)
            elif probability in range(94, 97):
                character = Character(input("Вам выпал Эпический персонаж. Придумайте ему имя!"), "Эпический", 500)
                prize.append(character)
            elif probability in range(98, 99):
                character = Character(input("Вам выпал Мифический персонаж. Придумайте ему имя!"), "Мифический", 685)
                prize.append(character)
            else:
                character = Character(input("Вам выпал Легендарный персонаж. Придумайте ему имя!"), "Легендарный", 900)
                prize.append(character)
        return prize

pack = Pack(5)
print_arr(pack.open())

print("Напиши 'начать_игру'")
run = False
characters = []

while not run:
    command = input()
    if command == "начать_игру":
        run = True
        print(name + ", приветствую тебя в 'паки с персонажами'! Держи начального персонажа - Шелли!")
        sleep(1)
        print("Вы получили нового персонажа - Шелли!")
        characters.append(Character("Шелли", "Начальный персонаж", 170))
        sleep(1)
        print("Напиши 'команды'")
        command = input()

packs = {"Обычные": 2, "Большие": 0, "Мега": 0}

while True:
    if command == "команды":
        print(" персонажи \n бой \n пак \n выход")
    elif command == "выход":
        print("Выхожу...")
        break
    elif command == "персонажи":
        print_arr(characters)
    elif command == "пак":
        print(packs)
        print("открыть")
        print("Чтобы выйти, напишите любую команду(кроме 'открыть').")
        command = input()
        if command == "открыть":
            print("обычный \n большой \n мега")
    else:
        print("Я тебя не понял. Напиши 'команды', чтобы узнать возможные команды.")
    command = input()
