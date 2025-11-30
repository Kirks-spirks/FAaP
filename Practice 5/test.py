import math
def integral_wish (board_a, board_b):
    """
    Вычисляет определенный интеграл для функции y=x^2+2

    Args:
        board_a, board_b: Ограничения интеграла.

    Returns:
         integral_test: Результат интегрирования.
    """
    integral_test = (board_a**2/3+board_a*2-board_b**2/3+board_b*2)
    print(integral_test)
    return integral_test
integral_wish(12,4)