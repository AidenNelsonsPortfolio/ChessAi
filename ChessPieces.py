knightMoves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]


def getMoves(board, pieceName, square):
    moves = []

    if pieceName[0] == "Q":
        #moves.append(pieceName)

        temp = 1

        while square[0] + temp < 8 and board[square[0] + temp][square[1]] is None:
            moves.append([square[0] + temp, square[1], square[0], square[1]])
            temp += 1

        temp = 1

        while square[0] - temp > -1 and board[square[0] - temp][square[1]] is None:
            moves.append([square[0] - temp, square[1], square[0], square[1]])
            temp += 1

        temp = 1

        while square[1] + temp < 8 and board[square[0]][square[1] + temp] is None:
            moves.append([square[0], square[1] + temp, square[0], square[1]])
            temp += 1

        temp = 1

        while square[1] - temp > -1 and board[square[0]][square[1] - temp] is None:
            moves.append([square[0], square[1] - temp, square[0], square[1]])
            temp += 1

        temp = 1

        while -1 < temp + square[1] < 8 and -1 < temp + square[0] < 8 and board[temp + square[0]][
            square[1] + temp] is None:
            moves.append([square[0] + temp, square[1] + temp, square[0], square[1]])
            temp += 1

        temp = 1

        while -1 < square[1] - temp < 8 and -1 < temp + square[0] < 8 and board[temp + square[0]][
            square[1] - temp] is None:
            moves.append([square[0] + temp, square[1] - temp, square[0], square[1]])
            temp += 1

        temp = 1

        while -1 < square[1] - temp < 8 and -1 < square[0] - temp < 8 and board[square[0] - temp][
            square[1] - temp] is None:
            moves.append([square[0] - temp, square[1] - temp, square[0], square[1]])
            temp += 1

        temp = 1

        while -1 < square[1] + temp < 8 and -1 < square[0] - temp < 8 and board[square[0] - temp][
            square[1] + temp] is None:
            moves.append([square[0] - temp, square[1] + temp, square[0], square[1]])
            temp += 1

        return moves

    elif pieceName[0] == "B":

        #moves.append(pieceName)

        temp = 1
        while -1 < temp + square[1] < 8 and -1 < temp + square[0] < 8 and board[temp + square[0]][
            square[1] + temp] is None:
            moves.append([square[0] + temp, square[1] + temp, square[0], square[1]])
            temp += 1
        temp = 1
        while -1 < square[1] - temp < 8 and -1 < temp + square[0] < 8 and board[temp + square[0]][
            square[1] - temp] is None:
            moves.append([square[0] + temp, square[1] - temp, square[0], square[1]])
            temp += 1
        temp = 1
        while -1 < square[1] - temp < 8 and -1 < square[0] - temp < 8 and board[square[0] - temp][
            square[1] - temp] is None:
            moves.append([square[0] - temp, square[1] - temp, square[0], square[1]])
            temp += 1
        temp = 1
        while -1 < square[1] + temp < 8 and -1 < square[0] - temp < 8 and board[square[0] - temp][
            square[1] + temp] is None:
            moves.append([square[0] - temp, square[1] + temp, square[0], square[1]])
            temp += 1
        return moves



    elif pieceName[0] == "N":
        #moves.append(pieceName)
        for move in knightMoves:
            tempY = square[0] + move[0]
            tempX = square[1] + move[1]
            if -1 < tempY < 8 and -1 < tempX < 8 and board[tempY][tempX] is None:
                moves.append([tempY, tempX, square[0], square[1]])
        return moves


    elif pieceName[0] == "R":
        #moves.append(pieceName)

        temp = 1

        while square[0] + temp < 8 and board[square[0] + temp][square[1]] is None:
            moves.append([square[0] + temp, square[1], square[0], square[1]])
            temp += 1

        temp = 1

        while square[0] - temp > -1 and board[square[0] - temp][square[1]] is None:
            moves.append([square[0] - temp, square[1], square[0], square[1]])
            temp += 1

        temp = 1

        while square[1] + temp < 8 and board[square[0]][square[1] + temp] is None:
            moves.append([square[0], square[1] + temp, square[0], square[1]])
            temp += 1

        temp = 1

        while square[1] - temp > -1 and board[square[0]][square[1] - temp] is None:
            moves.append([square[0], square[1] - temp, square[0], square[1]])
            temp += 1

        return moves


    elif pieceName[0] == "P":

        #moves.append(pieceName)

        if pieceName[1] == 'B':
            maxSquare = 7
            colorDirection = 1

        else:
            maxSquare = 0
            colorDirection = -1

        if (square[0] * colorDirection) < maxSquare and board[square[0] + colorDirection][square[1]] is None:
            moves.append([square[0] + colorDirection, square[1], square[0], square[1]])

        if pieceName[3] == 'T' and board[square[0] + (colorDirection * 2)][square[1]] is None:
            moves.append([square[0] + (colorDirection * 2), square[1], square[0], square[1]])

        return moves


    elif pieceName[0] == "K":
        #moves.append(pieceName)

        if square[0] + 1 < 8 and board[square[0] + 1][square[1]] is None:
            moves.append([square[0] + 1, square[1], square[0], square[1]])

        if square[1] + 1 < 8 and square[0] + 1 < 8 and board[square[0] + 1][square[1] + 1] is None:
            moves.append([square[0] + 1, square[1] + 1, square[0], square[1]])

        if square[0] + 1 < 8 and square[1] - 1 > -1 and board[square[0] + 1][square[1] - 1] is None:
            moves.append([square[0] + 1, square[1] - 1, square[0], square[1]])

        if square[1] + 1 < 8 and board[square[0]][square[1] + 1] is None:
            moves.append([square[0], square[1] + 1, square[0], square[1]])

        if square[1] - 1 > -1 and square[1] - 1 > -1 and board[square[0]][square[1] - 1] is None:
            moves.append([square[0], square[1] - 1, square[0], square[1]])

        if square[0] - 1 > -1 and board[square[0] - 1][square[1]] is None:
            moves.append([square[0] - 1, square[1], square[0], square[1]])

        if square[0] - 1 > -1 and square[1] + 1 < 8 and board[square[0] - 1][square[1] + 1] is None:
            moves.append([square[0] - 1, square[1] + 1, square[0], square[1]])

        if square[0] - 1 > -1 and square[1] - 1 > -1 and board[square[0] - 1][
            square[1] - 1] is None:
            moves.append([square[0] - 1, square[1] - 1, square[0], square[1]])

        return moves

