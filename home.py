import pygame
from time import sleep
import multiplayer
import comp
pygame.init()
WIDTH = 450
window = pygame.display.set_mode((WIDTH, WIDTH))
window.fill((255, 255, 255))
pygame.display.set_caption("Tic Tac Toe!")
bg = pygame.image.load("bg.png")
against = pygame.image.load("against.png")
multi = pygame.image.load("multi.png")
clock = pygame.time.Clock()
turn = 0
playedx = False


def main(window):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.blit(bg, (0, 0))
        window.blit(multi, (25, 330))
        window.blit(against, (233, 330))
        if 25 < mx < 216 and 330 < my < 440:
            pygame.draw.rect(window, (0, 225, 0), (28, 337, 183, 95), 6)
            if click[0] == 1:
                window.fill((255, 255, 255))
                sleep(0.2)
                multiplayer.main(window)
                run = False
        if 233 < mx < 426 and 330 < my < 440:
            pygame.draw.rect(window, (0, 225, 0), (236, 337, 183, 95), 6)
            if click[0] == 1:
                window.fill((255, 255, 255))
                comp.main(window)
                run = False
        pygame.display.update()


if __name__ == "__main__":
    main(window)
