import  pygame
import sys

MAX_X = 800
MAX_Y = 800
IMG_SIZE = 100
game_over = False
bg_color = (0, 0, 0,)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))        # создание окна игры
pygame.display.set_caption('My first PyGame')

myimage = pygame.image.load('pygame1.jpg').convert()
myimage = pygame.transform.scale(myimage, (IMG_SIZE, IMG_SIZE))   #уменшает картинку до 100х100


x = 200
y = 200

move_right = False      #чтобы при зажатии клавиши было движение (раньше) x, y -/+= 20
move_left = False
move_up = False
move_down = False

while game_over == False:
    for event in pygame.event.get():         # считывает все события в игре (нажатие клавиш, мышки...)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:     # при нажатии клавиши задаеться значение
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:       #при отжатии клавиши значения
            if event.key == pygame.K_ESCAPE:
                game_over = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_left == True:      #для движения при нажатии
        x = x-0.3
        if x < 0:           #чтобы не уходил за экран
            x = 0

    if move_right == True:
        x = x+0.3
        if x > MAX_X - IMG_SIZE:
            x = MAX_X - IMG_SIZE

    if move_up == True:
        y = y-0.3
        if y < 0:
            y = 0

    if move_down == True:
        y = y + 0.3
        if y > MAX_Y - IMG_SIZE:
            y = MAX_Y - IMG_SIZE


    if event.type == pygame.MOUSEBUTTONDOWN:    #перемещение картинки за мышкой
            x, y = event.pos

    screen.fill(bg_color)                    # заливка фона цветом для удаления следа картинки
    screen.blit(myimage, (x, y))             # размещение картинки на поле
    pygame.display.flip()                    # выводит на экран
