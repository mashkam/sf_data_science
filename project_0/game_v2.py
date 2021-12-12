"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binsearch(number: int = 1) -> int:
    """Бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # счетчик попыток
    prdict_number_min = 1
    prdict_number_max = 101

    while True:
        count += 1

        predict_number = (prdict_number_max + prdict_number_min) // 2
        if number > predict_number:
            prdict_number_min = predict_number
        elif number < predict_number:
            prdict_number_max = predict_number
        else:
            break  # выход из цикла если угадали
    return count


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binsearch)
