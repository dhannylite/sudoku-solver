import numpy as np
x = [
[5,0,0,0,0,0,9,0,1],
[0,3,0,0,0,0,5,0,0],
[0,0,0,4,0,0,0,0,0],
[0,0,0,0,1,5,0,0,0],
[0,0,7,0,0,0,0,4,0],
[2,0,0,0,0,0,0,0,0],
[0,8,0,0,6,0,1,0,0],
[0,0,4,8,0,0,0,7,0],
[0,0,0,0,0,0,0,0,0],
]

# x = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

def valid(n, pos):
    for i in range(len(x)):
        if x[pos[0]][i] == n:
            return False
    for j in range(len(x)):
        if x[j][pos[1]] == n:
            return False
    for i in range((pos[0]//3)*3,((pos[0]//3)*3) + 3):
        for j in range((pos[1]//3)*3,((pos[1]//3)*3) + 3):
            if x[i][j] == n:
                return False

    return True
def sud():
    for i in range(9):
        for j in range(9):
            if x[i][j] == 0:
                for n in range(1,10):
                    if valid(n, (i,j)):
                        x[i][j] = n
                        sud()
                        if not filled():
                            x[i][j] = 0
                return
def filled():
    for i in range(9):
        for j in range(9):
            if x[i][j] == 0:
                return False
    return True
sud()
# print(valid(1,(0,1)))
print(np.matrix(x))