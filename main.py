# main program for creating the game board
from solution_search import decide

class Board(object):
    def __init__(self, board):
        self.board = board

    def update(self, piles, num):
        self.board[piles] -= num

    def computerUpdate(self):
        self.board = decide(self.board, -float('inf'), float('inf'), True)[1][1]

def isValid(remove, board):
    if not remove or len(remove) != 2: return False
    if remove[0] > 0 and remove[1] >= 0 and remove[1] < len(board) and remove[0] <= board[remove[1]]:
        return True
    return False

if __name__ == "__main__":

    print("Starting Nim!")

    ele = int(input("Input the number of piles "))
    lis = []

    print("Input the number of sticks in each pile (separate with ENTER)")
    for _ in range(ele):
        lis.append(int(input()))

    game = Board(lis)
    print("Enter the number of sticks to remove, then space followed by the pile to remove them from (starting from 0)")
    print("The person who removes the last stick loses!")
    print("Example: to remove 3 sticks from pile 2, enter 3 2")

    player_win = True
    while True:
       
        print("Pile state %s" % (game.board))

        player_remove = None

        while not isValid(player_remove, game.board):
            user = str(input("Player turn: "))
            player_remove = [int(i) for i in user.split(' ')]

        game.update(player_remove[1], player_remove[0])

        if sum(game.board) == 0:
            player_win = False
            break
        elif sum(game.board) == 1:
            break

        print("Computer turn")
        game.computerUpdate()

        if sum(game.board) == 0:
            break
        elif sum(game.board) == 1:
            player_win = False
            break

    if player_win:
        print(game.board)
        print("You won!")
    else:
        print(game.board)
        print("You lost!")

