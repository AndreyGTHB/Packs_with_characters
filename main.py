from time import sleep

name = input("Как тебя зовут?")
sleep(1)

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
        characters.append("Шелли")
        sleep(1)
        print("Напиши 'команды'")
        command = input()
while True:
    if command == "команды":
        print(" персонажи \n бой \n открыть_пак \n открыть_большой_пак \n открыть")
    elif command == "персонажи":
        print(characters)
    else:
        print("Я тебя не понял. Напиши 'команды', чтобы узнать возможные команды.")
    command = input()