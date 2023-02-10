array = list(map(int, input('введите числа через пробел: ').split()))
print(array)
element = int(input('Введите число в рамках последовательности: '))
while element:
    if element not in range(min(array) + 1, max(array)):
        print('Некорректное число')
        element = int(input('Введите число в рамках последовательности: '))
    else:
        break
for i in range(len(array)):
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]
print(array)
def binary_search(array_list, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array_list[middle] == number:
        return middle
    elif number < array_list[middle]:

        return binary_search(array_list, number, left, middle - 1)
    else:
        return binary_search(array_list, number, middle + 1, right)


a = (binary_search(array, element, 0, len(array) - 1))
print(f'номер позиции меньше введенного пользователем числа', a-1)
print('номер позиции равен введеному числу', a)