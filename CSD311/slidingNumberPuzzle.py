# program to input a sliding 8 number puzzle and then the python code will show the steps to solve it starting what number to slide to what position.


BLANK = 0
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


#initializing the puzzle
puzzle = [[0,0,0],[0,0,0],[0,0,0]]

#inputting the puzzle
for i in range(3):
    for j in range(3):
        puzzle[i][j] = int(input("Enter the number in the puzzle: "))
        if puzzle[i][j] == 0:
            x = i
            y = j


def getNewBoard():
    """Return a list that represents a new tile puzzle."""
    board = []
    for i in range(1, SIZE * SIZE):
        board.append(i)
    board.append(BLANK)
    return board

#function to print the puzzle
def printPuzzle():
    for i in range(3):
        for j in range(3):
            print(puzzle[i][j], end = " ")
        print()
    print()

#calling the function to print the puzzle
printPuzzle()

