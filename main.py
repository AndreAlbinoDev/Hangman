import pygame as pg
import random

branco = (255, 255, 255)
black = (0, 0, 0)

window = pg.display.set_mode((1000, 600))

pg.font.init()
font = pg.font.SysFont("Courier New", 50)
font_rb = pg.font.SysFont("Courier New", 30)

words = ['ELEPHANT',
        'COMPUTER',
        'SUNSHINE',
        'CHOCOLATE'
        'GUITAR'
        'RAINBOW'
        'BUTTERFLY'
        'ADVENTURE'
        'FIREWORKS'
        'MYSTERY']


trys = [' ', '-']
chossen_word = ''
camouflaged_word = ''
end_game = True
chance = 0
letter = ' '
click_last_status = False

def gallows_drawing(window, chance):
    pg.draw.rect(window, branco, (0, 0, 1000, 600))
    pg.draw.line(window, black, (100, 500), (100, 100), 10)
    pg.draw.line(window, black, (50, 500), (150, 500), 10)
    pg.draw.line(window, black, (100, 100), (300, 100), 10)
    pg.draw.line(window, black, (300, 100), (300, 150), 10)
    if chance >= 1:
        pg.draw.circle(window, black, (300, 200), 50, 10)
    if chance >= 2:
        pg.draw.line(window, black, (300, 250), (300, 350), 10)
    if chance >= 3:
        pg.draw.line(window, black, (300, 260), (225, 350), 10)
    if chance >= 4:
        pg.draw.line(window, black, (300, 260), (375, 350), 10)
    if chance >= 5:
        pg.draw.line(window, black, (300, 350), (375, 450), 10)
        pg.draw.line(window, black, (300, 350), (225, 450), 10)

def Restart_Button(window):
    pg.draw.rect(window, black, (700, 100, 200, 65))
    text = font_rb.render('Restart', 1, branco)
    window.blit(text, (740, 120))

def draw_word(word, chossen_word, end_game):
    if end_game == True:
        palavra_n = random.randint(0, len(word) - 1)
        chossen_word = word[palavra_n]
        end_game = False
        chance = 0
    return chossen_word, end_game

def camouflage_word(chossen_word, camouflage_word, tentativas_de_letras):
    camouflage_word = chossen_word
    for n in range(len(camouflage_word)):
        if camouflage_word[n:n + 1] not in tentativas_de_letras:
            camouflage_word = camouflage_word.replace(camouflage_word[n], '#')
    return camouflage_word

def try_letter(try_letters, chossen_word, letter, chance):
    if letter not in try_letters:
        try_letters.append(letter)
        if letter not in chossen_word:
            chance += 1
    elif letter in try_letters:
        pass
    return try_letters, chance

def game_word(window, camouflaged_word):
    palavra = font.render(camouflaged_word, 1, black)
    window.blit(palavra, (200, 500))

def restart_do_Jogo(camouflaged_word, end_game, chance, letter, attempt_letters, click_last_status, click, x, y):
    count = 0
    limite = len(camouflaged_word)
    for n in range(len(camouflaged_word)):
        if camouflaged_word[n] != '#':
            count += 1
    if count == limite and click_last_status == False and click[0] == True:
        print('Ok')
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            attempt_letters = [' ', '-']
            end_game = True
            chance = 0
            letter = ' '
    return end_game, chance, attempt_letters, letter

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letter = str(pg.key.name(event.key)).upper()

    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    click = pg.mouse.get_pressed()

    gallows_drawing(window, chance)
    Restart_Button(window)
    chossen_word, end_game = draw_word(words, chossen_word, end_game)
    camouflaged_word = camouflage_word(chossen_word, camouflaged_word, trys)
    trys, chance = try_letter(trys, chossen_word, letter, chance)
    game_word(window, camouflaged_word)
    end_game, chance, trys, letter = restart_do_Jogo(camouflaged_word, end_game, chance, letter, trys, click_last_status, click, mouse_position_x, mouse_position_y)

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()