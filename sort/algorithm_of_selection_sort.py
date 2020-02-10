def selection_sort(arr):
    """=== Алгоритм сортировки выбором ===

    Объект 'arr' сортируем по возрастанию.
    Алгоритмическая сложность: O(N ** 2)

    + простота реализации

    - низкая скорость

    :param arr: list или tuple, который нужно отсортировать.
                Подразумевается, что он имеет сравнимые
                между собой типы данных.
    :return: Возвращает отсортированные объект.
    """
    result = []

    for i in range(len(arr)):
        minimal = arr[0]
        index_min = 0

        for j in range(len(arr)):
            if arr[j] < minimal:
                minimal = arr[j]
                index_min = j
        else:
            result.append(minimal)
            arr.pop(index_min)
    else:
        return result
