from time import sleep
from random import randint

from Character import *
from Pack import *


def print_arr(arr):
    for i in arr:
        print("    " + str(i))


pack = Pack(20)
print_arr(pack.open())
print_arr(pack.open())

print("Напиши 'начать_игру'")
run = False
characters = []

while not run:
    command = input()
    if command == "начать_игру":
        run = True
        name = input("Как тебя зовут?")
        sleep(1)
        print(name + ", приветствую тебя в 'паки с персонажами'! Держи начального персонажа - Шелли!")
        sleep(1)
        print("Вы получили нового персонажа - Шелли!")
        characters.append(Character("Шелли", "Начальный персонаж", 170))
        sleep(1)
        print("Напиши 'команды'")
        command = input()

packs_info = {"Обычные": 2, "Большие": 0, "Мега": 0}

while True:
    if command == "команды":
        print(" персонажи \n бой \n пак \n выход")
    elif command == "выход":
        print("Выхожу...")
        break
    elif command == "персонажи":
        print_arr(characters)
    elif command == "пак":
        print(packs_info)
        print("открыть")
        print("Чтобы выйти, напишите любую команду(кроме 'открыть').")
        command = input()
        if command == "открыть":
            print("обычный \n большой \n мега")
    else:
        print("Я тебя не понял. Напиши 'команды', чтобы узнать возможные команды.")
    command = input()
