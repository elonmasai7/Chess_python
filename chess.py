import pygame
import sys
import math
from pieces import Piece
 
class Piece:
       def __init__(self, i, j):
           # Initialize the piece with its position (i, j)
           self.x = i
           self.y = j

pygame.init()

# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set the board size
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

# Set the piece size
PIECE_SIZE = 50

# Set the number of players
NUM_PLAYERS = 2

# Create the game board
board = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Create the pieces
pieces = []
for i in range(NUM_PLAYERS):
    for j in range(BOARD_WIDTH):
        piece = Piece(i, j)
        pieces.append(piece)

# Add the pieces to the board
for piece in pieces:
    board[piece.row][piece.col] = piece

# Set the current player
current_player = 0

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the game loop flag
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_piece.move_up()
            elif event.key == pygame.K_DOWN:
                current_piece.move_down()
            elif event.key == pygame.K_LEFT:
                current_piece.move_left()
            elif event.key == pygame.K_RIGHT:
                current_piece.move_right()

    # Update the game state

    # Check for a winner

    # Render the game画面にオブジェクトを表示
    screen.fill(BLACK)
    for piece in pieces:
        pygame.draw.rect(screen, piece.color, piece.rect)

    # Swap the current player
    current_player = (current_player + 1) % NUM_PLAYERS

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
sys.exit()


class Piece:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = BLUE if row == 0 else RED
        self.rect = pygame.Rect(self.col * PIECE_SIZE, self.row * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE)

    def move_up(self):
        if self.row > 0:
            self.row -= 1
            self.rect.y -= PIECE_SIZE

    def move_down(self):
        if self.row < BOARD_HEIGHT - 1:
            self.row += 1
            self.rect.y += PIECE_SIZE

    def move_left(self):
        if self.col > 0:
            self.col -= 1
            self.rect.x -= PIECE_SIZE

    def move_right(self):
        if self.col < BOARD_WIDTH - 1:
            self.col += 1
            self.rect.x += PIECE_SIZE