def inputting(txt: str = 'Ввод: ') -> str | int:
    """
    Модифицированный input()
    :rtype: object
    :type txt: str
    :param txt: текст для вывода перед вводом. Работает также как input('dsaj').
    :return: Если было введено число выдает число. Иначе строку.
    """
    try:
        inp = int(input(txt))
        return inp
    except Exception:
        inp = input(txt)
        return inp


def validation(lst: list[str]) -> str:
    """
    Проверка ввода.
    :param lst: Допустимые значения.
    :return: Ввод.
    """
    x = input('Ввод:')
    while x not in lst:
        x = input(f'Неправильный ввод. выберите из доступных значений {lst}\nВвод: ')
    return x

