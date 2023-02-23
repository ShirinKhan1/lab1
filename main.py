from itertools import groupby

dictionary = input('Введите словарь ').split(sep=' ')
dictionary = [el for el, _ in groupby(dictionary)]
n = len(dictionary)
# word = list(input('Введите слово '))
# k = len(word)
#
#
# def first_ex(key=k, N=0):
#     global n, dictionary, word, k
#     if key > 0:
#         symbol = dictionary.index(word[k - key]) + 1
#         N += (n ** (key - 1)) * symbol
#         return first_ex(key - 1, N)
#     else:
#         return N


number = int(input('Введите число '))


def second_ex_past1(array=None):
    global n, number

    def bol1(arr):
        if arr[0] > n:
            return True
        else:
            return False

    # def bol2(arr):
    #     if arr[2] not in range(1, n):
    #         return False
    #     else:
    #         return True

    if array is None:
        if number <= n:
            return [number]
        else:
            if number % n == 0:
                array = [(number // n) - 1, n, n]
            else:
                array = [number // n, n, number % n]

    def find_int(ar_r):
        if not (type(ar_r[0]) == int):
            return find_int(ar_r[0])
        else:
            return ar_r

    arr = find_int(array)

    if bol1(arr):
        if arr[0] % n == 0:
            arr[0] = [(arr[0] // n) - 1, n, n]
        else:
            arr[0] = [arr[0] // n, n, arr[0] % n]
        return second_ex_past1(array)
    else:
        return array


def second_ex_past2(array):
    global n
    def find_array_int(ar_r):
        if not (type(ar_r[0][0]) == int):
            return find_array_int(ar_r[0])
        else:
            return ar_r
    arr = find_array_int(array)
    # print(arr)
    def change_arr(arr):
        first,last = arr.pop(0), [arr.pop(0),arr.pop(0)]
        for i in range(1,len(first),2):
            first[i]*=n
        arr.extend(first+last)
    change_arr(arr)
    if type(array[0]) == int:
        return array
    else:
        return second_ex_past2(array)
    #[i*3 for i in a]


array = second_ex_past1()
# print(array)
print(second_ex_past2(array))

# print(first_ex())
