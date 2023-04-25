
import chess
import time

#########################
# Chess Environment
#########################
N = 8
E = 1
S = -8
W = -1
directions_a1 = {#a1
    "P": {N, N+E, N+N, N+W}, # pawn will be dealt with on class since it depends on other things
    "N": {N+N+E, N+E+E}, # knight
    "B": {N+E:7}, #length of movement will be dealt inside class since it depends on other things
    "R": {N:7, E:7},
    "Q": {N:7, E:7, N+E:7},
    "K": {N, E, N+E},}
directions_b1 = { #b1
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, N+N+W},
    "B": {N+E:6, N+W:1},
    "R": {N:7, E:6, W:1},
    "Q": {N:7, E:6, N+E:6, N+W:1, W:1},
    "K": {N, E, N+E, N+W, W},}
directions_a2 = { #a2
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E},
    "B": {N+E:6, S+E:1},
    "R": {N:6, E:7, S:1},
    "Q": {N:6, E:7, N+E:6, S:1, S+E:1},
    "K": {N, E, N+E, S, S+E},}
directions_c1 = { #c1
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, N+N+W, N+W+W},
    "B": {N+E:5, N+W:2},
    "R": {N:7, E:5, W:2},
    "Q": {N:7, E:5, N+E:5, W:2, N+W:2},
    "K": {N, E, N+E, W, N+W},}
directions_d1 = { #d1
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, N+N+W, N+W+W},
    "B": {N+E:4, N+W:3},
    "R": {N:7, E:4, W:3},
    "Q": {N:7, E:4, N+E:4, W:3, N+W:3},
    "K": {N, E, N+E, W, N+W},}
directions_a3 = { #a3
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+S+E},
    "B": {N+E:5, S+E:2},
    "R": {N:5, E:7, S:2},
    "Q": {N:5, E:7, N+E:5, S:2, S+E:2},
    "K": {N, E, N+E, S, S+E},}
directions_a4 = { #a4
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+S+E},
    "B": {N+E:4, S+E:3},
    "R": {N:4, E:7, S:3},
    "Q": {N:4, E:7, N+E:4, S:3, S+E:3},
    "K": {N, E, N+E, S, S+E},}
directions_b2 = { #b2
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+N+W, N+E+E, S+E+E},
    "B": {N+E:6, N+W:1, S+E:1, S+W:1},
    "R": {N:6, E:6, S:1, W:1},
    "Q": {N:6, E:6, S:1, W:1, N+E:6, S+E:1, S+W:1, N+W:1},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_b3 = { #b3
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+N+W, N+E+E, S+E+E, S+S+E, S+S+W},
    "B": {N+E:5, N+W:1, S+E:2, S+W:1},
    "R": {N:5, E:6, S:2, W:1},
    "Q": {N:5, E:6, S:2, W:1, N+E:5, S+E:2, S+W:1, N+W:1},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_c2 = { #c2
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E,N+N+W, N+E+E, S+E+E, N+W+W, S+W+W},
    "B": {N+E:5, N+W:2, S+E:1, S+W:1},
    "R": {N:6, E:5, S:1, W:2},
    "Q": {N:6, E:5, S:1, W:2, N+E:5, S+E:1, S+W:1, N+W:2},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_c3 = { #centre squares c3
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+S+E, S+S+W, S+W+W, N+W+W, N+N+W},
    "B": {N+E:5, N+W:2, S+E:2, S+W:2},
    "R": {N:5, E:5, S:2, W:2},
    "Q": {N:5, E:5, S:2, W:2, N+E:5, S+E:2, S+W:2, N+W:2},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_d3 = { #centre squares d3
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+S+E, S+S+W, S+W+W, N+W+W, N+N+W},
    "B": {N+E:4, N+W:3, S+E:2, S+W:2},
    "R": {N:5, E:4, S:2, W:3},
    "Q": {N:5, E:4, S:2, W:3, N+E:4, S+E:2, S+W:2, N+W:3},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_c4 = { #centre squares c4
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+S+E, S+S+W, S+W+W, N+W+W, N+N+W},
    "B": {N+E:4, N+W:2, S+E:3, S+W:2},
    "R": {N:4, E:5, S:3, W:2},
    "Q": {N:4, E:5, S:3, W:2, N+E:4, S+E:3, S+W:2, N+W:2},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_d4 = { #centre squares d4
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+S+E, S+S+W, S+W+W, N+W+W, N+N+W},
    "B": {N+E:4, N+W:3, S+E:3, S+W:3},
    "R": {N:4, E:4, S:3, W:3},
    "Q": {N:4, E:4, S:3, W:3, N+E:4, S+E:3, S+W:3, N+W:3},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_b4 = { #b4
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+S+E, S+S+W, N+N+W},
    "B": {N+E:4, N+W:1, S+E:3, S+W:1},
    "R": {N:4, E:7, S:3, W:1},
    "Q": {N:4, E:7, S:3, W:1, N+E:4, S+E:3, S+W:1, N+W:1},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}
directions_d2 = { #d2
    "P": {N, N+E, N+N, N+W},
    "N": {N+N+E, N+E+E, S+E+E, S+W+W, N+W+W, N+N+W},
    "B": {N+E:4, N+W:3, S+E:1, S+W:1},
    "R": {N:6, E:4, S:1, W:3},
    "Q": {N:6, E:4, S:1, W:3, N+E:4, S+E:1, S+W:1, N+W:3},
    "K": {N, E, S, W, N+E, S+E, S+W, N+W},}

DirectionsDict = {0: directions_a1, 1: directions_b1,
                  8: directions_a2, 2: directions_c1, 3:directions_d1,
                  16: directions_a3, 24: directions_a4, 9: directions_b2,
                  17: directions_b3, 25: directions_b4, 10: directions_c2,
                  11: directions_d2, 18: directions_c3, 19: directions_d3,
                  26: directions_c4, 27: directions_d4}
board = [ 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R',
         'P', 'P', 'r', 'P', 'klk', 'P', 'P', 'P',
         '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '0', 'k', '0', '0', '0', '0', '0',
         '0', '0', '0', '0', '0', '0', '0', '0',
         '0', '2', 'm', '0', '0', '0', '0', '0',
         'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
         'r', 'n', 'b', 'q', 'k', 'b', 'n', 'k' ]

# Position Class
from collections import namedtuple
from collections import Counter

Move = namedtuple("Move", "i j prom score")  # The Move class is a named tuple that stores information about a
# move in the chess game. It has three fields: i and j, which are
# the starting and ending positions of the piece being moved, respectively,
# and prom, which is the promotion piece if the move is a pawn promotion.
# and score +2 captures
# +1 checks
import copy


class Position:
    def __init__(self, board, psquare, wc, bc, history,
                 turn):  # When creating a Position we will have to specify these variables
        self.board = board  # an array of length 64
        self.psquare = psquare  # An integer representing the square that can be captured using en passant.
        # It will be -1 if the last move wasn't a double pawn move.
        # I will change the passant variable every time a double pawn move is made in
        # the move method.
        self.wc = wc
        self.bc = bc  # The castling rights, these will be lists of two Boolean variables. The first element
        # of the list represents kingside castle, the second queenside castle. They only check
        # if the king or rook has already moved (to check if there are in between checks we do
        # it in gen_moves method).
        self.history = [''.join(self.board)]
        self.turn = turn  # True if white, False if black

    def checks_pins(self):
        checks = [0]
        pins = {}
        for square, piece in enumerate(self.board):
            if piece not in 'prqnb':  # We check for all opponents pieces that can give checks (not kings)
                continue
            downwards = False
            flipsquare = square  # flipsquare is the corresponding square in the first quarterboard
            flipsquarelist = list(range(64))
            flipboard = self.board
            if any(square in range(start, start + 4) for start in [4, 12, 20, 28]):
                # h1 quadrant
                flipboard = [square for row in [self.board[i:i + 8][::-1] for i in range(0, 64, 8)] for square in row]
                flipsquarelist = [square for row in [list(range(64))[i:i + 8][::-1] for i in range(0, 64, 8)] for square
                                  in row]
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [36, 44, 52, 60]):  # h8 quadrant
                # Quadrant h8
                downwards = True
                flipboard = list(reversed(self.board))  # Flip the board pieces horizontally
                flipsquarelist = list(reversed(range(64)))  # correct
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [32, 40, 48, 56]):  # a8 quadrant
                # Quadrant a8
                downwards = True
                flipboard = [square for row in [self.board[i:i + 8] for i in range(0, 64, 8)][::-1] for square in row]
                flipsquarelist = [square for row in [list(range(64))[::-1][i:i + 8][::-1] for i in range(0, 64, 8)] for
                                  square in row]
                flipsquare = flipsquarelist[square]
            if piece in 'rqb':  # Opponents sliders
                for d in DirectionsDict[flipsquare][piece.upper()].keys():
                    squareslist = [square]
                    count = 0
                    outer_break = False
                    for k in range(DirectionsDict[flipsquare][piece.upper()][d]):
                        jflip = flipsquare + (k + 1) * d
                        j = flipsquarelist[jflip]
                        q = flipboard[jflip]  # What is on destination square
                        if q.islower():  # Own piece is blocking
                            break
                        if q.isupper() and q != 'K':
                            count += 1
                            pinned_square = j
                        if count >= 2:
                            break
                        if q == 'K':
                            outer_break = True  # No need to check for other directions
                            if count == 0:
                                checks[0] += 1
                                checks.append(squareslist)
                            else:
                                pins[pinned_square] = squareslist
                            break
                        squareslist.append(j)
                    if outer_break:
                        break
            else:  # Opponents Crawlers
                for d in DirectionsDict[flipsquare][piece.upper()]:
                    if piece == 'p' and (d == N or d == N + N):
                        continue
                    if piece == 'p' and not downwards:
                        if d == 7:
                            d = -9
                        if d == 9:
                            d = -7
                    jflip = flipsquare + d
                    j = flipsquarelist[jflip]
                    q = self.board[j]  # What is on destination square
                    if q == 'K':
                        checks[0] += 1
                        checks.append([square])
        return [checks, pins]

    def own_attacked_squares(self):  # Getting the squares where our pieces are being attacked
        attacked_squares = []
        for square, piece in enumerate(self.board):
            if piece not in 'prqnbk':  # We check for all opponents pieces
                continue
            downwards = False
            flipsquare = square  # flipsquare is the corresponding square in the first quarterboard
            flipsquarelist = list(range(64))
            flipboard = self.board
            if any(square in range(start, start + 4) for start in [4, 12, 20, 28]):
                # h1 quadrant
                flipboard = [square for row in [self.board[i:i + 8][::-1] for i in range(0, 64, 8)] for square in row]
                flipsquarelist = [square for row in [list(range(64))[i:i + 8][::-1] for i in range(0, 64, 8)] for square
                                  in row]
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [36, 44, 52, 60]):  # h8 quadrant
                # Quadrant h8
                downwards = True
                flipboard = list(reversed(self.board))  # Flip the board pieces horizontally
                flipsquarelist = list(reversed(range(64)))  # correct
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [32, 40, 48, 56]):  # a8 quadrant
                # Quadrant a8
                downwards = True
                flipboard = [square for row in [self.board[i:i + 8] for i in range(0, 64, 8)][::-1] for square in row]
                flipsquarelist = [square for row in [list(range(64))[::-1][i:i + 8][::-1] for i in range(0, 64, 8)] for
                                  square in row]
                flipsquare = flipsquarelist[square]
            if piece in 'rqb':  # Opponents sliders
                for d in DirectionsDict[flipsquare][piece.upper()].keys():
                    for k in range(DirectionsDict[flipsquare][piece.upper()][d]):
                        jflip = flipsquare + (k + 1) * d
                        j = flipsquarelist[jflip]
                        q = flipboard[jflip]  # What is on destination square
                        if q.islower():  # Own piece is blocking
                            break
                        if q.isupper() and q != 'P':
                            attacked_squares.append(j)
            else:  # Opponents Crawlers
                for d in DirectionsDict[flipsquare][piece.upper()]:
                    d1 = d
                    if piece == 'p' and not downwards:
                        if d == 7:
                            d1 = -9
                        if d == 9:
                            d1 = -7
                        if d == 8:
                            continue
                    jflip = flipsquare + d1
                    j = flipsquarelist[jflip]
                    q = self.board[j]  # What is on destination square
                    if q.isupper() and q != 'P':
                        attacked_squares.append(j)
        return attacked_squares

    def out_of_attack_moves(self):
        score = 0
        checks_pins = self.checks_pins()
        checks = checks_pins[0]
        pins = checks_pins[1]
        for square, piece in enumerate(self.board):
            attacked_squares = self.own_attacked_squares()
            # MAYBE INSTEAD OF CREATING FLIPBOARD AND FLIPSQUARE WE CAN CREATE A FOR LOOP, RUNNING THROUGH
            # THE DIRECTIONS ON EACH OF THE 4 BY 4 QUARTERBOARDS, I WILL CHECK WHEN FINISHED IF THIS IS MORE
            # EFFICIENT(MAYBE BECAUSE LESS MEMORY USAGE?).
            if not piece.isupper():  # We only check for white pieces(rotation will allow then to check for black)
                continue
            if square not in attacked_squares and checks[0] == 0:
                continue
            downwards = False
            flipsquare = square  # flipsquare is the corresponding square in the first quarterboard
            flipsquarelist = list(range(64))
            flipboard = self.board
            if any(square in range(start, start + 4) for start in [4, 12, 20, 28]):
                # h1 quadrant
                flipboard = [square for row in [self.board[i:i + 8][::-1] for i in range(0, 64, 8)] for square in row]
                flipsquarelist = [square for row in [list(range(64))[i:i + 8][::-1] for i in range(0, 64, 8)] for square
                                  in row]
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [36, 44, 52, 60]):  # h8 quadrant
                # Quadrant h8
                downwards = True
                flipboard = list(reversed(self.board))  # Flip the board pieces horizontally
                flipsquarelist = list(reversed(range(64)))  # correct
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [32, 40, 48, 56]):  # a8 quadrant
                # Quadrant a8
                downwards = True
                flipboard = [square for row in [self.board[i:i + 8] for i in range(0, 64, 8)][::-1] for square in row]
                flipsquarelist = [square for row in [list(range(64))[::-1][i:i + 8][::-1] for i in range(0, 64, 8)] for
                                  square in row]
                flipsquare = flipsquarelist[square]
            if piece in 'RQB' and checks[0] == 0:  # Sliders without checks
                for d in DirectionsDict[flipsquare][piece].keys():
                    for k in range(DirectionsDict[flipsquare][piece][d]):
                        jflip = flipsquare + (k + 1) * d
                        j = flipsquarelist[jflip]
                        if square in pins.keys():  # If piece is pinned we can only move through pin
                            if j not in pins[square]:
                                break
                        q = flipboard[jflip]  # What is on destination square
                        # Castling, by sliding the rook next to the king
                        if q.isupper():
                            break  # we cant move if our own piece is blocking
                        yield Move(square, j, "", score)
                        # Captures prevent more moves in that direction
                        if q.islower():  # Capture prevent more moves in that direction
                            break
            elif piece in 'NK' and checks[0] == 0:  # Crawlers without checks
                for d in DirectionsDict[flipsquare][piece]:
                    jflip = flipsquare + d
                    j = flipsquarelist[jflip]
                    if square in pins.keys():  # If piece is pinned we can only move through pin
                        if j not in pins[square]:
                            continue
                    if piece == 'K':  # Making sure we dont move the king in check
                        if self.null_move(Move(square, j, '', score)).rotate().checks_pins()[0][0] != 0:
                            continue
                    q = self.board[j]  # What is on destination square
                    if q.isupper():
                        continue  # we cant move if our own piece is blocking
                    yield Move(square, j, "", score)

            elif piece in 'QRB' and checks[0] == 1:  # In 1 check, Sliders can be captured, blocked or move king
                if square in pins.keys():  # If check, pinned pieces cant move
                    continue
                for d in DirectionsDict[flipsquare][piece].keys():
                    for k in range(DirectionsDict[flipsquare][piece][d]):
                        jflip = flipsquare + (k + 1) * d
                        j = flipsquarelist[jflip]
                        q = flipboard[jflip]  # What is on destination square
                        if q.isupper():  # we cant move more in that direction
                            break
                        if j not in checks[1]:
                            continue  # We don't interfere with check
                        yield Move(square, j, '', score)
            elif piece in 'NPK' and checks[0] == 1:  # In 1 check, Only capture or move king
                if square in pins.keys():  # If check, pinned pieces cant move
                    continue
                for d in DirectionsDict[flipsquare][piece]:
                    if piece == 'P' and downwards:
                        if d == 7:
                            d = -9
                        if d == 9:
                            d = -7
                        if d == 8:
                            d = -8
                    jflip = flipsquare + d
                    j = flipsquarelist[jflip]
                    if j not in checks[1] and piece != 'K':
                        continue
                    if piece == 'K':  # Making sure we dont move the king in check
                        if self.null_move(Move(square, j, '', score)).rotate().checks_pins()[0][0] != 0:
                            continue
                    q = self.board[j]  # What is on destination square
                    if q.isupper():
                        continue
                    if piece == "P":  # Pawn move, double move and capture
                        if d in (N, N + N) and q != "0":  # can't move
                            continue
                        if d in (N + N, -N - N) and (
                                square > 15 or flipboard[flipsquare + N] != "0"):  # can't move twice
                            continue
                        if (d in (N + W, N + E, -N - W, -N - E) and (q == "0" and self.psquare != j)):
                            continue  # Can't capture or en passant
                        if 56 <= j:  # If we move to the last row, we can promote
                            for prom in "NBRQ":
                                yield Move(square, j, prom, score)
                                continue
                    yield Move(square, j, '', score)
            else:  # There are multiple checks so we may only move king
                if piece != 'K':
                    continue
                for d in DirectionsDict[flipsquare]['K']:
                    jflip = flipsquare + d
                    j = flipsquarelist[jflip]
                    if piece == 'K':  # Making sure we dont move the king in check
                        if self.null_move(Move(square, j, '', score)).rotate().checks_pins()[0][0] != 0:
                            continue
                    q = self.board[j]
                    if q.isupper():
                        continue
                    yield Move(square, j, '', score)

    def gen_moves(self):
        # The gen_moves method generates all legal moves for the current position, and returns
        # a generator that yields Move objects. It iterates through each of the player's pieces
        # on the board and, for each piece, iterates through each possible 'ray' of moves, as
        # defined in the directions map. The rays are broken by captures or immediately in the
        # case of crawlers such as knights.
        checks_pins = self.checks_pins()
        checks = checks_pins[0]
        pins = checks_pins[1]
        for square, piece in enumerate(self.board):
            # MAYBE INSTEAD OF CREATING FLIPBOARD AND FLIPSQUARE WE CAN CREATE A FOR LOOP, RUNNING THROUGH
            # THE DIRECTIONS ON EACH OF THE 4 BY 4 QUARTERBOARDS, I WILL CHECK WHEN FINISHED IF THIS IS MORE
            # EFFICIENT(MAYBE BECAUSE LESS MEMORY USAGE?).
            if not piece.isupper():  # We only check for white pieces(rotation will allow then to check for black)
                continue
            downwards = False
            flipsquare = square  # flipsquare is the corresponding square in the first quarterboard
            flipsquarelist = list(range(64))
            flipboard = self.board
            if any(square in range(start, start + 4) for start in [4, 12, 20, 28]):
                # h1 quadrant
                flipboard = [square for row in [self.board[i:i + 8][::-1] for i in range(0, 64, 8)] for square in row]
                flipsquarelist = [square for row in [list(range(64))[i:i + 8][::-1] for i in range(0, 64, 8)] for square
                                  in row]
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [36, 44, 52, 60]):  # h8 quadrant
                # Quadrant h8
                downwards = True
                flipboard = list(reversed(self.board))  # Flip the board pieces horizontally
                flipsquarelist = list(reversed(range(64)))  # correct
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [32, 40, 48, 56]):  # a8 quadrant
                # Quadrant a8
                downwards = True
                flipboard = [square for row in [self.board[i:i + 8] for i in range(0, 64, 8)][::-1] for square in row]
                flipsquarelist = [square for row in [list(range(64))[::-1][i:i + 8][::-1] for i in range(0, 64, 8)] for
                                  square in row]
                flipsquare = flipsquarelist[square]
            if piece in 'RQB' and checks[0] == 0:  # Sliders without checks
                for d in DirectionsDict[flipsquare][piece].keys():
                    for k in range(DirectionsDict[flipsquare][piece][d]):
                        score = 0
                        jflip = flipsquare + (k + 1) * d
                        j = flipsquarelist[jflip]
                        if square in pins.keys():  # If piece is pinned we can only move through pin
                            if j not in pins[square]:
                                break
                        q = flipboard[jflip]  # What is on destination square
                        if q.islower():
                            score += 1  # capture gets a score
                            if q != 'p':
                                score += 1
                        if self.null_move(Move(square, j, '', 0)).checks_pins()[0][0] != 0:
                            score += 3  # Checks get a score

                        # Castling, by sliding the rook next to the king
                        if square == 0 and self.wc[1] and q == 'K':
                            position2 = self
                            if self.null_move(Move(j + E, j, '', 0)).rotate().checks_pins()[0][0] != 0 or \
                                    position2.null_move(Move(j + E, j + W, '', 0)).rotate().checks_pins()[0][0] != 0:
                                break
                            yield Move(j + E, j + W, "", score)  # castling is represented by the king move (makes
                            # move method easier)
                            break
                        if square == 7 and self.wc[0] and q == 'K':
                            position2 = self
                            if self.null_move(Move(j + W, j, '', 0)).rotate().checks_pins()[0][0] != 0 or \
                                    position2.null_move(Move(j + W, j + E, '', 0)).rotate().checks_pins()[0][0] != 0:
                                break
                            yield Move(j + W, j + E, "", score)
                            break
                        if q.isupper():
                            break  # we cant move if our own piece is blocking
                        yield Move(square, j, "", score)
                        # Captures prevent more moves in that direction
                        if q.islower():  # Capture prevent more moves in that direction
                            break
            elif piece in 'NKP' and checks[0] == 0:  # Crawlers without checks
                for d in DirectionsDict[flipsquare][piece]:
                    score = 0
                    if piece == 'P' and downwards:
                        if d == 7:
                            d = -9
                        if d == 9:
                            d = -7
                        if d == 8:
                            d = -8
                    jflip = flipsquare + d
                    j = flipsquarelist[jflip]
                    if square in pins.keys():  # If piece is pinned we can only move through pin
                        if j not in pins[square]:
                            continue
                    if piece == 'K':  # Making sure we dont move the king in check
                        if self.null_move(Move(square, j, '', score)).rotate().checks_pins()[0][0] != 0:
                            continue
                    q = self.board[j]  # What is on destination square
                    if q.isupper():
                        continue  # we cant move if our own piece is blocking
                    if piece == "P":  # Pawn move, double move and capture
                        if d in (N, N + N, -N, -N - N) and q != "0":  # can't move
                            continue
                        if d in (N + N, -N - N) and (
                                square > 15 or flipboard[flipsquare + N] != "0"):  # can't move twice
                            continue
                        if (d in (7, -7, 9, -9) and (q == "0" and self.psquare != j)):
                            continue  # Can't capture or en passant
                        if 56 <= j:  # If we move to the last row, we can promote
                            for prom in "NBRQ":
                                yield Move(square, j, prom, score)
                            continue
                        if self.psquare == j and d in (N + W, N + E, -N - W,
                                                       -N - E):  # Sometimes we cant enpassant because otherwise we are in check, however the pawn is not pinned
                            if self.null_move(Move(square, j, '', 0)).rotate().checks_pins()[0][0] != 0:
                                continue

                    if q.islower() or j == self.psquare:
                        score += 1
                        if q != 'p':
                            score += 1

                    if self.null_move(Move(square, j, '', 0)).checks_pins()[0][0] != 0:
                        score += 3  # Checks get a score
                    yield Move(square, j, "", score)

            elif piece in 'QRB' and checks[0] == 1:  # In 1 check, Sliders can be captured, blocked or move king
                if square in pins.keys():  # If check, pinned pieces cant move
                    continue
                for d in DirectionsDict[flipsquare][piece].keys():
                    for k in range(DirectionsDict[flipsquare][piece][d]):
                        score = 0
                        jflip = flipsquare + (k + 1) * d
                        j = flipsquarelist[jflip]
                        q = flipboard[jflip]  # What is on destination square
                        if q.isupper():  # we cant move more in that direction
                            break
                        if j not in checks[1]:
                            continue  # We don't interfere with check
                        if q.islower():
                            score += 1
                            if q != 'p':
                                score += 1
                        yield Move(square, j, '', score)
            elif piece in 'NPK' and checks[0] == 1:  # In 1 check, Only capture or move king
                if square in pins.keys():  # If check, pinned pieces cant move
                    continue
                for d in DirectionsDict[flipsquare][piece]:
                    score = 0
                    if piece == 'P' and downwards:
                        if d == 7:
                            d = -9
                        if d == 9:
                            d = -7
                        if d == 8:
                            d = -8
                    jflip = flipsquare + d
                    j = flipsquarelist[jflip]
                    if j not in checks[1] and piece != 'K' and piece != 'P':
                        continue  # King can move out of check and en passant can capture pawn giving check without moving to pawns square
                    if piece == 'P' and j not in checks[1] and j != self.psquare:
                        continue  # unless en passant, if we cant capture piece directly or block we cant move pawn
                    if piece == 'P' and j == self.psquare:
                        if self.null_move(Move(square, j, '', score)).rotate().checks_pins()[0][0] != 0:
                            print('MAL')
                            continue  # If we capture en passant we see if we are in check after capturing
                    if piece == 'K':  # Making sure we dont move the king in check
                        if self.null_move(Move(square, j, '', score)).rotate().checks_pins()[0][0] != 0:
                            continue
                    q = self.board[j]  # What is on destination square
                    if q.isupper():
                        continue
                    if q.islower():
                        score += 1
                        if q != 'p':
                            score += 1
                    if piece == "P":  # Pawn move, double move and capture
                        if d in (N, N + N) and q != "0":  # can't move
                            continue
                        if d in (N + N, -N - N) and (
                                square > 15 or flipboard[flipsquare + N] != "0"):  # can't move twice
                            continue
                        if (d in (N + W, N + E, -N - W, -N - E) and (q == "0" and self.psquare != j)):
                            continue  # Can't capture or en passant
                        if 56 <= j:  # If we move to the last row, we can promote
                            for prom in "NBRQ":
                                yield Move(square, j, prom, score)
                            continue
                    yield Move(square, j, '', score)
            else:  # There are multiple checks so we may only move king
                if piece != 'K':
                    continue
                for d in DirectionsDict[flipsquare]['K']:
                    score = 0
                    jflip = flipsquare + d
                    j = flipsquarelist[jflip]
                    if piece == 'K':  # Making sure we dont move the king in check
                        if self.null_move(Move(square, j, '', score)).rotate().checks_pins()[0][0] != 0:
                            continue
                    q = self.board[j]
                    if q.isupper():
                        continue
                    if q.islower():
                        score += 1
                        if q != 'p':
                            score += 1
                    yield Move(square, j, '', score)

    def own_quiet(self):
        checks_pins = self.checks_pins()
        checks = checks_pins[0]
        pins = checks_pins[1]
        if checks[0] != 0:  # If there is a check, position isn't quiet
            return False
        for square, piece in enumerate(self.board):
            if not piece.isupper():  # We only check for our own pieces
                continue
            downwards = False
            flipsquare = square  # flipsquare is the corresponding square in the first quarterboard
            flipsquarelist = list(range(64))
            flipboard = self.board
            if any(square in range(start, start + 4) for start in [4, 12, 20, 28]):
                # Quadrant h1
                flipboard = [square for row in [self.board[i:i + 8][::-1] for i in range(0, 64, 8)] for square in row]
                flipsquarelist = [square for row in [list(range(64))[i:i + 8][::-1] for i in range(0, 64, 8)] for square
                                  in row]
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [36, 44, 52, 60]):
                # Quadrant h8
                downwards = True
                flipboard = list(reversed(self.board))  # Flip the board pieces horizontally
                flipsquarelist = list(reversed(range(64)))  # correct
                flipsquare = flipsquarelist[square]
            elif any(square in range(start, start + 4) for start in [32, 40, 48, 56]):
                # Quadrant a8
                downwards = True
                flipboard = [square for row in [self.board[i:i + 8] for i in range(0, 64, 8)][::-1] for square in row]
                flipsquarelist = [square for row in [list(range(64))[::-1][i:i + 8][::-1] for i in range(0, 64, 8)] for
                                  square in row]
                flipsquare = flipsquarelist[square]
            if piece in 'RQB':  # Our sliders
                for d in DirectionsDict[flipsquare][piece].keys():
                    for k in range(DirectionsDict[flipsquare][piece][d]):
                        jflip = flipsquare + (k + 1) * d
                        j = flipsquarelist[jflip]
                        if square in pins.keys():  # If piece is pinned we can only move through pin
                            if j not in pins[square]:
                                break
                        q = flipboard[jflip]  # What is on destination square
                        if q.isupper():  # We cant move more in that direction
                            break
                        if q.islower() and q != 'p':  # we can capture a piece
                            return False
                        if q == 'p':
                            break

            if piece in 'KNP':  # Our crawlers
                for d in DirectionsDict[flipsquare][piece]:
                    if piece == 'P' and (d == N or d == N + N):
                        continue  # We cant capture with pawns moving upwards
                    d1 = d
                    if piece == 'P' and downwards:
                        if d == 7:
                            d1 = -9
                        if d == 9:
                            d1 = -7
                    jflip = flipsquare + d1
                    j = flipsquarelist[jflip]
                    if square in pins.keys():  # If piece is pinned we can only move through pin
                        if j not in pins[square]:
                            break
                    q = flipboard[jflip]
                    if q.islower() and q != 'p':
                        return False
        return True

    def rotate(self):
        # Switch the roles of black and white. It also swaps the case of all the pieces and preserves
        # en passant unless it is a null move. White's castling rights become black's and viceversa.
        return Position([x.swapcase() for x in self.board[::-1]], self.psquare, self.bc, self.wc, self.history,
                        self.turn)

    def null_move(self, move):
        # Null move doesnt change actual position, it only creates a new position, where the only
        # thing changing is the board, it makes a move and changes players perspective
        position_copy = copy.deepcopy(self)
        i, j, prom, capt = move  # prom is the letter representing the piece we are promoting to
        piece, q, board = position_copy.board[i], position_copy.board[
            j], position_copy.board  # piece and destination piece/space
        wc, bc = position_copy.wc, position_copy.bc
        put = lambda board, i, p: board[:i] + [p] + board[i + 1:]
        newpsquare, newwc, newbc = -1, position_copy.wc, position_copy.bc
        # Actual move
        newboard = put(position_copy.board, j, position_copy.board[i])
        newboard = put(newboard, i, "0")
        # If we move the rook or capture the opponent's the castling rights are lost
        if i == 0: wc = (False, wc[1])
        if i == 7: wc = (wc[0], False)
        if j == 56: bc = (bc[0], False)
        if j == 63: bc = (False, bc[1])
        # Castling
        if piece == "K":
            wc = (False, False)  # if king moves then player can't castle
            if abs(j - i) == 2:  # if castling... ¡¡¡ARREGLAR ESTO!!!
                newboard = put(newboard, 0 if j < i else 7, "0")
                newboard = put(newboard, 2 if j < i else 4, "R")
        # Pawn promotion, double move and en passant capture
        if piece == "P":
            if 56 <= j:
                newboard = put(newboard, j, prom)  # changing the pawn to the promoting piece
            if j - i == N + N:  # If we move pawn two squares, the enpassant square becomes...
                newpsquare = list(range(64))[i + N]
            if j == position_copy.psquare:  # If we capture en passant
                newboard = put(newboard, j + S, "0")
        # We rotate the returned position, so it's ready for the next player
        # Making a move will change the actual position object
        # This will later make code more memory efficient
        newboard = [x.swapcase() for x in newboard[::-1]]
        return Position(newboard, newpsquare, newwc, newbc, position_copy.history, position_copy.turn)

    def opponent_quiet(self):
        opponent_position = self
        return opponent_position.rotate().own_quiet()

    def move(self, move):
        # The move method takes a Move object as an argument and returns a new Position
        # object representing the state of the game after the move has been made. It first
        # checks if the move is castling, pawn promotion, or en passant, and updates the
        # board accordingly. It then updates the castling rights and en passant square if
        # necessary, and rotates the board to return a new Position object.
        i, j, prom, capt = move  # prom is the letter representing the piece we are promoting to
        piece, q, board = self.board[i], self.board[j], self.board  # piece and destination piece/space
        wc, bc = self.wc, self.bc
        put = lambda board, i, p: board[:i] + [p] + board[i + 1:]
        newpsquare, newwc, newbc = -1, self.wc, self.bc
        # Actual move
        newboard = put(self.board, j, self.board[i])
        newboard = put(newboard, i, "0")
        # If we move the rook or capture the opponent's the castling rights are lost
        if i == 0: wc = (False, wc[1])
        if i == 7: wc = (wc[0], False)
        if j == 56: bc = (bc[0], False)
        if j == 63: bc = (False, bc[1])
        # Castling
        if piece == "K":
            wc = (False, False)  # if king moves then player can't castle
            if abs(j - i) == 2:  # if castling... ¡¡¡ARREGLAR ESTO!!!
                newboard = put(newboard, 0 if j < i else 7, "0")
                newboard = put(newboard, 2 if j < i else 4, "R")
        # Pawn promotion, double move and en passant capture
        if piece == "P":
            if 56 <= j:
                newboard = put(newboard, j, prom)  # changing the pawn to the promoting piece
            if j - i == N + N:  # If we move pawn two squares, the enpassant square becomes...
                newpsquare = list(reversed(range(64)))[i + N]
            if j == self.psquare:  # If we capture en passant
                newboard = put(newboard, j + S, "0")
        # We rotate the returned position, so it's ready for the next player
        if self.turn == True:  # If white has moved
            self.history.append(''.join(newboard))  # Making a move will add the new board to history
        if self.turn == False:  # If black has moved we add board to history from white's perspective
            self.history.append(''.join([x.swapcase() for x in newboard[::-1]]))
        self.turn = not self.turn  # making a move changes turn
        # Making a move will change the actual position object
        # This will later make code more memory efficient
        self.board, self.psquare, self.wc, self.bc = [x.swapcase() for x in newboard[::-1]], newpsquare, newwc, newbc
        return self

    def ordered_moves(self):  # We order legal moves in terms of score
        moves = self.gen_moves()
        return sorted(moves, key=lambda move: move.score, reverse=True)

    def three_fold(self):  # The engine will see repeating a position as evaluation 0
        counted = Counter(self.history)
        if any(count >= 2 for count in counted.values()):
            return True  # 3-fold repetition
        else:
            return False

    def pop(self):  # ¡¡¡ADD ALSO WC BC PSQUARE(AND FOR HISTORY TOO)!!!
        self.history.pop(-1)  # Delete current board from history
        self.turn = not self.turn  # We change turns
        board = list(self.history[-1])
        if self.turn == True:  # If after going back it is white's turn
            self.board = board  # Current board -> last board
        if self.turn == False:
            self.board = [x.swapcase() for x in board[::-1]]  # we want self.board to be from players move perspective
        return self

    def quiet(self):
        if self.own_quiet() and self.opponent_quiet():
            return True
        else:
            return False

###############################
# Evaluation Function
###############################

def evaluate_position_from_fen(fen): # Simple position evaluation to check engine algorithm
    board = chess.Board(fen)
    material_value = {
        "P": 100, "N": 300, "B": 300, "R": 500, "Q": 900,
        "p": -100, "n": -300, "b": -300, "r": -500, "q": -900
    }
    total_material = 0
    for piece in fen.split()[0]:
        if piece in material_value:
            total_material += material_value[piece]
    return total_material

def evaluate_position_from_board(board): # Simple position evaluation to check engine algorithm
    material_value = {
        "P": 100, "N": 300, "B": 300, "R": 500, "Q": 900,
        "p": -100, "n": -300, "b": -300, "r": -500, "q": -900
    }
    total_material = 0
    for square, piece in enumerate(board):
        if piece in material_value:
            total_material += material_value[piece]
    return total_material

####################################
# Search Algorithm
####################################

Squares_Dict = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
                'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
                'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
                'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
                'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
                'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
                'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
                'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']


class Engine:
    def alpha_beta(position, depth, alpha, beta, our_turn):
        ordered_moves = position.ordered_moves()
        if position.three_fold():  # Repetitions
            return 0, 0

        if len(ordered_moves) == 0 and position.checks_pins()[0][0] == 0:  # Stalemate
            return 0, 0

        if len(ordered_moves) == 0 and our_turn:  # Checkmate against us
            return -1003, 0

        if len(ordered_moves) == 0 and not our_turn:  # Checkmate against opponent
            return 1003, 0

        if depth <= 0 and position.quiet() and our_turn:
            return evaluate_position_from_board(position.board), 0

        if depth <= 0 and position.quiet() and not our_turn:
            return -evaluate_position_from_board(position.board), 0

        if depth <= 0 and not position.quiet():  # If depth is reached we continue with captures (not pawns) and
            ordered_moves = [move for move in ordered_moves if move.score >= 2]  # checks until quiet position

        '''if len(ordered_moves)==0 and len(position.own_attacked_squares())>=2:
            print('strange case where king cannot take 1')
            ordered_moves = list(position.out_of_attack_moves())'''

        if len(ordered_moves) == 0 and our_turn:
            return evaluate_position_from_board(position.board), 0

        if len(ordered_moves) == 0 and not our_turn:
            return -evaluate_position_from_board(position.board), 0

        best_move = ordered_moves[0]

        if our_turn:  # If we have to move, we want to maximize. This is ensured by the above
            value1 = -1000  # This is the best evaluation for white in the child_values
            for move in ordered_moves:
                position.move(move)
                child_value = Engine.alpha_beta(position, depth - 1, alpha, beta, False)[0]
                if child_value > value1:
                    value1 = child_value
                    best_move = move
                position.pop()
                if value1 >= beta:
                    break  # Because if our best move is better than the best in another set of moves that lead from
                alpha = max(alpha,
                            value1)  # a different move from opponent, then the opponent will choose the other move.

        else:  # If opponent has to move
            value2 = 1001
            for move in ordered_moves:
                position.move(move)
                child_value = Engine.alpha_beta(position, depth - 1, alpha, beta, True)[0]
                if child_value < value2:
                    value2 = child_value
                    best_move = move
                position.pop()
                if alpha >= value2:  # Because if our opponents best move is better (less than) than the best
                    break  # in another set of moves that lead from a different move from us,
                beta = min(beta, value2)  # then we will choose the other move.
        return (value1, best_move) if our_turn else (value2, best_move)

    def Search(position, is_our_move, depth):
        # alpha is the current best evaluation for white, it will start at -1000
        # beta is the current best evaluation for black, it will start at +1000
        start_time = time.time()
        best_move = None
        if is_our_move:
            alpha = -10000  # Current best evaluation for us
            beta = 10000  # Current best evaluation for opponent
            best_value, best_move = Engine.alpha_beta(position, depth, alpha, beta, True)
            end_time = time.time()
            elapsed_time = end_time - start_time
            return ["Time taken:", elapsed_time, "seconds", "Best move: ", best_move, "Evaluation: ", best_value]
        else:  # Now we make the engine think while it isn't it's turn ¡¡¡ACABAR ESTO!!!
            Dict = {}
            new_position = position.move(move)
            best_move = None
            Dict[move] = (new_engine_position(new_position, is_our_move, depth + 1)[4],
                          new_engine_position(new_position, is_our_move, depth + 1)[6])
            return (Dict)  # This is a dictionary of the form {move: best response, evaluation}

    def Tell_Move(move):  # Spit move to UCI
        square = Squares_Dict[move.i]
        destination = Squares_Dict[move.j]
        return ''.join([square, destination, move.prom])

#######################################
# UCI
#######################################