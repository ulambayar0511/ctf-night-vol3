import socket  # you know socket?


def cal(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i * i
    return sum
