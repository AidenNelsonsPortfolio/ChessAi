import ChessPieces
import PositionNode
import Eval
import time

BOARD_SIZE = 8
color = 'white'
max_depth = 6
whiteKingPos = [7,4]
blackKingPos = [0,4]

board = [['RB1', 'NB1', 'BB1', 'QB', 'KB', 'BB2', 'NB2', 'RB2'],
         ['PB1T', 'PB2T', 'PB3T', 'PB4T', 'PB5T', 'PB6T', 'PB7T', 'PB8T'],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         ['PW1T', 'PW2T', 'PW3T', 'PW4T', 'PW5T', 'PW6T', 'PW7T', 'PW8T'],
         ['RW1', 'NW1', 'BW1', 'QW', 'KW', 'BW2', 'NW2', 'RW2']]

bestBoard = []
globalMax = 0
root = PositionNode.PosNode(board, None, color, 0)
level = 0
temp = None


def checkmate(curBoard, turn):
    if turn == 'white' and ChessPieces.getMoves(curBoard, 'KW', whiteKingPos) is []:
        return True
    if turn == 'black' and ChessPieces.getMoves(curBoard, 'KB', blackKingPos) is []:
        return True
    return False


def getBestMove(node, level):
    global globalMax, bestBoard

    node.getchildren()

    maxchildval = max(node.childrenvalues)

    index = [i for i, j in enumerate(node.childrenvalues) if j == maxchildval]

    if node.evaluation > globalMax:
        globalMax = node.evaluation
        bestBoard = node.children[index[0]]

    if level < max_depth and node.evaluation == globalMax:

        level += 1

        for ind in index:
            temp = PositionNode.PosNode(node.children[ind], node, color, node.evaluation)
            getBestMove(temp, level)


    # now, call findBestMove with the parent node, then re-call the addToPosTree, maybe with an incremented index
    # now finding the best move for black, or, at least, the best next move for white to make, up to a certain depth
    # using the node pruning, where you explore the nodes and their moves in terms of precedence first.

    # improve move finding, add in the possiblity to take diagonally if position is occupied by enemy for pawn
    # plus for the king to capture to escape checkmate, as well as other pieces to block if possible.

    # begin development of the engine for evaluation of positions, as well as add database functionality
    # to send winning/losing moves to, so that the computer can search a database for how to best play a
    # position based upon past games / my advice from games I have already played and uploaded (SQL, prob)

    # make array for each piece of its ideal locations/diagonals/columns, for rating of positions

    # furthermore, evaulate only the first 5-7 moves for the first move, then only 4-5, then 3-4, then to 2 moves
    # up to whatever depth or time limit it has. In this way, we can properly prune the thing
    # furthermore, cut off entire branch of children if one of the opposition moves can make the position unfavorable.

starttime = time.time_ns()
getBestMove(root, 0)
endtime = time.time_ns()

print(starttime)
print(endtime)

print("Done")

print(globalMax)

for row in bestBoard:
    print(row)