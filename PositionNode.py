import ChessPieces
import copy
import Eval


class PosNode:
    def __init__(self, board, parent, color, evaluation):
        self.evaluation = evaluation
        self.origEval = evaluation
        self.children = []
        self.childrenvalues = []
        self.data = board
        self.parent = parent
        self.color = color

    def getchildren(self):
        temp = []
        j = 0
        k = 0
        if self.parent is None or self.color == 'black':
            for row in self.data:
                for piece in row:
                    if piece is not None and piece[1] == 'W':
                        for move in ChessPieces.getMoves(self.data, piece, [j,k]):
                            temp = copy.deepcopy(self.data)
                            temp[j][k] = None
                            temp[move[0]][move[1]] = piece
                            neweval = self.evaluation
                            neweval += Eval.improve(temp, self.data, piece, move)
                            self.childrenvalues.append(neweval)
                            self.children.append(temp)

                    k +=1
                j +=1
                k = 0
        else:
            for row in self.data:
                for piece in row:
                    if piece is not None and piece[1] == 'W':
                        for move in ChessPieces.getMoves(self.data, piece, [j,k]):
                            temp = copy.deepcopy(self.data)
                            temp[j][k] = None
                            temp[move[0]][move[1]] = piece
                            neweval = self.evaluation
                            neweval += Eval.improve(self.data, temp, piece, move)
                            self.evaluation = self.origEval
                            self.childrenvalues.append(neweval)
                            self.children.append(temp)
                    k +=1
                j +=1
                k = 0

        self.evaluation += max(self.childrenvalues)