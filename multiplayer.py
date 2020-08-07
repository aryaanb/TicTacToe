import pygame
from time import sleep
import home

X = pygame.image.load("X.png")
O = pygame.image.load("O.png")
linev = pygame.image.load("line.png")
lineh = pygame.image.load("lineh.png")
line_d1 = pygame.image.load("diagonal1.png")
line_d2 = pygame.image.load("diagonal2.png")
clock = pygame.time.Clock()
turn = 0
playedx = False
game_over = False

class box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hover = False
        self.playx = False
        self.playo = False
        self.played = False
        self.blit = False

    def draw_hover(self, window):
        if self.hover:
            pygame.draw.rect(window, (0, 128, 255), (self.x, self.y, 150, 150), 3)

    def play(self, window):
        global turn, playedx
        if not self.blit:
            if turn % 2 == 0:
                window.blit(X, (self.x, self.y))
                playedx = True
                self.playx = True
            elif turn % 2 != 0 and playedx:
                window.blit(O, (self.x, self.y))
                playedx = False
                self.playo = True
            turn += 1
        self.blit = True


def redraw(window, boxes):
    pygame.draw.line(window, (0, 0, 255), (450 // 3, 0), (450 // 3, 450), 3)
    pygame.draw.line(window, (0, 0, 255), (300, 0), (300, 450), 3)
    pygame.draw.line(window, (0, 0, 255), (0, 450 // 3), (450, 450 // 3), 3)
    pygame.draw.rect(window, (0, 0, 255), (0, 0, 450, 450), 3)
    pygame.draw.line(window, (0, 0, 255), (0, 300), (450, 300), 3)

    for i in range(3):
        for j in range(3):
            if boxes[i][j].played:
                boxes[i][j].play(window)

    for i in range(3):
        for j in range(3):
            if boxes[i][j].hover:
                boxes[i][j].draw_hover(window)

    pygame.display.update()


def game_result(window, boxes):
    global game_over
    if (boxes[0][0].playx and boxes[0][1].playx and boxes[0][2].playx) or (
            boxes[0][0].playo and boxes[0][1].playo and boxes[0][2].playo):
        window.blit(lineh, (20, 60))
        game_over = True
    if (boxes[1][0].playx and boxes[1][1].playx and boxes[1][2].playx) or (
            boxes[1][0].playo and boxes[1][1].playo and boxes[1][2].playo):
        window.blit(lineh, (20, 215))
        game_over = True
    if (boxes[2][0].playx and boxes[2][1].playx and boxes[2][2].playx) or (
            boxes[2][0].playo and boxes[2][1].playo and boxes[2][2].playo):
        window.blit(lineh, (20, 370))
        game_over = True
    if (boxes[0][0].playx and boxes[1][0].playx and boxes[2][0].playx) or (
            boxes[0][0].playo and boxes[1][0].playo and boxes[2][0].playo):
        window.blit(linev, (60, 20))
        game_over = True
    if (boxes[0][1].playx and boxes[1][1].playx and boxes[2][1].playx) or boxes[0][1].playo and boxes[1][1].playo and \
            boxes[2][1].playo:
        window.blit(linev, (210, 20))
        game_over = True
    if (boxes[2][2].playx and boxes[1][2].playx and boxes[0][2].playx) or (
            boxes[2][2].playo and boxes[1][2].playo and boxes[0][2].playo):
        window.blit(linev, (360, 20))
        game_over = True
    if (boxes[0][0].playx and boxes[1][1].playx and boxes[2][2].playx) or (
            boxes[0][0].playo and boxes[1][1].playo and boxes[2][2].playo):
        window.blit(line_d1, (0, 0))
        game_over = True
    if (boxes[0][2].playx and boxes[1][1].playx and boxes[2][0].playx) or (
            boxes[0][2].playo and boxes[1][1].playo and boxes[2][0].playo):
        window.blit(line_d2, (0, 0))
        game_over = True


def main(window):
    global playedx, turn, game_over
    boxes = [
        [box(0, 0), box(150, 0), box(300, 0)],
        [box(0, 150), box(150, 150), box(300, 150)],
        [box(0, 300), box(150, 300), box(300, 300)]
    ]
    run = True
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    window.fill((255, 255, 255))

                    boxes = [
                        [box(0, 0), box(150, 0), box(300, 0)],
                        [box(0, 150), box(150, 150), box(300, 150)],
                        [box(0, 300), box(150, 300), box(300, 300)]
                    ]
                    turn = 0
                    playedx = False
                    game_over = False
                    home.main(window)
                    run = False
        if keys[pygame.K_r]:
            window.fill((255, 255, 255))

            boxes = [
                [box(0, 0), box(150, 0), box(300, 0)],
                [box(0, 150), box(150, 150), box(300, 150)],
                [box(0, 300), box(150, 300), box(300, 300)]
            ]
            turn = 0
            playedx = False
            game_over = False
        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if not game_over:
            if mx < 150 and my < 150:
                boxes[0][0].hover = True
                if click[0] == 1:
                    boxes[0][0].played = True

            if 150 < mx < 300 and my < 150:
                boxes[0][1].hover = True
                if click[0] == 1:
                    boxes[0][1].played = True

            if 300 < mx < 450 and my < 150:
                boxes[0][2].hover = True
                if click[0] == 1:
                    boxes[0][2].played = True

            if 0 < mx < 150 and 150 < my < 300:
                boxes[1][0].hover = True
                if click[0] == 1:
                    boxes[1][0].played = True

            if 150 < mx < 300 and 150 < my < 300:
                boxes[1][1].hover = True
                if click[0] == 1:
                    boxes[1][1].played = True

            if 300 < mx < 450 and 150 < my < 300:
                boxes[1][2].hover = True
                if click[0] == 1:
                    boxes[1][2].played = True

            if 0 < mx < 150 and 300 < my < 450:
                boxes[2][0].hover = True
                if click[0] == 1:
                    boxes[2][0].played = True

            if 150 < mx < 300 and 300 < my < 450:
                boxes[2][1].hover = True
                if click[0] == 1:
                    boxes[2][1].played = True

            if 300 < mx < 450 and 300 < my < 450:
                boxes[2][2].hover = True
                if click[0] == 1:
                    boxes[2][2].played = True
        game_result(window, boxes)
        redraw(window, boxes)

        for i in range(3):
            for j in range(3):
                boxes[i][j].hover = False
