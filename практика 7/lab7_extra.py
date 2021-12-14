"""
Решение задачи "ход конем", реализованное с помощью правила Варнсдорфа
"""

# Определяем возможные ходы шахматного коня:

movements = [[1, 2], [2, 1], [-1, 2], [1, -2], [-2, 1], [2, -1], [-2, -1], [-1, -2]]


def table(list):  # Переформатируем двумерный список в таблицу
    a = len(list)
    b = len(list[0])
    output = ""
    for i in range(a):
        output += ("{:<3} " * b).format(*list[i]) + "\n"
    return output.rstrip()


def moves(x, y):  # Доступные пути из точки с координатами (x, y)
    poss_moves = []
    for m in movements:
        if (0 <= x + m[0] < N) and (0 <= y + m[1] < M) and (chess_board[y + m[1]][x + m[0]]) == 0:
            poss_moves.append(m)
    return poss_moves


def method():
    """
    Решение задачи с помощью правила Варнсдорфа. Принцип правила: конь двигается в ту клетку, из которой
    может быть сделано минимальное число ходов.
    """
    x = X - 1
    y = Y - 1
    for i in range(1, M * N + 1):
        chess_board[y][x] = i
        next_move = []
        min = 9
        for move in moves(x, y):
            count = len(moves(x + move[0], y + move[1]))
            if count < min and (count != 0 or i == N * M - 1):
                min = count
                next_move = move
        if len(next_move) == 0:
            break
        x = x + next_move[0]
        y = y + next_move[1]
        if i != M * N:
            print(f"Маршрут не существует, конь остановился на x: {x}, y: {y}")


# Осовная программа: считывание входных данных из файла

file = open("input_01.txt")
d = file.read().split()
M = int(d[0])
N = int(d[1])
X = int(d[2])
Y = int(d[3])
file.close()

chess_board = [[0 for j in range(N)] for i in range(M)]  # Создание шахматной доски
method()
print(table(chess_board))  # Вывод результата
