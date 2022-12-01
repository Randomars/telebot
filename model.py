import random

startBons = 15
maxTakeBons = 28
players = ['Компьютер', 'Игрок']

def getBons() -> int:
    global startBons
    return startBons

def setBons(newValue: int):
    global startBons
    startBons = newValue

# def inputBons(curBons: int):
#     inpBons = 0
#     while (inpBons < 1) or (inpBons > maxBons) or (inpBons > curBons) or (inpBons == ''):
#         try:
#             inpBons = int(input(f'Сколько взять конфет?: '))
#         except:
#             pass
#     return inpBons

# def chooseTurn(trn: int):
#     if trn%2 > 0:
#         return 1
#     else:
#         return 0

# def getBonsBot(bon: int):
#     if bon <= maxBons:
#         return bon
#     else:
#         inpBons = 1
#         while not (bon == inpBons + bon//maxBons*maxBons + 1) and (inpBons < maxBons):
#             inpBons += 1
#         return inpBons


# bonBons = startBons
# getBons = 0

# print('Бросаем жребий.')
# turn = random.randint(1,2)
# print(f'Начинает {players[chooseTurn(turn)]}.')
# print(f'На столе {bonBons} конфет.')


# while bonBons > 0:
#     print(f'Ход игрока: {players[chooseTurn(turn)]}')
#     if chooseTurn(turn) == 0:
#         getBons = getBonsBot(bonBons)
#     else:
#         getBons = inputBons(bonBons)
#     bonBons -= getBons
#     print(f'Игрок взял {getBons} конфет.')
#     print(f'Осталось {bonBons} конфет.')
#     turn += 1

# print(f'Победитель - {players[chooseTurn(turn-1)]}!')