# https://www.acmicpc.net/problem/12100
import sys, copy
from itertools import product

input = sys.stdin.readline
num = int(input())

board = []

for i in range(num):
    board.append(list(map(int, input().split())))


def summation(numbers):
    original_numbers = numbers
    numbers = list(filter(lambda num: num != 0, numbers))

    if len(numbers) >= 1:
        new_numbers = []

        for i in range(0, len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                new_numbers.append(numbers[i] * 2)
                numbers[i], numbers[i + 1] = 0, 0
            elif numbers[i] != numbers[i + 1] and numbers[i] != 0:
                new_numbers.append(numbers[i])

        if numbers[-1] != 0:
            new_numbers.append(numbers[-1])
            numbers[-1] = 0

        if len(new_numbers) < num:
            for _ in range(num - len(new_numbers)):
                new_numbers.append(0)

        return new_numbers

    else:
        return original_numbers


# print(summation([8,0,8,32]))

def swipe_up(temp_board):
    # print(temp_board)
    for row in range(num):
        numbers = []
        for col in range(num):
            numbers.append(temp_board[col][row])

        numbers = summation(numbers)

        for col in range(num):
            temp_board[col][row] = numbers[col]
    return temp_board


def swipe_down(temp_board):
    # print(temp_board)
    for row in range(num):
        numbers = []
        for col in range(num - 1, -1, -1):
            numbers.append(temp_board[col][row])

        numbers = summation(numbers)

        for col in range(num - 1, -1, -1):
            temp_board[col][row] = numbers[num - col - 1]
    return temp_board


def swipe_left(temp_board):
    # print(temp_board)
    for col in range(num):
        numbers = []
        for row in range(num):
            numbers.append(temp_board[col][row])

        numbers = summation(numbers)

        for row in range(num):
            temp_board[col][row] = numbers[row]
    return temp_board


def swipe_right(temp_board):
    for col in range(num):
        numbers = []
        for row in range(num - 1, -1, -1):
            numbers.append(temp_board[col][row])

        numbers = summation(numbers)

        for row in range(num - 1, -1, -1):
            temp_board[col][row] = numbers[num - row - 1]
    return temp_board


def find_max(temp_board):
    b = 0
    for i in temp_board:
        b = max(b, max(i))
    return b


max_value = 0
count = 0

directions = ['r', 'l', 'u', 'd']
possibilities = list(product(directions, repeat=5))


def run(route):
    global max_value
    temp = copy.deepcopy(board)

    for el in route:
        if el == 'u':
            temp = swipe_up(temp)
        if el == 'd':
            temp = swipe_down(temp)
        if el == 'r':
            temp = swipe_right(temp)
        if el == 'l':
            temp = swipe_left(temp)

    max_value = max(max_value, find_max(temp))


for route in possibilities:
    run(route)

print(max_value)

# def dfs(b, level, direction):
#     global max_value
#     global count
#
#     temp_board = copy.deepcopy(b)
#
#     if level == 5:
#         if find_max(temp_board) > max_value:
#             print(level, direction)
#             print('check')
#             print(find_max(temp_board))
#             for i in temp_board:
#                 print(i)
#             print('\n')
#         max_value = max(max_value, find_max(temp_board))
#         count += 1
#         return
#     else:
#         dfs(swipe_down(temp_board), level + 1, direction + ' down')
#         dfs(swipe_up(temp_board), level + 1, direction + ' up')
#         dfs(swipe_right(temp_board), level + 1, direction + ' right')
#         dfs(swipe_left(temp_board), level + 1, direction + ' left')
#
#
# def dfs_test(b, level, direction):
#     global max_value
#     global count
#
#     print(level, direction)
#
#     temp_board = copy.deepcopy(b)
#
#     if level == 5:
#         if find_max(temp_board) > max_value:
#             print(level, direction)
#             print('check')
#             print(find_max(temp_board))
#             for i in temp_board:
#                 print(i)
#             print('\n')
#         max_value = max(max_value, find_max(temp_board))
#         count += 1
#         return
#     elif level == 0:
#         dfs_test(swipe_down(temp_board), level + 1, direction + ' down')
#     elif level == 1:
#         dfs_test(swipe_down(temp_board), level + 1, direction + ' down')
#     elif level == 2:
#         dfs_test(swipe_down(temp_board), level + 1, direction + ' down')
#     elif level == 3:
#         dfs_test(swipe_left(temp_board), level + 1, direction + ' left')
#     elif level == 4:
#         dfs_test(swipe_left(temp_board), level + 1, direction + ' left')
#
#
# dfs(board, 0, 'initial')
# dfs_test(board, 0, 'initial')
# print(max_value)


# def print_board(board):
#     for i in board:
#         print(i)
#     print('\n')

# swipe_down(board)
# print_board(board)
# swipe_down(board)
# print_board(board)
# swipe_down(board)
# print_board(board)
# swipe_left(board)
# print_board(board)
# swipe_left(board)
# print_board(board)
