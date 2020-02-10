def binary_search(arr, item):
    """=== Алгоритм бинарного поиска ===

    В объекте 'arr' ищем объект 'item'.
    Алгоритмическая сложность: O(log N)

    + высокая скорость

    - объект должен быть отсортированным

    :param  arr: ОТСОРТИРОВАННЫЙ list или tuple.
    :param item: обычно int или float. Но если list или tuple заполнен
                 другими сравнимыми между собой объектами,
                 в примеру - строками, и он отсортирован - тоже можно.
    :return: Возвращает индекс искомого элемента.
             Если такой элемент не был найден - возвращает None.
    """
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        # examples: 1 // 2 == 0, 3 // 2 == 0, ...
        mid = (begin + end) // 2

        if item == arr[mid]:
            return mid
        elif item > arr[mid]:
            begin = mid + 1
        else:
            end = mid - 1
    else:
        print('Элемент {0} не был обнаружен!'.format(item))
        return
