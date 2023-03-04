def check(user_input):
    compare_flag = [12960000, 1336336, 390625, 16, 168896016, 2401, 200533921, 2313441, 6765201, 4879681, 810000, 1048576,
             181063936, 1874161, 168896016, 810000, 187388721, 4879681, 9834496, 112550881, 5764801, 7311616, 163047361,
             11316496, 157351936, 194481, 3748096, 6250000, 625, 1336336]

    user_flag = []

    if len(user_input) != 30: return

    for char in user_input:
        user_flag.append(ord(char) ^ ord('A'))
    for i in range(0, int(len(user_flag) / 2), 2):
        user_flag[i], user_flag[len(user_flag) - 1 - i] = user_flag[len(user_flag) - 1 - i], user_flag[i]

    for i, char in enumerate(user_flag):
        user_flag[i] = char ** 4

    if compare_flag != user_flag:
        return
    else:
        print("Good job")


if __name__ == "__main__":
    user_input = input("Please enter your flag >  ")
    check(user_input)
