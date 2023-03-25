#  """
# Теперь сравни fibo из первого и второго задания.
# Найди закономерность.
# Сделай функцию, которая принимает два аргумента.
# Первый - это n, номер числа в последовательности
# Второй - start, сколько единиц в начале и сколько элементов в сумме следующего числа
#
# То есть твой новая fibo должна при таких вызовах выполнять первое задание
# fibo(8, 2) - должно вернуть 21
# fibo(3, 2) - должно вернуть 2
# А при таких - второе задание:
# fibo(5, 3)    # 5
# fibo(80, 3) # 351892690889787253855
# fibo(9, 3)   #57
# """
from fibonachi import fibo_1


def fibo(n, start):
    if start == 2:
        return fibo_1(n)
    else:
        res = []
        for uno in range(start):
            res.append(1)
            # print(res)
        for val in range(n-start):
            res.append(sum(res))
            res.remove(res[0])
            # print(res)
    return res[-1]


print(fibo(9, 3))  # 57
print(fibo(8, 2)) #21
print(fibo(10, 6)) #41
print(fibo(5, 3))
