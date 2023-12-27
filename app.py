import sys
import math
import pygame
import tkinter
import tkinter.messagebox

pygame.init()

WIDTH, HEIGHT = 300, 300
CELL_SIZE = WIDTH // 3
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
PLAYER_X_COLOR = (255, 0, 0)
PLAYER_O_COLOR = (0, 0, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 36
BUTTON_COLOR = (200, 200, 200)
BUTTON_SELECTED_COLOR = (150, 150, 150)
BOX_COLOR = (220, 220, 220)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.Font(None, FONT_SIZE)

player_score = 0
computer_score = 0

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'O'):
        return -1
    if is_winner(board, 'X'):
        return 1
    if is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move if best_move is not None else (0, 0)  

def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

def draw_symbols(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, PLAYER_X_COLOR, (col * CELL_SIZE, row * CELL_SIZE),
                                 ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), 2)
                pygame.draw.line(screen, PLAYER_X_COLOR, ((col + 1) * CELL_SIZE, row * CELL_SIZE),
                                 (col * CELL_SIZE, (row + 1) * CELL_SIZE), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, PLAYER_O_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 5, 2)

def get_indices_from_mouse(pos):
    return pos[1] // CELL_SIZE, pos[0] // CELL_SIZE

def display_game_over_message(message):
    global player_score, computer_score  
    root = tkinter.Tk()
    root.withdraw()

    result = tkinter.messagebox.askyesno("Game Over", f"{message}\n\n Score: {player_score} - {computer_score}.", icon='warning')

    if result:
        return True
    else:
        pygame.quit()
        sys.exit()


def draw_button(text, rect, button_color, selected_color, selected=False):
    pygame.draw.rect(screen, selected_color if selected else button_color, rect)
    pygame.draw.rect(screen, LINE_COLOR, rect, 2)
    button_text = font.render(text, True, FONT_COLOR)
    screen.blit(button_text, (rect.x + rect.width // 2 - button_text.get_width() // 2,
                              rect.y + rect.height // 2 - button_text.get_height() // 2))

def get_user_symbol():
    x_text = font.render("Play as X", True, FONT_COLOR)
    o_text = font.render("Play as O", True, FONT_COLOR)
    button_width, button_height = max(x_text.get_width(), o_text.get_width()) + 20, x_text.get_height() + 20

    x_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 3 - button_height // 2, button_width, button_height)
    o_rect = pygame.Rect(WIDTH // 2 - button_width // 2, 2 * HEIGHT // 3 - button_height // 2, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if x_rect.collidepoint(mouse_pos):
                    return 'X'
                elif o_rect.collidepoint(mouse_pos):
                    return 'O'

        screen.fill(BG_COLOR)
        draw_button("Play as X", x_rect, (255, 0, 0), BUTTON_SELECTED_COLOR)
        draw_button("Play as O", o_rect, (0, 0, 255), BUTTON_SELECTED_COLOR)
        pygame.display.flip()



if __name__ == "__main__":
    while True:
        player_symbol = get_user_symbol()
        computer_symbol = 'O' if player_symbol == 'X' else 'X'

        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_turn = True
        game_over = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if not game_over:
                    if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                        mouse_pos = pygame.mouse.get_pos()
                        row, col = get_indices_from_mouse(mouse_pos)

                        if board[row][col] == ' ':
                            board[row][col] = player_symbol
                            player_turn = False

            screen.fill(BG_COLOR)
            draw_grid()
            draw_symbols(board)

            if not game_over:
                if not player_turn:
                    computer_row, computer_col = find_best_move(board)
                    board[computer_row][computer_col] = computer_symbol
                    player_turn = True

                if is_winner(board, player_symbol):
                    game_over = True
                    message = "Tu as gagné ! Veux-tu rejouer ?"
                    player_score += 1
                elif is_winner(board, computer_symbol):
                    game_over = True
                    message = "Tu as perdu ! Veux-tu rejouer ?"
                    computer_score += 1
                elif is_board_full(board):
                    game_over = True
                    message = "Nul ! Veux-tu rejouer ?"

            pygame.display.flip()

            if game_over:
                pygame.time.delay(1000)
                screen.fill(BG_COLOR)
                draw_grid()
                draw_symbols(board)
                pygame.display.flip()  
                
                if display_game_over_message(message):
                    player_turn = True
                    game_over = False
                    board = [[' ' for _ in range(3)] for _ in range(3)]
                    break  
                else:
                    player_score = 0
                    computer_score = 0
                    pygame.quit()
                    sys.exit()