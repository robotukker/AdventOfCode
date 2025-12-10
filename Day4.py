import numpy as np

def CheckTile(matrix, row, col, rowBorder, colBorder):
    return -1 < row and row < rowBorder and -1 < col and col < colBorder and matrix[row][col] == "@"

if __name__ == "__main__":
    # Handle input
    with open('Input4.txt', 'r') as file:
        input = file.read()

    matrix = np.array([list(row) for row in input.split("\n")])
    outputMatrix = matrix.copy()
    xBorder = matrix.shape[1]
    yBorder = matrix.shape[0]
    accessibleTile = 0
    removeRolls = []
    prevRemovedRolls = []
    running = True

    print(matrix)

    while running:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                adjacentRolls = 0

                if matrix[i][j] == "@":
                    # vertical and horizontal 
                    if CheckTile(matrix, i+1, j, yBorder,xBorder): # bottom
                        adjacentRolls += 1

                    if CheckTile(matrix, i-1, j, yBorder,xBorder): # top
                        adjacentRolls += 1

                    if CheckTile(matrix, i, j+1, yBorder,xBorder): # right
                        adjacentRolls += 1

                    if CheckTile(matrix, i, j-1, yBorder,xBorder): # left
                        adjacentRolls += 1

                    # diagonal
                    if CheckTile(matrix, i+1, j+1, yBorder,xBorder): # right-bottom
                        adjacentRolls += 1

                    if CheckTile(matrix, i-1, j-1, yBorder,xBorder): # left - top
                        adjacentRolls += 1

                    if CheckTile(matrix, i-1, j+1, yBorder,xBorder): # right - top
                        adjacentRolls += 1

                    if CheckTile(matrix, i+1, j-1, yBorder,xBorder): # left - bottom 
                        adjacentRolls += 1

                    if adjacentRolls < 4:
                        accessibleTile += 1
                        outputMatrix[i][j] = "x"
                        removeRolls.append([i,j])

        if removeRolls == prevRemovedRolls:
            running = False
        prevRemovedRolls = removeRolls.copy()

        # Remove the rolls
        for i,j in removeRolls:
            matrix[i,j] = "."

        # print(outputMatrix)
        # print(matrix)

    print(matrix)
    print(accessibleTile)

