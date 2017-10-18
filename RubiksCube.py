from termcolor import colored
from collections import deque
import random

colorDict = {"W": "white", "Y": "yellow", "G": "green", "B": "blue", "O": "magenta", "R": "red"}
backDict = {"W": "on_grey", "Y": "on_yellow", "G": "on_green", "B": "on_blue", "O": "on_magenta", "R": "on_red"}

instructions = """
Python Rubik's Cube Instructions
--------------------------------
Type Move Or String Of Moves from L, L', R, R', U, U', D, D', F, F', B, B'
Type (M)oves to see the moves for the cube configuration
Type (N)ew to reset the cube
Type (S)cramble to scramble the cube
Type (H)elp to see the instructions again
Type (Q)uit to quit
"""


def coloredCubeChar(c):
    return colored(c, colorDict[c])

class RubiksCube:
    def __init__(self, configuration=None):
        if not configuration:
            self.configuration = [[["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]],
                                  [["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]],
                                  [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
                                  [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]],
                                  [["R", "R", "R"], ["R", "R", "R"], ["R", "R", "R"]],
                                  [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]]]
        else:
            self.configuration = configuration

        self.moveSet = ["U","U'","F","F'","R","R'","L","L'","D","D'","B","B'"]

        self.moveLog = deque()

    def __str__(self):
        topSeparator = "".join([" " * 8, "- " * 3,  "\n"])

        def sideRowString(row):
            return "".join([" ".join(map(coloredCubeChar, self.configuration[1][row])), " | ",
                    " ".join(map(coloredCubeChar, self.configuration[2][row])), " | ",
                    " ".join(map(coloredCubeChar, self.configuration[3][row])), " | ",
                    " ".join(map(coloredCubeChar, self.configuration[4][row])), "\n"])

        def topOrBottomeRowString(face, row):
            return "".join([" " * 8, " ".join(map(coloredCubeChar, self.configuration[face][row])), "\n"])

        cube_string = topSeparator
        cube_string += topOrBottomeRowString(0, 0) + topOrBottomeRowString(0, 1) + topOrBottomeRowString(0, 2)
        cube_string += topSeparator
        cube_string += sideRowString(0) + sideRowString(1) + sideRowString(2)
        cube_string += topSeparator
        cube_string += topOrBottomeRowString(5, 0) + topOrBottomeRowString(5, 1) + topOrBottomeRowString(5, 2)

        return cube_string

    def rotateFaceClockwise(self, i):
        self.configuration[i][0][0] ,self.configuration[i][0][1], self.configuration[i][0][2] ,\
        self.configuration[i][1][0] ,self.configuration[i][1][1], self.configuration[i][1][2] ,\
        self.configuration[i][2][0] ,self.configuration[i][2][1], self.configuration[i][2][2] = \
        self.configuration[i][2][0], self.configuration[i][1][0], self.configuration[i][0][0],\
        self.configuration[i][2][1], self.configuration[i][1][1], self.configuration[i][0][1],\
        self.configuration[i][2][2], self.configuration[i][1][2], self.configuration[i][0][2]

    def rotateCubeAlongX(right=True):
        if right:
            pass
        else:
            pass

    def rotateCubeAlongY(forward=True):
        if forward:
            pass
        else:
            pass

    def rotateCubeAlongZ(clockwise=True):
        if clockwise:
            pass
        else:
            pass

    def rotateFaceCounterClockwise(self, i):
        self.configuration[i][0][0], self.configuration[i][0][1], self.configuration[i][0][2],\
        self.configuration[i][1][0], self.configuration[i][1][1], self.configuration[i][1][2],\
        self.configuration[i][2][0], self.configuration[i][2][1], self.configuration[i][2][2] = \
        self.configuration[i][0][2], self.configuration[i][1][2], self.configuration[i][2][2],\
        self.configuration[i][0][1], self.configuration[i][1][1], self.configuration[i][2][1],\
        self.configuration[i][0][0], self.configuration[i][1][0], self.configuration[i][2][0]

    def rotateRowClockwise(self, i):
        self.configuration[1][i], self.configuration[2][i], self.configuration[3][i], self.configuration[4][i] = \
        self.configuration[2][i], self.configuration[3][i], self.configuration[4][i], self.configuration[1][i]

    def rotateRowCounterClockwise(self, i):
        self.configuration[1][i], self.configuration[2][i], self.configuration[3][i], self.configuration[4][i] = \
        self.configuration[4][i], self.configuration[1][i], self.configuration[2][i], self.configuration[3][i]

    def rotateColumnDown(self, col):
        idx = [0, 2, 5, 4]

        backFaceColumn = [2, 1, 0]

        temp = [[self.configuration[idx[3]][2][backFaceColumn[col]], self.configuration[idx[3]][1][backFaceColumn[col]], self.configuration[idx[3]][0][backFaceColumn[col]]],
                [self.configuration[idx[0]][0][col], self.configuration[idx[0]][1][col], self.configuration[idx[0]][2][col]],
                [self.configuration[idx[1]][0][col], self.configuration[idx[1]][1][col], self.configuration[idx[1]][2][col]],
                [self.configuration[idx[2]][2][col], self.configuration[idx[2]][1][col], self.configuration[idx[2]][0][col]]]

        for i in range(3):
            self.configuration[idx[i]][0][col], self.configuration[idx[i]][1][col], self.configuration[idx[i]][2][col] = \
                temp[i][0], temp[i][1], temp[i][2]

        self.configuration[idx[3]][0][backFaceColumn[col]], self.configuration[idx[3]][1][backFaceColumn[col]], self.configuration[idx[3]][2][backFaceColumn[col]] = \
            temp[i + 1][0], temp[i + 1][1], temp[i + 1][2]

    def rotateColumnUp(self, col):
        idx = [5, 2, 0, 4]

        backFaceColumn = [2, 1, 0]

        temp = [[self.configuration[idx[3]][2][backFaceColumn[col]], self.configuration[idx[3]][1][backFaceColumn[col]], self.configuration[idx[3]][0][backFaceColumn[col]]],
                [self.configuration[idx[0]][0][col], self.configuration[idx[0]][1][col], self.configuration[idx[0]][2][col]],
                [self.configuration[idx[1]][0][col], self.configuration[idx[1]][1][col], self.configuration[idx[1]][2][col]],
                [self.configuration[idx[2]][0][col], self.configuration[idx[2]][1][col], self.configuration[idx[2]][2][col]]]

        for i in range(3):
            self.configuration[idx[i]][0][col], self.configuration[idx[i]][1][col], self.configuration[idx[i]][2][col] = \
                temp[i][0], temp[i][1], temp[i][2]

        self.configuration[idx[3]][0][backFaceColumn[col]], self.configuration[idx[3]][1][backFaceColumn[col]], \
        self.configuration[idx[3]][2][backFaceColumn[col]] = \
            temp[i + 1][0], temp[i + 1][1], temp[i + 1][2]

    def spinFrontFaceCW(self):

        self.configuration[0][2][0], self.configuration[0][2][1], self.configuration[0][2][2], \
        self.configuration[1][0][2], self.configuration[1][1][2], self.configuration[1][2][2], \
        self.configuration[5][0][0], self.configuration[5][0][1], self.configuration[5][0][2], \
        self.configuration[3][0][0], self.configuration[3][1][0], self.configuration[3][2][0] = \
        self.configuration[1][2][2], self.configuration[1][1][2], self.configuration[1][0][2], \
        self.configuration[5][0][0], self.configuration[5][0][1], self.configuration[5][0][2], \
        self.configuration[3][2][0], self.configuration[3][1][0], self.configuration[3][0][0], \
        self.configuration[0][2][0], self.configuration[0][2][1], self.configuration[0][2][2]

    def spinFrontFaceCCW(self):

        self.configuration[0][2][0], self.configuration[0][2][1], self.configuration[0][2][2], \
        self.configuration[1][0][2], self.configuration[1][1][2], self.configuration[1][2][2], \
        self.configuration[5][0][0], self.configuration[5][0][1], self.configuration[5][0][2], \
        self.configuration[3][0][0], self.configuration[3][1][0], self.configuration[3][2][0] = \
        self.configuration[3][0][0], self.configuration[3][1][0], self.configuration[3][2][0], \
        self.configuration[0][2][2], self.configuration[0][2][1], self.configuration[0][2][0], \
        self.configuration[1][0][2], self.configuration[1][1][2], self.configuration[1][2][2], \
        self.configuration[5][0][2], self.configuration[5][0][1], self.configuration[5][0][0]

    def spinBackFaceCW(self):

        self.configuration[0][0][0], self.configuration[0][0][1], self.configuration[0][0][2], \
        self.configuration[1][0][0], self.configuration[1][1][0], self.configuration[1][2][0], \
        self.configuration[5][2][0], self.configuration[5][2][1], self.configuration[5][2][2], \
        self.configuration[3][0][2], self.configuration[3][1][2], self.configuration[3][2][2] = \
        self.configuration[3][0][2], self.configuration[3][1][2], self.configuration[3][2][2], \
        self.configuration[0][0][0], self.configuration[0][0][1], self.configuration[0][0][2], \
        self.configuration[1][0][0], self.configuration[1][1][0], self.configuration[1][2][0], \
        self.configuration[5][2][2], self.configuration[5][2][1], self.configuration[5][2][0]

    def spinBackFaceCCW(self):

        self.configuration[0][0][0], self.configuration[0][0][1], self.configuration[0][0][2], \
        self.configuration[1][0][0], self.configuration[1][1][0], self.configuration[1][2][0], \
        self.configuration[5][2][0], self.configuration[5][2][1], self.configuration[5][2][2], \
        self.configuration[3][0][2], self.configuration[3][1][2], self.configuration[3][2][2] = \
        self.configuration[1][0][0], self.configuration[1][1][0], self.configuration[1][2][0], \
        self.configuration[5][2][0], self.configuration[5][2][1], self.configuration[5][2][2], \
        self.configuration[3][0][2], self.configuration[3][1][2], self.configuration[3][2][2], \
        self.configuration[0][0][2], self.configuration[0][0][1], self.configuration[0][0][0]

    def move(self, move):
        if move == "U":
            self.rotateRowClockwise(0)
            self.rotateFaceClockwise(0)
        elif move == "U'":
            self.rotateRowCounterClockwise(0)
            self.rotateFaceCounterClockwise(0)
        elif move == "D":
            self.rotateRowCounterClockwise(2)
            self.rotateFaceClockwise(5)
        elif move == "D'":
            self.rotateRowClockwise(2)
            self.rotateFaceCounterClockwise(5)
        elif move == "L":
            self.rotateColumnDown(0)
            self.rotateFaceClockwise(1)
        elif move == "L'":
            self.rotateColumnUp(0)
            self.rotateFaceCounterClockwise(1)
        elif move == "R":
            self.rotateColumnUp(2)
            self.rotateFaceCounterClockwise(3)
        elif move == "R'":
            self.rotateColumnDown(2)
            self.rotateFaceClockwise(3)
        elif move == "F":
            self.spinFrontFaceCW()
            self.rotateFaceClockwise(2)
        elif move == "F'":
            self.spinFrontFaceCCW()
            self.rotateFaceCounterClockwise(2)
        elif move == "B":
            self.spinBackFaceCW()
            self.rotateFaceClockwise(4)
        elif move == "B'":
            self.spinBackFaceCCW()
            self.rotateFaceCounterClockwise(4)

    def moveSeries(self, moveString):
        moves = moveString.split()

        for move in moves:
            if move in cube.moveSet:
                self.move(move)
                cube.moveLog.append(move)

    def scramble(self, n):
        for i in range(n):
            move = random.choice(self.moveSet)
            self.move(move)
            cube.moveLog.append(move)




if __name__ == "__main__":


    cube = RubiksCube()

    print("\n")
    print("------Initial Cube------\n")

    print(cube)
    print(instructions)

    while True:

        printCube = True

        command = input("Enter Command: ")

        if command in ["q", "quit"]:
            break
        elif command.upper() in cube.moveSet:
            cube.move(command)
            cube.moveLog.append(command)
        elif command.lower() in ["n", "new"]:
            print("Resetting")
            cube = RubiksCube()
        elif command.lower() in ["s", "scramble"]:
            cube.scramble(10)
        elif command.lower() in ["m", "moves"]:
            printCube = False
            print("Moves: ["," ".join(cube.moveLog),"]")
        elif command.lower() in ["h", "help"]:
            print(instructions)
            printCube = False
        else:
            cube.moveSeries(command.upper())

        if printCube:
            print(cube)
