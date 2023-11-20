class Operation:
    def operation_with_element(self, element: str | int):
        """
        Операции над элементом
        :param element: Элемент списка.
        :return: Измененный элемент.
        """
        raise NotImplementedError()

    def apply_to_list(self, lst: list):
        """
        Применение к списку изменений
        :param lst: Список который нужно изменить
        """
        for ind in range(len(lst)):
            el = lst[ind]
            lst[ind] = self.operation_with_element(el)


class X:
    def apply_to_list(self, lst: list, inp: object) -> list:
        """
        Делает все элементы в списке равными с введенным элементом.
        :type inp: object
        :type lst: list
        :param inp: Элемент на который все изменяется.
        :param lst: Список который нужно изменить.
        :return: Измененный список.
        """
        for ind in range(len(lst)):
            lst[ind] = inp
        return lst


class Max:
    def apply_to_list(self, lst: list) -> tuple:
        """
        Определяет максимальный элемент.
        :type lst: list
        :param lst: Список для поиска.
        :return: Кортеж со значением и индексом.
        """
        el_name = max(lst)
        el = lst.index(el_name)
        result = (el_name, el)
        return result


class Summ(Operation):
    """
    Находит сумму отрицательных чисел.
    """

    def operation_with_element(self, element: str | int) -> int:
        if element < 0:
            return element
        else:
            return 0

    def apply_to_list(self, lst: list) -> int:
        super().apply_to_list(lst)
        summ = 0
        for el in lst:
            summ += el
        return summ


class Index(Operation):
    """
    Находит порядковые номера положительных элементов списка.
    """

    def operation_with_element(self, element: str | int) -> int:
        if element > 0:
            return True
        else:
            return False

    def apply_to_list(self, lst: list) -> list:
        super().apply_to_list(lst)
        for ind in range(len(lst)):
            if lst[ind]:
                lst.append(ind)
                lst.pop(0)
            else:
                lst.pop()
        return lst
