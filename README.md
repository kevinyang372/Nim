# Nim

## Game Description
Nim is a mathematical game of strategy in which two players take turns removing (i.e., nimming) objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap/pile. The goal of the game is to avoid taking the last object. ([from Wikipedia](https://en.wikipedia.org/wiki/Nim))

## Algorithm Description
The computer player in this algorithm implements [minimax](https://en.wikipedia.org/wiki/Minimax) decision tree search and [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) technique to find the next optimal step. Try your best to beat the computer!

## Code Design
The program is divided into two major sections. `main.py` controls the overall flow of the game and `solution_search.py` controls the path search algorithm for computer player.

`main.py`
* The overall gameflow is defined under `if __name__ == "__main__"`, including:
  * Define board attributes (number of piles / number of sticks in each pile)
  * Iteratively update the board with player and computer moves
  * Capture the winning condition

`solution_search.py`
* The solution search section is divided into two steps:
  * Generate all possible next moves from the current board
  * Use minimax algorithm to select the best move by searching the game tree with pruning


## Example
__Warning__: minimax algorithm have exponential time complexity when searching for deep decision trees. Try starting with the classic (7,5,3) setting to avoid a long running time.

```
>>> python main.py
Starting Nime!
Input the number of piles 3
Input the number of sticks in each pile (separate with ENTER)
7
5
3
Enter the number of sticks to remove, then space followed by the pile to remove them from (starting from 0)
The person who removes the last stick loses!
Example: to remove 3 sticks from pile 2, enter 3 2
Pile state [7, 5, 3]
Player turn:2 1
Computer turn
Pile state [0, 3, 3]
Player turn:1 1
Computer turn
Pile state [0, 2, 2]
Player turn:1 1
Computer turn
[0, 1, 0]
You lost!
```
