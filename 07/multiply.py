import numpy as np


def multiply(alpha: np.array, betta: np.array) -> np.array:
    result = np.zeros(shape=(alpha.shape[0], betta.shape[1]))
    for i in range(alpha.shape[0]):
        for j in range(betta.shape[1]):
            for k in range(betta.shape[0]):
                result[i][j] += alpha[i][k] * betta[k][j]
    return result


if __name__ == '__main__':
    pass
