from math import inf as infinity
import pygame
import home

X = pygame.image.load("images/X.png")
O = pygame.image.load("images/O.png")
linev = pygame.image.load("images/line.png")
lineh = pygame.image.load("images/lineh.png")
line_d1 = pygame.image.load("images/diagonal1.png")
line_d2 = pygame.image.load("images/diagonal2.png")
turn = 0
playedx = False
humanWin = False
compWin = False
game_over = False
clock = pygame.time.Clock()


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


comp = "X"
human = "O"


def game_state(state):
    global humanWin, compWin
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [human, human, human] in win_state:
        return -10
    elif [comp, comp, comp] in win_state:
        return 10
    else:
        return 0


def count_empty(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == "":
                count += 1
    return count


def minimax(newBoard, player, depth, alpha, beta):
    score = game_state(newBoard)
    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if count_empty(newBoard) == 0:
        return 0
    if player == comp:
        best = -infinity
        for i in range(3):
            for j in range(3):
                if newBoard[i][j] == "":
                    newBoard[i][j] = player
                    result = minimax(newBoard, human, depth + 1, alpha, beta)
                    if result > best:
                        best = result
                    alpha = max(best, alpha)
                    newBoard[i][j] = ""

                    if beta <= alpha:
                        break
        return best

    else:
        best = infinity
        for i in range(3):
            for j in range(3):
                if newBoard[i][j] == "":
                    newBoard[i][j] = player
                    result = minimax(newBoard, comp, depth + 1, alpha, beta)
                    if result < best:
                        best = result
                    beta = min(beta, best)
                    newBoard[i][j] = ""
                    if beta <= alpha:
                        break
        return best


def find_best_move(newBoard, player):
    best_val = -infinity
    row = None
    column = None

    for i in range(3):
        for j in range(3):
            if newBoard[i][j] == "":
                newBoard[i][j] = player
                move_val = minimax(newBoard, human, 0, -infinity, infinity)
                newBoard[i][j] = ""
                if move_val > best_val:
                    best_val = move_val
                    row, column = i, j

    return row, column


def main(window):
    global playedx, turn, game_over
    boxes = [
        [box(0, 0), box(150, 0), box(300, 0)],
        [box(0, 150), box(150, 150), box(300, 150)],
        [box(0, 300), box(150, 300), box(300, 300)]
    ]

    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    current_player = human
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
                    board = [["", "", ""],
                             ["", "", ""],
                             ["", "", ""]]
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
            board = [["", "", ""],
                     ["", "", ""],
                     ["", "", ""]]
            game_over = False

        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if turn % 2 != 0 and not game_over:
            if mx < 150 and my < 150:
                boxes[0][0].hover = True
                if click[0] == 1 and not boxes[0][0].played:
                    boxes[0][0].played = True
                    board[0][0] = human
                    current_player = comp

            if 150 < mx < 300 and my < 150:
                boxes[0][1].hover = True
                if click[0] == 1 and not boxes[0][1].played:
                    boxes[0][1].played = True
                    board[0][1] = human
                    current_player = comp

            if 300 < mx < 450 and my < 150:
                boxes[0][2].hover = True
                if click[0] == 1 and not boxes[0][2].played:
                    boxes[0][2].played = True
                    board[0][2] = human
                    current_player = comp

            if 0 < mx < 150 and 150 < my < 300:
                boxes[1][0].hover = True
                if click[0] == 1 and not boxes[1][0].played:
                    boxes[1][0].played = True
                    board[1][0] = human
                    current_player = comp

            if 150 < mx < 300 and 150 < my < 300:
                boxes[1][1].hover = True
                if click[0] == 1 and not boxes[1][1].played:
                    boxes[1][1].played = True
                    board[1][1] = human
                    current_player = comp

            if 300 < mx < 450 and 150 < my < 300:
                boxes[1][2].hover = True
                if click[0] == 1 and not boxes[1][2].played:
                    boxes[1][2].played = True
                    board[1][2] = human
                    current_player = comp

            if 0 < mx < 150 and 300 < my < 450:
                boxes[2][0].hover = True
                if click[0] == 1 and not boxes[2][0].played:
                    boxes[2][0].played = True
                    board[2][0] = human
                    current_player = comp

            if 150 < mx < 300 and 300 < my < 450:
                boxes[2][1].hover = True
                if click[0] == 1 and not boxes[2][1].played:
                    boxes[2][1].played = True
                    board[2][1] = human
                    current_player = comp

            if 300 < mx < 450 and 300 < my < 450:
                boxes[2][2].hover = True
                if click[0] == 1 and not boxes[2][2].played:
                    boxes[2][2].played = True
                    board[2][2] = human
                    current_player = comp

        elif turn % 2 == 0 and not game_over:
            try:
                moves = find_best_move(board, comp)
                boxes[moves[0]][moves[1]].played = True
                board[moves[0]][moves[1]] = comp
            except Exception as e:
                print("GAME OVER")

        game_result(window, boxes)
        redraw(window, boxes)
        for i in range(3):
            for j in range(3):
                boxes[i][j].hover = False
