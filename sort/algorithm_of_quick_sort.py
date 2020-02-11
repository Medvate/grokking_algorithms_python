def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        # Опорный элемент.
        prop_el = arr[0]

        # Список элементов, меньше опорного.
        less = [i for i in arr[1:] if i <= prop_el]
        # Список элементов, больше опорного.
        more = [i for i in arr[1:] if i > prop_el]

        return quick_sort(less) + [prop_el] + quick_sort(more)


a = [0, -3, 2, 1, 17, -100, 200, 561, 5, -9, -10, 9, -9, 0]
print(a)
a = quick_sort(a)
print(a)

