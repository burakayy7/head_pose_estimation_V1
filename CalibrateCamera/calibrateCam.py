import cv2
import numpy as np


calibrationSquareDimension = 0.02485
chessboardDimensions = (6, 9)

def creatKnownBoardPositions(boardSize, squareEdgeLength, corners):
    corners = np.empty(shape = [boardSize[0], boardSize[1]],dtype=np.float32 ) # type: ignore

    for i in range(0, boardSize[1], 1):
        for j in range(0, boardSize[0], 1):
            corners.pushback((j*squareEdgeLength, i*squareEdgeLength, 0))
            corners = np.append([j*squareEdgeLength, i*squareEdgeLength, 0.0]) # type: ignore

def getChessboardCorners(images, allFoundCorners, showResults = False):
    for 

