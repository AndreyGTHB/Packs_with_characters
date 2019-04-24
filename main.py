from time import sleep
from random import randint

name = input("Как тебя зовут?")
sleep(1)


def print_arr(arr):
    for i in arr:
        print("    " + str(i))


def open_pack(size):
    probability = randint(1, 100)
    if size == 1:
        if probability in range(1, 84):
            coins = randint(25 * size, 50 * size)
            points_forces = [randint(10 * size, 19 * size), randint(10 * size, 19 * size)]



class Character:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.rank = 1
        self.trophies = 0
        self.strength = 1

    def __str__(self):
        return self.name + "\n" + "Редкость:" + self.rarity + "\n" + "Трофеи:" + str(self.trophies) \
               + "\n" + "Ранг:" + str(self.rank) + "\n" + "Сила:" + str(self.strength)

print("Напиши 'начать_игру'")
run = False
characters = []

while not run:
    command = input()
    if command == "начать_игру":
        run = True
        print(name, ", приветствую тебя в 'паки с персонажами'! Держи начального персонажа - Шелли!")
        sleep(1)
        print("Вы получили нового персонажа - Шелли!")
        characters.append(Character("Шелли", "Начальный персонаж"))
        sleep(1)
        print("Напиши 'команды'")
        command = input()
while True:
    if command == "команды":
        print(" персонажи \n бой \n пак")
    elif command == "персонажи":
        print_arr(characters)
    else:
        print("Я тебя не понял. Напиши 'команды', чтобы узнать возможные команды.")
    command = input()
