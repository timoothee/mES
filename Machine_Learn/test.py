import pygame
import chess
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)
TEXT_COLOR = (0, 0, 0)

# Piece values for evaluation
PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000  # King has high value but should not be captured
}

# Initialize board
board = chess.Board()
selected_square = None

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Draw board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw pieces as text
def draw_pieces():
    font = pygame.font.Font(None, 36)
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                text = font.render(piece.symbol(), True, TEXT_COLOR)
                screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4))

# Convert mouse position to chess square
def get_square_from_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = 7 - (y // SQUARE_SIZE)
    return chess.square(col, row)

# Evaluate board position
def evaluate_board():
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = PIECE_VALUES.get(piece.piece_type, 0)
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
    return score

# Minimax with alpha-beta pruning
def minimax(depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board()
    
    legal_moves = list(board.legal_moves)
    if maximizing:
        max_eval = -float("inf")
        for move in legal_moves:
            board.push(move)
            eval = minimax(depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in legal_moves:
            board.push(move)
            eval = minimax(depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# AI selects the best move
def ai_move():
    best_move = None
    best_value = -float("inf")
    
    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(3, -float("inf"), float("inf"), False)  # Depth 3 search
        board.pop()
        
        if board_value > best_value:
            best_value = board_value
            best_move = move
    
    if best_move:
        board.push(best_move)

# Main loop
running = True
while running:
    draw_board()
    draw_pieces()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if board.turn == chess.WHITE:
                square = get_square_from_mouse(event.pos)
                if selected_square is None:
                    if board.piece_at(square):
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        ai_move()  # AI moves after the player
                    selected_square = None

pygame.quit()