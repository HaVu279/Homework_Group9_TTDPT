import numpy as np
import matplotlib.pyplot as plt


def chessboard():
    chessboard = np.zeros((8, 8))
    chessboard[1::2, 0::2] = 1
    chessboard[0::2, 1::2] = 1
    return chessboard

chessboard = chessboard()
plt.imshow(chessboard, cmap='binary')
plt.show()
