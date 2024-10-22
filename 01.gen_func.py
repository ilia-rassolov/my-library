"""
Производящая функция последовательности find_distribution вычисляет количество
возможных сочетаний чисел (из списка numbers), чтобы получилось
определённая сумма (amount).
  find_distribution(7, [1, 2, 3]) # 8
  3+3+1
  3+2+2
  3+2+1+1
  3+1+1+1
  2+2+2+1
  2+2+1+1+1
  2+1+1+1+1+1
  1+1+1+1+1+1+1
  Итого 8 сочетаний
Может принимать наборы значений в numbers. Тогда вычисляет возможные сочетания чисел
(только по одному из каждого набора numbers), чтобы получилось определённая сумма (amount)
  find_distribution(10, [[2, 3, 6, 7], [3, 4, 5, 8, 9]]) # 3
  2+8
  6+4
  7+3
  Итого 3 сочетания
"""
from itertools import product
from collections import Counter


def gen_row(index, amount):
    row = list(range(0, amount + 1, index))
    return row


def find_distribution(amount: int, numbers: list):
    if [x for x in numbers if isinstance(x, int)] == numbers:  # проверка на то, что в numbers только числа
        rows = map(lambda x: gen_row(x, amount), numbers)
    elif [x for x in numbers if isinstance(x, list)] == numbers:
        rows = numbers
    else:
        raise Exception('incorrect arguments')
    tuples = product(*rows)
    amounts = map(sum, tuples)
    return Counter(amounts)[amount]
